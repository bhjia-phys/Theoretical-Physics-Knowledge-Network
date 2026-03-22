# The Jacobian Sign Defines The Local Chirality

- ID: `derivation_step:jacobian-sign-defines-local-chirality`
- Type: `derivation_step`
- Domain: `topological-phases-of-matter`
- Subdomain: `weyl-semimetals`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
The sign of the determinant of the linearized Pauli-vector Jacobian is the handedness or chirality of the Weyl node.

## Scope
Final local step that converts the linearized Hamiltonian into a signed topological charge.

## Regime
Local topological classification of an isolated Weyl node.

## Assumptions
- `The local linear map is invertible.`

## Representation
Local chirality extracted from the orientation of the linearized Pauli-vector map.

## Source Anchors
- `lecture-one/three-dimensions | eqs: perd | The determinant sign is Witten's compact local chirality formula.`

## Mathematical Content
- `kind=display` | `label=perd` | Local handedness of the Weyl cone.
$$
\chi=\operatorname{sign}\det\bigl((\partial_j b_i)_{\vec p_*}\bigr)
$$

## Symbols
- none

## Dependencies
- [An Invertible Linear Term Gives A Weyl Hamiltonian](invertible-linear-term-gives-weyl-hamiltonian.md)
- [Chirality Sign](../Quantities/chirality-sign.md)

## Related Units
- [Chirality Of A Weyl Node](../Concepts/chirality-of-weyl-node.md)
- [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)

## Step Inputs
- [An Invertible Linear Term Gives A Weyl Hamiltonian](invertible-linear-term-gives-weyl-hamiltonian.md)
- [Chirality Sign](../Quantities/chirality-sign.md)

## Step Justification
- The determinant records whether the linear map from momentum space to Pauli-vector space preserves or reverses orientation.
- That orientation sign is the local degree of the normalized map on a small enclosing sphere.

## Retrieval Hints
- `Use when a derivation answer must justify why the Jacobian sign is the Weyl-node chirality.`

## Outgoing Edges
- `supports` -> [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md): The chirality step completes the local Weyl-node definition.

## Incoming Edges
- none
