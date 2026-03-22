# Chirality Sign

- ID: `quantity:chirality-sign`
- Type: `quantity`
- Domain: `topological-phases-of-matter`
- Subdomain: `weyl-semimetals`
- Canonical Family: ``
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

## Representation
Sign of the local Jacobian determinant.

## Source Anchors
- `lecture-one/three-dimensions | eqs: perd | The determinant sign is the chirality label.`

## Mathematical Content
- none

## Symbols
| Symbol | Meaning |
|---|---|
| `sign det(b_ij)` | chirality sign of the Weyl node |

## Dependencies
- none

## Related Units
- [Chirality Of A Weyl Node](../Concepts/chirality-of-weyl-node.md)
- [Lattice Weyl Nodes Sum To Zero Net Chirality](../Claims/lattice-weyl-nodes-sum-to-zero-net-chirality.md)

## Failure Modes
- `Sign conventions can differ between references.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when a query asks what plus or minus Weyl chirality means.`

## Outgoing Edges
- none

## Incoming Edges
- [Chirality Of A Weyl Node](../Concepts/chirality-of-weyl-node.md) -> `depends_on`: The chirality concept is operationalized by the determinant sign.
