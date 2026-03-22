from __future__ import annotations

from collections import Counter, defaultdict

from check_protocol import run_checks
from kb_common import (
    ROOT,
    anchor_summary,
    build_edge_maps,
    markdown_link,
    portal_path_for_unit,
    queue_portal_path,
    regression_log_portal_path,
    regression_suite_portal_path,
    sorted_units,
    unit_link,
    write_json,
    write_jsonl,
    write_text,
)


def format_list(items: list[str]) -> str:
    if not items:
        return "- none\n"
    return "".join(f"- {item}\n" for item in items)


def format_math_expressions(expressions: list[dict]) -> str:
    if not expressions:
        return "- none\n"
    parts: list[str] = []
    for expr in expressions:
        metadata: list[str] = []
        if expr.get("kind"):
            metadata.append(f"`kind={expr['kind']}`")
        if expr.get("equation_label"):
            metadata.append(f"`label={expr['equation_label']}`")
        if expr.get("notes"):
            metadata.append(expr["notes"])
        if metadata:
            parts.append("- " + " | ".join(metadata))
        parts.append("$$")
        parts.append(expr["latex"])
        parts.append("$$")
    return "\n".join(parts) + "\n"


def format_symbol_table(symbols: list[dict]) -> str:
    if not symbols:
        return "- none\n"
    lines = ["| Symbol | Meaning |", "|---|---|"]
    for symbol in symbols:
        lines.append(f"| `{symbol['symbol']}` | {symbol['meaning']} |")
    return "\n".join(lines) + "\n"


