# Object Model

## Source Of Truth

The kernel now has five canonical surfaces:

- `sources/`: public source manifests
- `units/`: reusable typed knowledge objects
- `edges/`: typed graph relations
- `queues/`: durable unresolved and prerequisite routing state
- `regressions/`: topic regression manifests and pass logs

Everything else is a projection.

## Unit Families

Current unit families are:

- `concept`
- `definition`
- `theorem`
- `lemma`
- `equivalence`
- `conjecture`
- `theorem_family`
- `definition_family`
- `notation_family`
- `feasibility_question`
- `dependency_request`
- `proof_search_request`
- `equation`
- `equation_context`
- `quantity`
- `claim`
- `derivation`
- `proof_fragment`
- `proof_obligation`
- `proof_state`
- `derivation_step`
- `dependency_graph_snapshot`
- `method`
- `model`
- `warning`
- `bridge`
- `notation_map`
- `source_fusion_record`
- `conflict_record`
- `open_gap`
- `question_oracle`
- `regression_question`
- `followup_source_task`
- `source_map`

The point of the expanded family list is simple:

- concepts and equations are not enough for proof-grade theoretical-physics notes;
- derivation steps and proof fragments must be promotable as first-class objects;
- proof obligations and proof states must survive as first-class objects when a theorem family is too detailed for one card;
- equation contexts and dependency-graph snapshots must carry the exact local role of formulas and prerequisites;
- theorem or notation families must be allowed to fuse several source-local views without erasing source-local differences;
- unresolved prerequisites and regression assets must also be durable rather than hidden in agent memory.

## Required Common Fields

Every unit still carries the common backbone:

- `id`
- `type`
- `title`
- `summary`
- `domain`
- `tags`
- `aliases`
- `assumptions`
- `regime`
- `scope`
- `dependencies`
- `related_units`
- `source_anchors`
- `formalization_status`
- `validation_status`
- `maturity`
- `created_at`
- `updated_at`

## Extended Proof-Grade Fields

Units may additionally carry structured proof-facing fields such as:

- `human_projection_profile`
- `motivation`
- `prerequisite_story`
- `local_context_story`
- `forward_links_story`
- `canonical_questions`
- `scope_boundaries`
- `math_expressions`
- `symbols`
- `step_inputs`
- `step_output`
- `step_justification`
- `source_omission_flag`
- `followup_required`
- `prompt`
- `question_family`
- `primary_retrieval_paths`
- `pass_conditions`
- `mandatory_unit_ids`
- `mandatory_equation_labels`
- `obligation_ids`
- `supporting_obligation_ids`
- `equation_context_ids`
- `dependency_graph_snapshot_id`
- `family_member_ids`
- `fusion_member_ids`
- `conflict_unit_ids`
- `derivation_spine`
- `mandatory_logical_moves`
- `common_failure_patterns`
- `grading_rubric`
- `failure_triggers`
- `blocking_units`
- `resolution_targets`
- `resolves_gaps`
- `routes_back_to`
- `candidate_sources`
- `canonical_family`
- `formal_theory_role`
- `definition_trust_tier`
- `statement_graph_role`
- `statement_graph_parents`
- `statement_graph_children`
- `target_statement_id`
- `faithfulness_status`
- `faithfulness_strategy`
- `faithfulness_notes`
- `comparator_audit_status`
- `comparator_risks`
- `provenance_kind`
- `attribution_requirements`
- `prerequisite_closure_status`
- `lean_namespace`
- `lean_declaration`
- `lean_statement_kind`
- `admissible_assumptions`
- `lean_prerequisite_ids`
- `formalization_blockers`
- `gap_kind`
- `recovery_source_type`
- `task_status`
- `reentry_targets`
- `future_buffered`
- `runtime_gap_kinds`
- `runtime_return_to_stages`
- `topic_queue_ids`

These fields exist so that a derivation or oracle can expose formulas, assumptions, and missing prerequisites explicitly instead of collapsing into prose.

The Lean-planning fields have a narrower role:

