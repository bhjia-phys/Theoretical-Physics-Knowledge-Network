# Separate Anomaly Intuition From The Lattice Proof

- ID: `regression_question:separate-anomaly-intuition-from-lattice-proof`
- Type: `regression_question`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Tests whether the topic can say exactly why continuum anomaly language is helpful intuition but not the actual Lecture One proof of Nielsen-Ninomiya, using explicit local units instead of hand-waving toward a future source recovery.

## Scope
Gap-identification question at the boundary between Lecture One and the later anomaly discussion.

## Regime
Topic regression for the Witten Lecture One exemplar.

## Assumptions
- `The answer must use the now-explicit local cited-source units rather than leaving the distinction as a future gap.`

## Representation
Gap-family regression prompt.

## Source Anchors
- `lecture-two/edge-states-and-anomaly-inflow | Anomaly inflow belongs to the boundary-consistency story rather than the actual lattice theorem proof.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Continuum Anomaly To Lattice No-Go](../Bridges/continuum-anomaly-to-lattice-no-go.md)
- [Continuum Parity Anomaly Does Not Establish Lattice Charge Cancellation](../Proof-Fragments/continuum-parity-anomaly-does-not-establish-lattice-charge-cancellation.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](../Proof-Fragments/friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)

## Related Units
- [Oracle For Separating Anomaly Intuition From The Lattice Proof](../Question-Oracles/separate-anomaly-intuition-from-lattice-proof.md)

## Prompt
Explain why parity-anomaly or anomaly-inflow intuition does not replace the actual lattice proof of Nielsen-Ninomiya, and cite the local units that make this distinction explicit.

## Question Family
`gap`

## Pass Conditions
- The answer explicitly distinguishes the Lecture One lattice proof from later continuum anomaly arguments.
- The answer identifies Friedan's compact-BZ Chern-number route as the theorem proof and Haldane or Callan-Harvey as neighboring anomaly motivation sources.
- The answer does not falsely present the anomaly argument as the theorem proof.

## Primary Retrieval Paths
- [Continuum Anomaly To Lattice No-Go](../Bridges/continuum-anomaly-to-lattice-no-go.md)
- [Continuum Parity Anomaly Does Not Establish Lattice Charge Cancellation](../Proof-Fragments/continuum-parity-anomaly-does-not-establish-lattice-charge-cancellation.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](../Proof-Fragments/friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)
- [Continuum Parity Anomaly Is Not Lattice No-Go](../Conflict-Records/continuum-parity-anomaly-is-not-lattice-no-go.md)

## Retrieval Hints
- `Use in regression runs to expose hidden conflations between proof and motivation.`

## Outgoing Edges
- `tests` -> [Former Parity-Anomaly Versus Lattice-No-Go Scope Gap (Closed)](../Open-Gaps/parity-anomaly-motivates-but-does-not-prove-lattice-no-go.md): The regression question tests whether the proof/intution gap is surfaced honestly.
- `blocked_by` -> [Former Parity-Anomaly Versus Lattice-No-Go Scope Gap (Closed)](../Open-Gaps/parity-anomaly-motivates-but-does-not-prove-lattice-no-go.md): This regression question remains only partially satisfied until the anomaly/proof distinction is backed by ingested sources.

## Incoming Edges
- [Oracle For Separating Anomaly Intuition From The Lattice Proof](../Question-Oracles/separate-anomaly-intuition-from-lattice-proof.md) -> `oracles`: This oracle records the failure conditions for the anomaly/proof distinction question.