def select_exemplar_manifest(manifests: dict) -> dict | None:
    for manifest in manifests.values():
        section_ids = [entry.get("id", "") for entry in manifest.get("section_map", [])]
        if any(section_id.startswith("lecture-one/") for section_id in section_ids):
            return manifest
    return next(iter(manifests.values()), None)


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
        f"- Canonical Family: `{unit.get('canonical_family', '')}`",
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
        "## Representation",
        unit.get("representation", "No explicit representation recorded."),
        "",
        "## Source Anchors",
        format_list([f"`{item}`" for item in anchor_lines]).rstrip(),
        "",
        "## Mathematical Content",
        format_math_expressions(unit.get("math_expressions", [])).rstrip(),
        "",
        "## Symbols",
        format_symbol_table(unit.get("symbols", [])).rstrip(),
        "",
        "## Dependencies",
        format_list(dependency_links).rstrip(),
        "",
        "## Related Units",
        format_list(related_links).rstrip(),
        "",
    ]

    if unit.get("prompt"):
        lines.extend(["## Prompt", unit["prompt"], ""])
    if unit.get("question_family"):
        lines.extend(["## Question Family", f"`{unit['question_family']}`", ""])
    if unit.get("step_inputs"):
        step_inputs = [unit_link(page_path, units[item]) for item in unit["step_inputs"] if item in units]
        lines.extend(["## Step Inputs", format_list(step_inputs).rstrip(), ""])
    if unit.get("step_output"):
        output = units.get(unit["step_output"])
        output_text = unit_link(page_path, output) if output else f"`{unit['step_output']}`"
        lines.extend(["## Step Output", f"- {output_text}", ""])
    if unit.get("step_justification"):
        lines.extend(["## Step Justification", format_list(unit["step_justification"]).rstrip(), ""])
    if unit.get("pass_conditions"):
        lines.extend(["## Pass Conditions", format_list(unit["pass_conditions"]).rstrip(), ""])
    if unit.get("failure_triggers"):
        lines.extend(["## Failure Triggers", format_list(unit["failure_triggers"]).rstrip(), ""])
    if unit.get("mandatory_unit_ids"):
        mandatory = [unit_link(page_path, units[item]) for item in unit["mandatory_unit_ids"] if item in units]
        lines.extend(["## Mandatory Units", format_list(mandatory).rstrip(), ""])
    if unit.get("mandatory_equation_labels"):
        lines.extend(
            ["## Mandatory Equation Labels", format_list([f"`{item}`" for item in unit["mandatory_equation_labels"]]).rstrip(), ""]
        )
    if unit.get("obligation_ids"):
        obligations = [unit_link(page_path, units[item]) for item in unit["obligation_ids"] if item in units]
        lines.extend(["## Proof Obligations", format_list(obligations).rstrip(), ""])
    if unit.get("supporting_obligation_ids"):
        obligations = [unit_link(page_path, units[item]) for item in unit["supporting_obligation_ids"] if item in units]
        lines.extend(["## Supporting Obligations", format_list(obligations).rstrip(), ""])
    if unit.get("equation_context_ids"):
        contexts = [unit_link(page_path, units[item]) for item in unit["equation_context_ids"] if item in units]
        lines.extend(["## Equation Contexts", format_list(contexts).rstrip(), ""])
    if unit.get("dependency_graph_snapshot_id"):
        graph = units.get(unit["dependency_graph_snapshot_id"])
        graph_text = unit_link(page_path, graph) if graph else f"`{unit['dependency_graph_snapshot_id']}`"
        lines.extend(["## Dependency Graph Snapshot", f"- {graph_text}", ""])
    if unit.get("family_member_ids"):
        family_members = [unit_link(page_path, units[item]) for item in unit["family_member_ids"] if item in units]
        lines.extend(["## Family Members", format_list(family_members).rstrip(), ""])
    if unit.get("fusion_member_ids"):
        fusion_members = [unit_link(page_path, units[item]) for item in unit["fusion_member_ids"] if item in units]
        lines.extend(["## Fusion Members", format_list(fusion_members).rstrip(), ""])
    if unit.get("conflict_unit_ids"):
        conflicts = [unit_link(page_path, units[item]) for item in unit["conflict_unit_ids"] if item in units]
        lines.extend(["## Conflict Units", format_list(conflicts).rstrip(), ""])
    if unit.get("derivation_spine"):
        lines.extend(["## Derivation Spine", format_list(unit["derivation_spine"]).rstrip(), ""])
    if unit.get("mandatory_logical_moves"):
        lines.extend(["## Mandatory Logical Moves", format_list(unit["mandatory_logical_moves"]).rstrip(), ""])
    if unit.get("common_failure_patterns"):
        lines.extend(["## Common Failure Patterns", format_list(unit["common_failure_patterns"]).rstrip(), ""])
    if unit.get("grading_rubric"):
        lines.extend(["## Grading Rubric", format_list(unit["grading_rubric"]).rstrip(), ""])
    if unit.get("blocking_units"):
        blocking = [unit_link(page_path, units[item]) for item in unit["blocking_units"] if item in units]
        lines.extend(["## Blocking Units", format_list(blocking).rstrip(), ""])
    if unit.get("gap_kind"):
        lines.extend(["## Gap Kind", f"`{unit['gap_kind']}`", ""])
    if unit.get("recovery_source_type"):
        lines.extend(["## Recovery Source Type", f"`{unit['recovery_source_type']}`", ""])
    if unit.get("task_status"):
        lines.extend(["## Task Status", f"`{unit['task_status']}`", ""])
    if unit.get("resolution_targets"):
        targets = [unit_link(page_path, units[item]) for item in unit["resolution_targets"] if item in units]
        lines.extend(["## Resolution Targets", format_list(targets).rstrip(), ""])
    if unit.get("resolves_gaps"):
        gaps = [unit_link(page_path, units[item]) for item in unit["resolves_gaps"] if item in units]
        lines.extend(["## Resolves Gaps", format_list(gaps).rstrip(), ""])
    if unit.get("routes_back_to"):
        routes = [unit_link(page_path, units[item]) for item in unit["routes_back_to"] if item in units]
        lines.extend(["## Routes Back To", format_list(routes).rstrip(), ""])
    if unit.get("reentry_targets"):
        reentry = [unit_link(page_path, units[item]) for item in unit["reentry_targets"] if item in units]
        lines.extend(["## Reentry Targets", format_list(reentry).rstrip(), ""])
    if unit.get("topic_completion_status"):
        lines.extend(["## Topic Completion Status", f"`{unit['topic_completion_status']}`", ""])
    if unit.get("supporting_regression_question_ids"):
        questions = [unit_link(page_path, units[item]) for item in unit["supporting_regression_question_ids"] if item in units]
        lines.extend(["## Supporting Regression Questions", format_list(questions).rstrip(), ""])
    if unit.get("supporting_oracle_ids"):
        oracles = [unit_link(page_path, units[item]) for item in unit["supporting_oracle_ids"] if item in units]
        lines.extend(["## Supporting Oracles", format_list(oracles).rstrip(), ""])
    if unit.get("supporting_regression_run_ids"):
        lines.extend(
            [
                "## Supporting Regression Runs",
                format_list([f"`{item}`" for item in unit["supporting_regression_run_ids"]]).rstrip(),
                "",
            ]
        )
    if unit.get("promotion_blockers"):
        lines.extend(["## Promotion Blockers", format_list(unit["promotion_blockers"]).rstrip(), ""])
    if "split_required" in unit:
        lines.extend(["## Split Required", f"`{unit['split_required']}`", ""])
    if unit.get("recovery_source_refs"):
        lines.extend(
            ["## Recovery Source Refs", format_list([f"`{item}`" for item in unit["recovery_source_refs"]]).rstrip(), ""]
        )
    if unit.get("primary_retrieval_paths"):
        paths = [unit_link(page_path, units[item]) for item in unit["primary_retrieval_paths"] if item in units]
        lines.extend(["## Primary Retrieval Paths", format_list(paths).rstrip(), ""])
    if unit.get("candidate_sources"):
        candidate_lines = [f"`{item['citation']}`: {item.get('why', 'no rationale recorded')}" for item in unit["candidate_sources"]]
        lines.extend(["## Candidate Sources", format_list(candidate_lines).rstrip(), ""])
    if unit.get("failure_modes"):
        lines.extend(["## Failure Modes", format_list([f"`{item}`" for item in unit["failure_modes"]]).rstrip(), ""])
    if unit.get("formal_targets"):
        lines.extend(["## Formal Targets", format_list([f"`{item}`" for item in unit["formal_targets"]]).rstrip(), ""])
    if any(
        unit.get(field)
        for field in (
            "lean_namespace",
            "lean_declaration",
            "lean_statement_kind",
            "admissible_assumptions",
            "lean_prerequisite_ids",
            "formalization_blockers",
        )
    ):
        lines.extend(["## Lean Formalization Plan", ""])
        if unit.get("lean_namespace"):
            lines.append(f"- Namespace: `{unit['lean_namespace']}`")
        if unit.get("lean_declaration"):
            lines.append(f"- Declaration: `{unit['lean_declaration']}`")
        if unit.get("lean_statement_kind"):
            lines.append(f"- Statement kind: `{unit['lean_statement_kind']}`")
        if unit.get("admissible_assumptions"):
            lines.extend(["", "### Admissible assumptions", "", format_list(unit["admissible_assumptions"]).rstrip()])
        if unit.get("lean_prerequisite_ids"):
            prerequisites = [
                unit_link(page_path, units[item]) for item in unit["lean_prerequisite_ids"] if item in units
            ]
            lines.extend(["", "### Lean prerequisites", "", format_list(prerequisites).rstrip()])
        if unit.get("formalization_blockers"):
            lines.extend(["", "### Formalization blockers", "", format_list(unit["formalization_blockers"]).rstrip()])
        lines.append("")
    if any(
        unit.get(field)
        for field in (
            "formal_theory_role",
            "definition_trust_tier",
            "statement_graph_role",
            "statement_graph_parents",
            "statement_graph_children",
            "target_statement_id",
            "prerequisite_closure_status",
        )
    ):
        lines.extend(["## Formal-Theory Guardrails", ""])
        if unit.get("formal_theory_role"):
            lines.append(f"- Formal theory role: `{unit['formal_theory_role']}`")
        if unit.get("definition_trust_tier"):
            lines.append(f"- Definition trust tier: `{unit['definition_trust_tier']}`")
        if unit.get("statement_graph_role"):
            lines.append(f"- Statement graph role: `{unit['statement_graph_role']}`")
        if unit.get("prerequisite_closure_status"):
            lines.append(f"- Prerequisite closure status: `{unit['prerequisite_closure_status']}`")
        if unit.get("target_statement_id"):
            target_unit = units.get(unit["target_statement_id"])
            target_label = unit_link(page_path, target_unit) if target_unit else f"`{unit['target_statement_id']}`"
            lines.append(f"- Target statement: {target_label}")
        if unit.get("statement_graph_parents"):
            parent_links = [unit_link(page_path, units[item]) if item in units else f"`{item}`" for item in unit["statement_graph_parents"]]
            lines.extend(["", "### Statement graph parents", "", format_list(parent_links).rstrip()])
        if unit.get("statement_graph_children"):
            child_links = [unit_link(page_path, units[item]) if item in units else f"`{item}`" for item in unit["statement_graph_children"]]
            lines.extend(["", "### Statement graph children", "", format_list(child_links).rstrip()])
        lines.append("")
    if any(unit.get(field) for field in ("faithfulness_status", "faithfulness_strategy", "faithfulness_notes")):
        lines.extend(["## Faithfulness Review", ""])
        if unit.get("faithfulness_status"):
            lines.append(f"- Status: `{unit['faithfulness_status']}`")
        if unit.get("faithfulness_strategy"):
            lines.append(f"- Strategy: {unit['faithfulness_strategy']}")
        if unit.get("faithfulness_notes"):
            lines.append(f"- Notes: {unit['faithfulness_notes']}")
        lines.append("")
    if any(unit.get(field) for field in ("comparator_audit_status", "comparator_risks")):
        lines.extend(["## Comparator Audit", ""])
        if unit.get("comparator_audit_status"):
            lines.append(f"- Status: `{unit['comparator_audit_status']}`")
        if unit.get("comparator_risks"):
            lines.extend(["", "### Comparator risks", "", format_list(unit["comparator_risks"]).rstrip()])
        lines.append("")
    if any(unit.get(field) for field in ("provenance_kind", "attribution_requirements")):
        lines.extend(["## Provenance And Attribution", ""])
        if unit.get("provenance_kind"):
            lines.append(f"- Provenance kind: `{unit['provenance_kind']}`")
        if unit.get("attribution_requirements"):
            lines.extend(["", "### Attribution requirements", "", format_list(unit["attribution_requirements"]).rstrip()])
        lines.append("")
    if any(unit.get(field) for field in ("runtime_gap_kinds", "runtime_return_to_stages", "topic_queue_ids")):
        lines.extend(["## Runtime Gap Bridge", ""])
        if unit.get("runtime_gap_kinds"):
            lines.append("- Runtime gap kinds: " + ", ".join(f"`{item}`" for item in unit["runtime_gap_kinds"]))
        if unit.get("runtime_return_to_stages"):
            lines.append(
                "- Runtime return stages: "
                + ", ".join(f"`{item}`" for item in unit["runtime_return_to_stages"])
            )
        if unit.get("topic_queue_ids"):
            lines.append("- Topic queues: " + ", ".join(f"`{item}`" for item in unit["topic_queue_ids"]))
        lines.append("")
    if unit.get("retrieval_hints"):
        lines.extend(["## Retrieval Hints", format_list([f"`{item}`" for item in unit["retrieval_hints"]]).rstrip(), ""])

    lines.extend(
        [
            "## Outgoing Edges",
            format_list(outgoing_lines).rstrip(),
            "",
            "## Incoming Edges",
            format_list(incoming_lines).rstrip(),
            "",
        ]
    )
    return "\n".join(lines)


