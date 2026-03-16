# Berry Curvature

- ID: `concept:berry-curvature`
- Type: `concept`
- Domain: `topological-phases-of-matter`
- Subdomain: `berry-geometry`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
Berry curvature is the curvature two-form of the Berry connection; in Lecture One its flux through a sphere around a bad point measures the node's topological charge.

## Scope
Lecture One abelian curvature of a two-band occupied-state line bundle.

## Regime
Regular momentum-space region away from bad points.

## Assumptions
- `The occupied-state bundle is smooth on the punctured region.`
- `Singular points are excised before computing dF=0.`

## Dependencies
- [Berry Connection](berry-connection.md)
- [Berry Curvature Two-Form](../Quantities/berry-curvature-two-form.md)

## Related Units
- [Weyl Node](weyl-node.md)
- [Winding Number](../Quantities/winding-number.md)
- [Berry Flux Gives Node Charge](../Derivations/berry-flux-gives-node-charge.md)

## Source Anchors
- `lecture-one/the-berry-connection | eqs: fc, zif, wif | The flux formula and dF=0 organize the topological analysis.`

## Outgoing Edges
- `depends_on` -> [Berry Connection](berry-connection.md): Curvature is defined from the connection.
- `uses` -> [Berry Curvature Two-Form](../Quantities/berry-curvature-two-form.md): The curvature concept is represented by the two-form F.

## Incoming Edges
- [Weyl Node To Berry Monopole](../Bridges/weyl-node-to-berry-monopole.md) -> `bridges_to`: The bridge lands on the Berry-curvature picture of the node.
- [Berry Flux Gives Node Charge](../Derivations/berry-flux-gives-node-charge.md) -> `derived_from`: The derivation is driven by Berry-curvature flux.

## Failure Modes
- `If the subspace is not isolated, the abelian description breaks down.`

## Formal Targets
- `aitp-l2`
- `lean`
