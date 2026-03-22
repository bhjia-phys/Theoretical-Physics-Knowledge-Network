# Reconstruct The Local Weyl Linearization

- ID: `regression_question:reconstruct-local-weyl-linearization`
- Type: `regression_question`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Tests whether the topic can reconstruct the actual derivation from the generic local 2x2 Hamiltonian to the Weyl cone and its chirality.

## Scope
Flagship derivation question for the local Weyl-node branch.

## Regime
Topic regression for the Witten Lecture One exemplar.

## Assumptions
- `The answer should expose explicit intermediate formulas, not only the endpoint.`

## Representation
Derivation-family regression prompt.

## Source Anchors
- `lecture-one/three-dimensions | eqs: localexp, xpa, perd | The derivation must expose the Taylor expansion, invertible linear map, and chirality sign.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Taylor Expand The Two-Band Hamiltonian Near The Crossing](../Derivation-Steps/taylor-expand-two-band-hamiltonian-near-crossing.md)
- [An Invertible Linear Term Gives A Weyl Hamiltonian](../Derivation-Steps/invertible-linear-term-gives-weyl-hamiltonian.md)
- [The Jacobian Sign Defines The Local Chirality](../Derivation-Steps/jacobian-sign-defines-local-chirality.md)

## Related Units
- [Oracle For Reconstructing The Local Weyl Linearization](../Question-Oracles/reconstruct-local-weyl-linearization.md)

## Prompt
Starting from the local 2x2 Hamiltonian near a bad point, reconstruct the derivation that gives the Weyl Hamiltonian and the chirality sign.

## Question Family
`derivation`

## Pass Conditions
- The answer writes the Taylor expansion around the bad point.
- The answer explains why an invertible Jacobian leads to a standard Weyl cone after a linear change of coordinates.
- The answer identifies the determinant sign as the local chirality.

## Primary Retrieval Paths
- [Taylor Expand The Two-Band Hamiltonian Near The Crossing](../Derivation-Steps/taylor-expand-two-band-hamiltonian-near-crossing.md)
- [An Invertible Linear Term Gives A Weyl Hamiltonian](../Derivation-Steps/invertible-linear-term-gives-weyl-hamiltonian.md)
- [The Jacobian Sign Defines The Local Chirality](../Derivation-Steps/jacobian-sign-defines-local-chirality.md)

## Retrieval Hints
- `Use in regression runs to test whether the KB can actually reconstruct the local Weyl derivation.`

## Outgoing Edges
- `tests` -> [An Invertible Linear Term Gives A Weyl Hamiltonian](../Derivation-Steps/invertible-linear-term-gives-weyl-hamiltonian.md): The regression question tests whether the local Weyl derivation can be reconstructed step by step.

## Incoming Edges
- [Oracle For Reconstructing The Local Weyl Linearization](../Question-Oracles/reconstruct-local-weyl-linearization.md) -> `oracles`: This oracle records the derivation spine for the local Weyl linearization question.
