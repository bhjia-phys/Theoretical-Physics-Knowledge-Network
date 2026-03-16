from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[1]

UNIT_TYPE_TO_DIR = {
    "concept": "units/concepts",
    "equation": "units/equations",
    "quantity": "units/quantities",
    "claim": "units/claims",
    "derivation": "units/derivations",
    "method": "units/methods",
    "model": "units/models",
    "warning": "units/warnings",
    "bridge": "units/bridges",
    "source_map": "units/source-maps",
}

PORTAL_DIR_BY_TYPE = {
    "concept": "Concepts",
    "equation": "Equations",
    "quantity": "Quantities",
    "claim": "Claims",
    "derivation": "Derivations",
    "method": "Methods",
    "model": "Models",
    "warning": "Warnings",
    "bridge": "Bridges",
    "source_map": "Source-Maps",
}

EDGE_RELATIONS = {
    "depends_on",
    "defines",
    "uses",
    "explains",
    "motivates",
    "specializes",
    "generalizes",
    "contrasts_with",
    "derived_from",
    "supports",
    "warned_by",
    "bridges_to",
    "formalizes_toward",
    "anchored_in_source",
}

ID_RE = re.compile(r"^[a-z_]+:[a-z0-9-]+$")
EDGE_ID_RE = re.compile(r"^edge:[a-z0-9-]+$")
REQUIRED_FIELDS = [
    "id",
    "type",
    "title",
    "summary",
    "domain",
    "tags",
    "aliases",
    "assumptions",
    "regime",
    "scope",
    "dependencies",
    "related_units",
    "source_anchors",
    "formalization_status",
    "validation_status",
    "maturity",
    "created_at",
    "updated_at",
]
LIST_FIELDS = [
    "tags",
    "aliases",
    "assumptions",
    "dependencies",
    "related_units",
    "source_anchors",
]
REF_LIST_FIELDS = [
    "dependencies",
    "related_units",
    "model_refs",
    "equation_refs",
    "quantity_refs",
]
PREFIX_BY_FIELD = {
    "model_refs": "model:",
    "equation_refs": "equation:",
    "quantity_refs": "quantity:",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(json.dumps(row, ensure_ascii=False, sort_keys=False) for row in rows)
    path.write_text(text + ("\n" if text else ""), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def iter_unit_files() -> Iterable[Tuple[str, Path]]:
    for unit_type, rel_dir in UNIT_TYPE_TO_DIR.items():
        unit_dir = ROOT / rel_dir
        for path in sorted(unit_dir.glob("*.json")):
            yield unit_type, path


def load_units() -> Dict[str, dict]:
    units: Dict[str, dict] = {}
    for expected_type, path in iter_unit_files():
        unit = read_json(path)
        unit["_path"] = str(path.relative_to(ROOT))
        unit["_expected_type"] = expected_type
        units[unit["id"]] = unit
    return units


def load_edges() -> List[dict]:
    path = ROOT / "edges" / "edges.jsonl"
    rows: List[dict] = []
    if not path.exists():
        return rows
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def load_manifests() -> Dict[str, dict]:
    manifests: Dict[str, dict] = {}
    for path in sorted((ROOT / "sources").glob("*/manifest.json")):
        manifest = read_json(path)
        manifest["_path"] = str(path.relative_to(ROOT))
        manifests[manifest["source_id"]] = manifest
    return manifests


def sorted_units(units: Dict[str, dict]) -> List[dict]:
    return [units[key] for key in sorted(units)]


def slug_from_id(object_id: str) -> str:
    return object_id.split(":", 1)[1]


def portal_path_for_unit(unit: dict) -> Path:
    return (
        ROOT
        / "portal"
        / "Topological-Phases-Of-Matter"
        / PORTAL_DIR_BY_TYPE[unit["type"]]
        / f"{slug_from_id(unit['id'])}.md"
    )


def markdown_link(from_path: Path, to_path: Path, label: str) -> str:
    rel = os.path.relpath(to_path, start=from_path.parent)
    return f"[{label}]({rel})"


def unit_link(from_path: Path, unit: dict) -> str:
    return markdown_link(from_path, portal_path_for_unit(unit), unit["title"])


def build_edge_maps(edges: List[dict]) -> Tuple[dict, dict]:
    outgoing = defaultdict(list)
    incoming = defaultdict(list)
    for edge in sorted(edges, key=lambda item: item["id"]):
        outgoing[edge["source"]].append(edge)
        incoming[edge["target"]].append(edge)
    return outgoing, incoming


def manifest_section_map(manifest: dict) -> Dict[str, dict]:
    return {entry["id"]: entry for entry in manifest.get("section_map", [])}


def manifest_equation_map(manifest: dict) -> Dict[str, dict]:
    return {entry["label"]: entry for entry in manifest.get("equation_map", [])}


def manifest_figure_map(manifest: dict) -> Dict[str, dict]:
    return {entry["id"]: entry for entry in manifest.get("figure_map", [])}


def anchor_summary(anchor: dict) -> str:
    section = anchor["section"]
    parts = [section]
    equation_labels = anchor.get("equation_labels", [])
    if equation_labels:
        parts.append("eqs: " + ", ".join(equation_labels))
    figure_ids = anchor.get("figure_ids", [])
    if figure_ids:
        parts.append("figs: " + ", ".join(figure_ids))
    if anchor.get("notes"):
        parts.append(anchor["notes"])
    return " | ".join(parts)


def run_checks() -> dict:
    units = load_units()
    manifests = load_manifests()
    edges = load_edges()
    errors: list[str] = []

    if not units:
        errors.append("No unit files found.")
    if not manifests:
        errors.append("No source manifests found.")

    manifest_sections = {source_id: manifest_section_map(manifest) for source_id, manifest in manifests.items()}
    manifest_equations = {source_id: manifest_equation_map(manifest) for source_id, manifest in manifests.items()}
    manifest_figures = {source_id: manifest_figure_map(manifest) for source_id, manifest in manifests.items()}

    for unit in sorted_units(units):
        for field in REQUIRED_FIELDS:
            if field not in unit:
                errors.append(f"{unit.get('id', unit['_path'])}: missing required field '{field}'")
        unit_id = unit.get("id", "")
        unit_type = unit.get("type", "")
        expected_type = unit.get("_expected_type")
        if not ID_RE.match(unit_id):
            errors.append(f"{unit['_path']}: invalid id '{unit_id}'")
        if unit_type != expected_type:
            errors.append(f"{unit['_path']}: type '{unit_type}' does not match directory type '{expected_type}'")
        if unit_id and unit_type and not unit_id.startswith(unit_type + ":"):
            errors.append(f"{unit['_path']}: id '{unit_id}' does not use '{unit_type}:' prefix")
        for field in LIST_FIELDS:
            if field in unit and not isinstance(unit[field], list):
                errors.append(f"{unit['_path']}: field '{field}' must be a list")
        if not unit.get("source_anchors"):
            errors.append(f"{unit['_path']}: source_anchors must be non-empty")
        for anchor in unit.get("source_anchors", []):
            if not isinstance(anchor, dict):
                errors.append(f"{unit['_path']}: each source anchor must be an object")
                continue
            if "source_id" not in anchor or "section" not in anchor:
                errors.append(f"{unit['_path']}: source anchors require source_id and section")
                continue
            source_id = anchor["source_id"]
            section = anchor["section"]
            if source_id not in manifests:
                errors.append(f"{unit['_path']}: unknown source_id '{source_id}'")
                continue
            if section not in manifest_sections[source_id]:
                errors.append(f"{unit['_path']}: unknown section '{section}' in source '{source_id}'")
            for label in anchor.get("equation_labels", []):
                entry = manifest_equations[source_id].get(label)
                if entry is None:
                    errors.append(f"{unit['_path']}: unknown equation label '{label}' in source '{source_id}'")
                elif entry["section"] != section:
                    errors.append(
                        f"{unit['_path']}: equation label '{label}' belongs to section '{entry['section']}', not '{section}'"
                    )
            for figure_id in anchor.get("figure_ids", []):
                entry = manifest_figures[source_id].get(figure_id)
                if entry is None:
                    errors.append(f"{unit['_path']}: unknown figure id '{figure_id}' in source '{source_id}'")
                elif entry["section"] != section:
                    errors.append(
                        f"{unit['_path']}: figure id '{figure_id}' belongs to section '{entry['section']}', not '{section}'"
                    )
        for field in REF_LIST_FIELDS:
            for ref in unit.get(field, []):
                if ref not in units:
                    errors.append(f"{unit['_path']}: unknown reference '{ref}' in field '{field}'")
                prefix = PREFIX_BY_FIELD.get(field)
                if prefix and not ref.startswith(prefix):
                    errors.append(f"{unit['_path']}: reference '{ref}' in field '{field}' must start with '{prefix}'")
        for field in ("formal_targets", "symmetries", "failure_modes", "retrieval_hints"):
            if field in unit and not isinstance(unit[field], list):
                errors.append(f"{unit['_path']}: optional field '{field}' must be a list if present")
        if "symbols" in unit:
            if not isinstance(unit["symbols"], list):
                errors.append(f"{unit['_path']}: symbols must be a list if present")
            for symbol in unit["symbols"]:
                if not isinstance(symbol, dict) or "symbol" not in symbol or "meaning" not in symbol:
                    errors.append(f"{unit['_path']}: each symbol entry needs 'symbol' and 'meaning'")

    seen_edge_ids: set[str] = set()
    for edge in edges:
        edge_id = edge.get("id", "")
        if not EDGE_ID_RE.match(edge_id):
            errors.append(f"edges/edges.jsonl: invalid edge id '{edge_id}'")
        if edge_id in seen_edge_ids:
            errors.append(f"edges/edges.jsonl: duplicate edge id '{edge_id}'")
        seen_edge_ids.add(edge_id)
        if edge.get("source") not in units:
            errors.append(f"edges/edges.jsonl: unknown edge source '{edge.get('source')}'")
        if edge.get("target") not in units:
            errors.append(f"edges/edges.jsonl: unknown edge target '{edge.get('target')}'")
        if edge.get("relation") not in EDGE_RELATIONS:
            errors.append(f"edges/edges.jsonl: invalid relation '{edge.get('relation')}'")

    return {
        "units": units,
        "manifests": manifests,
        "edges": edges,
        "errors": errors,
    }


def format_list(items: list[str]) -> str:
    if not items:
        return "- none\n"
    return "".join(f"- {item}\n" for item in items)


def render_unit_page(unit: dict, units: dict, outgoing: dict, incoming: dict) -> str:
    page_path = portal_path_for_unit(unit)
    dependency_links = [unit_link(page_path, units[item]) for item in unit.get("dependencies", []) if item in units]
    related_links = [unit_link(page_path, units[item]) for item in unit.get("related_units", []) if item in units]
    anchor_lines = [anchor_summary(anchor) for anchor in unit.get("source_anchors", [])]
    outgoing_lines = []
    for edge in outgoing.get(unit["id"], []):
        target = units.get(edge["target"])
        target_label = unit_link(page_path, target) if target else edge["target"]
        outgoing_lines.append(f"`{edge['relation']}` -> {target_label}: {edge['summary']}")
    incoming_lines = []
    for edge in incoming.get(unit["id"], []):
        source = units.get(edge["source"])
        source_label = unit_link(page_path, source) if source else edge["source"]
        incoming_lines.append(f"{source_label} -> `{edge['relation']}`: {edge['summary']}")

    lines = [
        f"# {unit['title']}",
        "",
        f"- ID: `{unit['id']}`",
        f"- Type: `{unit['type']}`",
        f"- Domain: `{unit['domain']}`",
        f"- Subdomain: `{unit.get('subdomain', '')}`",
        f"- Formalization: `{unit['formalization_status']}`",
        f"- Validation: `{unit['validation_status']}`",
        f"- Maturity: `{unit['maturity']}`",
        "",
        "## Summary",
        unit["summary"],
        "",
        "## Scope",
        unit["scope"],
        "",
        "## Regime",
        unit["regime"],
        "",
        "## Assumptions",
        format_list([f"`{item}`" for item in unit.get("assumptions", [])]).rstrip(),
        "",
        "## Dependencies",
        format_list(dependency_links).rstrip(),
        "",
        "## Related Units",
        format_list(related_links).rstrip(),
        "",
        "## Source Anchors",
        format_list([f"`{item}`" for item in anchor_lines]).rstrip(),
        "",
        "## Outgoing Edges",
        format_list(outgoing_lines).rstrip(),
        "",
        "## Incoming Edges",
        format_list(incoming_lines).rstrip(),
        "",
    ]

    if unit.get("failure_modes"):
        lines.extend(["## Failure Modes", format_list([f"`{item}`" for item in unit["failure_modes"]]).rstrip(), ""])
    if unit.get("formal_targets"):
        lines.extend(["## Formal Targets", format_list([f"`{item}`" for item in unit["formal_targets"]]).rstrip(), ""])
    return "\n".join(lines)


def render_index_page(units: dict, manifests: dict) -> str:
    grouped = defaultdict(list)
    for unit in sorted_units(units):
        grouped[unit["type"]].append(unit)
    lines = [
        "# Topological Phases Of Matter",
        "",
        "This portal is generated from the typed object store under `units/`, `edges/`, and `sources/`.",
        "",
        "## Exemplar",
        "- Edward Witten, *Three Lectures On Topological Phases Of Matter*",
        "- Current scope: Lecture One",
        f"- Source portal entry: {markdown_link(ROOT / 'portal' / 'Topological-Phases-Of-Matter' / 'Index.md', ROOT / 'portal' / 'Topological-Phases-Of-Matter' / 'Lecture-One.md', 'Lecture-One.md')}",
        "",
        "## Counts By Type",
    ]
    for unit_type in sorted(grouped):
        lines.append(f"- `{unit_type}`: {len(grouped[unit_type])}")
    lines.extend(["", "## Entry Points"])
    for entry_id in [
        "concept:weyl-node",
        "concept:nielsen-ninomiya-theorem",
        "concept:berry-connection",
        "concept:fermi-arc",
        "source_map:witten-topological-phases-lecture-one",
    ]:
        if entry_id in units:
            lines.append(f"- {unit_link(ROOT / 'portal' / 'Topological-Phases-Of-Matter' / 'Index.md', units[entry_id])}")
    if manifests:
        manifest = next(iter(manifests.values()))
        lines.extend(["", "## Source", f"- `{manifest['source_id']}`", f"- `{manifest['urls']['abs']}`"])
    lines.append("")
    return "\n".join(lines)


def render_lecture_page(units: dict, manifests: dict) -> str:
    manifest = next(iter(manifests.values()))
    page_path = ROOT / "portal" / "Topological-Phases-Of-Matter" / "Lecture-One.md"
    section_to_units = defaultdict(set)
    for unit in sorted_units(units):
        for anchor in unit.get("source_anchors", []):
            if anchor["source_id"] == manifest["source_id"]:
                section_to_units[anchor["section"]].add(unit["id"])

    lines = [
        "# Lecture One",
        "",
        f"- Source ID: `{manifest['source_id']}`",
        f"- Title: {manifest['title']}",
        f"- arXiv: `{manifest['urls']['abs']}`",
        "",
        "## Coverage By Section",
    ]
    for section in manifest["section_map"]:
        lines.extend(["", f"## {section['title']}", section["summary"], ""])
        unit_ids = sorted(section_to_units.get(section["id"], set()))
        if not unit_ids:
            lines.append("- no curated units yet")
            continue
        for unit_id in unit_ids:
            lines.append(f"- {unit_link(page_path, units[unit_id])}")
    lines.append("")
    return "\n".join(lines)


def command_check() -> int:
    result = run_checks()
    errors = result["errors"]
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Protocol check failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        "Protocol check passed:",
        f"{len(result['units'])} units,",
        f"{len(result['edges'])} edges,",
        f"{len(result['manifests'])} source manifest(s).",
    )
    return 0


def command_build() -> int:
    check_result = run_checks()
    if check_result["errors"]:
        for error in check_result["errors"]:
            print(f"ERROR: {error}")
        print(f"Build aborted: protocol check failed with {len(check_result['errors'])} error(s).")
        return 1

    units = check_result["units"]
    manifests = check_result["manifests"]
    edges = sorted(check_result["edges"], key=lambda item: item["id"])

    unit_rows = []
    symbol_rows = []
    anchor_rows = []
    formal_rows = []
    domain_index = defaultdict(lambda: {"counts_by_type": Counter(), "units": [], "tags": set(), "sources": set()})

    for unit in sorted_units(units):
        unit_rows.append(
            {
                "id": unit["id"],
                "type": unit["type"],
                "title": unit["title"],
                "summary": unit["summary"],
                "path": unit["_path"],
                "domain": unit["domain"],
                "subdomain": unit.get("subdomain", ""),
                "tags": unit["tags"],
                "aliases": unit["aliases"],
                "dependencies": unit["dependencies"],
                "related_units": unit["related_units"],
                "formalization_status": unit["formalization_status"],
                "validation_status": unit["validation_status"],
                "maturity": unit["maturity"],
                "source_anchor_count": len(unit.get("source_anchors", [])),
            }
        )
        formal_rows.append(
            {
                "id": unit["id"],
                "title": unit["title"],
                "type": unit["type"],
                "formalization_status": unit["formalization_status"],
                "formal_targets": unit.get("formal_targets", []),
                "dependencies": unit.get("dependencies", []),
                "maturity": unit["maturity"],
            }
        )
        bucket = domain_index[unit["domain"]]
        bucket["counts_by_type"][unit["type"]] += 1
        bucket["units"].append(unit["id"])
        bucket["tags"].update(unit["tags"])
        for anchor in unit.get("source_anchors", []):
            bucket["sources"].add(anchor["source_id"])
            anchor_rows.append(
                {
                    "unit_id": unit["id"],
                    "unit_title": unit["title"],
                    "source_id": anchor["source_id"],
                    "section": anchor["section"],
                    "equation_labels": anchor.get("equation_labels", []),
                    "figure_ids": anchor.get("figure_ids", []),
                    "notes": anchor.get("notes", ""),
                }
            )
        for symbol in unit.get("symbols", []):
            symbol_rows.append(
                {
                    "symbol": symbol["symbol"],
                    "meaning": symbol["meaning"],
                    "unit_id": unit["id"],
                    "unit_title": unit["title"],
                    "unit_type": unit["type"],
                }
            )

    edge_rows = [
        {
            "id": edge["id"],
            "source": edge["source"],
            "relation": edge["relation"],
            "target": edge["target"],
            "summary": edge["summary"],
            "confidence": edge["confidence"],
        }
        for edge in edges
    ]

    final_domain_index = {}
    for domain, payload in sorted(domain_index.items()):
        final_domain_index[domain] = {
            "counts_by_type": dict(sorted(payload["counts_by_type"].items())),
            "units": sorted(payload["units"]),
            "tags": sorted(payload["tags"]),
            "sources": sorted(payload["sources"]),
        }

    write_jsonl(ROOT / "indexes" / "unit_index.jsonl", unit_rows)
    write_jsonl(ROOT / "indexes" / "edge_index.jsonl", edge_rows)
    write_jsonl(ROOT / "indexes" / "symbol_index.jsonl", sorted(symbol_rows, key=lambda row: (row["symbol"], row["unit_id"])))
    write_jsonl(
        ROOT / "indexes" / "source_anchor_index.jsonl",
        sorted(anchor_rows, key=lambda row: (row["source_id"], row["section"], row["unit_id"])),
    )
    write_json(ROOT / "indexes" / "domain_index.json", final_domain_index)
    write_jsonl(ROOT / "indexes" / "formalization_index.jsonl", formal_rows)

    outgoing, incoming = build_edge_maps(edges)
    for unit in sorted_units(units):
        write_text(portal_path_for_unit(unit), render_unit_page(unit, units, outgoing, incoming))

    portal_root = ROOT / "portal" / "Topological-Phases-Of-Matter"
    write_text(portal_root / "Index.md", render_index_page(units, manifests))
    write_text(portal_root / "Lecture-One.md", render_lecture_page(units, manifests))

    print(
        "Build completed:",
        f"{len(unit_rows)} units,",
        f"{len(edge_rows)} edges,",
        f"{len(symbol_rows)} symbols,",
        f"{len(anchor_rows)} anchors,",
        f"{len(manifests)} manifest(s),",
        "indexes + portal refreshed.",
    )
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Protocol checker and deterministic builder for theoretical-physics-knowledge-network."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("check", help="Validate canonical objects, anchors, and edges.")
    subparsers.add_parser("build", help="Validate and regenerate indexes plus portal projections.")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.command == "check":
        return command_check()
    if args.command == "build":
        return command_build()
    print(f"Unknown command: {args.command}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
