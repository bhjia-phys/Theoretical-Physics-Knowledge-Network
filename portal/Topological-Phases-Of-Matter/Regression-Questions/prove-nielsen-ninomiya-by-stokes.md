# Prove Nielsen-Ninomiya By Stokes

- ID: `regression_question:prove-nielsen-ninomiya-by-stokes`
- Type: `regression_question`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Tests whether the topic can reconstruct the degree-theoretic Stokes proof of charge cancellation on the punctured Brillouin zone and also identify the equivalent cited Friedan route that packages the same theorem as a spectral-bundle Chern-number statement.

## Scope
Flagship theorem-proof question for the lattice no-go branch.

## Regime
Topic regression for the Witten Lecture One exemplar.

## Assumptions
- `The answer should use the punctured Brillouin-zone argument and not replace it with anomaly intuition.`

## Representation
Derivation-family regression prompt for the theorem proof.

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: wnn, weta, cl | The answer should follow the actual Stokes spine of the lecture theorem.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Pullback Of The Area Form Represents The Local Degree](../Proof-Fragments/pullback-area-form-represents-local-degree.md)
- [The Punctured Brillouin Zone Boundary Sum Vanishes](../Proof-Fragments/punctured-brillouin-zone-boundary-sum.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](../Proof-Fragments/friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)

## Related Units
- [Oracle For Proving Nielsen-Ninomiya By Stokes](../Question-Oracles/prove-nielsen-ninomiya-by-stokes.md)

## Prompt
Prove the Lecture One Nielsen-Ninomiya theorem by the punctured-Brillouin-zone Stokes argument, making every nontrivial step explicit, and identify the equivalent Friedan spectral-bundle route that gives the same vanishing theorem.

## Question Family
`derivation`

## Pass Conditions
- The answer identifies the local charge as the degree integral on a small surrounding sphere.
- The answer defines the punctured Brillouin zone and its boundary spheres.
- The answer applies Stokes's theorem to a closed form and derives the zero total charge.
- The answer can name the Friedan spectral-projection or cobordism reformulation as the cited rigorous route for the same theorem.

## Primary Retrieval Paths
- [Pullback Of The Area Form Represents The Local Degree](../Proof-Fragments/pullback-area-form-represents-local-degree.md)
- [The Punctured Brillouin Zone Boundary Sum Vanishes](../Proof-Fragments/punctured-brillouin-zone-boundary-sum.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)

## Retrieval Hints
- `Use in regression runs to test whether the KB can reconstruct the actual theorem proof rather than only the statement.`

## Outgoing Edges
- `tests` -> [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md): The regression question tests whether the theorem proof can be reconstructed explicitly.

## Incoming Edges
- [Oracle For Proving Nielsen-Ninomiya By Stokes](../Question-Oracles/prove-nielsen-ninomiya-by-stokes.md) -> `oracles`: This oracle records the proof requirements for the Stokes derivation question.
