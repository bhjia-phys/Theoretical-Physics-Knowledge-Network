---
title: "Nielsen-Ninomiya Theorem"
type: concept
domain: "Quantum Matter"
status: reviewed
aliases:
  - "fermion doubling theorem"
sources:
  - "arXiv:1510.07698v2"
  - "Internal: units/concepts/nielsen-ninomiya-theorem.json"
created: 2026-03-16
updated: 2026-03-16
kb_unit_id: concept:nielsen-ninomiya-theorem
---

## Definition (strict)

> [!definition] Nielsen-Ninomiya Theorem
> For a lattice band structure with isolated Weyl crossings, the sum of all node charges over the Brillouin zone is zero, forbidding a net chirality in a strictly lattice-regularized system.

^def-nielsen-ninomiya-theorem

## Equivalent formulations

- In a lattice Weyl system, positive and negative node charges must balance globally.
- This is the topological form of fermion doubling.

## Mathematical formulation

- Witten Lecture One derives the sum rule through winding-number language and again through Berry-curvature language.
- Compactness of the Brillouin zone is the global ingredient that makes the cancellation unavoidable.

## Physical intuition

A local Weyl cone may carry definite chirality, but a lattice cannot carry a net uncompensated chirality across the whole Brillouin zone. Whatever is created locally must be canceled globally.

## Examples / counterexamples

- Example: explicit lattice Weyl models create nodes in opposite-charge pairs.
- Counterexample: a purely local continuum Weyl model does not by itself enforce the same global sum rule.

## Common pitfalls

- The theorem is global, not merely local.
- It assumes isolated point nodes.

## Research Layer

This note is the public human mirror of `concept:nielsen-ninomiya-theorem`.

## Claim Ledger

| Claim | Evidence | Confidence |
|-------|----------|------------|
| The total node charge in a compact Brillouin zone must vanish. | arXiv:1510.07698v2, `lecture-one/the-nielsen-ninomiya-theorem`, equation labels `nwn`, `cl`. | HIGH |
| The same theorem is recovered from Berry-curvature reasoning. | arXiv:1510.07698v2, `lecture-one/the-berry-connection`, equation label `nna`. | HIGH |

## Knowledge Graph

### Prerequisites

- [[human-mirror/Quantum Matter/Topological Phases/Weyl Node|Weyl Node]]

### Related

- [[human-mirror/Quantum Matter/Topological Phases/Berry Curvature|Berry Curvature]]
- [[human-mirror/Quantum Matter/Topological Phases/Fermi Arc|Fermi Arc]]
- [[human-mirror/Quantum Matter/Topological Phases/Witten Lecture One Source Map|Witten Lecture One Source Map]]

## Unresolved Links Queue

- Add the supporting public mirrors for the Stokes-type derivation and the lattice-consistency warning.

## References

- arXiv:1510.07698v2, Lecture One, `lecture-one/the-nielsen-ninomiya-theorem`, equation labels `nwn`, `wnn`, `cl`
- arXiv:1510.07698v2, Lecture One, `lecture-one/the-berry-connection`, equation label `nna`
- Internal: `units/concepts/nielsen-ninomiya-theorem.json`