def render_index_page(units: dict, manifests: dict, queues: dict, regression_suites: dict, regression_logs: dict) -> str:
    grouped = defaultdict(list)
    families = defaultdict(list)
    for unit in sorted_units(units):
        grouped[unit["type"]].append(unit)
        if unit.get("canonical_family"):
            families[unit["canonical_family"]].append(unit["id"])
    index_path = ROOT / "portal" / "Topological-Phases-Of-Matter" / "Index.md"
    lines = [
        "# Topological Phases Of Matter",
        "",
        "This portal is generated from the canonical store under `sources/`, `units/`, `edges/`, `queues/`, and `regressions/`.",
        "",
        "## Exemplar",
        "- Edward Witten, *Three Lectures On Topological Phases Of Matter*",
        "- Stage-two target: Lecture One proof-grade exemplar plus Lecture Two / Three flagship theorem seeds and a topic-level regression surface",
        "",
        "## Counts By Type",
    ]
    for unit_type in sorted(grouped):
        lines.append(f"- `{unit_type}`: {len(grouped[unit_type])}")
    lines.extend(
        [
            f"- queue manifests: {len(queues)}",
            f"- regression suites: {len(regression_suites)}",
            f"- regression logs: {len(regression_logs)}",
            f"- canonical families: {len(families)}",
            "",
            "## Entry Points",
        ]
    )
    for entry_id in [
        "source_map:topological-phases-core",
        "source_map:witten-topological-phases-lecture-one",
        "theorem:integer-quantum-hall-response-equals-band-and-many-body-chern-number",
        "theorem:sign-changing-dirac-mass-supports-chiral-edge-mode",
        "theorem:nielsen-ninomiya-charge-cancellation",
        "definition:weyl-node-as-isolated-three-dimensional-two-band-crossing",
        "open_gap:parity-anomaly-motivates-but-does-not-prove-lattice-no-go",
    ]:
        if entry_id in units:
            lines.append(f"- {unit_link(index_path, units[entry_id])}")
    lecture_pages = [
        ("Lecture One", ROOT / "portal" / "Topological-Phases-Of-Matter" / "Lecture-One.md"),
        ("Lecture Two", ROOT / "portal" / "Topological-Phases-Of-Matter" / "Lecture-Two.md"),
        ("Lecture Three", ROOT / "portal" / "Topological-Phases-Of-Matter" / "Lecture-Three.md"),
    ]
    lines.extend(["", "## Lecture Pages"])
    for label, path in lecture_pages:
        lines.append(f"- {markdown_link(index_path, path, label)}")
    if queues:
        lines.extend(["", "## Queue Pages"])
        for queue in sorted(queues.values(), key=lambda item: item["queue_id"]):
            lines.append(f"- {markdown_link(index_path, queue_portal_path(queue), queue['title'])}")
    if regression_suites:
        lines.extend(["", "## Regression Suites"])
        for suite in sorted(regression_suites.values(), key=lambda item: item["suite_id"]):
            lines.append(f"- {markdown_link(index_path, regression_suite_portal_path(suite), suite['title'])}")
    if regression_logs:
        lines.extend(["", "## Latest Regression Logs"])
        for log in sorted(regression_logs.values(), key=lambda item: item["run_id"]):
            lines.append(f"- {markdown_link(index_path, regression_log_portal_path(log), log['run_id'])}")
    if manifests:
        manifest = select_exemplar_manifest(manifests)
        if manifest is not None:
            exemplar_url = manifest.get("urls", {}).get("abs")
            if not exemplar_url:
                exemplar_url = next(iter(manifest.get("urls", {}).values()), "")
            lines.extend(["", "## Source", f"- `{manifest['source_id']}`"])
            if exemplar_url:
                lines.append(f"- `{exemplar_url}`")
    lines.append("")
    return "\n".join(lines)


