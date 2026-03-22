# Taylor Expand The Two-Band Hamiltonian Near The Crossing

- ID: `derivation_step:taylor-expand-two-band-hamiltonian-near-crossing`
- Type: `derivation_step`
- Domain: `topological-phases-of-matter`
- Subdomain: `weyl-semimetals`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Start from the local 2x2 Bloch Hamiltonian, subtract the scalar part, and Taylor expand the Pauli-vector coefficients around the isolated bad point.

## Scope
First nontrivial step in the local derivation of the Weyl Hamiltonian.

## Regime
Local momentum-space analysis near a bad point.

## Assumptions
- `The crossing point \vec p_* is isolated.`
- `The scalar shift does not affect whether the two levels cross.`

## Representation
Low-energy Taylor expansion of the local 2x2 Bloch Hamiltonian.

## Source Anchors
- `lecture-one/three-dimensions | eqs: localexp | Witten first writes the generic 2x2 Hamiltonian and then expands around the bad point.`

## Mathematical Content
- `kind=display` | `label=localexp` | Generic local two-band Hamiltonian.
$$
H(\vec p)=a(\vec p)+\sum_i b_i(\vec p)\sigma^i
$$
- `kind=display` | Taylor expansion after using b_i(\vec p_*)=0 at the bad point.
$$
b_i(\vec p_*+\delta \vec p)=\sum_j (\partial_j b_i)_{\vec p_*}\,\delta p_j+O(\delta p^2)
$$

## Symbols
- none

## Dependencies
- [Two-Band Hamiltonian A Plus B Dot Sigma](../Equations/two-band-hamiltonian-d-dot-sigma.md)
- [Band Crossing](../Concepts/band-crossing.md)

## Related Units
- [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md)
- [An Invertible Linear Term Gives A Weyl Hamiltonian](invertible-linear-term-gives-weyl-hamiltonian.md)

## Step Inputs
- [Two-Band Hamiltonian A Plus B Dot Sigma](../Equations/two-band-hamiltonian-d-dot-sigma.md)
- [Band Crossing](../Concepts/band-crossing.md)

## Step Justification
- A crossing requires the Pauli-vector coefficients to vanish at the bad point after the scalar shift is removed.
- A smooth Bloch Hamiltonian can be Taylor expanded around the isolated crossing momentum.
- Quadratic terms are suppressed in the low-energy limit compared with the linear term.

## Retrieval Hints
- `Use when a derivation answer must show where the linearized Weyl Hamiltonian actually comes from.`

## Outgoing Edges
- `supports` -> [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md): The Taylor expansion is the first explicit step behind the Weyl-node definition.

## Incoming Edges
- none
