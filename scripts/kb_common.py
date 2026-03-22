from __future__ import annotations

import json
import os
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[1]

UNIT_TYPE_TO_DIR = {
    "concept": "units/concepts",
    "definition": "units/definitions",
    "theorem": "units/theorems",
    "lemma": "units/lemmas",
    "equivalence": "units/equivalences",
    "conjecture": "units/conjectures",
    "theorem_family": "units/theorem-families",
    "definition_family": "units/definition-families",
    "notation_family": "units/notation-families",
    "feasibility_question": "units/feasibility-questions",
    "dependency_request": "units/dependency-requests",
    "proof_search_request": "units/proof-search-requests",
    "equation": "units/equations",
    "equation_context": "units/equation-contexts",
    "quantity": "units/quantities",
    "claim": "units/claims",
    "derivation": "units/derivations",
    "proof_fragment": "units/proof-fragments",
    "proof_obligation": "units/proof-obligations",
    "proof_state": "units/proof-states",
    "derivation_step": "units/derivation-steps",
    "dependency_graph_snapshot": "units/dependency-graph-snapshots",
    "method": "units/methods",
    "model": "units/models",
    "warning": "units/warnings",
    "bridge": "units/bridges",
    "notation_map": "units/notation-maps",
    "source_fusion_record": "units/source-fusion-records",
    "conflict_record": "units/conflict-records",
    "open_gap": "units/open-gaps",
    "question_oracle": "units/question-oracles",
    "regression_question": "units/regression-questions",
    "followup_source_task": "units/followup-source-tasks",
    "source_map": "units/source-maps",
}

PORTAL_DIR_BY_TYPE = {
    "concept": "Concepts",
    "definition": "Definitions",
    "theorem": "Theorems",
    "lemma": "Lemmas",
    "equivalence": "Equivalences",
    "conjecture": "Conjectures",
    "theorem_family": "Theorem-Families",
    "definition_family": "Definition-Families",
    "notation_family": "Notation-Families",
    "feasibility_question": "Feasibility-Questions",
    "dependency_request": "Dependency-Requests",
    "proof_search_request": "Proof-Search-Requests",
    "equation": "Equations",
    "equation_context": "Equation-Contexts",
    "quantity": "Quantities",
    "claim": "Claims",
    "derivation": "Derivations",
    "proof_fragment": "Proof-Fragments",
    "proof_obligation": "Proof-Obligations",
    "proof_state": "Proof-States",
    "derivation_step": "Derivation-Steps",
    "dependency_graph_snapshot": "Dependency-Graph-Snapshots",
    "method": "Methods",
    "model": "Models",
    "warning": "Warnings",
    "bridge": "Bridges",
    "notation_map": "Notation-Maps",
    "source_fusion_record": "Source-Fusion-Records",
    "conflict_record": "Conflict-Records",
    "open_gap": "Open-Gaps",
    "question_oracle": "Question-Oracles",
    "regression_question": "Regression-Questions",
    "followup_source_task": "Followup-Source-Tasks",
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
    "tests",
    "oracles",
    "blocked_by",
    "resolves",
    "routes_to",
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


def load_queue_manifests() -> Dict[str, dict]:
    queues: Dict[str, dict] = {}
    queue_root = ROOT / "queues"
    if not queue_root.exists():
        return queues
    for path in sorted(queue_root.rglob("*.json")):
        queue = read_json(path)
        queue["_path"] = str(path.relative_to(ROOT))
        queues[queue["queue_id"]] = queue
    return queues


def load_regression_suites() -> Dict[str, dict]:
    suites: Dict[str, dict] = {}
    regression_root = ROOT / "regressions"
    if not regression_root.exists():
        return suites
    for path in sorted(regression_root.rglob("*-suite.json")):
        suite = read_json(path)
        suite["_path"] = str(path.relative_to(ROOT))
        suites[suite["suite_id"]] = suite
    return suites


def load_regression_logs() -> Dict[str, dict]:
    logs: Dict[str, dict] = {}
    regression_root = ROOT / "regressions"
    if not regression_root.exists():
        return logs
    for path in sorted(regression_root.rglob("*-log.json")):
        log = read_json(path)
        log["_path"] = str(path.relative_to(ROOT))
        logs[log["run_id"]] = log
    return logs


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


def queue_portal_path(queue: dict) -> Path:
    return ROOT / "portal" / "Topological-Phases-Of-Matter" / "Queues" / f"{slug_from_id(queue['queue_id'])}.md"


def regression_suite_portal_path(suite: dict) -> Path:
    return ROOT / "portal" / "Topological-Phases-Of-Matter" / "Regression-Suites" / f"{slug_from_id(suite['suite_id'])}.md"


def regression_log_portal_path(log: dict) -> Path:
    return ROOT / "portal" / "Topological-Phases-Of-Matter" / "Regression-Logs" / f"{slug_from_id(log['run_id'])}.md"


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