def render_lecture_page(manifest: dict, lecture_prefix: str, lecture_title: str, units: dict) -> str:
    page_path = ROOT / "portal" / "Topological-Phases-Of-Matter" / f"{lecture_title.replace(' ', '-')}.md"
    section_to_units = defaultdict(set)
    for unit in sorted_units(units):
        for anchor in unit.get("source_anchors", []):
            if anchor["source_id"] == manifest["source_id"] and anchor["section"].startswith(lecture_prefix):
                section_to_units[anchor["section"]].add(unit["id"])

    lines = [
        f"# {lecture_title}",
        "",
        f"- Source ID: `{manifest['source_id']}`",
        f"- Title: {manifest['title']}",
        f"- arXiv: `{manifest['urls']['abs']}`",
        "",
        "## Coverage By Section",
    ]
    for section in manifest["section_map"]:
        if not section["id"].startswith(lecture_prefix):
            continue
        lines.extend(["", f"## {section['title']}", section["summary"], ""])
        unit_ids = sorted(section_to_units.get(section["id"], set()))
        if not unit_ids:
            lines.append("- no curated units yet")
            continue
        for unit_id in unit_ids:
            lines.append(f"- {unit_link(page_path, units[unit_id])}")
    lines.append("")
    return "\n".join(lines)


