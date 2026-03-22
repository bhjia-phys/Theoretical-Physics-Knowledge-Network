# Three-Dimensional Two-Band Crossing Symbols

- ID: `notation_map:three-dimensional-two-band-crossing-symbols`
- Type: `notation_map`
- Domain: `topological-phases-of-matter`
- Subdomain: `notation`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
This notation map fixes the symbols used in Lecture One for the local 2x2 crossing Hamiltonian, its Taylor expansion, and the resulting chirality sign.

## Scope
Reusable symbol map for the local crossing-to-Weyl derivation.

## Regime
Lecture One local Weyl-node analysis.

## Assumptions
- `The local band problem has already been reduced to a two-band description.`

## Representation
Symbol table for the local crossing Hamiltonian and its Jacobian.

## Source Anchors
- `lecture-one/three-dimensions | eqs: localexp, xpa, perd | The notation here is what the local linearization and chirality formula reuse downstream.`

## Mathematical Content
- none

## Symbols
| Symbol | Meaning |
|---|---|
| `a(\vec p)` | scalar shift of the local 2x2 Hamiltonian |
| `b_i(\vec p)` | Pauli-vector coefficients whose zero locates the crossing |
| `\sigma^i` | Pauli matrices acting on the local two-band space |
| `(\partial_j b_i)_{\vec p_*}` | Jacobian of the Pauli-vector coefficients at the bad point |

## Dependencies
- [Two-Band Hamiltonian A Plus B Dot Sigma](../Equations/two-band-hamiltonian-d-dot-sigma.md)
- [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md)

## Related Units
- [Weyl Node](../Concepts/weyl-node.md)
- [Taylor Expand The Two-Band Hamiltonian Near The Crossing](../Derivation-Steps/taylor-expand-two-band-hamiltonian-near-crossing.md)

## Retrieval Hints
- `Use whenever a proof or regression answer needs to state Witten's local symbols explicitly.`

## Outgoing Edges
- `supports` -> [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md): The notation map fixes the symbols needed for the Weyl-node definition.

## Incoming Edges
- none
