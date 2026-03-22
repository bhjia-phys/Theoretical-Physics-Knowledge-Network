# Topic Regression Suite Protocol

This document defines the general protocol for topic-level regression suites.

It complements:

- `docs/PAPER_INGESTION_QUALITY_PROTOCOL.md`
- `docs/L2_RETRIEVAL_PROTOCOL.md`

## R0. Purpose

Paper ingestion alone is not enough.

Once a branch becomes reusable, the system needs a stable way to ask:

- can the topic define its core objects precisely
- can it reconstruct flagship derivations
- can it expose dependencies between those results
- can it connect nearby concepts and neighboring papers
- can it honestly identify what still requires `L0` follow-up

That stable question set is the topic regression suite.

## R1. Required Topic Surfaces

Every reusable topic should maintain:

1. a topic charter or source-map backbone
2. a regression suite manifest
3. stable `regression_question` units
4. stable `question_oracle` units
5. recent run logs with `pass`, `partial`, or `fail`
6. queue writeback from non-pass results into `open_gap` and `followup_source_task` routing

`unsafe-pass` is also allowed for runs where the local derivation surface is
strong enough to answer the question, but the surrounding theorem family still
carries explicit cited-source or fusion risk that the answer must not hide.

## R2. Question Families

A good suite should cover at least:

- `definition`
- `derivation`
- `dependency`
- `bridge`
- `gap`

The point is not to reach a slogan like "100 questions."

The point is to reach enough stable questions that the topic's real weak points can no longer hide.

## R3. Question Contract

Each `regression_question` should carry:

- a stable question id
- a family label
- a natural-language prompt
- primary retrieval paths
- pass conditions

Each `question_oracle` should carry:

- the exact units that should be traversed first
- mandatory formulas, symbols, or equation labels when relevant
- supporting proof obligations and dependency snapshots when relevant
- mandatory logical moves when the proof order itself matters
- an explicit derivation spine or dependency spine
- common failure patterns
- grading rubric
- failure triggers

These are not optional decoration for a proof-grade topic.
They are the minimum machine-visible surface needed to keep a regression bank
from collapsing back into slogan checking.

## R3.5 Research-Grade Oracle Density

For a mature topic, each flagship theorem family should have a dense enough
question/oracle bank that a reviewer can probe any critical turn of the proof.

That usually means covering:

- the strict definition surface,
- the main derivation spine,
- prerequisite and dependency identification,
- cited-versus-local scope boundaries,
- and the failure modes that most often masquerade as understanding.

If an oracle cannot say what counts as a partial answer, what the common proof
collapse looks like, and what exact artifacts should be traversed first, that
oracle is still too weak.

## R4. Grading Contract

Each evaluated question receives one of:

- `pass`
- `unsafe-pass`
- `partial`
- `fail`

Use `pass` only when the current notes satisfy the oracle in substance, not only in theme.

Use `unsafe-pass` when the immediate answer can be reconstructed faithfully from
the current network, but the surrounding family still has an explicit external
recovery or fusion risk that must remain visible.

Use `partial` when the answer is mostly present but still hides a derivation step, prerequisite edge, or gap classification.

Use `fail` when the current topic cannot answer honestly from the existing network.

## R5. Failure Handling

A regression pass must not stop at scoring.

Each `partial` or `fail` should trigger one or more of:

- expand an existing note locally
- split a wide note into derivation-step or proof-fragment neighbors
- add missing dependency or bridge edges
- create or update an `open_gap`
- create or update a `followup_source_task`
- enqueue the result in a queue manifest

## R6. Script Boundary

Scripts may:

- persist suite manifests
- build regression indexes
- aggregate run logs
- diff pass matrices over time

Scripts must not decide whether an answer is mathematically clear enough.

That remains an agent task under the paper-ingestion quality gates.

## R7. Stability Criterion

A topic should not be treated as regression-stable merely because it has many notes.

It becomes regression-stable only when:

- flagship definition questions pass
- flagship derivation questions pass without hidden proof gaps
- dependency paths are encoded for major theorems
- bridge questions are answered explicitly rather than ad hoc
- gap questions correctly identify what still needs `L0` follow-up

Regression stability is still not identical to promotion readiness.

Topic completion and blocking metadata live in `docs/TOPIC_COMPLETION_PROTOCOL.md`.

## R8. First Exemplar

The first explicit exemplar is the topological-phases branch seeded by Witten's `Three Lectures On Topological Phases Of Matter`.

Stage-one target:

- Lecture One proof-grade regression suite
- Lecture Two and Lecture Three source maps with explicit queues and follow-up tasks, even before their flagship theorem chains are promoted

Stage-two target:

- a topic-level `Topological Phases` regression suite that fuses Witten with the TKNN, Haldane, Jackiw-Rebbi, and Callan-Harvey branches
- family-aware regression questions that test canonical objects rather than only one paper presentation
- research-grade oracles with explicit grading rubrics and failure patterns for every flagship branch
- a future-research buffer queue for broad branches such as fractional Hall topological order that are known but not yet proof-grade
