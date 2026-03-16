# Fermi Arcs Terminate At Projected Weyl Nodes

- ID: `claim:fermi-arcs-terminate-at-projected-weyl-nodes`
- Type: `claim`
- Domain: `topological-phases-of-matter`
- Subdomain: `boundary-phenomena`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
The endpoints of a Fermi arc in the surface Brillouin zone are fixed by the projections of bulk Weyl nodes that source the changing topological data across momentum slices.

## Scope
Lecture One qualitative bulk-boundary statement for Fermi arcs.

## Regime
Boundary spectrum of a Weyl semimetal.

## Assumptions
- `A boundary orientation is chosen.`
- `Projected Weyl nodes remain distinguishable on the boundary.`

## Dependencies
- [Fermi Arc](../Concepts/fermi-arc.md)
- [Weyl Node](../Concepts/weyl-node.md)
- [Bulk-Boundary Correspondence To Fermi Arc](../Bridges/bulk-boundary-correspondence-to-fermi-arc.md)

## Related Units
- [Crossing Away From The Fermi Energy Is Not Yet A Clean Weyl Semimetal](../Warnings/crossing-away-from-fermi-energy-is-not-yet-a-clean-weyl-semimetal.md)

## Source Anchors
- `lecture-one/weyl-fermions-and-fermi-arcs | Lecture One identifies Fermi arcs as boundary signatures tied to bulk Weyl nodes.`

## Outgoing Edges
- `derived_from` -> [Bulk-Boundary Correspondence To Fermi Arc](../Bridges/bulk-boundary-correspondence-to-fermi-arc.md): The Fermi-arc endpoint claim is obtained through the bulk-boundary bridge.

## Incoming Edges
- [Bulk-Boundary Correspondence To Fermi Arc](../Bridges/bulk-boundary-correspondence-to-fermi-arc.md) -> `supports`: The bridge supports the boundary endpoint claim for Fermi arcs.

## Failure Modes
- `Surface reconstructions or coincident projections can obscure the simple arc picture.`

## Formal Targets
- `aitp-l2`
