# Chirality Sign

- ID: `quantity:chirality-sign`
- Type: `quantity`
- Domain: `topological-phases-of-matter`
- Subdomain: `weyl-semimetals`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `stable`

## Summary
The chirality sign is the plus or minus label attached to a Weyl node by the sign of the Jacobian determinant of the local linearized map.

## Scope
Lecture One sign data for isolated linear Weyl crossings.

## Regime
Local Weyl-node analysis.

## Assumptions
- `An orientation convention has been fixed.`

## Dependencies
- none

## Related Units
- [Chirality Of A Weyl Node](../Concepts/chirality-of-weyl-node.md)
- [Lattice Weyl Nodes Sum To Zero Net Chirality](../Claims/lattice-weyl-nodes-sum-to-zero-net-chirality.md)

## Source Anchors
- `lecture-one/three-dimensions | eqs: perd | The determinant sign is the chirality label.`

## Outgoing Edges
- none

## Incoming Edges
- [Chirality Of A Weyl Node](../Concepts/chirality-of-weyl-node.md) -> `depends_on`: The chirality concept is operationalized by the determinant sign.

## Failure Modes
- `Sign conventions can differ between references.`

## Formal Targets
- `aitp-l2`
- `lean`
