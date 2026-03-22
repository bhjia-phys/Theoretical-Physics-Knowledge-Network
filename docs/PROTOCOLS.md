# Protocols

This file is the normative contract for `open-physics-kb`.

See also:

- `docs/L2_RETRIEVAL_PROTOCOL.md`
- `docs/PAPER_INGESTION_QUALITY_PROTOCOL.md`
- `docs/TOPIC_REGRESSION_SUITE_PROTOCOL.md`
- `docs/TOPIC_COMPLETION_PROTOCOL.md`

## P0. Repository Role

The repository is a standalone theoretical-physics knowledge kernel.

It must remain:

- independent from Obsidian as the source of truth
- independent from AITP runtime orchestration
- compatible with typed `L2` retrieval
- readable to humans through generated portal projections
- explicit about unresolved proof gaps and their follow-up routing

## P1. Canonical Storage Protocol

The canonical surfaces are:

- `sources/`
- `units/`
- `edges/`
- `queues/`
- `regressions/`

The projection surfaces are:

- `indexes/`
- `portal/`

Generated projections must never be hand-edited as the authoritative source.

## P2. Unit Protocol

Every reusable knowledge object must:

- live in exactly one JSON file under the matching `units/<family>/` directory
- carry a stable typed id such as `concept:weyl-node`
- expose explicit scope, regime, assumptions, dependencies, and source anchors
- expose explicit mathematical content whenever the source contains it
- record formalization and validation status
- stay small enough to serve retrieval rather than only archival storage

The expanded family list exists because proof-grade theoretical-physics work needs more than concepts and equations:

- `definition`, `theorem`, `lemma`, `equivalence`
- `proof_fragment`, `proof_obligation`, `proof_state`, `derivation_step`, `dependency_graph_snapshot`
- `equation_context`
- `theorem_family`, `definition_family`, `notation_family`, `source_fusion_record`, `conflict_record`
- `notation_map`
- `open_gap`
- `regression_question`, `question_oracle`
- `followup_source_task`

Mathematical-content rule:

- a formal unit must not hide its key equation, invariant formula, or boundary condition only inside `summary`
- when the source presents a concrete displayed equation or compact formula, store it in `math_expressions`
- when the source introduces symbols reused downstream, store them in `symbols`
- `representation` is interpretive prose, not a substitute for the equation itself

Human-learning projection rule:

- units that should project to a standalone learning page rather than a thin object card must set `human_projection_profile: "learning-note"`
- such units must explain why the note exists, what must already be understood, where the note sits in the local source argument, and what it feeds into next
- the minimal explanatory field set is:
  - `motivation`
  - `prerequisite_story`
  - `local_context_story`
  - `forward_links_story`
  - `canonical_questions`
- a learning-note unit must also expose explicit scope boundaries through `scope_boundaries` or `failure_modes`
- if a learning-note unit claims anchored source equations, it must expose the corresponding formulas in `math_expressions`
- this gate exists because a retrieval-ready unit that remains unreadable as a standalone learning page is not yet good enough for theoretical-physics study

Derivation-detail rule:

- theorem-like and derivation-like units must preserve as much of the source derivation spine as the source actually gives
- do not compress a multi-step argument into a one-sentence summary when the source provides intermediate constructions or formulas
- whenever a nontrivial conclusion depends on an intermediate formula, that formula should appear explicitly in `math_expressions` or in adjacent `derivation_step` / `proof_fragment` units
- if one typed unit becomes too wide, split it rather than collapsing the steps into prose
- when a theorem family becomes wide enough that "the proof" is really several bounded subclaims, emit `proof_obligation` and `proof_state` units rather than keeping the structure implicit
- when a formula changes role across source-local arguments, capture that role in `equation_context` instead of treating the equation label as self-explanatory
- if the source skips steps, mark that honestly and route to `open_gap` / `followup_source_task` when needed

Family-fusion rule:

- a canonical family may unify several source-local statements only when assumptions and regime remain explicit
- use `theorem_family`, `definition_family`, or `notation_family` to group reusable members
- use `source_fusion_record` to explain why the grouping is valid
- use `conflict_record` when nearby sources do not yet align cleanly

Formalization-planning rule:

- if a unit claims `formal_targets` that include `lean`, it should also expose an explicit Lean-facing plan
- the minimum plan consists of:
  - `lean_namespace`
  - `lean_declaration`
  - `lean_statement_kind`
  - `admissible_assumptions`
  - `lean_prerequisite_ids`
  - `formalization_blockers`
- theorem families should point to bounded `proof_obligation` units rather than pretending the whole family is one opaque theorem
- proof states may use `lean_statement_kind: scaffold` when the current object is a planning surface rather than a final theorem declaration

Formal-theory trust-boundary rule:

- a unit that participates in theorem-family formalization should say whether it is a `trusted_target`, `intermediate_theory`, or `supporting_context`
- do not silently let a scaffold, proof-state ledger, or explanatory bridge replace the trusted scientific target
- the minimum trust-boundary surface is:
  - `formal_theory_role`
  - `statement_graph_role`
  - `statement_graph_parents`
  - `statement_graph_children`
  - `target_statement_id` when the current unit is only intermediate theory
- translated definitions and theorem-family wrappers may also expose `definition_trust_tier`

Faithfulness and comparator rule:

- formalization planning is not enough on its own; the unit should also say whether the current statement is faithful to the source claim
- use:
  - `faithfulness_status`
  - `faithfulness_strategy`
  - `faithfulness_notes`
