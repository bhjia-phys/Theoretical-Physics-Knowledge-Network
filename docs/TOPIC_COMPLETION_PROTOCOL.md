# Topic Completion Protocol

This document defines when a topic branch is mature enough to be treated as reusable rather than merely interesting.

It complements:

- `docs/PAPER_INGESTION_QUALITY_PROTOCOL.md`
- `docs/TOPIC_REGRESSION_SUITE_PROTOCOL.md`

## C0. Purpose

Dense notes are not enough.

A topic becomes completion-ready only when the KB can say:

- which flagship objects are locally derivable;
- which regression questions support that claim;
- which blockers still prevent automatic promotion or broader reuse;
- which unresolved branches must route back through `L0 -> L1 -> L3 -> L2`.

## C1. Unit-Level Completion Metadata

Promotion-surface units should expose:

- `topic_completion_status`
- `supporting_regression_question_ids`
- `supporting_oracle_ids`
- `supporting_regression_run_ids`
- `promotion_blockers`
- `split_required`
- `recovery_source_refs`

The point is not bureaucratic tagging.

The point is to make automatic writeback and automatic refusal both inspectable.

## C2. Allowed Completion States

- `not_assessed`: no reliable completion judgment exists yet.
- `gap-aware`: the unit is honest about missing context but is not regression-backed.
- `regression-seeded`: some coverage and local proof structure exist, but the stable regression surface is still thin.
- `regression-stable`: the unit is backed by durable regression/oracle coverage, but promotion blockers may still remain elsewhere.
- `promotion-blocked`: the unit is regression-backed enough to discuss promotion, but explicit blockers, cited recovery, or split requirements still prevent it.
- `promotion-ready`: the unit is regression-backed and carries no known blocker that should stop bounded promotion.

## C3. Promotion-Readiness Rule

Use `promotion-ready` only when all of the following are true:

- the core derivation branch is explicit locally;
- supporting regression questions and oracles exist;
- a concrete regression run demonstrates the branch;
- `promotion_blockers` is empty;
- `split_required` is false.

If a residual external route still matters for honesty, keep it as blocker metadata or as an `open_gap` / `followup_source_task`, not as silent background.

## C4. Regression-Log Completion Surface

Recent regression logs should also expose:

- `topic_completion_status`
- `promotion_readiness`
- `blocking_unit_ids`

This gives one durable answer to the question:

"Is this topic actually reusable yet, and if not, what is stopping it?"

## C5. Witten Exemplar Interpretation

For the current topological-phases exemplar:

- Lecture Two and Lecture Three flagship theorem families may become `promotion-ready` even while narrower enrichment routes remain explicit.
- The overall topic remains `promotion-blocked` until the remaining lattice-no-go / anomaly-separation blockers are closed or explicitly buffered out of the core promotion target.
