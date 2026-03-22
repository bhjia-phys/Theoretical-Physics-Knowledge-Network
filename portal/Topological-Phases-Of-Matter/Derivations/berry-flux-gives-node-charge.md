# Berry Flux Gives Node Charge

- ID: `derivation:berry-flux-gives-node-charge`
- Type: `derivation`
- Domain: `topological-phases-of-matter`
- Subdomain: `berry-geometry`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Once the occupied states are organized into a line bundle, the flux of Berry curvature through a small sphere around a bad point yields the node's integer topological charge.

## Scope
Lecture One curvature-based derivation of node charge.

## Regime
Berry-geometric analysis of isolated Weyl nodes.

## Assumptions
- `The sphere encloses only one bad point.`
- `The occupied bundle is regular on the punctured sphere.`

## Representation
Geometric derivation from curvature flux to integer node charge.

## Source Anchors
- `lecture-one/the-berry-connection | eqs: fc, zif | The derivation uses the Berry bundle and its curvature.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Berry Connection](../Concepts/berry-connection.md)
- [Berry Curvature](../Concepts/berry-curvature.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)

## Related Units
- [Weyl Node To Berry Monopole](../Bridges/weyl-node-to-berry-monopole.md)
- [Chirality Of A Weyl Node](../Concepts/chirality-of-weyl-node.md)

## Failure Modes
- `The abelian derivation needs modification for multiple occupied bands.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use for the geometric route from Berry data to Weyl-node charge.`

## Outgoing Edges
- `derived_from` -> [Berry Curvature](../Concepts/berry-curvature.md): The derivation is driven by Berry-curvature flux.

## Incoming Edges
- none
