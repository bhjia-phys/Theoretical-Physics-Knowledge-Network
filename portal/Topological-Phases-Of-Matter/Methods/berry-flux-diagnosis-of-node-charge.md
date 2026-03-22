# Berry-Flux Diagnosis Of Node Charge

- ID: `method:berry-flux-diagnosis-of-node-charge`
- Type: `method`
- Domain: `topological-phases-of-matter`
- Subdomain: `diagnostics`
- Canonical Family: ``
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

## Representation
Local computational diagnostic using curvature flux.

## Source Anchors
- `lecture-one/the-berry-connection | eqs: zif | Lecture One states the flux rule explicitly.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Berry Curvature](../Concepts/berry-curvature.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Winding Number](../Quantities/winding-number.md)

## Related Units
- [Berry Flux Gives Node Charge](../Derivations/berry-flux-gives-node-charge.md)
- [Weyl Node To Berry Monopole](../Bridges/weyl-node-to-berry-monopole.md)

## Failure Modes
- `The method must be modified for non-abelian occupied subspaces.`

## Formal Targets
- `aitp-l2`

## Retrieval Hints
- `Use as an explicit procedure rather than only a conceptual statement.`

## Outgoing Edges
- `uses` -> [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md): The diagnostic method is the operational use of the flux formula.

## Incoming Edges
- none
