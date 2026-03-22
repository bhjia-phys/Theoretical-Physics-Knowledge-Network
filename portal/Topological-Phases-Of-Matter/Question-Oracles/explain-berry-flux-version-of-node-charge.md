# Oracle For The Berry-Flux Version Of The Node Charge

- ID: `question_oracle:explain-berry-flux-version-of-node-charge`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: ``
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for the Berry-curvature charge and zero-sum question.

## Scope
Detailed answer key for the Berry-curvature route to charge and charge cancellation.

## Regime
Topic regression oracle.

## Assumptions
- `The answer must include both the local charge formula and the global Stokes step.`

## Representation
Detailed oracle object.

## Source Anchors
- `lecture-one/the-berry-connection | eqs: zif, wif, nna | The answer must reconstruct the local Berry-flux charge formula and the punctured-zone dF=0 argument.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Explain The Berry-Flux Version Of The Node Charge](../Regression-Questions/explain-berry-flux-version-of-node-charge.md)

## Related Units
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Berry Curvature Closedness Repeats The Same Stokes Sum](../Proof-Fragments/berry-curvature-closedness-repeats-stokes-sum.md)

## Prompt
Detailed oracle for regression_question:explain-berry-flux-version-of-node-charge.

## Failure Triggers
- Fail if the answer never writes the flux integral.
- Fail if the answer states dF=0 without using it to derive the boundary sum.

## Mandatory Units
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Berry Curvature Closedness Repeats The Same Stokes Sum](../Proof-Fragments/berry-curvature-closedness-repeats-stokes-sum.md)

## Mandatory Equation Labels
- `zif`
- `wif`
- `nna`

## Derivation Spine
- Write the flux formula for the local node charge.
- State that the Berry curvature is closed away from singular points.
- Apply Stokes's theorem on the punctured Brillouin zone to derive the global sum rule.

## Common Failure Patterns
- Mentioning Berry curvature qualitatively without writing the sphere flux integral for the node charge.
- Giving the local flux formula but never using the punctured-zone Stokes argument to derive the zero-sum law.

## Grading Rubric
- Pass requires both the local Berry-flux charge formula and the global punctured-zone Stokes derivation of charge cancellation.
- Partial is appropriate if the answer gets either the local charge or the global zero-sum argument right but not both.

## Outgoing Edges
- `oracles` -> [Explain The Berry-Flux Version Of The Node Charge](../Regression-Questions/explain-berry-flux-version-of-node-charge.md): This oracle records the proof requirements for the Berry-flux question.

## Incoming Edges
- none
