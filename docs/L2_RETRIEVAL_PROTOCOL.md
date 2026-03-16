# L2 Retrieval Protocol

This document states how `open-physics-kb` is meant to be queried as an `L2`-compatible backend.

For write-back from `L2` into this repository, see `docs/L2_BRIDGE_PROTOCOL.md`.

## Retrieval Surfaces

`L2` retrieval should read from generated indexes, not from portal markdown.

Primary surfaces:

- `indexes/unit_index.jsonl`
- `indexes/edge_index.jsonl`
- `indexes/source_anchor_index.jsonl`
- `indexes/symbol_index.jsonl`
- `indexes/formalization_index.jsonl`
- `indexes/domain_index.json`

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
- `dependencies`
- `related_units`
- `formalization_status`
- `validation_status`
- `maturity`

For source-grounding and citation recovery, retrieval must also use:

- `source_id`
- `section`
- `equation_labels`
- `figure_ids`

## Query Order

Default query order:

1. `unit_index.jsonl` for candidate objects;
2. `edge_index.jsonl` for graph expansion around the selected ids;
3. `source_anchor_index.jsonl` for source recovery;
4. `formalization_index.jsonl` if the query is pushing toward Lean or other formal targets.

## Human Mirror Contract

Human-facing notes under `human-mirror/` are mirrors, not the `L2` store.

The intended repository rule is:

- `human-mirror/` should be authored as a human-facing surface that stays structurally compatible with `L2`;
- `open-physics-kb` remains the canonical typed backend and retrieval source.

Structural compatibility means:

- object-like mirror notes should preserve a one-to-one typed binding through `kb_unit_id` or `kb_source_map_id`;
- human control notes such as indexes, migration audits, or unresolved queues may exist, but should declare a `kb_surface` role when appropriate and must not be treated as standalone `L2` objects;
- human readability may add explanatory sections, intuition, examples, and navigation, but must not replace source-grounded ids, anchors, assumptions, regime, and dependency information when the note is mirroring a typed object.

If a human note is meant to mirror a typed `L2` object, it should carry at least one of:

- `kb_unit_id: <typed-id>`
- `kb_source_map_id: <typed-id>`

If neither field exists, the note should be treated as:

- a migration candidate;
- a reading note;
- or a local human-only aid,

not as a trusted `L2` retrieval object.

## Write Boundary

`L2` should retrieve from `indexes/`, but when it writes back into this repository it must write into:

- `sources/`
- `units/`
- `edges/`

and only then regenerate:

- `indexes/`
- `portal/`

`human-mirror/` may be updated as a secondary bound surface, never as the canonical write target.
