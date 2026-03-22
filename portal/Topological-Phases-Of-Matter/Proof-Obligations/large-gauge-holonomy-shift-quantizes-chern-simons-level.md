# Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level

- ID: `proof_obligation:large-gauge-holonomy-shift-quantizes-chern-simons-level`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the proof obligation that the Hall-response coefficient k is integer by evaluating the Chern-Simons functional on S^2 times S^1 with unit flux and demanding invariance under the large-gauge holonomy shift.

## Scope
First proof obligation in the Lecture Two flagship theorem family.

## Regime
Closed-manifold quantization argument.

## Assumptions
- `The effective action appears in the path integral exponent.`
- `The gauge field is compact, so large gauge transformations are physically allowed.`

## Representation
Bounded proof obligation for the integrality of the Chern-Simons level.

## Source Anchors
- `lecture-two/quantization-of-the-chern-simons-coupling | eqs: unitf, nifty, prif | The closed-manifold large-gauge step that forces integrality of k.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Lecture Two Large-Gauge Holonomy Shift Context](../Equation-Contexts/lecture-two-large-gauge-holonomy-shift.md)

## Related Units
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Lecture Two Hall-Response / Chern-Number Dependency Graph](../Dependency-Graph-Snapshots/lecture-two-hall-response-chern-number-proof.md)

## Pass Conditions
- The answer introduces the unit-flux background on S^2 times S^1.
- The answer states that the Chern-Simons functional shifts by 2pi under the allowed large gauge transformation.
- The answer concludes that exp(i k I_CS) is gauge invariant only when k is integral.

## Mandatory Logical Moves
- Evaluate the Chern-Simons functional on the unit-flux background.
- Apply the large gauge transformation that shifts the temporal holonomy by 2pi.
- Translate invariance of the path integral into integrality of k.

## Common Failure Patterns
- Asserting k is integer without mentioning the S^2 times S^1 background.
- Quoting gauge invariance abstractly without the 2pi action shift.
- Using Hall-current quantization before the level has been quantized.

## Grading Rubric
- Full credit requires the actual large-gauge argument, not only the slogan that Chern-Simons levels are quantized.
- Partial credit is appropriate if the answer knows the conclusion but omits the holonomy-shift mechanism.

## Retrieval Hints
- `Use when the proof must justify the integer nature of k before any Hall-current or Berry-curvature step.`

## Outgoing Edges
- none

## Incoming Edges
- none
