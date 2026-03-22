# Chirality Of A Weyl Node

- ID: `concept:chirality-of-weyl-node`
- Type: `concept`
- Domain: `topological-phases-of-matter`
- Subdomain: `weyl-semimetals`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
The chirality of a Weyl node is the sign of the Jacobian relating momentum deviations to the Pauli-vector coefficients in the local Hamiltonian, equivalently the sign of its Berry-flux charge.

## Scope
Lecture One chirality sign from both local Hamiltonian and Berry-flux viewpoints.

## Regime
Local three-dimensional Weyl-point analysis.

## Assumptions
- `The local crossing is simple and linear.`
- `Orientation conventions are fixed consistently.`

## Representation
Orientation sign of the local Weyl map.

## Source Anchors
- `lecture-one/three-dimensions | eqs: perd | The sign of the determinant is the local chirality label.`
- `lecture-one/the-berry-connection | eqs: zif | Berry flux gives the same topological sign.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Weyl Node](weyl-node.md)
- [Chirality Sign](../Quantities/chirality-sign.md)
- [Winding Number](../Quantities/winding-number.md)

## Related Units
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Two-Band Hamiltonian A Plus B Dot Sigma](../Equations/two-band-hamiltonian-d-dot-sigma.md)
- [Weyl Node To Berry Monopole](../Bridges/weyl-node-to-berry-monopole.md)

## Failure Modes
- `Mixed sign conventions can flip the reported chirality without changing the physics.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when a query asks how chirality is computed or interpreted.`

## Outgoing Edges
- `depends_on` -> [Chirality Sign](../Quantities/chirality-sign.md): The chirality concept is operationalized by the determinant sign.

## Incoming Edges
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md) -> `explains`: Berry flux supplies the same sign and integer data as local chirality.
- [Weyl Node](weyl-node.md) -> `explains`: Chirality is a property of an isolated Weyl node.
