---
title: "Fermi Arc"
type: concept
domain: "Quantum Matter"
status: reviewed
aliases: []
sources:
  - "arXiv:1510.07698v2"
  - "Internal: units/concepts/fermi-arc.json"
created: 2026-03-16
updated: 2026-03-16
kb_unit_id: concept:fermi-arc
---

## Definition (strict)

> [!definition] Fermi Arc
> A Fermi arc is a surface-state locus in boundary momentum space whose endpoints lie at the projections of bulk Weyl nodes of opposite total charge.

^def-fermi-arc

## Equivalent formulations

- A Fermi arc is a boundary-spectrum signature of bulk Weyl-node topology.
- It is an open surface-state curve whose endpoints are fixed by projected bulk nodes.

## Mathematical formulation

- In the current exemplar the key structure is the relation between projected bulk node data and the support of surface states in boundary momentum space.

## Physical intuition

Unlike an ordinary closed Fermi surface, a Fermi arc is open in the surface Brillouin zone. It exists because the boundary theory must encode the bulk topology of Weyl nodes.

## Examples / counterexamples

- Example: Weyl semimetal surfaces exhibit arcs connecting projections of bulk nodes.
- Counterexample: if projected nodes coincide, the simple arc picture can reorganize.

## Common pitfalls

- A Fermi arc is not just any open-looking surface feature.
- It is a boundary object, not the bulk node itself.

## Research Layer

This note is the public human mirror of `concept:fermi-arc`.

## Claim Ledger

| Claim | Evidence | Confidence |
|-------|----------|------------|
| Fermi arcs are introduced in Lecture One as boundary signatures of bulk Weyl topology. | arXiv:1510.07698v2, `lecture-one/weyl-fermions-and-fermi-arcs`. | HIGH |
| Their endpoints are tied to projected bulk nodes. | `units/concepts/fermi-arc.json`. | HIGH |

## Knowledge Graph

### Prerequisites

- [[human-mirror/Quantum Matter/Topological Phases/Weyl Node|Weyl Node]]

### Related

- [[human-mirror/Quantum Matter/Topological Phases/Nielsen-Ninomiya Theorem|Nielsen-Ninomiya Theorem]]
- [[human-mirror/Quantum Matter/Topological Phases/Witten Lecture One Source Map|Witten Lecture One Source Map]]

## Unresolved Links Queue

- Add the supporting public mirror for the bulk-boundary bridge object.

## References

- arXiv:1510.07698v2, Lecture One, `lecture-one/weyl-fermions-and-fermi-arcs`
- Internal: `units/concepts/fermi-arc.json`
