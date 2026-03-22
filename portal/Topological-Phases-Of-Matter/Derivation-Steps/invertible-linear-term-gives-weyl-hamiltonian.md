# An Invertible Linear Term Gives A Weyl Hamiltonian

- ID: `derivation_step:invertible-linear-term-gives-weyl-hamiltonian`
- Type: `derivation_step`
- Domain: `topological-phases-of-matter`
- Subdomain: `weyl-semimetals`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
If the Jacobian of the Pauli-vector coefficients at the bad point is invertible, the linearized Hamiltonian is equivalent to the standard Weyl Hamiltonian after a linear change of coordinates.

## Scope
Second nontrivial step in the derivation of the Weyl-node local form.

## Regime
Low-energy local analysis of an isolated point node.

## Assumptions
- `The linear map (\partial_j b_i)_{\vec p_*} is invertible.`
- `Only the linearized low-energy structure is being kept.`

## Representation
Linearized Weyl Hamiltonian extracted from the first-order Pauli-vector term.

## Source Anchors
- `lecture-one/three-dimensions | eqs: xpa | The local Hamiltonian is put into Weyl form by linearizing the Pauli-vector coefficients.`

## Mathematical Content
- `kind=display` | The linearized Hamiltonian with V_{ij}=(\partial_j b_i)_{\vec p_*}.
$$
H_{\mathrm{lin}}(\delta \vec p)=\sum_{i,j}V_{ij}\,\delta p_j\,\sigma^i
$$
- `kind=display` | `label=xpa` | After a linear redefinition of momentum coordinates, the local cone is the Weyl Hamiltonian.
$$
H_{\mathrm{lin}}\sim \chi\,\sum_{i=1}^3 q_i\sigma^i
$$

## Symbols
- none

## Dependencies
- [Taylor Expand The Two-Band Hamiltonian Near The Crossing](taylor-expand-two-band-hamiltonian-near-crossing.md)
- [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md)

## Related Units
- [Weyl Node](../Concepts/weyl-node.md)
- [The Jacobian Sign Defines The Local Chirality](jacobian-sign-defines-local-chirality.md)

## Step Inputs
- [Taylor Expand The Two-Band Hamiltonian Near The Crossing](taylor-expand-two-band-hamiltonian-near-crossing.md)

## Step Justification
- An invertible Jacobian means the three components of b_i change independently to first order.
- A nonsingular linear change of momentum coordinates reduces the linear term to the standard Weyl form.
- The sign of the determinant survives the coordinate change and becomes the chirality data.

## Retrieval Hints
- `Use when a proof must explain why a generic isolated 3D two-band crossing is locally Weyl.`

## Outgoing Edges
- `supports` -> [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md): The invertible linear term turns the generic crossing into the Weyl Hamiltonian.

## Incoming Edges
- [Reconstruct The Local Weyl Linearization](../Regression-Questions/reconstruct-local-weyl-linearization.md) -> `tests`: The regression question tests whether the local Weyl derivation can be reconstructed step by step.
