# Weyl Node As An Isolated Three-Dimensional Two-Band Crossing

- ID: `definition:weyl-node-as-isolated-three-dimensional-two-band-crossing`
- Type: `definition`
- Domain: `topological-phases-of-matter`
- Subdomain: `weyl-semimetals`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
A Weyl node is an isolated three-dimensional two-band crossing whose linearized Hamiltonian has an invertible Pauli-vector Jacobian, so the crossing carries a nonzero local topological charge.

## Scope
Lecture One local definition of a Weyl node in terms of the 2x2 Bloch Hamiltonian.

## Regime
Low-energy expansion near an isolated 3D crossing.

## Assumptions
- `The crossing is isolated in three-dimensional momentum space.`
- `A two-band local reduction is valid near the crossing.`
- `The linear term in the Pauli-vector coefficients has nonzero determinant.`

## Representation
Local 2x2 Bloch Hamiltonian with an invertible linear Pauli-vector term at the bad point.

## Source Anchors
- `lecture-one/three-dimensions | eqs: localexp, xpa, perd | Witten reduces the local crossing to a Pauli-vector Hamiltonian and identifies the chirality by the Jacobian sign.`

## Mathematical Content
- `kind=display` | `label=localexp` | Universal local two-band form.
$$
H(\vec p)=a(\vec p)+\sum_{i=1}^3 b_i(\vec p)\sigma^i
$$
- `kind=display` | Taylor expansion at the isolated crossing point after subtracting the scalar shift.
$$
H(\vec p_*+\delta \vec p)=a(\vec p_*)+\sum_{i,j}(\partial_j b_i)_{\vec p_*}\,\delta p_j\,\sigma^i+O(\delta p^2)
$$
- `kind=display` | `label=perd` | The local Jacobian sign determines the Weyl-node chirality.
$$
\chi=\operatorname{sign}\det\bigl((\partial_j b_i)_{\vec p_*}\bigr)
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `\vec p_*` | isolated momentum-space crossing point |
| `b_i(\vec p)` | Pauli-vector coefficients of the local Bloch Hamiltonian |
| `\chi` | local Weyl-node chirality or topological sign |

## Dependencies
- [Two-Band Hamiltonian A Plus B Dot Sigma](../Equations/two-band-hamiltonian-d-dot-sigma.md)
- [Chirality Sign](../Quantities/chirality-sign.md)

## Related Units
- [Weyl Node](../Concepts/weyl-node.md)
- [Taylor Expand The Two-Band Hamiltonian Near The Crossing](../Derivation-Steps/taylor-expand-two-band-hamiltonian-near-crossing.md)
- [An Invertible Linear Term Gives A Weyl Hamiltonian](../Derivation-Steps/invertible-linear-term-gives-weyl-hamiltonian.md)
- [The Jacobian Sign Defines The Local Chirality](../Derivation-Steps/jacobian-sign-defines-local-chirality.md)
- [Three-Dimensional Two-Band Crossing Symbols](../Notation-Maps/three-dimensional-two-band-crossing-symbols.md)

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when a query asks for the precise local definition of a Weyl node rather than only intuition.`

## Outgoing Edges
- `defines` -> [Weyl Node](../Concepts/weyl-node.md): The new definition unit makes the local Weyl-node assumptions explicit.

## Incoming Edges
- [The Jacobian Sign Defines The Local Chirality](../Derivation-Steps/jacobian-sign-defines-local-chirality.md) -> `supports`: The chirality step completes the local Weyl-node definition.
- [An Invertible Linear Term Gives A Weyl Hamiltonian](../Derivation-Steps/invertible-linear-term-gives-weyl-hamiltonian.md) -> `supports`: The invertible linear term turns the generic crossing into the Weyl Hamiltonian.
- [Taylor Expand The Two-Band Hamiltonian Near The Crossing](../Derivation-Steps/taylor-expand-two-band-hamiltonian-near-crossing.md) -> `supports`: The Taylor expansion is the first explicit step behind the Weyl-node definition.
- [Define A Weyl Node With Its Assumptions](../Regression-Questions/define-weyl-node-with-assumptions.md) -> `tests`: The regression question tests whether the definition branch is precise and complete.
- [Three-Dimensional Two-Band Crossing Symbols](../Notation-Maps/three-dimensional-two-band-crossing-symbols.md) -> `supports`: The notation map fixes the symbols needed for the Weyl-node definition.
