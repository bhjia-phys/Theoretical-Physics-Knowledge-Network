# Paper Ingestion Quality Protocol

This document defines the general quality protocol for turning any theoretical-physics paper into reusable `L2` knowledge.

It is intentionally general:

- it applies to any future paper, not only the current topological-phases exemplar;
- it treats scripts as infrastructure only;
- it requires content quality to be judged by agent reasoning, not by schema presence alone.

See also:

- `docs/PROTOCOLS.md`
- `docs/L2_RETRIEVAL_PROTOCOL.md`
- `docs/TOPIC_REGRESSION_SUITE_PROTOCOL.md`

## G0. Core Principle

The target is not to produce many notes quickly.

The target is to produce notes such that, after writeback, an agent can:

- state the concept precisely;
- reconstruct the derivation in detail;
- explain which assumptions are used at each step;
- place the note in the paper's local and global context;
- identify which missing steps require follow-up sources.

If a note does not satisfy those conditions, it is not yet `L2`-ready even if its schema is complete.

## G1. Script Boundary Rule

Scripts may help with:

- chunking;
- indexing;
- deterministic projection building;
- mirror synchronization;
- diffing and auditing;
- schema validation.

Scripts must not be trusted to decide:

- whether a concept is actually understood;
- whether a derivation is clear enough;
- whether context links are sufficient;
- whether a note is promotion-ready in substance.

Those are agent-judged protocol gates.

## G2. Required Gates Before Promotion

Every reusable paper-derived note must pass the following gates.

### G2.1 Atomic Clarity Gate

The note must answer:

- What exactly is being defined, proved, derived, or related?
- What is in scope and what is out of scope?
- Which assumptions or regime restrictions are active?
- Which symbols are essential?

If the note cannot be explained without leaning on vague paper prose, it fails this gate.

### G2.2 Derivation Completeness Gate

If the source contains an actual derivation or proof spine, the note set must preserve it.

The required visible structure is:

1. starting point;
2. intermediate nontrivial step(s);
3. identity, assumption, symmetry, or approximation used at each step;
4. final result.

Failure conditions:

- only the endpoint is stored;
- the note says "one finds" or "it follows" without exposing the nontrivial step;
- a key approximation or boundary condition is used but not named;
- a multi-step argument is flattened into one summary sentence.

If one note would become too wide, split the reasoning into adjacent `derivation_step`, `proof_fragment`, `equivalence`, `definition`, and `theorem` units.

### G2.3 Context-Connection Gate

The note must make its context explicit:

- what earlier concepts/results it depends on;
- what later results it supports;
- where it sits in the paper's local argument;
- whether it is a local technical lemma, a reusable theorem, a motivating picture, or a source-map waypoint.

If a note is atomized but isolated, it fails this gate.

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

### G2.5 Honest Gap Gate

If the source itself skips a step, that is allowed.

But the note must say so explicitly. The agent must not fabricate unsupported intermediate formulas.

Allowed outcomes:

- the skipped step is marked as source-omitted;
- the note links to a follow-up source target;
- the note stays in `L3` until the gap is resolved.

## G3. Automatic L0 Follow-Up Trigger

If any promotion candidate fails one of the above gates because of a real knowledge gap, the workflow must automatically step back:

1. return to `L0` to collect the cited or clearly relevant background source;
2. run `L1` analysis on that source;
3. reshape the resulting explanation in `L3`;
4. only then promote into `L2`.

Typical triggers:

- the review paper cites a theorem but does not derive it;
- the derivation depends on a standard construction that is not explained locally;
- the paper assumes a geometric or topological invariant without rebuilding it;
- the paper compresses a field-theory argument into a phrase like "as is well known".

## G4. Promotion Decision Rule

Promotion to `L2` is allowed only when:

- the note is source-grounded;
- the concept is clear;
- the derivation spine is visible at the correct granularity;
- the context links are explicit;
- known missing steps are either resolved or honestly marked and kept out of the promoted core.

Schema completeness alone is not enough.

## G5. Preferred Note Topology

For a strong paper parse, prefer a layered note topology:

- source-map notes for paper navigation;
- atomic reusable notes for concepts, equations, quantities, definitions, theorems, and derivation steps;
- derivation chains that connect the atomic notes;
- unresolved/follow-up notes that track why some units remain noncanonical.

Do not choose between atomization and context. A good parse needs both.

## G6. Witten Exemplar Rule

`Three Lectures On Topological Phases Of Matter` is the first explicit exemplar for this protocol.

For that paper, the quality target is stronger than "good summaries":

- a reader should be able to reconstruct the major argument chains from the note network in `human-mirror/` or any bound human surface;
- whenever Witten leans on earlier literature instead of deriving something fully, the follow-up source should be identified and routed back through `L0 -> L1 -> L3 -> L2`;
- the exemplar is not finished until the branch exposes both atomic notes and derivation-chain visibility.

## G7. Topic Regression Requirement

When a paper parse has matured into a reusable topic branch, it should also maintain a topic regression suite.

That suite should test at least:

- precise definitions;
- flagship derivations;
- dependency visibility;
- bridge visibility between neighboring note clusters;
- honest gap routing back to `L0`.

A paper branch is not “complete enough for downstream use” merely because it has many notes.

It also needs a recent regression pass that shows which questions already pass and which still route to local expansion or background follow-up.
