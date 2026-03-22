# Topic Regression Suite Protocol

This document defines the general protocol for topic-level regression suites.

It complements:

- `docs/PAPER_INGESTION_QUALITY_PROTOCOL.md`
- `docs/L2_RETRIEVAL_PROTOCOL.md`

## R0. Purpose

Paper ingestion alone is not enough.

Once a branch becomes a reusable topic, the system needs a stable way to ask:

- can the topic define its core objects precisely;
- can it reconstruct its flagship derivations;
- can it expose dependencies between those results;
- can it connect nearby concepts and neighboring papers;
- can it honestly identify what still requires `L0` follow-up?

That stable question set is the topic regression suite.

## R1. Required Topic Surfaces

Every topic that aims to be reusable should maintain:

1. a topic charter that states the completeness target;
2. topic source maps that expose the local argument structure;
3. a topic regression suite with stable question ids;
4. a detailed regression oracle or answer key that states what each question requires in proof, notation, and dependency terms;
5. regression pass logs that record pass/partial/fail outcomes;
6. unresolved-queue writeback that turns failures into concrete next actions.

## R2. Question Families

A good suite should cover at least these families.

### R2.1 Definition questions

These test whether the topic can state its basic objects, symbols, regimes, and scope conditions precisely.

### R2.2 Derivation questions

These test whether the topic can reconstruct a flagship proof or calculation with explicit intermediate steps, not only the endpoint formula.

### R2.3 Dependency questions

These test whether the topic knows which earlier notes, lemmas, constructions, or background theorems are required before a result can be used responsibly.

### R2.4 Bridge questions

These test whether the topic can explain how one cluster of notes connects to another cluster, or how one paper's formal object relates to another paper's formal object.

### R2.5 Gap questions

These test whether the topic can identify missing background, skipped derivations, and source-compressed arguments honestly enough to route back through `L0 -> L1 -> L3 -> L2`.

## R3. Question Record Contract

Each regression question should carry:

- a stable question id;
- a family label such as `definition`, `derivation`, `dependency`, `bridge`, or `gap`;
- a natural-language prompt;
- a primary retrieval path such as canonical notes or source maps;
- a pass condition describing what a good answer must make visible.

In addition, every stable question should have a linked detailed oracle record that carries:

- the exact local notes that should be traversed first;
- the mandatory formulas, symbols, and assumptions that must appear in the answer when the question is formal;
- an explicit derivation spine, dependency spine, or bridge spine;
- any required external `L0` source anchors if the local notes are not sufficient by themselves;
- failure triggers that explain what would force the grade down to `partial` or `fail`.

Question count is coverage-driven, not fixed.

The target is not “100 questions” as a slogan.

The target is “enough stable questions that the topic's real weak points can no longer hide.”

## R4. Grading Contract

Each evaluated question should receive one of:

- `pass`
- `partial`
- `fail`

### R4.1 Pass

Use `pass` only when the current topic notes can answer the question with:

- precise definitions;
- visible formulas when the source contains them;
- explicit derivation steps when the question is derivation-heavy;
- explicit assumptions and scope;
- satisfaction of the detailed oracle for that question rather than only a vague topic-level resemblance;
- honest handling of any remaining source-local caveat.

### R4.2 Partial

Use `partial` when the topic can mostly answer the question but still lacks one or more of:

- explicit intermediate steps;
- explicit prerequisite edges;
- explicit bridge notes;
- explicit local gap classification.

### R4.3 Fail

Use `fail` when the current topic cannot answer the question honestly from the existing note network, or when even the missing-background route is not clearly encoded.

## R5. Failure Handling

A regression pass must not stop at scoring.

Each `partial` or `fail` should trigger one of:

- expand the existing note locally;
- split a too-wide note into derivation-step or proof-fragment neighbors;
- add missing dependency edges or bridge notes;
- refine the detailed oracle if the question itself was underspecified;
- return to `L0` for a cited/background source;
- keep the object explicit in `L3` if the gap is still unresolved.

## R6. Script Boundary

Scripts may:

- persist question manifests;
- collect result matrices;
- diff pass logs over time;
- build summary projections.

Scripts must not decide whether an answer is mathematically clear enough.

That judgment remains an agent task under the paper-ingestion quality gates.

## R7. Stability Criterion

A topic should not be treated as regression-stable merely because it has many notes.

It becomes regression-stable only when:

- flagship definition questions pass;
- flagship derivation questions pass without hidden proof gaps;
- dependency paths are encoded for major theorems;
- bridge questions are answered explicitly rather than by ad hoc improvisation;
- gap questions correctly identify what still needs `L0` follow-up.

## R8. First Exemplar

The first explicit exemplar for this protocol is the topological-phases branch seeded by Witten's `Three Lectures On Topological Phases Of Matter`.

Its suite should remain the first serious benchmark for whether the protocol is working in practice.
