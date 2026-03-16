# Protocols

This file is the normative contract for `open-physics-kb`.

See also `docs/L2_RETRIEVAL_PROTOCOL.md` for the concrete retrieval-facing surface.

## P0. Repository Role

The repository is a standalone theoretical-physics knowledge kernel.

It must remain:

- independent from Obsidian as the source of truth;
- independent from AITP runtime orchestration;
- compatible with typed `L2` retrieval;
- readable to humans through generated portal projections.

## P1. Canonical Storage Protocol

Only the following paths are canonical:

- `sources/`
- `units/`
- `edges/`

The following are not canonical:

- `indexes/`
- `portal/`
- `human-mirror/`

Generated projections must never be hand-edited as the authoritative source.

`human-mirror/` may be hand-edited for human readability, but it must never supersede the canonical backend.

## P2. Unit Protocol

Every reusable knowledge object must:

- live in exactly one JSON file under the matching `units/<family>/` directory;
- carry a stable typed id such as `concept:weyl-node`;
- expose explicit scope, regime, assumptions, dependencies, and source anchors;
- record formalization and validation status;
- stay small enough to serve retrieval rather than only archival storage.

## P3. Source Anchor Protocol

Every promoted unit must anchor to at least one public source location.

Anchors must resolve to:

- a known `source_id`;
- a known section id in that source manifest;
- known equation labels or figure ids when such labels are claimed.

If a source claim cannot be anchored, it is not yet canonical.

## P4. Edge Protocol

All graph relations must live in `edges/edges.jsonl`.

Relations must use the finite vocabulary already declared by the repository.

If a relation feels missing, first test whether the knowledge should instead be encoded in:

- the unit summary;
- a warning unit;
- a bridge unit;
- a derivation unit.

Do not expand relation types casually.

## P5. Projection Protocol

`indexes/` and `portal/` are deterministic projections from the canonical store.

Required generated surfaces are:

- `indexes/unit_index.jsonl`
- `indexes/edge_index.jsonl`
- `indexes/source_anchor_index.jsonl`
- `indexes/symbol_index.jsonl`
- `indexes/formalization_index.jsonl`
- `indexes/domain_index.json`
- `portal/Topological-Phases-Of-Matter/**`

## P6. Change Protocol

For any canonical change:

1. edit canonical files only;
2. run `python3 scripts/kb.py check`;
3. run `python3 scripts/kb.py build`;
4. inspect the generated portal and indexes as projections, not as the source of truth.

## P7. Script Minimality Protocol

Python is allowed here only for two repository-local duties:

- enforcing written protocols;
- building deterministic projections.

The minimal script surface is:

- `scripts/kb.py`

Any additional Python script needs a strong reason tied to one of the two duties above.

## P8. L2 Bridge Protocol

If knowledge arrives from an AITP `L2` workflow, it must enter this repository through a promotion bridge rather than a runtime dump.

That means:

- `L2` queries repository indexes first;
- `L2` decides update-vs-create explicitly for typed objects;
- only promoted, source-grounded units enter `sources/`, `units/`, and `edges/`;
- runtime notes stay upstream unless and until they are canonicalized;
- `human-mirror/` stays secondary to typed objects.

The operational contract for this bridge lives in `docs/L2_BRIDGE_PROTOCOL.md`.
