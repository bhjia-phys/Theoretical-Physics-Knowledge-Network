# Weyl Node To Berry Monopole

- ID: `bridge:weyl-node-to-berry-monopole`
- Type: `bridge`
- Domain: `topological-phases-of-matter`
- Subdomain: `bridge-objects`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
A Weyl node can be read either as a linearized band crossing or as a momentum-space monopole of Berry curvature whose flux equals the node charge.

## Scope
Lecture One conceptual bridge between Hamiltonian and curvature pictures.

## Regime
Local Weyl-node analysis with Berry geometry.

## Assumptions
- `The node is isolated and the occupied-state bundle is defined away from it.`

## Dependencies
- [Weyl Node](../Concepts/weyl-node.md)
- [Berry Curvature](../Concepts/berry-curvature.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)

## Related Units
- [Chirality Of A Weyl Node](../Concepts/chirality-of-weyl-node.md)
- [Berry-Flux Diagnosis Of Node Charge](../Methods/berry-flux-diagnosis-of-node-charge.md)

## Source Anchors
- `lecture-one/the-berry-connection | eqs: zif | The flux formula is the bridge between node and monopole viewpoints.`

## Outgoing Edges
- `bridges_to` -> [Berry Curvature](../Concepts/berry-curvature.md): The bridge lands on the Berry-curvature picture of the node.

## Incoming Edges
- [Weyl Node](../Concepts/weyl-node.md) -> `bridges_to`: The local crossing picture is bridged to the Berry-flux picture.

## Failure Modes
- `The monopole language is only valid on the punctured region where the Berry bundle is defined.`

## Formal Targets
- `aitp-l2`
