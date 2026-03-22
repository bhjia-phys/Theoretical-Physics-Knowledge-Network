# Paper Ingestion Quality Protocol

This document defines the quality protocol for turning any theoretical-physics paper into reusable `L2` knowledge.

It is intentionally general:

- it applies to future papers, not only the current topological-phases exemplar
- it treats scripts as infrastructure only
- it requires content quality to be judged by agent reasoning, not by schema presence alone

## G0. Core Principle

The target is not to produce many notes quickly.

The target is to produce notes such that, after writeback, an agent can:

- state the concept precisely
- reconstruct the derivation in detail
- explain which assumptions are used at each step
- place the note in the paper's local and global context
- identify which missing steps require follow-up sources

If a note does not satisfy those conditions, it is not yet `L2`-ready even if its schema is complete.

## G1. Script Boundary Rule

Scripts may help with:

- chunking
- indexing
- deterministic projection building
- mirror synchronization
- diffing and auditing
- schema validation
- queue and regression index aggregation

Scripts must not decide:

- whether a concept is actually understood
- whether a derivation is clear enough
- whether context links are sufficient
- whether a note is promotion-ready in substance

Those remain agent-judged protocol gates.

## G2. Required Gates Before Promotion

Every reusable paper-derived note must pass these gates.

### G2.1 Atomic Clarity Gate

The note must answer:

- what exactly is being defined, proved, derived, or related
- what is in scope and what is out of scope
- which assumptions or regime restrictions are active
- which symbols are essential

If the note cannot be explained without leaning on vague paper prose, it fails.

### G2.2 Derivation Completeness Gate

If the source contains an actual derivation or proof spine, the note set must preserve it.

The required visible structure is:

1. starting point
2. intermediate nontrivial step(s)
3. identity, assumption, symmetry, or approximation used at each step
4. final result

Failure conditions:

- only the endpoint is stored
- the note says "one finds" or "it follows" without exposing the nontrivial step
- a key approximation or boundary condition is used but not named
- a multi-step argument is flattened into one summary sentence

If one note would become too wide, split the reasoning into adjacent `definition`, `theorem`, `proof_fragment`, `derivation_step`, `equivalence`, and `equation` units.

### G2.3 Context-Connection Gate

The note must make its context explicit:

- what earlier concepts or results it depends on
- what later results it supports
- where it sits in the paper's local argument
- whether it is a local lemma, reusable theorem, motivating picture, source-map waypoint, or unresolved follow-up

If a note is atomized but isolated, it fails.

### G2.4 Self-Interrogation Gate

After writing a note, the agent must interrogate itself with at least these questions:

1. If the source text were hidden, could I still state the note precisely?
2. Do I know how to derive the main formula or conclusion step by step?
3. Do I know what justifies each nontrivial step?
4. Do I know which assumptions, limits, symmetry arguments, or conventions are being used?
5. Do I know how this note connects to the immediately previous and next concepts in the paper?
6. If I cannot reconstruct some step, do I know exactly what is missing?
7. Is the missing piece likely to be in the same paper, or does it require a cited background source?

If the answer to any substantive question is "no" or "not really", the note is not yet complete.

### G2.4a Human-Learning Projection Gate

If a unit is intended to appear as a direct study note, it must be able to answer, inside the note itself:

- why this note exists at this point in the argument
- what minimal prerequisites the reader must already command
- where the note sits in the paper's local flow
- what later derivation, theorem, or invariant it supports
- which questions a careful reader should be able to ask and answer after reading it

For `open-physics-kb`, this gate is represented canonically by `human_projection_profile: "learning-note"` plus the explanatory fields required by the protocol checker.

### G2.5 Honest Gap Gate

If the source itself skips a step, that is allowed.

But the note must say so explicitly. The agent must not fabricate unsupported intermediate formulas.

Allowed outcomes:

- the skipped step is marked as source-omitted
- an `open_gap` unit is created
- the note links to a `followup_source_task`
- the object stays out of the promoted core until the gap is resolved

## G3. Automatic L0 Follow-Up Trigger

If a promotion candidate fails because of a real knowledge gap, the workflow must step back:

1. create or update an `open_gap`
2. route it into a queue manifest
3. create or update a `followup_source_task` if the gap needs external background
4. return to `L0` to collect the cited or clearly relevant source
5. run `L1` analysis on that source
6. reshape the resulting explanation in `L3`
7. only then promote the recovered explanation into `L2`

Typical triggers:

- the review paper cites a theorem but does not derive it
- the derivation depends on a standard construction that is not explained locally
- the paper assumes a geometric or topological invariant without rebuilding it
- the paper compresses an argument into a phrase like "as is well known"

The recovery objects should now be explicit enough to automate:

