# Oracle For Separating Anomaly Intuition From The Lattice Proof

- ID: `question_oracle:separate-anomaly-intuition-from-lattice-proof`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for distinguishing continuum anomaly intuition from the actual lattice proof route now that the cited-source distinction is explicit locally.

## Scope
Detailed answer key for a gap-identification question at the proof/intution boundary.

## Regime
Topic regression oracle.

## Assumptions
- `The answer should now remain fully local and no longer route this distinction to an unresolved follow-up.`

## Representation
Detailed oracle object.

## Source Anchors
- `lecture-two/edge-states-and-anomaly-inflow | The answer should place anomaly inflow on the boundary-consistency side rather than on the Lecture One lattice-proof side.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Separate Anomaly Intuition From The Lattice Proof](../Regression-Questions/separate-anomaly-intuition-from-lattice-proof.md)

## Related Units
- [Continuum Parity Anomaly Does Not Establish Lattice Charge Cancellation](../Proof-Fragments/continuum-parity-anomaly-does-not-establish-lattice-charge-cancellation.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](../Proof-Fragments/friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)
- [Continuum Parity Anomaly Is Not Lattice No-Go](../Conflict-Records/continuum-parity-anomaly-is-not-lattice-no-go.md)

## Prompt
Detailed oracle for regression_question:separate-anomaly-intuition-from-lattice-proof.

## Pass Conditions
- The answer clearly says that anomaly intuition is not the Lecture One proof.
- The answer contrasts the continuum anomaly formulas with the compact-BZ Chern-number proof route.

## Failure Triggers
- Fail if the answer identifies the parity-anomaly argument as the proof of Nielsen-Ninomiya.
- Fail if the answer hides the logical difference between Haldane or Callan-Harvey motivation and Friedan's theorem proof.

## Mandatory Units
- [Continuum Parity Anomaly Does Not Establish Lattice Charge Cancellation](../Proof-Fragments/continuum-parity-anomaly-does-not-establish-lattice-charge-cancellation.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](../Proof-Fragments/friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)

## Common Failure Patterns
- Treating the parity anomaly or Callan-Harvey inflow as if they were the proof of the compact-Brillouin-zone lattice theorem.
- Overcorrecting by denying any conceptual relation between continuum anomaly arguments and the neighboring topological-phase consistency story.

## Grading Rubric
- Pass requires an explicit scope boundary together with the correct compact-BZ proof route for Nielsen-Ninomiya.
- Partial is appropriate if the answer states the boundary but does not explain what the continuum anomaly branch still contributes conceptually.

## Outgoing Edges
- `oracles` -> [Separate Anomaly Intuition From The Lattice Proof](../Regression-Questions/separate-anomaly-intuition-from-lattice-proof.md): This oracle records the failure conditions for the anomaly/proof distinction question.

## Incoming Edges
- none
