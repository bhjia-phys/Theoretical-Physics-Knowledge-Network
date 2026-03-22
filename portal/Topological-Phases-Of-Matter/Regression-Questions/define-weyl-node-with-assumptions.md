# Define A Weyl Node With Its Assumptions

- ID: `regression_question:define-weyl-node-with-assumptions`
- Type: `regression_question`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Tests whether the topic can state the Weyl-node definition with the correct local assumptions and notational data.

## Scope
Flagship definition question for the local Weyl-node branch.

## Regime
Topic regression for the Witten Lecture One exemplar.

## Assumptions
- `The answer is expected to come from the curated Lecture One branch.`

## Representation
Definition-family regression prompt.

## Source Anchors
- `lecture-one/three-dimensions | eqs: localexp, xpa, perd | The answer should recover Witten's local 2x2 form, the linearized Weyl cone, and the chirality sign.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md)
- [Three-Dimensional Two-Band Crossing Symbols](../Notation-Maps/three-dimensional-two-band-crossing-symbols.md)

## Related Units
- [Oracle For Defining A Weyl Node With Assumptions](../Question-Oracles/define-weyl-node-with-assumptions.md)

## Prompt
State precisely what a Weyl node is in Witten Lecture One, including the local 2x2 Hamiltonian, the nondegeneracy assumption, and the chirality data.

## Question Family
`definition`

## Pass Conditions
- The answer states that the crossing is isolated, three-dimensional, and locally reduced to two bands.
- The answer names the invertible linear Pauli-vector Jacobian as the nondegeneracy condition.
- The answer explains that chirality is the sign of the determinant and not merely a vague handedness label.

## Primary Retrieval Paths
- [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md)
- [Three-Dimensional Two-Band Crossing Symbols](../Notation-Maps/three-dimensional-two-band-crossing-symbols.md)
- [Witten Topological Phases Lecture One Source Map](../Source-Maps/witten-topological-phases-lecture-one.md)

## Retrieval Hints
- `Use in regression runs to test whether the KB can give a precise local Weyl-node definition.`

## Outgoing Edges
- `tests` -> [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md): The regression question tests whether the definition branch is precise and complete.

## Incoming Edges
- [Oracle For Defining A Weyl Node With Assumptions](../Question-Oracles/define-weyl-node-with-assumptions.md) -> `oracles`: This oracle records the pass conditions for the Weyl-node definition question.