- `open_gap.gap_kind`
- `open_gap.recovery_source_type`
- `open_gap.reentry_targets`
- `followup_source_task.task_status`
- `followup_source_task.reentry_targets`
- `open_gap.runtime_gap_kinds`
- `open_gap.runtime_return_to_stages`
- `open_gap.topic_queue_ids`

If the missing branch is too wide to be responsibly promoted in the current pass, it should go into a `future_buffer` queue instead of being promoted prematurely.

## G4. Promotion Decision Rule

Promotion to `L2` is allowed only when:

- the note is source-grounded
- the concept is clear
- the derivation spine is visible at the correct granularity
- the context links are explicit
- known missing steps are either resolved or honestly marked and routed

Schema completeness alone is not enough.

## G4a. Formalization-Planning Gate

If a unit is intended to be reusable later in Lean or another proof assistant,
the current pass should already expose a bounded formalization plan rather than
only a generic `formal_targets` flag.

The minimum planning surface is:

- a stable `lean_namespace`
- a stable `lean_declaration`
- a `lean_statement_kind`
- explicit `admissible_assumptions`
- explicit `lean_prerequisite_ids`
- explicit `formalization_blockers`

This does not require the Lean theorem to be written now.

It does require the knowledge object to say:

- what declaration should eventually exist
- which sublemmas or proof obligations it depends on
- which assumptions may remain at the theorem wrapper
- what still blocks honest formalization

## G4b. Trust-Boundary Gate

If a note is meant to support later formalization, it must also say what kind of
formal object it currently is.

Required questions:

- Is this the trusted target statement, or only intermediate theory?
- If it is intermediate theory, which target statement is it serving?
- Which local prerequisites and child statements make up the current statement graph?

For `open-physics-kb`, this is recorded with:

- `formal_theory_role`
- `statement_graph_role`
- `statement_graph_parents`
- `statement_graph_children`
- `target_statement_id` when needed

## G4c. Faithfulness And Comparator Gate

It is not enough for a note to be formalizable.
It must still match the scientific source claim rather than a cleaner but weaker
nearby statement.

Required questions:

- Is the current statement faithful to the source?
- What is the strategy for checking that faithfulness?
- Which nearby weaker or drifted statements are the main comparison risks?

For `open-physics-kb`, this is recorded with:

- `faithfulness_status`
- `faithfulness_strategy`
- `faithfulness_notes`
- `comparator_audit_status`
- `comparator_risks`

## G4d. Provenance And Attribution Gate

If a formal note imports, adapts, or rewrites material, the note must record
that provenance explicitly.

For `open-physics-kb`, this is recorded with:

- `provenance_kind`
- `attribution_requirements`

## G4e. Prerequisite-Closure Gate

Promotion-ready formal notes should not merely list prerequisites.
They should also say whether prerequisite closure is actually done.

For `open-physics-kb`, this is recorded with:

- `prerequisite_closure_status`

For AITP promotion-grade branches, this should also leave a durable kernel-side
audit trail under the corresponding `theory-packets/<candidate>/` directory:

- `faithfulness_review.json`
- `comparator_audit_record.json`
- `provenance_review.json`
- `prerequisite_closure_review.json`
- `formal_theory_review.json/.md`

The KB fields are still the local retrieval surface, but these review artifacts
are the auditable evidence of why the current trust judgment is allowed.

## G5. Preferred Note Topology

For a strong paper parse, prefer a layered topology:

- source-map notes for paper navigation
- atomic reusable notes for concepts, definitions, equations, quantities, theorems, derivation steps, and proof fragments
- explicit gap and follow-up notes for what is not yet settled
- regression questions and oracles for what the topic must eventually answer

Do not choose between atomization and context. A good parse needs both.

## G6. Witten Exemplar Rule

`Three Lectures On Topological Phases Of Matter` is the first explicit exemplar.

For that paper, the quality target is stronger than "good summaries":

- Lecture One should become proof-grade
- Lecture Two and Lecture Three should expose source maps, flagship theorem chains where available, and explicit gap, follow-up, or future-buffer routing where recovery is still incomplete
- the exemplar is not finished until the branch exposes both atomic notes and derivation-chain visibility

## G7. Topic Regression Requirement

When a paper parse matures into a reusable topic branch, it should also maintain:

- a regression suite manifest
- question and oracle objects
- recent run logs
- queue writeback from partial and fail results

If those regressions are then used to talk about model quality or
autoformalization performance, the suite must also say whether it is a clean
benchmark or a protocol-internal workflow check.

A paper branch is not complete enough for downstream use merely because it has many notes.

## G8. Topic Completion Writeback

Once a paper branch becomes a reusable topic branch, the flagship theorem, proof-state, family, and fusion objects should also record:

- their completion state;
- which regression questions and oracles support that state;
- which regression run actually backs the claim;
- which blockers still stop promotion.

That metadata does not replace the notes.

It makes the promotion claim inspectable.
