# Band Crossing

- ID: `concept:band-crossing`
- Type: `concept`
- Domain: `topological-phases-of-matter`
- Subdomain: `lecture-one`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
A band crossing is a momentum-space point where two energy bands become degenerate; in Lecture One it is the local seed from which Weyl and Dirac low-energy descriptions are extracted.

## Scope
Lecture One local crossing analysis in one, two, and three spatial dimensions.

## Regime
Noninteracting or effectively single-particle band theory.

## Assumptions
- `Bloch-band description is valid.`
- `The crossing is analyzed in momentum space.`

## Representation
Degenerate point in a Bloch Hamiltonian family.

## Source Anchors
- `lecture-one/three-dimensions | eqs: localexp | Generic two-band crossings are organized through H=a+b.sigma.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- none

## Related Units
- [Weyl Node](weyl-node.md)
- [Dirac Point In Two Dimensions](dirac-point-in-2d.md)
- [Isolated 3D Two-Band Crossings Are Weyl Nodes](../Claims/isolated-3d-two-band-crossings-are-weyl-nodes.md)

## Failure Modes
- `Extended nodal lines or surfaces require different treatment.`
- `Crossings away from the Fermi energy may not determine low-energy physics.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when a query asks what a Weyl or Dirac point is locally.`

## Outgoing Edges
- `explains` -> [Dirac Point In Two Dimensions](dirac-point-in-2d.md): A two-dimensional Dirac point is another dimension-specific form of band crossing.
- `explains` -> [Weyl Node](weyl-node.md): A Weyl node is a special isolated three-dimensional band crossing.
- `warned_by` -> [Crossing Away From The Fermi Energy Is Not Yet A Clean Weyl Semimetal](../Warnings/crossing-away-from-fermi-energy-is-not-yet-a-clean-weyl-semimetal.md): A crossing away from the Fermi energy does not automatically define the low-energy phase.

## Incoming Edges
- none
