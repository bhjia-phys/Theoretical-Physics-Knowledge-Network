# Berry-Flux Diagnosis Of Node Charge

- ID: `method:berry-flux-diagnosis-of-node-charge`
- Type: `method`
- Domain: `topological-phases-of-matter`
- Subdomain: `diagnostics`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
To determine the charge of an isolated Weyl node, surround it by a small sphere in momentum space, compute the Berry curvature of the occupied state, and integrate the flux over the sphere.

## Scope
Operational procedure distilled from Lecture One.

## Regime
Local diagnostic for an isolated point node.

## Assumptions
- `A local occupied-state bundle can be constructed on the surrounding sphere.`

## Dependencies
- [Berry Curvature](../Concepts/berry-curvature.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Winding Number](../Quantities/winding-number.md)

## Related Units
- [Berry Flux Gives Node Charge](../Derivations/berry-flux-gives-node-charge.md)
- [Weyl Node To Berry Monopole](../Bridges/weyl-node-to-berry-monopole.md)

## Source Anchors
- `lecture-one/the-berry-connection | eqs: zif | Lecture One states the flux rule explicitly.`

## Outgoing Edges
- `uses` -> [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md): The diagnostic method is the operational use of the flux formula.

## Incoming Edges
- none

## Failure Modes
- `The method must be modified for non-abelian occupied subspaces.`

## Formal Targets
- `aitp-l2`