def render_queue_page(queue: dict, units: dict) -> str:
    page_path = queue_portal_path(queue)
    lines = [
        f"# {queue['title']}",
        "",
        f"- Queue ID: `{queue['queue_id']}`",
        f"- Topic: `{queue['topic']}`",
        f"- Kind: `{queue['queue_kind']}`",
        "",
        "## Summary",
        queue["summary"],
        "",
        "## Items",
    ]
    for item in queue.get("items", []):
        unit = units.get(item["unit_id"])
        label = unit_link(page_path, unit) if unit else f"`{item['unit_id']}`"
        lines.append(f"- {label} | status=`{item['status']}` | priority=`{item['priority']}` | {item.get('notes', 'no note')}")
    lines.append("")
    return "\n".join(lines)


def render_regression_suite_page(suite: dict, units: dict, logs_by_suite: dict) -> str:
    page_path = regression_suite_portal_path(suite)
    source_map = units.get(suite["source_map_id"])
    source_map_line = unit_link(page_path, source_map) if source_map else f"`{suite['source_map_id']}`"
    lines = [
        f"# {suite['title']}",
        "",
        f"- Suite ID: `{suite['suite_id']}`",
        f"- Topic: `{suite['topic']}`",
        f"- Source Map: {source_map_line}",
        "",
        "## Summary",
        suite["summary"],
        "",
    ]
    if any(suite.get(field) for field in ("benchmark_contamination", "benchmark_use", "contamination_notes")):
        lines.extend(["## Benchmark Governance", ""])
        if suite.get("benchmark_contamination"):
            lines.append(f"- Contamination status: `{suite['benchmark_contamination']}`")
        if suite.get("benchmark_use"):
            lines.append(f"- Declared use: `{suite['benchmark_use']}`")
        if suite.get("contamination_notes"):
            lines.append(f"- Notes: {suite['contamination_notes']}")
        lines.append("")
    lines.append("## Questions")
    for question_id in suite.get("question_ids", []):
        question = units.get(question_id)
        lines.append(f"- {unit_link(page_path, question) if question else f'`{question_id}`'}")
    lines.extend(["", "## Oracles"])
    for oracle_id in suite.get("oracle_ids", []):
        oracle = units.get(oracle_id)
        lines.append(f"- {unit_link(page_path, oracle) if oracle else f'`{oracle_id}`'}")
    if suite.get("focus_units"):
        lines.extend(["", "## Focus Units"])
        for unit_id in suite["focus_units"]:
            unit = units.get(unit_id)
            lines.append(f"- {unit_link(page_path, unit) if unit else f'`{unit_id}`'}")
    logs = logs_by_suite.get(suite["suite_id"], [])
    if logs:
        lines.extend(["", "## Recorded Runs"])
        for log in logs:
            lines.append(f"- {markdown_link(page_path, regression_log_portal_path(log), log['run_id'])} | status=`{log['status']}`")
    lines.append("")
    return "\n".join(lines)


