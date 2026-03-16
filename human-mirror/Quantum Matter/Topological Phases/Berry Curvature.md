---
title: "Berry Curvature"
type: concept
domain: "Quantum Matter"
status: reviewed
aliases: []
sources:
  - "arXiv:1510.07698v2"
  - "Internal: units/concepts/berry-curvature.json"
created: 2026-03-16
updated: 2026-03-16
kb_unit_id: concept:berry-curvature
---

## Definition (strict)

> [!definition] Berry Curvature
> Berry curvature is the curvature two-form of the Berry connection; in Lecture One its flux through a sphere around a bad point measures the node's topological charge.

^def-berry-curvature

## Equivalent formulations

- Berry curvature is the field strength of the Berry connection.
- In the Weyl-node setting it is the monopole-like flux density whose integral yields node charge.

## Mathematical formulation

- In the abelian setting the curvature is the exterior derivative of the Berry connection.
- Witten Lecture One uses the flux integral over a sphere around a bad point to recover topological charge.

## Physical intuition

Berry curvature measures how geometric phase transport fails to be flat. Its local field-strength language is what turns the qualitative Berry-phase picture into a concrete topological-charge computation.

## Examples / counterexamples

- Example: flux through a sphere around a Weyl node gives the node sign.
- Counterexample: if the occupied subspace is not isolated, the simple abelian description breaks down.

## Common pitfalls

- Do not confuse the connection one-form with its curvature.
- Smooth bundle language applies only away from singular points.

## Research Layer

This note is the public human mirror of `concept:berry-curvature`.

## Claim Ledger

| Claim | Evidence | Confidence |
|-------|----------|------------|
| Berry curvature is the curvature of the Berry connection. | arXiv:1510.07698v2, `lecture-one/the-berry-connection`, equation labels `fc`, `wif`. | HIGH |
| Its flux measures Weyl-node topological charge. | arXiv:1510.07698v2, `lecture-one/the-berry-connection`, equation label `zif`. | HIGH |

## Knowledge Graph

### Prerequisites

- [[human-mirror/Quantum Matter/Topological Phases/Berry Connection|Berry Connection]]

### Related

- [[human-mirror/Quantum Matter/Topological Phases/Weyl Node|Weyl Node]]
- [[human-mirror/Quantum Matter/Topological Phases/Nielsen-Ninomiya Theorem|Nielsen-Ninomiya Theorem]]

## Unresolved Links Queue

- Add the supporting public mirror for the Berry-flux equation object.

## References

- arXiv:1510.07698v2, Lecture One, `lecture-one/the-berry-connection`, equation labels `fc`, `zif`, `wif`
- Internal: `units/concepts/berry-curvature.json`
