# Justify Large-Gauge Quantization Before Hall-Response Equivalence

- ID: `regression_question:justify-large-gauge-quantization-before-hall-response-equivalence`
- Type: `regression_question`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Tests whether the topic can reconstruct the closed-manifold large-gauge argument that forces the integer Hall-response level before invoking the rest of the Lecture Two theorem.

## Scope
Proof-focused regression prompt for the large-gauge quantization step.

## Regime
Topic regression for the Lecture Two prerequisite proof.

## Assumptions
- `The answer must expose the holonomy-shift argument, not only the final statement that k is integral.`

## Representation
Lecture Two prerequisite regression prompt.

## Source Anchors
- `lecture-two/quantization-of-the-chern-simons-coupling | eqs: unitf, nifty, prif | The answer should reconstruct the actual large-gauge proof.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)
- [Lecture Two Large-Gauge Holonomy Shift Context](../Equation-Contexts/lecture-two-large-gauge-holonomy-shift.md)

## Related Units
- [Oracle For Large-Gauge Quantization Before Hall-Response Equivalence](../Question-Oracles/justify-large-gauge-quantization-before-hall-response-equivalence.md)

## Prompt
Explain in detail why the Chern-Simons level k must be an integer by using Witten's S^2 times S^1 large-gauge argument before any Hall-current or TKNN step is invoked.

## Question Family
`derivation`

## Pass Conditions
- The answer states the unit-flux background on S^2 times S^1.
- The answer explains how the holonomy shifts by 2pi under a large gauge transformation.
- The answer concludes that gauge invariance of exp(i k I_CS) requires k to be integer.

## Primary Retrieval Paths
- [Lecture Two Large-Gauge Holonomy Shift Context](../Equation-Contexts/lecture-two-large-gauge-holonomy-shift.md)
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)

## Outgoing Edges
- none

## Incoming Edges
- none
