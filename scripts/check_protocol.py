from __future__ import annotations

import re
import sys

from kb_common import (
    EDGE_RELATIONS,
    load_edges,
    load_manifests,
    load_queue_manifests,
    load_regression_logs,
    load_regression_suites,
    load_units,
    manifest_equation_map,
    manifest_figure_map,
    manifest_section_map,
    sorted_units,
)

ID_RE = re.compile(r"^[a-z_]+:[a-z0-9-]+$")
EDGE_ID_RE = re.compile(r"^edge:[a-z0-9-]+$")
QUEUE_ID_RE = re.compile(r"^queue:[a-z0-9-]+$")
SUITE_ID_RE = re.compile(r"^regression_suite:[a-z0-9-]+$")
RUN_ID_RE = re.compile(r"^regression_run:[a-z0-9-]+$")
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
    "step_inputs",
    "blocking_units",
    "resolution_targets",
    "resolves_gaps",
    "routes_back_to",
    "reentry_targets",
    "mandatory_unit_ids",
    "obligation_ids",
    "supporting_obligation_ids",
    "equation_context_ids",
    "family_member_ids",
    "fusion_member_ids",
    "conflict_unit_ids",
    "primary_retrieval_paths",
    "lean_prerequisite_ids",
    "statement_graph_parents",
    "statement_graph_children",
]
PREFIX_BY_FIELD = {
    "model_refs": "model:",
    "equation_refs": "equation:",
    "quantity_refs": "quantity:",
    "resolves_gaps": "open_gap:",
    "obligation_ids": "proof_obligation:",
    "supporting_obligation_ids": "proof_obligation:",
    "equation_context_ids": "equation_context:",
}
SINGLE_REF_PREFIX_BY_FIELD = {
    "dependency_graph_snapshot_id": "dependency_graph_snapshot:",
}
STRING_LIST_FIELDS = [
    "formal_targets",
    "comparator_risks",
    "attribution_requirements",
    "admissible_assumptions",
    "formalization_blockers",
    "symmetries",
    "failure_modes",
    "retrieval_hints",
    "step_justification",
    "pass_conditions",
    "failure_triggers",
    "derivation_spine",
    "mandatory_equation_labels",
    "mandatory_logical_moves",
    "common_failure_patterns",
    "grading_rubric",
    "promotion_blockers",
    "recovery_source_refs",
    "canonical_questions",
    "scope_boundaries",
    "runtime_gap_kinds",
    "runtime_return_to_stages",
]
LEARNING_NOTE_PROFILE = "learning-note"
LEARNING_NOTE_SUPPORTED_TYPES = {
    "concept",
    "definition",
    "theorem",
    "proof_fragment",
    "derivation_step",
    "equation",
    "quantity",
    "derivation",
    "method",
}
LEARNING_NOTE_REQUIRED_TEXT_FIELDS = [
    "motivation",
    "prerequisite_story",
    "local_context_story",
    "forward_links_story",
]
QUESTION_FAMILIES = {"definition", "derivation", "dependency", "bridge", "gap"}
QUEUE_KINDS = {"unresolved", "prerequisite", "promotion_candidate", "future_buffer"}
QUEUE_STATUSES = {"open", "in_progress", "resolved", "deferred"}
QUEUE_PRIORITIES = {"high", "medium", "low"}
RUN_GRADES = {"pass", "unsafe-pass", "partial", "fail"}
RUN_STATUSES = {"pass", "mixed", "fail"}
LEAN_STATEMENT_KINDS = {"definition", "theorem", "lemma", "structure", "scaffold", "namespace-plan"}
FORMAL_THEORY_ROLES = {"trusted_target", "intermediate_theory", "supporting_context"}
DEFINITION_TRUST_TIERS = {"trusted", "reviewed_translation", "provisional", "scaffold_only"}
STATEMENT_GRAPH_ROLES = {"target_statement", "prerequisite", "intermediate_lemma", "temporary_scaffold", "explanatory_bridge"}
FAITHFULNESS_STATUSES = {"not_applicable", "pending", "bounded", "reviewed"}
COMPARATOR_AUDIT_STATUSES = {"not_applicable", "pending", "passed", "failed"}
PROVENANCE_KINDS = {
    "source_derived",
    "retrieved_existing_formalization",
    "adapted_existing_formalization",
    "generated_from_scratch",
    "mixed",
}
PREREQUISITE_CLOSURE_STATUSES = {"not_needed", "pending", "partial", "closed"}
RUNTIME_GAP_KINDS = {
    "missing_definition",
    "missing_lemma",
    "missing_cited_result",
    "missing_derivation_step",
    "cross_paper_dependency",
    "formalization_blocker",
}
RUNTIME_RETURN_TO_STAGES = {"L0", "L1", "L3", "L4_formalization"}
TOPIC_COMPLETION_STATUSES = {
    "not_assessed",
    "gap-aware",
    "regression-seeded",
    "regression-stable",
    "promotion-blocked",
    "promotion-ready",
}
PROMOTION_READINESS_STATUSES = {"not-assessed", "ready", "blocked", "future-buffer"}
PROMOTION_SURFACE_UNIT_TYPES = {"theorem", "theorem_family", "proof_state", "source_fusion_record"}
GAP_KINDS = {"missing-proof", "missing-background", "missing-bridge", "missing-notation", "source-omitted", "too-wide-topic"}
RECOVERY_SOURCE_TYPES = {"cited-paper", "standard-reference", "neighboring-paper", "deferred"}
FOLLOWUP_TASK_STATUSES = {"created", "source-selected", "l1-analyzed", "l3-shaped", "resolved-into-l2", "retired", "superseded"}
BENCHMARK_CONTAMINATION_STATUSES = {"clean", "contaminated", "internal-only", "unknown"}
BENCHMARK_USES = {"workflow_regression", "research_iteration", "external_evaluation"}


