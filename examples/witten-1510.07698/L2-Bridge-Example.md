# Witten L2 Bridge Example

This example shows how an AI agent should promote new knowledge from an AITP `L2` reading flow into this repository.

## Scenario

Assume `L2` has read Lecture One of Witten's `1510.07698v2` and extracted a reusable bridge object:

- local Weyl-node analysis;
- Berry-flux interpretation of node charge;
- bulk-boundary transition toward Fermi-arc reasoning.

The agent wants to record the first bridge explicitly instead of leaving it only as runtime prose.

## Correct Write Mode

This is primarily:

- `unit-promotion`

and secondarily:

- `graph-refinement`
- `mirror-sync`

## Search First

The agent should first inspect:

- `indexes/unit_index.jsonl`
- `indexes/source_anchor_index.jsonl`
- `edges/edges.jsonl`

Expected finding in the current skeleton:

- `concept:weyl-node` already exists;
- `concept:berry-curvature` already exists;
- `source_map:witten-topological-phases-lecture-one` already exists.

Therefore this is not a source-onboarding change.

## Canonical Write Plan

If no suitable bridge unit already exists, the next canonical move is:

1. create a new bridge unit such as `bridge:local-weyl-node-to-berry-flux`;
2. anchor it to the relevant Lecture One section and equation labels in `sources/witten-1510.07698/manifest.json`;
3. connect it with finite-vocabulary edges in `edges/edges.jsonl`;
4. rebuild indexes and portal;
5. optionally add a mirror note under `human-mirror/Quantum Matter/Topological Phases/`.

## Files That Should Change

Minimal expected file set:

- `units/bridges/local-weyl-node-to-berry-flux.json`
- `edges/edges.jsonl`
- `indexes/*`
- `portal/*`

Optional human-facing file:

- `human-mirror/Quantum Matter/Topological Phases/Local Weyl Node To Berry Flux Bridge.md`

## Files That Should Not Change

Do not add:

- runtime logs;
- AITP run state;
- copied long prose from the lecture;
- ad hoc helper scripts.

## Mirror Note Contract

If the optional human note is created, it should contain:

- `kb_unit_id: bridge:local-weyl-node-to-berry-flux`
- a concise explanation of the bridge;
- stable wiki-links to nearby mirrors such as:
  - `[[human-mirror/Quantum Matter/Topological Phases/Weyl Node|Weyl Node]]`
  - `[[human-mirror/Quantum Matter/Topological Phases/Berry Curvature|Berry Curvature]]`

## PR Summary Shape

The pull request description should say:

- write mode: `unit-promotion`
- source id: `witten-1510.07698`
- created unit: `bridge:local-weyl-node-to-berry-flux`
- updated edges: list the exact edge ids
- mirror sync: yes or no
- unresolved items: what still remains upstream in `L2`

## Acceptance

The change is acceptable only if:

- `python3 scripts/kb.py check` passes;
- `python3 scripts/kb.py build` passes;
- the bridge is source-grounded and retrieval-sized;
- the mirror note, if present, is clearly secondary to the canonical unit.
