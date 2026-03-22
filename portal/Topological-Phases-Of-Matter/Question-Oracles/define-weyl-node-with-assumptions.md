# Oracle For Defining A Weyl Node With Assumptions

- ID: `question_oracle:define-weyl-node-with-assumptions`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for the flagship Weyl-node definition question.

## Scope
Detailed answer key for the Weyl-node definition question.

## Regime
Topic regression oracle.

## Assumptions
- `This oracle is scoped to the current Lecture One exemplar.`

## Representation
Detailed oracle object.

## Source Anchors
- `lecture-one/three-dimensions | eqs: localexp, xpa, perd | The oracle expects the local 2x2 form, the linearized Weyl cone, and the chirality sign.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Define A Weyl Node With Its Assumptions](../Regression-Questions/define-weyl-node-with-assumptions.md)

## Related Units
- [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md)

## Prompt
Detailed oracle for regression_question:define-weyl-node-with-assumptions.

## Pass Conditions
- The answer states the local two-band Hamiltonian and the isolated three-dimensional setting.
- The answer names the invertible Jacobian or equivalent nondegeneracy condition.
- The answer identifies chirality as the sign of the local determinant.

## Failure Triggers
- Only saying 'a Weyl node is a band crossing with chirality' without the local Hamiltonian is insufficient.
- Fail if the answer omits the nondegeneracy condition on the linear term.

## Mandatory Units
- [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md)
- [Three-Dimensional Two-Band Crossing Symbols](../Notation-Maps/three-dimensional-two-band-crossing-symbols.md)

## Mandatory Equation Labels
- `localexp`
- `xpa`
- `perd`

## Common Failure Patterns
- Treating any band crossing as a Weyl node without stating the isolated and nondegenerate local conditions.
- Naming chirality without tying it to the determinant sign of the linearized map.

## Grading Rubric
- Pass requires the local 2x2 Hamiltonian, the isolated three-dimensional crossing assumption, the nondegeneracy condition, and the determinant-sign definition of chirality.
- Partial is appropriate if the answer captures the general picture but omits either the local formula or the Jacobian criterion.

## Outgoing Edges
- `oracles` -> [Define A Weyl Node With Its Assumptions](../Regression-Questions/define-weyl-node-with-assumptions.md): This oracle records the pass conditions for the Weyl-node definition question.

## Incoming Edges
- none