- `lean_namespace`, `lean_declaration`, and `lean_statement_kind` say what the eventual formal object should be;
- `admissible_assumptions` records which physics assumptions are allowed to remain at the wrapper statement;
- `lean_prerequisite_ids` names the supporting local declarations or proof obligations;
- `formalization_blockers` records what still prevents honest formalization.

The newer formal-theory governance fields answer a different question: even if a
Lean-facing plan exists, what exactly is being trusted?

- `formal_theory_role` separates trusted targets from intermediate theory and supporting context
- `statement_graph_role`, `statement_graph_parents`, and `statement_graph_children` make the local statement graph explicit
- `target_statement_id` says which trusted target an intermediate scaffold is serving
- `definition_trust_tier` records whether a translated definition is already trusted, only reviewed as a translation, still provisional, or merely scaffold-level
- `faithfulness_status`, `faithfulness_strategy`, and `faithfulness_notes` record whether the current unit still matches the scientific source claim
- `comparator_audit_status` and `comparator_risks` record the anti-cheat comparison against nearby weakened statements
- `provenance_kind` and `attribution_requirements` record where the current formal material came from and what reuse obligations remain
- `prerequisite_closure_status` says whether the prerequisite graph is actually closed or still pending/partial

For promotion-grade AITP branches, these unit-local fields should be backed by
durable kernel review artifacts in the matching `theory-packets/<candidate>/`
directory. The most important artifacts are:

- `faithfulness_review.json`
- `comparator_audit_record.json`
- `provenance_review.json`
- `prerequisite_closure_review.json`
- `formal_theory_review.json/.md`

The KB object model does not force one fixed field name for those external
paths, but the review ledger itself is part of the intended protocol surface.

The newer human-projection fields exist for a different but related reason: a typed unit may be retrieval-ready yet still be confusing when mirrored directly for study. `human_projection_profile: "learning-note"` marks the units that must carry enough context to read as standalone learning pages rather than anonymous graph nodes.

`canonical_family` is the first explicit multi-source fusion field. It groups source-specific presentations that belong to the same reusable theorem or derivation family.

The newer family and fusion objects make that grouping auditable:

- `theorem_family`, `definition_family`, and `notation_family` collect the reusable members;
- `source_fusion_record` explains why the grouping is legitimate;
- `conflict_record` preserves unresolved differences instead of hiding them.

`gap_kind`, `recovery_source_type`, `task_status`, and `reentry_targets` make the `open_gap` and `followup_source_task` lifecycle explicit instead of leaving recovery routing implicit in prose.

The runtime-gap bridge fields finish the loop:

- `runtime_gap_kinds` says which AITP follow-up gap kinds should map back to this topic object;
- `runtime_return_to_stages` records the recovery stage expected by the runtime gap contract;
- `topic_queue_ids` records which durable queue surfaces should carry the gap on the topic side.

## Queue And Regression Surfaces

`queues/` stores durable topic-level work routing:

- unresolved queues
- prerequisite queues
- promotion-candidate queues
- future-research buffers

`regressions/` stores:

- suite manifests
- latest or historical run logs

Regression suites may also expose benchmark-governance metadata:

- `benchmark_contamination`
- `benchmark_use`
- `contamination_notes`

The queue and regression layers are canonical because downstream automation needs stable failure writeback targets.

Topic-level regression is now first-class, not only paper-local regression. A topic suite may span several source manifests if the regression surface represents a fused canonical family rather than one paper.

## Edge Layer

Edges remain separate from units.

The current relation vocabulary includes the original semantic relations plus workflow-facing relations:

- `tests`
- `oracles`
- `blocked_by`
- `resolves`
- `routes_to`

These relations are intentionally limited. They exist only because proof-grade regression and gap routing became part of the canonical design.

## Projection Surfaces

- `indexes/` are deterministic retrieval surfaces for agents and scripts.
- `portal/` is the generated human-readable projection.

The portal is intentionally secondary to the typed object store and the queue/regression state.