def render_regression_log_page(log: dict, units: dict) -> str:
    page_path = regression_log_portal_path(log)
    lines = [
        f"# {log['run_id']}",
        "",
        f"- Suite ID: `{log['suite_id']}`",
        f"- Status: `{log['status']}`",
        f"- Created: `{log['created_at']}`",
        f"- Topic completion: `{log.get('topic_completion_status', '') or 'not_assessed'}`",
        f"- Promotion readiness: `{log.get('promotion_readiness', '') or 'not-assessed'}`",
        "",
    ]
    if log.get("blocking_unit_ids"):
        blocking_units = [
            unit_link(page_path, units[unit_id]) if unit_id in units else f"`{unit_id}`"
            for unit_id in log.get("blocking_unit_ids", [])
        ]
        lines.extend(["## Blocking Units", format_list(blocking_units).rstrip(), ""])
    lines.extend(
        [
        "## Results",
        ]
    )
    for result in log.get("results", []):
        question = units.get(result["question_id"])
        oracle = units.get(result["oracle_id"])
        question_label = unit_link(page_path, question) if question else f"`{result['question_id']}`"
        oracle_label = unit_link(page_path, oracle) if oracle else f"`{result['oracle_id']}`"
        writeback = [
            unit_link(page_path, units[unit_id]) if unit_id in units else f"`{unit_id}`"
            for unit_id in result.get("writeback_unit_ids", [])
        ]
        lines.append(f"- {question_label} | oracle={oracle_label} | grade=`{result['grade']}` | {result.get('notes', 'no note')}")
        if writeback:
            lines.append(f"  - writeback: {', '.join(writeback)}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    check_result = run_checks()
    if check_result["errors"]:
        for error in check_result["errors"]:
            print(f"ERROR: {error}")
        print(f"Build aborted: protocol check failed with {len(check_result['errors'])} error(s).")
        return 1

    units = check_result["units"]
    manifests = check_result["manifests"]
    edges = sorted(check_result["edges"], key=lambda item: item["id"])
    queues = check_result["queues"]
    regression_suites = check_result["regression_suites"]
    regression_logs = check_result["regression_logs"]

    unit_rows = []
    symbol_rows = []
    anchor_rows = []
    formal_rows = []
    gap_rows = []
    followup_rows = []
    family_rows = []
    queue_rows = []
    suite_rows = []
    run_rows = []
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
                "canonical_family": unit.get("canonical_family", ""),
                "tags": unit["tags"],
                "aliases": unit["aliases"],
                "assumptions": unit["assumptions"],
                "regime": unit["regime"],
                "scope": unit["scope"],
                "dependencies": unit["dependencies"],
                "related_units": unit["related_units"],
                "representation": unit.get("representation", ""),
                "math_expressions": unit.get("math_expressions", []),
                "symbols": unit.get("symbols", []),
                "source_anchors": unit.get("source_anchors", []),
                "formalization_status": unit["formalization_status"],
                "validation_status": unit["validation_status"],
                "maturity": unit["maturity"],
                "obligation_ids": unit.get("obligation_ids", []),
                "equation_context_ids": unit.get("equation_context_ids", []),
                "dependency_graph_snapshot_id": unit.get("dependency_graph_snapshot_id", ""),
                "family_member_ids": unit.get("family_member_ids", []),
                "formal_targets": unit.get("formal_targets", []),
                "retrieval_hints": unit.get("retrieval_hints", []),
            }
        )
        formal_rows.append(
            {
                "id": unit["id"],
                "title": unit["title"],
                "type": unit["type"],
                "canonical_family": unit.get("canonical_family", ""),
                "formal_theory_role": unit.get("formal_theory_role", ""),
                "statement_graph_role": unit.get("statement_graph_role", ""),
                "target_statement_id": unit.get("target_statement_id", ""),
                "formalization_status": unit["formalization_status"],
                "formal_targets": unit.get("formal_targets", []),
                "lean_namespace": unit.get("lean_namespace", ""),
                "lean_declaration": unit.get("lean_declaration", ""),
                "lean_statement_kind": unit.get("lean_statement_kind", ""),
                "lean_prerequisite_ids": unit.get("lean_prerequisite_ids", []),
                "dependencies": unit.get("dependencies", []),
                "obligation_ids": unit.get("obligation_ids", []),
                "dependency_graph_snapshot_id": unit.get("dependency_graph_snapshot_id", ""),
                "faithfulness_status": unit.get("faithfulness_status", ""),
                "comparator_audit_status": unit.get("comparator_audit_status", ""),
                "provenance_kind": unit.get("provenance_kind", ""),
                "prerequisite_closure_status": unit.get("prerequisite_closure_status", ""),
                "statement_graph_parent_count": len(unit.get("statement_graph_parents", [])),
                "statement_graph_child_count": len(unit.get("statement_graph_children", [])),
                "maturity": unit["maturity"],
                "math_expression_count": len(unit.get("math_expressions", [])),
                "formalization_blocker_count": len(unit.get("formalization_blockers", [])),
            }
        )
        if unit["type"] == "open_gap":
            gap_rows.append(
                {
                    "id": unit["id"],
                    "title": unit["title"],
                    "summary": unit["summary"],
                    "canonical_family": unit.get("canonical_family", ""),
                    "gap_kind": unit.get("gap_kind", ""),
                    "recovery_source_type": unit.get("recovery_source_type", ""),
                    "blocking_units": unit.get("blocking_units", []),
                    "resolution_targets": unit.get("resolution_targets", []),
                    "reentry_targets": unit.get("reentry_targets", []),
                    "runtime_gap_kinds": unit.get("runtime_gap_kinds", []),
                    "runtime_return_to_stages": unit.get("runtime_return_to_stages", []),
                    "topic_queue_ids": unit.get("topic_queue_ids", []),
                    "future_buffered": unit.get("future_buffered", False),
                    "topic_completion_status": unit.get("topic_completion_status", ""),
                    "supporting_regression_question_ids": unit.get("supporting_regression_question_ids", []),
                    "supporting_oracle_ids": unit.get("supporting_oracle_ids", []),
                    "supporting_regression_run_ids": unit.get("supporting_regression_run_ids", []),
                    "promotion_blockers": unit.get("promotion_blockers", []),
                    "split_required": unit.get("split_required", False),
                    "recovery_source_refs": unit.get("recovery_source_refs", []),
                    "path": unit["_path"],
                }
            )
        if unit["type"] == "followup_source_task":
            followup_rows.append(
                {
                    "id": unit["id"],
                    "title": unit["title"],
                    "summary": unit["summary"],
                    "canonical_family": unit.get("canonical_family", ""),
                    "task_status": unit.get("task_status", ""),
                    "recovery_source_type": unit.get("recovery_source_type", ""),
                    "resolves_gaps": unit.get("resolves_gaps", []),
                    "routes_back_to": unit.get("routes_back_to", []),
                    "reentry_targets": unit.get("reentry_targets", []),
                    "runtime_gap_kinds": unit.get("runtime_gap_kinds", []),
                    "runtime_return_to_stages": unit.get("runtime_return_to_stages", []),
                    "topic_queue_ids": unit.get("topic_queue_ids", []),
                    "candidate_sources": unit.get("candidate_sources", []),
                    "path": unit["_path"],
                }
            )
        bucket = domain_index[unit["domain"]]
        bucket["counts_by_type"][unit["type"]] += 1
        bucket["units"].append(unit["id"])
        bucket["tags"].update(unit["tags"])
        if unit.get("canonical_family"):
            family_rows.append(
                {
                    "canonical_family": unit["canonical_family"],
                    "unit_id": unit["id"],
                    "title": unit["title"],
                    "type": unit["type"],
                    "path": unit["_path"],
                }
            )
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

    for queue in sorted(queues.values(), key=lambda item: item["queue_id"]):
        queue_rows.append(
            {
                "queue_id": queue["queue_id"],
                "title": queue["title"],
                "topic": queue["topic"],
                "queue_kind": queue["queue_kind"],
                "summary": queue["summary"],
                "path": queue["_path"],
                "items": queue.get("items", []),
            }
        )

    for suite in sorted(regression_suites.values(), key=lambda item: item["suite_id"]):
        suite_rows.append(
            {
                "suite_id": suite["suite_id"],
                "title": suite["title"],
                "topic": suite["topic"],
                "summary": suite["summary"],
                "source_map_id": suite["source_map_id"],
                "question_ids": suite.get("question_ids", []),
                "oracle_ids": suite.get("oracle_ids", []),
                "focus_units": suite.get("focus_units", []),
                "benchmark_contamination": suite.get("benchmark_contamination", ""),
                "benchmark_use": suite.get("benchmark_use", ""),
                "contamination_notes": suite.get("contamination_notes", ""),
                "path": suite["_path"],
            }
        )

    for log in sorted(regression_logs.values(), key=lambda item: item["run_id"]):
        run_rows.append(
            {
                "run_id": log["run_id"],
                "suite_id": log["suite_id"],
                "status": log["status"],
                "topic_completion_status": log.get("topic_completion_status", ""),
                "promotion_readiness": log.get("promotion_readiness", ""),
                "blocking_unit_ids": log.get("blocking_unit_ids", []),
                "created_at": log["created_at"],
                "results": log.get("results", []),
                "path": log["_path"],
            }
        )

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
    write_jsonl(ROOT / "indexes" / "family_index.jsonl", sorted(family_rows, key=lambda row: (row["canonical_family"], row["unit_id"])))
    write_jsonl(ROOT / "indexes" / "formalization_index.jsonl", formal_rows)
    write_jsonl(ROOT / "indexes" / "gap_index.jsonl", gap_rows)
    write_jsonl(ROOT / "indexes" / "followup_task_index.jsonl", followup_rows)
    write_jsonl(ROOT / "indexes" / "queue_index.jsonl", queue_rows)
    write_jsonl(ROOT / "indexes" / "regression_suite_index.jsonl", suite_rows)
    write_jsonl(ROOT / "indexes" / "regression_run_index.jsonl", run_rows)

    outgoing, incoming = build_edge_maps(edges)
    for unit in sorted_units(units):
        write_text(portal_path_for_unit(unit), render_unit_page(unit, units, outgoing, incoming))

    logs_by_suite = defaultdict(list)
    for log in sorted(regression_logs.values(), key=lambda item: item["run_id"]):
        logs_by_suite[log["suite_id"]].append(log)

    for queue in queues.values():
        write_text(queue_portal_path(queue), render_queue_page(queue, units))
    for suite in regression_suites.values():
        write_text(regression_suite_portal_path(suite), render_regression_suite_page(suite, units, logs_by_suite))
    for log in regression_logs.values():
        write_text(regression_log_portal_path(log), render_regression_log_page(log, units))

    portal_root = ROOT / "portal" / "Topological-Phases-Of-Matter"
    write_text(portal_root / "Index.md", render_index_page(units, manifests, queues, regression_suites, regression_logs))
    manifest = select_exemplar_manifest(manifests)
    if manifest is not None:
        write_text(portal_root / "Lecture-One.md", render_lecture_page(manifest, "lecture-one/", "Lecture One", units))
        write_text(portal_root / "Lecture-Two.md", render_lecture_page(manifest, "lecture-two/", "Lecture Two", units))
        write_text(portal_root / "Lecture-Three.md", render_lecture_page(manifest, "lecture-three/", "Lecture Three", units))

    print(
        "Build completed:",
        f"{len(unit_rows)} units,",
        f"{len(edge_rows)} edges,",
        f"{len(symbol_rows)} symbols,",
        f"{len(anchor_rows)} anchors,",
        f"{len(queues)} queue manifest(s),",
        f"{len(regression_suites)} regression suite(s),",
        f"{len(regression_logs)} regression log(s),",
        f"{len(manifests)} manifest(s),",
        "indexes + portal refreshed.",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
