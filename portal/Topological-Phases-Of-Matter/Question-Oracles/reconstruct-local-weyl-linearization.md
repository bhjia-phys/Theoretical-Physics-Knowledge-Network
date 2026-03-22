# Oracle For Reconstructing The Local Weyl Linearization

- ID: `question_oracle:reconstruct-local-weyl-linearization`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for the flagship local Weyl derivation question.

## Scope
Detailed answer key for reconstructing the local Weyl-node derivation.

## Regime
Topic regression oracle.

## Assumptions
- `The answer must show intermediate steps, not only the endpoint Hamiltonian.`

## Representation
Detailed oracle object.

## Source Anchors
- `lecture-one/three-dimensions | eqs: localexp, xpa, perd | The derivation must be reconstructed from the lecture's actual local formulas.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Reconstruct The Local Weyl Linearization](../Regression-Questions/reconstruct-local-weyl-linearization.md)

## Related Units
- [Taylor Expand The Two-Band Hamiltonian Near The Crossing](../Derivation-Steps/taylor-expand-two-band-hamiltonian-near-crossing.md)
- [An Invertible Linear Term Gives A Weyl Hamiltonian](../Derivation-Steps/invertible-linear-term-gives-weyl-hamiltonian.md)
- [The Jacobian Sign Defines The Local Chirality](../Derivation-Steps/jacobian-sign-defines-local-chirality.md)

## Prompt
Detailed oracle for regression_question:reconstruct-local-weyl-linearization.

## Failure Triggers
- Fail if the answer jumps from the generic 2x2 form directly to the chirality sign.
- Fail if the answer never states why the invertible Jacobian matters.

## Mandatory Units
- [Taylor Expand The Two-Band Hamiltonian Near The Crossing](../Derivation-Steps/taylor-expand-two-band-hamiltonian-near-crossing.md)
- [An Invertible Linear Term Gives A Weyl Hamiltonian](../Derivation-Steps/invertible-linear-term-gives-weyl-hamiltonian.md)
- [The Jacobian Sign Defines The Local Chirality](../Derivation-Steps/jacobian-sign-defines-local-chirality.md)

## Mandatory Equation Labels
- `localexp`
- `xpa`
- `perd`

## Derivation Spine
- Write the local 2x2 Hamiltonian.
- Expand the Pauli-vector coefficients around the bad point.
- Use invertibility of the Jacobian to reduce the linear term to Weyl form.
- Read off chirality from the determinant sign.

## Common Failure Patterns
- Starting from the generic two-band Hamiltonian and skipping the actual Taylor expansion around the bad point.
- Naming chirality without showing how the determinant of the Jacobian enters the reduced Weyl cone.

## Grading Rubric
- Pass requires the ordered local expansion from the generic 2x2 form to the Weyl Hamiltonian together with the determinant-sign chirality rule.
- Partial is appropriate if the endpoint Weyl cone is correct but one of the intermediate reduction steps is hidden.

## Outgoing Edges
- `oracles` -> [Reconstruct The Local Weyl Linearization](../Regression-Questions/reconstruct-local-weyl-linearization.md): This oracle records the derivation spine for the local Weyl linearization question.

## Incoming Edges
- none
