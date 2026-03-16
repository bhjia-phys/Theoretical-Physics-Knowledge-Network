---
title: "Berry Connection"
type: concept
domain: "Quantum Matter"
status: reviewed
aliases:
  - "Berry gauge field"
sources:
  - "arXiv:1510.07698v2"
  - "Internal: units/concepts/berry-connection.json"
created: 2026-03-16
updated: 2026-03-16
kb_unit_id: concept:berry-connection
---

## Definition (strict)

> [!definition] Berry Connection
> The Berry connection is the `U(1)` connection on the line bundle of occupied states over regular momentum space, encoding phase transport of eigenstates along paths.

^def-berry-connection

## Equivalent formulations

- The Berry connection is the gauge field associated with local phase choice.
- Its holonomy gives the Berry phase around a closed loop.

## Mathematical formulation

- In the present exemplar the defining picture is parallel transport of the occupied state along a path.
- The curvature of this connection is the Berry curvature.

## Physical intuition

The Berry connection plays the role of a vector potential in parameter space. It is not itself gauge-invariant, but it organizes phase transport and leads to gauge-invariant curvature and holonomy data.

## Examples / counterexamples

- Example: adiabatic transport of a filled state along a loop yields a Berry phase.
- Counterexample: at singular points there is no globally smooth connection one-form.

## Common pitfalls

- The connection one-form is gauge-dependent.
- The simple abelian story assumes an isolated occupied state.

## Research Layer

This note is the public human mirror of `concept:berry-connection`.

## Claim Ledger

| Claim | Evidence | Confidence |
|-------|----------|------------|
| The Berry connection is defined through phase transport of occupied states. | arXiv:1510.07698v2, `lecture-one/the-berry-connection`, equation label `zb`. | HIGH |
| In the current exemplar it is a `U(1)` connection on the occupied-state line bundle. | `units/concepts/berry-connection.json`. | HIGH |

## Knowledge Graph

### Prerequisites

- [[human-mirror/Quantum Matter/Topological Phases/Index|Topological Phases]]

### Related

- [[human-mirror/Quantum Matter/Topological Phases/Berry Curvature|Berry Curvature]]
- [[human-mirror/Quantum Matter/Topological Phases/Witten Lecture One Source Map|Witten Lecture One Source Map]]

## Unresolved Links Queue

- Add the supporting mirror for the occupied-state line bundle.

## References

- arXiv:1510.07698v2, Lecture One, `lecture-one/the-berry-connection`, equation label `zb`
- Internal: `units/concepts/berry-connection.json`
