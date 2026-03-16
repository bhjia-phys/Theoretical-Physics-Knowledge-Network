---
title: "Theoretical Physics"
type: index
domain: "Theoretical Physics"
status: reviewed
aliases:
  - "Public Human Mirror"
sources:
  - "Internal: docs/PROTOCOLS.md"
  - "Internal: docs/L2_RETRIEVAL_PROTOCOL.md"
  - "Internal: human-mirror/Mirror Contract.md"
created: 2026-03-16
updated: 2026-03-16
kb_surface: human_index
---

## Research Layer

This folder is the public human-facing mirror for the repository.

Its role is to show how a knowledge base can remain readable to humans while preserving the same object boundaries and typed bindings used by the canonical backend.

## Claim Ledger

| Claim | Evidence | Confidence |
|-------|----------|------------|
| The canonical `L2` backend of this repository lives outside the human mirror. | `docs/PROTOCOLS.md` and `docs/L2_RETRIEVAL_PROTOCOL.md`. | HIGH |
| The public mirror should stay structurally compatible with the typed backend. | [[human-mirror/Mirror Contract|Mirror Contract]]. | HIGH |
| The current example focuses on a small topological-phases branch rather than a full domain map. | Current `human-mirror/` contents. | HIGH |

## Domain Map

- [[human-mirror/Quantum Matter/Index|Quantum Matter]]
- [[human-mirror/Mirror Contract|Mirror Contract]]

## L2 Retrieval Contract

- Query `indexes/` first for retrieval.
- Use the human mirror for navigation and explanation.
- Trust a mirror note as an object mirror only if it carries `kb_unit_id` or `kb_source_map_id`.

## Knowledge Graph

### Prerequisites

- none

### Related

- [[human-mirror/Mirror Contract|Mirror Contract]]
- [[human-mirror/Quantum Matter/Index|Quantum Matter]]

## Unresolved Links Queue

- Extend the public example into more domains only after the corresponding typed objects are stable.

## References

- Internal: `docs/PROTOCOLS.md`
- Internal: `docs/L2_RETRIEVAL_PROTOCOL.md`
- Internal contract note: [[human-mirror/Mirror Contract|Mirror Contract]]
