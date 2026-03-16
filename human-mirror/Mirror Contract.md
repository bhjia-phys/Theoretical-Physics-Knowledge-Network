---
title: "Mirror Contract"
type: index
domain: "Theoretical Physics"
status: reviewed
aliases:
  - "Human-Facing L2 Mirror Contract"
sources:
  - "Internal: docs/L2_RETRIEVAL_PROTOCOL.md"
  - "Internal: docs/PROTOCOLS.md"
created: 2026-03-16
updated: 2026-03-16
kb_surface: human_control
---

## Research Layer

This note defines how `human-mirror/` should be authored.

The governing rule is: the mirror is written for people, but its object structure should remain compatible with the canonical typed backend.

## Claim Ledger

| Claim | Evidence | Confidence |
|-------|----------|------------|
| Object mirrors should preserve typed identity rather than becoming free-form note blobs. | `docs/L2_RETRIEVAL_PROTOCOL.md`. | HIGH |
| Human readability may add explanation, examples, and navigation, but not replace backend structure. | `docs/L2_RETRIEVAL_PROTOCOL.md`. | HIGH |
| The public mirror is a presentation layer, not the canonical `L2` store. | `docs/PROTOCOLS.md`. | HIGH |

## Structural Rules

- Treat `sources/`, `units/`, and `edges/` as canonical.
- Treat `human-mirror/` as a human-facing mirror layer.
- New object-like notes in the mirror should trace back to typed `L2` objects.
- Use `kb_unit_id` or `kb_source_map_id` for object mirrors.
- Use `kb_surface` for structural control notes when helpful.

## Knowledge Graph

### Prerequisites

- [[human-mirror/Index|Theoretical Physics]]

### Related

- [[human-mirror/Quantum Matter/Index|Quantum Matter]]

## Unresolved Links Queue

- Keep the public mirror example intentionally small until new backend objects are stable enough to mirror.

## References

- Internal: `docs/L2_RETRIEVAL_PROTOCOL.md`
- Internal: `docs/PROTOCOLS.md`
