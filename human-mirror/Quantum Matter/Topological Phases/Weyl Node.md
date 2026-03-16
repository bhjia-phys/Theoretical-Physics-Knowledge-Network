---
title: "Weyl Node"
type: concept
domain: "Quantum Matter"
status: reviewed
aliases:
  - "Weyl point"
  - "Weyl crossing"
sources:
  - "arXiv:1510.07698v2"
  - "Internal: units/concepts/weyl-node.json"
  - "Internal: sources/witten-1510.07698/manifest.json"
created: 2026-03-16
updated: 2026-03-16
kb_unit_id: concept:weyl-node
---

## Definition (strict)

> [!definition] Weyl Node
> A Weyl node is an isolated three-dimensional two-band crossing whose linearized Hamiltonian is a Weyl Hamiltonian and whose local topological charge is nonzero.

^def-weyl-node

## Equivalent formulations

- A Weyl node is a local two-band crossing with nonzero chirality.
- A Weyl node is a momentum-space source or sink of Berry flux in the filled-state picture.

## Mathematical formulation

- In Lecture One the local Hamiltonian is expanded near the crossing into a `2 x 2` Weyl form.
- The Jacobian sign of the linearization gives the node chirality.

## Physical intuition

The Weyl node is the stable local particle-like crossing in three dimensions. It is local enough to be described by a small Hamiltonian patch, but topological enough that it cannot disappear by an arbitrarily small generic perturbation unless opposite charge is available elsewhere.

## Examples / counterexamples

- Example: a tunable lattice model can create and annihilate Weyl-node pairs.
- Counterexample: a crossing away from the Fermi energy is not automatically a clean Weyl semimetal.

## Common pitfalls

- A local Weyl cone does not by itself solve global lattice consistency.
- Not every band crossing is a Weyl node.

## Research Layer

This note is the public human mirror of `concept:weyl-node`.

## Claim Ledger

| Claim | Evidence | Confidence |
|-------|----------|------------|
| An isolated generic three-dimensional two-band crossing is locally a Weyl node. | arXiv:1510.07698v2, `lecture-one/three-dimensions`, equation labels `xpa`, `perd`. | HIGH |
| The node chirality is encoded by the Jacobian sign of the local linearization. | arXiv:1510.07698v2, `lecture-one/three-dimensions`, equation label `perd`. | HIGH |

## Knowledge Graph

### Prerequisites

- [[human-mirror/Quantum Matter/Topological Phases/Index|Topological Phases]]

### Related

- [[human-mirror/Quantum Matter/Topological Phases/Berry Curvature|Berry Curvature]]
- [[human-mirror/Quantum Matter/Topological Phases/Fermi Arc|Fermi Arc]]
- [[human-mirror/Quantum Matter/Topological Phases/Nielsen-Ninomiya Theorem|Nielsen-Ninomiya Theorem]]
- [[human-mirror/Quantum Matter/Topological Phases/Witten Lecture One Source Map|Witten Lecture One Source Map]]

## Unresolved Links Queue

- Add the public bridge mirror from the local Weyl picture to the Berry-monopole picture.

## References

- arXiv:1510.07698v2, Lecture One, `lecture-one/three-dimensions`, equation labels `xpa`, `perd`
- Internal: `units/concepts/weyl-node.json`
