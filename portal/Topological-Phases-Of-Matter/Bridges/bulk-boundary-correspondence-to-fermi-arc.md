# Bulk-Boundary Correspondence To Fermi Arc

- ID: `bridge:bulk-boundary-correspondence-to-fermi-arc`
- Type: `bridge`
- Domain: `topological-phases-of-matter`
- Subdomain: `bridge-objects`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
The same bulk topology that assigns charges to Weyl nodes reorganizes boundary spectra into open Fermi arcs, so the arc is a boundary projection of changing bulk topological data.

## Scope
Lecture One bridge from bulk node charge to surface Fermi arcs.

## Regime
Boundary manifestation of bulk Weyl-node topology.

## Assumptions
- `A boundary geometry is chosen.`
- `Bulk Weyl nodes are the relevant low-energy topological defects.`

## Dependencies
- [Weyl Node](../Concepts/weyl-node.md)
- [Fermi Arc](../Concepts/fermi-arc.md)

## Related Units
- [Fermi Arcs Terminate At Projected Weyl Nodes](../Claims/fermi-arcs-terminate-at-projected-weyl-nodes.md)

## Source Anchors
- `lecture-one/weyl-fermions-and-fermi-arcs | Lecture One treats Fermi arcs as the boundary face of the bulk Weyl-node story.`
- `lecture-one/gapless-boundary-modes-from-dirac-fermions | Boundary-mode intuition supports the bridge to surface spectra.`

## Outgoing Edges
- `supports` -> [Fermi Arcs Terminate At Projected Weyl Nodes](../Claims/fermi-arcs-terminate-at-projected-weyl-nodes.md): The bridge supports the boundary endpoint claim for Fermi arcs.

## Incoming Edges
- [Fermi Arcs Terminate At Projected Weyl Nodes](../Claims/fermi-arcs-terminate-at-projected-weyl-nodes.md) -> `derived_from`: The Fermi-arc endpoint claim is obtained through the bulk-boundary bridge.
- [Fermi Arc](../Concepts/fermi-arc.md) -> `bridges_to`: The boundary arc is connected to a bulk-boundary bridge object.

## Failure Modes
- `Boundary disorder or coincident node projections can complicate the visible arc structure.`

## Formal Targets
- `aitp-l2`