def run_checks() -> dict:
    units = load_units()
    manifests = load_manifests()
    edges = load_edges()
    queues = load_queue_manifests()
    regression_suites = load_regression_suites()
    regression_logs = load_regression_logs()
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
        if "canonical_family" in unit and not isinstance(unit["canonical_family"], str):
            errors.append(f"{unit['_path']}: canonical_family must be a string if present")
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
                    continue
                prefix = PREFIX_BY_FIELD.get(field)
                if prefix and not ref.startswith(prefix):
                    errors.append(f"{unit['_path']}: reference '{ref}' in field '{field}' must start with '{prefix}'")
        if "step_output" in unit:
            ref = unit["step_output"]
            if not isinstance(ref, str):
                errors.append(f"{unit['_path']}: step_output must be a string if present")
            elif ref not in units:
                errors.append(f"{unit['_path']}: unknown step_output '{ref}'")
        if "target_statement_id" in unit:
            ref = unit["target_statement_id"]
            if not isinstance(ref, str):
                errors.append(f"{unit['_path']}: target_statement_id must be a string if present")
            elif ref not in units:
                errors.append(f"{unit['_path']}: unknown target_statement_id '{ref}'")
        for field, prefix in SINGLE_REF_PREFIX_BY_FIELD.items():
            if field not in unit:
                continue
            ref = unit[field]
            if not isinstance(ref, str):
                errors.append(f"{unit['_path']}: field '{field}' must be a string if present")
                continue
            if ref not in units:
                errors.append(f"{unit['_path']}: unknown reference '{ref}' in field '{field}'")
            elif not ref.startswith(prefix):
                errors.append(f"{unit['_path']}: reference '{ref}' in field '{field}' must start with '{prefix}'")
        for field in STRING_LIST_FIELDS:
            if field in unit and not isinstance(unit[field], list):
                errors.append(f"{unit['_path']}: optional field '{field}' must be a list if present")
            for value in unit.get(field, []):
                if not isinstance(value, str):
                    errors.append(f"{unit['_path']}: field '{field}' must contain only strings")
        for field in LEARNING_NOTE_REQUIRED_TEXT_FIELDS:
            if field in unit and not isinstance(unit[field], str):
                errors.append(f"{unit['_path']}: optional field '{field}' must be a string if present")
        for field in (
            "lean_namespace",
            "lean_declaration",
            "lean_statement_kind",
            "formal_theory_role",
            "definition_trust_tier",
            "statement_graph_role",
            "faithfulness_status",
            "faithfulness_strategy",
            "faithfulness_notes",
            "comparator_audit_status",
            "provenance_kind",
            "prerequisite_closure_status",
        ):
            if field in unit and not isinstance(unit[field], str):
                errors.append(f"{unit['_path']}: field '{field}' must be a string if present")
        if unit.get("lean_statement_kind") and unit.get("lean_statement_kind") not in LEAN_STATEMENT_KINDS:
            errors.append(
                f"{unit['_path']}: lean_statement_kind must be in {sorted(LEAN_STATEMENT_KINDS)}"
            )
        if unit.get("formal_theory_role") and unit.get("formal_theory_role") not in FORMAL_THEORY_ROLES:
            errors.append(f"{unit['_path']}: formal_theory_role must be in {sorted(FORMAL_THEORY_ROLES)}")
        if unit.get("definition_trust_tier") and unit.get("definition_trust_tier") not in DEFINITION_TRUST_TIERS:
            errors.append(f"{unit['_path']}: definition_trust_tier must be in {sorted(DEFINITION_TRUST_TIERS)}")
        if unit.get("statement_graph_role") and unit.get("statement_graph_role") not in STATEMENT_GRAPH_ROLES:
            errors.append(f"{unit['_path']}: statement_graph_role must be in {sorted(STATEMENT_GRAPH_ROLES)}")
        if unit.get("faithfulness_status") and unit.get("faithfulness_status") not in FAITHFULNESS_STATUSES:
            errors.append(f"{unit['_path']}: faithfulness_status must be in {sorted(FAITHFULNESS_STATUSES)}")
        if unit.get("comparator_audit_status") and unit.get("comparator_audit_status") not in COMPARATOR_AUDIT_STATUSES:
            errors.append(
                f"{unit['_path']}: comparator_audit_status must be in {sorted(COMPARATOR_AUDIT_STATUSES)}"
            )
        if unit.get("provenance_kind") and unit.get("provenance_kind") not in PROVENANCE_KINDS:
            errors.append(f"{unit['_path']}: provenance_kind must be in {sorted(PROVENANCE_KINDS)}")
        if unit.get("prerequisite_closure_status") and unit.get("prerequisite_closure_status") not in PREREQUISITE_CLOSURE_STATUSES:
            errors.append(
                f"{unit['_path']}: prerequisite_closure_status must be in {sorted(PREREQUISITE_CLOSURE_STATUSES)}"
            )
        if unit.get("formal_theory_role") and not unit.get("statement_graph_role"):
            errors.append(f"{unit['_path']}: formal_theory_role requires statement_graph_role")
        if unit.get("formal_theory_role") == "intermediate_theory" and not str(unit.get("target_statement_id") or "").strip():
            errors.append(f"{unit['_path']}: intermediate_theory unit requires target_statement_id")
        if unit.get("faithfulness_status") not in {None, "not_applicable"} and not str(unit.get("faithfulness_strategy") or "").strip():
            errors.append(f"{unit['_path']}: faithfulness_status requires non-empty faithfulness_strategy")
        if unit.get("provenance_kind") and not unit.get("attribution_requirements"):
            errors.append(f"{unit['_path']}: provenance_kind requires non-empty attribution_requirements")
        if unit.get("comparator_audit_status") == "failed" and not unit.get("comparator_risks"):
            errors.append(f"{unit['_path']}: failed comparator audit requires comparator_risks")
        for value in unit.get("runtime_gap_kinds", []):
            if value not in RUNTIME_GAP_KINDS:
                errors.append(
                    f"{unit['_path']}: runtime_gap_kinds must stay within {sorted(RUNTIME_GAP_KINDS)}"
                )
        for value in unit.get("runtime_return_to_stages", []):
            if value not in RUNTIME_RETURN_TO_STAGES:
                errors.append(
                    f"{unit['_path']}: runtime_return_to_stages must stay within {sorted(RUNTIME_RETURN_TO_STAGES)}"
                )
        profile = str(unit.get("human_projection_profile") or "").strip()
        if profile and profile not in {"card", LEARNING_NOTE_PROFILE}:
            errors.append(f"{unit['_path']}: invalid human_projection_profile '{profile}'")
        if profile == LEARNING_NOTE_PROFILE:
            if unit_type not in LEARNING_NOTE_SUPPORTED_TYPES:
                errors.append(
                    f"{unit['_path']}: human_projection_profile '{LEARNING_NOTE_PROFILE}' "
                    f"is not supported for type '{unit_type}'"
                )
            for field in LEARNING_NOTE_REQUIRED_TEXT_FIELDS:
                if not str(unit.get(field) or "").strip():
                    errors.append(
                        f"{unit['_path']}: learning-note unit requires non-empty '{field}'"
                    )
            questions = [str(x).strip() for x in (unit.get("canonical_questions") or []) if str(x).strip()]
            if not questions:
                errors.append(f"{unit['_path']}: learning-note unit requires non-empty canonical_questions")
            boundaries = [str(x).strip() for x in (unit.get("scope_boundaries") or []) if str(x).strip()]
            failure_modes = [str(x).strip() for x in (unit.get("failure_modes") or []) if str(x).strip()]
            if not boundaries and not failure_modes:
                errors.append(
                    f"{unit['_path']}: learning-note unit requires scope_boundaries or failure_modes"
                )
            has_anchor_equations = any(
                isinstance(anchor, dict) and any(str(label).strip() for label in (anchor.get("equation_labels") or []))
                for anchor in unit.get("source_anchors", [])
            )
            if has_anchor_equations and not unit.get("math_expressions"):
                errors.append(
                    f"{unit['_path']}: learning-note unit with anchored equation labels requires math_expressions"
                )
        if "symbols" in unit:
            if not isinstance(unit["symbols"], list):
                errors.append(f"{unit['_path']}: symbols must be a list if present")
            for symbol in unit["symbols"]:
                if not isinstance(symbol, dict) or "symbol" not in symbol or "meaning" not in symbol:
                    errors.append(f"{unit['_path']}: each symbol entry needs 'symbol' and 'meaning'")
        if "math_expressions" in unit:
            if not isinstance(unit["math_expressions"], list):
                errors.append(f"{unit['_path']}: math_expressions must be a list if present")
            for expr in unit["math_expressions"]:
                if not isinstance(expr, dict) or "latex" not in expr:
                    errors.append(f"{unit['_path']}: each math expression needs a 'latex' field")
        if "candidate_sources" in unit:
            if not isinstance(unit["candidate_sources"], list):
                errors.append(f"{unit['_path']}: candidate_sources must be a list if present")
            for candidate in unit["candidate_sources"]:
                if not isinstance(candidate, dict) or "citation" not in candidate:
                    errors.append(f"{unit['_path']}: each candidate source must include 'citation'")
        if "topic_completion_status" in unit and unit.get("topic_completion_status") not in TOPIC_COMPLETION_STATUSES:
            errors.append(
                f"{unit['_path']}: topic_completion_status must be in {sorted(TOPIC_COMPLETION_STATUSES)}"
            )
        if "topic_queue_ids" in unit and not isinstance(unit.get("topic_queue_ids"), list):
            errors.append(f"{unit['_path']}: field 'topic_queue_ids' must be a list")
        for queue_id in unit.get("topic_queue_ids", []):
            if not isinstance(queue_id, str):
                errors.append(f"{unit['_path']}: topic_queue_ids must contain only strings")
            elif queue_id not in queues:
                errors.append(f"{unit['_path']}: unknown queue '{queue_id}' in field 'topic_queue_ids'")
        for field, prefix in (
            ("supporting_regression_question_ids", "regression_question:"),
            ("supporting_oracle_ids", "question_oracle:"),
        ):
            value = unit.get(field, [])
            if field in unit and not isinstance(value, list):
                errors.append(f"{unit['_path']}: field '{field}' must be a list")
                continue
            for ref in value:
                if ref not in units:
                    errors.append(f"{unit['_path']}: unknown reference '{ref}' in field '{field}'")
                elif not ref.startswith(prefix):
                    errors.append(f"{unit['_path']}: reference '{ref}' in field '{field}' must start with '{prefix}'")
        if "supporting_regression_run_ids" in unit and not isinstance(unit.get("supporting_regression_run_ids"), list):
            errors.append(f"{unit['_path']}: field 'supporting_regression_run_ids' must be a list")
        for run_id in unit.get("supporting_regression_run_ids", []):
            if not RUN_ID_RE.match(run_id):
                errors.append(f"{unit['_path']}: invalid supporting regression run id '{run_id}'")
        if "split_required" in unit and not isinstance(unit.get("split_required"), bool):
            errors.append(f"{unit['_path']}: split_required must be a boolean if present")
        completion_status = unit.get("topic_completion_status")
        if unit_type in PROMOTION_SURFACE_UNIT_TYPES and completion_status in {
            "regression-stable",
            "promotion-blocked",
            "promotion-ready",
        }:
            if not unit.get("supporting_regression_question_ids"):
                errors.append(
                    f"{unit['_path']}: promotion-surface unit with topic_completion_status '{completion_status}' "
                    "requires supporting_regression_question_ids"
                )
            if not unit.get("supporting_oracle_ids"):
                errors.append(
                    f"{unit['_path']}: promotion-surface unit with topic_completion_status '{completion_status}' "
                    "requires supporting_oracle_ids"
                )
            if not unit.get("supporting_regression_run_ids"):
                errors.append(
                    f"{unit['_path']}: promotion-surface unit with topic_completion_status '{completion_status}' "
                    "requires supporting_regression_run_ids"
                )
        if "lean" in unit.get("formal_targets", []) and unit_type in {
            "theorem_family",
            "proof_state",
            "proof_obligation",
        }:
            if not str(unit.get("lean_namespace") or "").strip():
                errors.append(f"{unit['_path']}: lean-target unit requires non-empty lean_namespace")
            if not str(unit.get("lean_statement_kind") or "").strip():
                errors.append(f"{unit['_path']}: lean-target unit requires non-empty lean_statement_kind")
            if not str(
                unit.get("lean_declaration") or ""
            ).strip():
                errors.append(f"{unit['_path']}: {unit_type} with lean target requires lean_declaration")
        if completion_status == "promotion-ready":
            if unit.get("promotion_blockers"):
                errors.append(f"{unit['_path']}: promotion-ready unit cannot keep promotion_blockers")
            if unit.get("split_required"):
                errors.append(f"{unit['_path']}: promotion-ready unit cannot set split_required=true")
        if unit_type == "regression_question":
            family = unit.get("question_family")
            if family not in QUESTION_FAMILIES:
                errors.append(f"{unit['_path']}: regression_question requires question_family in {sorted(QUESTION_FAMILIES)}")
            if not unit.get("prompt"):
                errors.append(f"{unit['_path']}: regression_question requires non-empty prompt")
            if not unit.get("primary_retrieval_paths"):
                errors.append(f"{unit['_path']}: regression_question requires non-empty primary_retrieval_paths")
            if not unit.get("pass_conditions"):
                errors.append(f"{unit['_path']}: regression_question requires non-empty pass_conditions")
        if unit_type == "question_oracle":
            if not unit.get("mandatory_unit_ids"):
                errors.append(f"{unit['_path']}: question_oracle requires non-empty mandatory_unit_ids")
            if not unit.get("grading_rubric"):
                errors.append(f"{unit['_path']}: question_oracle requires non-empty grading_rubric")
            if not unit.get("common_failure_patterns"):
                errors.append(f"{unit['_path']}: question_oracle requires non-empty common_failure_patterns")
            if not unit.get("failure_triggers"):
                errors.append(f"{unit['_path']}: question_oracle requires non-empty failure_triggers")
            linked_question_ids = [
                ref for ref in unit.get("dependencies", []) if isinstance(ref, str) and ref.startswith("regression_question:")
            ]
            linked_families = {
                str(units[ref].get("question_family") or "")
                for ref in linked_question_ids
                if ref in units
            }
            if linked_families.intersection({"derivation", "bridge", "dependency"}) and not unit.get("derivation_spine"):
                errors.append(
                    f"{unit['_path']}: question_oracle linked to {sorted(linked_families)} requires non-empty derivation_spine"
                )
        if unit_type == "open_gap":
            if unit.get("gap_kind") not in GAP_KINDS:
                errors.append(f"{unit['_path']}: open_gap requires gap_kind in {sorted(GAP_KINDS)}")
            if unit.get("recovery_source_type") not in RECOVERY_SOURCE_TYPES:
                errors.append(
                    f"{unit['_path']}: open_gap requires recovery_source_type in {sorted(RECOVERY_SOURCE_TYPES)}"
                )
            if not unit.get("reentry_targets"):
                errors.append(f"{unit['_path']}: open_gap requires non-empty reentry_targets")
            if unit.get("runtime_gap_kinds") and not unit.get("topic_queue_ids"):
                errors.append(f"{unit['_path']}: open_gap with runtime_gap_kinds requires non-empty topic_queue_ids")
        if unit_type == "followup_source_task":
            if unit.get("task_status") not in FOLLOWUP_TASK_STATUSES:
                errors.append(
                    f"{unit['_path']}: followup_source_task requires task_status in {sorted(FOLLOWUP_TASK_STATUSES)}"
                )
            if unit.get("recovery_source_type") not in RECOVERY_SOURCE_TYPES:
                errors.append(
                    f"{unit['_path']}: followup_source_task requires recovery_source_type in {sorted(RECOVERY_SOURCE_TYPES)}"
                )
            if not unit.get("reentry_targets"):
                errors.append(f"{unit['_path']}: followup_source_task requires non-empty reentry_targets")
            if unit.get("runtime_gap_kinds") and not unit.get("topic_queue_ids"):
                errors.append(
                    f"{unit['_path']}: followup_source_task with runtime_gap_kinds requires non-empty topic_queue_ids"
                )
        if unit_type == "proof_obligation":
            if not unit.get("pass_conditions"):
                errors.append(f"{unit['_path']}: proof_obligation requires non-empty pass_conditions")
            if not unit.get("mandatory_logical_moves"):
                errors.append(f"{unit['_path']}: proof_obligation requires non-empty mandatory_logical_moves")
        if unit_type == "proof_state" and not unit.get("obligation_ids"):
            errors.append(f"{unit['_path']}: proof_state requires non-empty obligation_ids")
        if unit_type == "equation_context" and not (unit.get("math_expressions") or unit.get("symbols")):
            errors.append(f"{unit['_path']}: equation_context requires math_expressions or symbols")
        if unit_type == "dependency_graph_snapshot":
            if not unit.get("mandatory_unit_ids"):
                errors.append(f"{unit['_path']}: dependency_graph_snapshot requires non-empty mandatory_unit_ids")
            if not unit.get("derivation_spine"):
                errors.append(f"{unit['_path']}: dependency_graph_snapshot requires non-empty derivation_spine")
        if unit_type in {"theorem_family", "definition_family", "notation_family"} and not unit.get("family_member_ids"):
            errors.append(f"{unit['_path']}: {unit_type} requires non-empty family_member_ids")
        if unit_type == "source_fusion_record" and not unit.get("fusion_member_ids"):
            errors.append(f"{unit['_path']}: source_fusion_record requires non-empty fusion_member_ids")
        if unit_type == "conflict_record" and not unit.get("conflict_unit_ids"):
            errors.append(f"{unit['_path']}: conflict_record requires non-empty conflict_unit_ids")

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

    for queue_id, queue in sorted(queues.items()):
        if not QUEUE_ID_RE.match(queue_id):
            errors.append(f"{queue['_path']}: invalid queue_id '{queue_id}'")
        for field in ("queue_id", "title", "topic", "queue_kind", "summary", "items", "created_at", "updated_at"):
            if field not in queue:
                errors.append(f"{queue['_path']}: missing required field '{field}'")
        if queue.get("queue_kind") not in QUEUE_KINDS:
            errors.append(f"{queue['_path']}: invalid queue_kind '{queue.get('queue_kind')}'")
        if not isinstance(queue.get("items", []), list):
            errors.append(f"{queue['_path']}: items must be a list")
            continue
        for item in queue.get("items", []):
            if not isinstance(item, dict) or "unit_id" not in item or "status" not in item or "priority" not in item:
                errors.append(f"{queue['_path']}: each queue item needs unit_id, status, and priority")
                continue
            if item["unit_id"] not in units:
                errors.append(f"{queue['_path']}: unknown queued unit '{item['unit_id']}'")
            if item["status"] not in QUEUE_STATUSES:
                errors.append(f"{queue['_path']}: invalid queue status '{item['status']}'")
            if item["priority"] not in QUEUE_PRIORITIES:
                errors.append(f"{queue['_path']}: invalid queue priority '{item['priority']}'")

    for suite_id, suite in sorted(regression_suites.items()):
        if not SUITE_ID_RE.match(suite_id):
            errors.append(f"{suite['_path']}: invalid suite_id '{suite_id}'")
        for field in ("suite_id", "title", "topic", "summary", "source_map_id", "question_ids", "oracle_ids", "created_at", "updated_at"):
            if field not in suite:
                errors.append(f"{suite['_path']}: missing required field '{field}'")
        if "benchmark_contamination" in suite and suite.get("benchmark_contamination") not in BENCHMARK_CONTAMINATION_STATUSES:
            errors.append(
                f"{suite['_path']}: benchmark_contamination must be in {sorted(BENCHMARK_CONTAMINATION_STATUSES)}"
            )
        if "benchmark_use" in suite and suite.get("benchmark_use") not in BENCHMARK_USES:
            errors.append(f"{suite['_path']}: benchmark_use must be in {sorted(BENCHMARK_USES)}")
        if "contamination_notes" in suite and not isinstance(suite.get("contamination_notes"), str):
            errors.append(f"{suite['_path']}: contamination_notes must be a string if present")
        if suite.get("benchmark_use") == "external_evaluation" and suite.get("benchmark_contamination") != "clean":
            errors.append(
                f"{suite['_path']}: external_evaluation suites must declare benchmark_contamination='clean'"
            )
        source_map_id = suite.get("source_map_id")
        if source_map_id not in units:
            errors.append(f"{suite['_path']}: unknown source_map_id '{source_map_id}'")
        elif not source_map_id.startswith("source_map:"):
            errors.append(f"{suite['_path']}: source_map_id must point to a source_map unit")
        for field, prefix in (("question_ids", "regression_question:"), ("oracle_ids", "question_oracle:")):
            value = suite.get(field, [])
            if not isinstance(value, list):
                errors.append(f"{suite['_path']}: field '{field}' must be a list")
                continue
            for ref in value:
                if ref not in units:
                    errors.append(f"{suite['_path']}: unknown reference '{ref}' in field '{field}'")
                elif not ref.startswith(prefix):
                    errors.append(f"{suite['_path']}: reference '{ref}' in field '{field}' must start with '{prefix}'")
        for ref in suite.get("focus_units", []):
            if ref not in units:
                errors.append(f"{suite['_path']}: unknown focus unit '{ref}'")

    for run_id, log in sorted(regression_logs.items()):
        if not RUN_ID_RE.match(run_id):
            errors.append(f"{log['_path']}: invalid run_id '{run_id}'")
        for field in ("run_id", "suite_id", "status", "results", "created_at"):
            if field not in log:
                errors.append(f"{log['_path']}: missing required field '{field}'")
        suite_id = log.get("suite_id")
        suite = regression_suites.get(suite_id)
        if suite is None:
            errors.append(f"{log['_path']}: unknown suite_id '{suite_id}'")
        if log.get("status") not in RUN_STATUSES:
            errors.append(f"{log['_path']}: invalid run status '{log.get('status')}'")
        if "topic_completion_status" in log and log.get("topic_completion_status") not in TOPIC_COMPLETION_STATUSES:
            errors.append(
                f"{log['_path']}: topic_completion_status must be in {sorted(TOPIC_COMPLETION_STATUSES)}"
            )
        if "promotion_readiness" in log and log.get("promotion_readiness") not in PROMOTION_READINESS_STATUSES:
            errors.append(
                f"{log['_path']}: promotion_readiness must be in {sorted(PROMOTION_READINESS_STATUSES)}"
            )
        if "blocking_unit_ids" in log and not isinstance(log.get("blocking_unit_ids"), list):
            errors.append(f"{log['_path']}: blocking_unit_ids must be a list")
        for ref in log.get("blocking_unit_ids", []):
            if ref not in units:
                errors.append(f"{log['_path']}: unknown blocking unit '{ref}'")
        if not isinstance(log.get("results", []), list):
            errors.append(f"{log['_path']}: results must be a list")
            continue
        suite_question_ids = set(suite.get("question_ids", [])) if suite else set()
        suite_oracle_ids = set(suite.get("oracle_ids", [])) if suite else set()
        for result in log.get("results", []):
            if not isinstance(result, dict) or "question_id" not in result or "oracle_id" not in result or "grade" not in result:
                errors.append(f"{log['_path']}: each regression result needs question_id, oracle_id, and grade")
                continue
            if result["question_id"] not in units:
                errors.append(f"{log['_path']}: unknown question '{result['question_id']}'")
            elif suite and result["question_id"] not in suite_question_ids:
                errors.append(f"{log['_path']}: question '{result['question_id']}' is not declared in suite '{suite_id}'")
            if result["oracle_id"] not in units:
                errors.append(f"{log['_path']}: unknown oracle '{result['oracle_id']}'")
            elif suite and result["oracle_id"] not in suite_oracle_ids:
                errors.append(f"{log['_path']}: oracle '{result['oracle_id']}' is not declared in suite '{suite_id}'")
            if result["grade"] not in RUN_GRADES:
                errors.append(f"{log['_path']}: invalid grade '{result['grade']}'")
            for ref in result.get("writeback_unit_ids", []):
                if ref not in units:
                    errors.append(f"{log['_path']}: unknown writeback unit '{ref}'")
        if log.get("promotion_readiness") == "ready":
            if log.get("status") != "pass":
                errors.append(f"{log['_path']}: promotion_readiness=ready requires status=pass")
            if log.get("blocking_unit_ids"):
                errors.append(f"{log['_path']}: promotion_readiness=ready requires empty blocking_unit_ids")
        if log.get("promotion_readiness") == "blocked" and not log.get("blocking_unit_ids"):
            errors.append(f"{log['_path']}: promotion_readiness=blocked requires blocking_unit_ids")

    return {
        "units": units,
        "manifests": manifests,
        "edges": edges,
        "queues": queues,
        "regression_suites": regression_suites,
        "regression_logs": regression_logs,
        "errors": errors,
    }


def main() -> int:
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
        f"{len(result['manifests'])} source manifest(s),",
        f"{len(result['queues'])} queue manifest(s),",
        f"{len(result['regression_suites'])} regression suite(s),",
        f"{len(result['regression_logs'])} regression log(s).",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
