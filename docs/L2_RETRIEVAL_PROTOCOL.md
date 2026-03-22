# L2 Retrieval Protocol

This document states how `open-physics-kb` is meant to be queried as an `L2`-compatible backend.

## Retrieval Surfaces

`L2` retrieval should read generated indexes, not portal markdown.

Primary retrieval surfaces:

- `indexes/unit_index.jsonl`
- `indexes/edge_index.jsonl`
- `indexes/source_anchor_index.jsonl`
- `indexes/symbol_index.jsonl`
- `indexes/formalization_index.jsonl`
- `indexes/domain_index.json`

Queue and regression surfaces that matter for proof-grade work:

- `indexes/gap_index.jsonl`
- `indexes/followup_task_index.jsonl`
- `indexes/queue_index.jsonl`
- `indexes/regression_suite_index.jsonl`
- `indexes/regression_run_index.jsonl`

## Minimum Retrieval Keys

For unit retrieval, the minimum fields are:

- `id`
- `type`
- `title`
- `summary`
- `aliases`
- `tags`
- `domain`
- `subdomain`
- `assumptions`
- `regime`
- `scope`
- `dependencies`
- `related_units`
- `representation`
- `math_expressions`
- `symbols`
- `source_anchors`
- `formalization_status`
- `validation_status`
- `maturity`

For source grounding and citation recovery, retrieval must use:

- `source_id`
- `section`
- `equation_labels`
- `figure_ids`

For proof-grade blocked queries, retrieval must also inspect:

- `blocking_units`
- `resolution_targets`
- `resolves_gaps`
- `routes_back_to`
- regression run grades and writeback targets

## Query Order

Default query order:

1. `unit_index.jsonl` for candidate objects
2. `edge_index.jsonl` for graph expansion around those ids
3. `source_anchor_index.jsonl` for source recovery
4. `formalization_index.jsonl` if the query is pushing toward formal targets

If the answer is incomplete or blocked:

5. `gap_index.jsonl` and `followup_task_index.jsonl`
6. `queue_index.jsonl`
7. `regression_suite_index.jsonl` and `regression_run_index.jsonl`

The point is not only to answer what is already known, but also to answer honestly what is still missing and how the system intends to recover it.

## Human Mirror Contract

Human-facing notes outside the canonical store may mirror these objects, but they are not the `L2` backend.

The intended repository rule is:

- the canonical backend remains `sources/`, `units/`, `edges/`, `queues/`, and `regressions/`
- human mirrors must preserve typed ids and source grounding if they claim to mirror typed objects
- formula-bearing units should appear in mirrors with explicit display math and symbol tables
- derivation-bearing or theorem-bearing units should expose visible proof structure, not only summary prose
- unresolved queues and regression summaries may appear in the human layer, but they must remain clearly secondary to the canonical surfaces
