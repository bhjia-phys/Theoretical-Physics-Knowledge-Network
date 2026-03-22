# Oracle For Large-Gauge Quantization Before Hall-Response Equivalence

- ID: `question_oracle:justify-large-gauge-quantization-before-hall-response-equivalence`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for the large-gauge quantization prerequisite in the Lecture Two theorem family.

## Scope
Detailed answer key for the large-gauge prerequisite proof.

## Regime
Topic regression oracle.

## Assumptions
- `The answer must not rely on later Hall-current or TKNN statements to justify integrality.`

## Representation
Detailed oracle object.

## Source Anchors
- `lecture-two/quantization-of-the-chern-simons-coupling | eqs: unitf, nifty, prif | The answer must reconstruct the S^2 times S^1 argument itself.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Justify Large-Gauge Quantization Before Hall-Response Equivalence](../Regression-Questions/justify-large-gauge-quantization-before-hall-response-equivalence.md)

## Related Units
- [Lecture Two Large-Gauge Holonomy Shift Context](../Equation-Contexts/lecture-two-large-gauge-holonomy-shift.md)
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)

## Prompt
Detailed oracle for regression_question:justify-large-gauge-quantization-before-hall-response-equivalence.

## Failure Triggers
- Fail if the answer only quotes the integer result without the S^2 times S^1 construction.
- Fail if the answer invokes the Hall current or Berry curvature before the level is quantized.

## Mandatory Units
- [Lecture Two Large-Gauge Holonomy Shift Context](../Equation-Contexts/lecture-two-large-gauge-holonomy-shift.md)
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)

## Mandatory Equation Labels
- `unitf`
- `nifty`
- `prif`

## Supporting Obligations
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)

## Derivation Spine
- Insert one unit of flux through the spatial two-sphere.
- Evaluate the Chern-Simons functional on S^2 times S^1 and identify it with the holonomy angle.
- Apply the large gauge transformation that shifts the holonomy by 2pi.
- Demand invariance of exp(i k I_CS) and conclude that k must be integral.

## Mandatory Logical Moves
- The unit-flux background must be named explicitly.
- The 2pi holonomy shift must appear explicitly.
- The conclusion k in Z must be derived from path-integral invariance.

## Common Failure Patterns
- Claiming Chern-Simons levels are quantized without the specific background argument.
- Using later parts of the Hall theorem to justify the prerequisite.

## Grading Rubric
- Pass requires the actual large-gauge proof.
- Unsafe-pass is not allowed here because the question is only about the local prerequisite proof.
- Partial is appropriate if the conclusion is known but the holonomy-shift step is missing.

## Outgoing Edges
- none

## Incoming Edges
- none
