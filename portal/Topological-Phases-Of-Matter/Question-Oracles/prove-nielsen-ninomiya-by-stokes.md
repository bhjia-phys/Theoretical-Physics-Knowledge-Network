# Oracle For Proving Nielsen-Ninomiya By Stokes

- ID: `question_oracle:prove-nielsen-ninomiya-by-stokes`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for the flagship lattice no-go theorem proof question, including the cited Friedan reformulation of the same theorem.

## Scope
Detailed answer key for the degree-theoretic proof of charge cancellation.

## Regime
Topic regression oracle.

## Assumptions
- `The proof should follow the punctured-zone Stokes route explicitly.`

## Representation
Detailed oracle object.

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: wnn, weta, cl | The proof must expose the local degree formula, closedness, the punctured-zone boundary sum, and the cited Friedan reformulation.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Prove Nielsen-Ninomiya By Stokes](../Regression-Questions/prove-nielsen-ninomiya-by-stokes.md)

## Related Units
- [Pullback Of The Area Form Represents The Local Degree](../Proof-Fragments/pullback-area-form-represents-local-degree.md)
- [The Punctured Brillouin Zone Boundary Sum Vanishes](../Proof-Fragments/punctured-brillouin-zone-boundary-sum.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](../Proof-Fragments/friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)

## Prompt
Detailed oracle for regression_question:prove-nielsen-ninomiya-by-stokes.

## Failure Triggers
- Fail if the answer states only the theorem without the punctured-zone construction.
- Fail if the answer replaces the proof with anomaly language.

## Mandatory Units
- [Pullback Of The Area Form Represents The Local Degree](../Proof-Fragments/pullback-area-form-represents-local-degree.md)
- [The Punctured Brillouin Zone Boundary Sum Vanishes](../Proof-Fragments/punctured-brillouin-zone-boundary-sum.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](../Proof-Fragments/friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)

## Mandatory Equation Labels
- `wnn`
- `weta`
- `cl`

## Derivation Spine
- Define the local charge as the degree integral on a surrounding sphere.
- Excise small balls around all bad points and define the punctured Brillouin zone.
- Use the closed form on the punctured zone and apply Stokes's theorem.
- Identify the boundary sum with the sum of local charges and conclude it vanishes.
- State that Friedan's cited route re-expresses the same vanishing theorem as a boundary Chern number of the spectral bundle.

## Common Failure Patterns
- Jumping from the local charge definition directly to vanishing total charge without constructing the punctured Brillouin zone.
- Mentioning Friedan's cited result as background lore instead of identifying it as an equivalent theorem route.

## Grading Rubric
- Pass requires the local degree formula, the punctured-zone construction, the Stokes step, the boundary-charge sum, and the cited Friedan reformulation.
- Partial is appropriate if the compact-BZ Stokes proof is mostly present but the Friedan equivalence or one nontrivial intermediate step is missing.

## Outgoing Edges
- `oracles` -> [Prove Nielsen-Ninomiya By Stokes](../Regression-Questions/prove-nielsen-ninomiya-by-stokes.md): This oracle records the proof requirements for the Stokes derivation question.

## Incoming Edges
- none