- when a theorem or scaffold is close enough to promotion that a weaker nearby statement would be a real risk, record:
  - `comparator_audit_status`
  - `comparator_risks`
- this is an anti-cheat surface: a formally neat but scientifically weakened statement must not pass as the original claim

Provenance and attribution rule:

- imported or adapted formal material must expose where it came from and what attribution is required
- use:
  - `provenance_kind`
  - `attribution_requirements`

Durable audit artifact rule:

- promotion-grade formal work should preserve the kernel-side audit artifacts that justified the current trust judgment
- in practice this means keeping stable pointers, notes, or mirrored summaries of:
  - `faithfulness_review.json`
  - `comparator_audit_record.json`
  - `provenance_review.json`
  - `prerequisite_closure_review.json`
  - `formal_theory_review.json/.md`
- unit-local fields remain the retrieval surface inside `open-physics-kb`, but the durable audit ledger is the cross-runtime evidence surface

Prerequisite-closure rule:

- prerequisite closure is a default gate, not an optional afterthought
- units that are used as formal targets or formal scaffolds should expose `prerequisite_closure_status`
- `partial` and `pending` remain blocking states even when a unit is already readable as a human note

Runtime-gap bridge rule:

- if an `open_gap` or `followup_source_task` is meant to receive AITP runtime follow-up writeback, it should expose:
  - `runtime_gap_kinds`
  - `runtime_return_to_stages`
  - `topic_queue_ids`
- this is the durable bridge from validation-run follow-up gaps back into topic-level unresolved or prerequisite governance

## P3. Source Anchor Protocol

Every promoted unit must anchor to at least one public source location.

Anchors must resolve to:

- a known `source_id`
- a known section id
- known equation labels or figure ids when such labels are claimed

If a source claim cannot be anchored, it is not yet canonical.

## P4. Edge Protocol

All graph relations must live in `edges/edges.jsonl`.

The finite relation vocabulary includes both semantic and workflow relations:

- semantic: `depends_on`, `defines`, `uses`, `explains`, `motivates`, `specializes`, `generalizes`, `contrasts_with`, `derived_from`, `supports`, `warned_by`, `bridges_to`, `formalizes_toward`, `anchored_in_source`
- workflow: `tests`, `oracles`, `blocked_by`, `resolves`, `routes_to`

Do not expand relation types casually.

## P5. Queue And Regression Protocol

`queues/` and `regressions/` are canonical because non-pass work must land somewhere durable.

Queue rules:

- queue manifests store stable queue ids, topic ids, item ids, status, and priority
- queue items point to typed units, not to ad hoc prose blobs
- unresolved and prerequisite routing must remain inspectable without replaying runtime logs

Regression rules:

- every regression suite stores stable question ids and oracle ids
- every run log stores grades plus writeback unit ids
- every regression question should expose a real retrieval surface and explicit pass conditions
- every question oracle should expose mandatory units, grading rubric, common failure patterns, and failure triggers
- `unsafe-pass` is allowed when a local answer satisfies the immediate oracle but still depends on unresolved external fusion, proof, or source-recovery risk
- non-pass results should route to `open_gap` or `followup_source_task`, not disappear into commentary
- regression suites used for topic curation should also expose:
  - `benchmark_contamination`
  - `benchmark_use`
  - `contamination_notes`
- protocol-internal suites may govern quality and promotion readiness, but they must not be advertised as clean external benchmarks unless contamination is explicitly `clean`

## P6. Projection Protocol

`indexes/` and `portal/` are deterministic projections from the canonical store.

Required generated surfaces now include:

- `indexes/unit_index.jsonl`
- `indexes/edge_index.jsonl`
- `indexes/source_anchor_index.jsonl`
- `indexes/symbol_index.jsonl`
- `indexes/formalization_index.jsonl`
- `indexes/domain_index.json`
- `indexes/gap_index.jsonl`
- `indexes/followup_task_index.jsonl`
- `indexes/queue_index.jsonl`
- `indexes/regression_suite_index.jsonl`
- `indexes/regression_run_index.jsonl`
- `portal/Topological-Phases-Of-Matter/**`

Projection contract for human notes:

- deterministic mirror writers may render `learning-note` units with richer sections such as motivation, prerequisites, local context, downstream use, and canonical questions
- the projection may be pedagogically richer than a raw object card, but it must remain a deterministic function of canonical fields
- human-facing notes must never invent formulas or derivation claims that are absent from the canonical store

## P7. Change Protocol

For any canonical change:

1. edit canonical files only
2. run `python3 scripts/check_protocol.py`
3. run `python3 scripts/build.py`
4. inspect the generated portal and indexes as projections, not as the source of truth

## P8. Script Minimality Protocol

Python is allowed here only for two repository-local duties:

- enforcing written protocols
- building deterministic projections and indexes

Any additional Python surface still needs a strong reason tied to those duties.

## P9. Topic Regression Protocol

If a branch is being treated as a reusable topic rather than a one-off parse, it should maintain:

- a stable regression suite
- durable queue writeback from non-pass results
- explicit routes from local gaps back through `L0 -> L1 -> L3 -> L2`

The operational details live in `docs/TOPIC_REGRESSION_SUITE_PROTOCOL.md`.

## P10. Topic Completion Protocol

Reusable topic branches should also expose explicit completion and promotion-readiness metadata.

The operational details live in `docs/TOPIC_COMPLETION_PROTOCOL.md`.
