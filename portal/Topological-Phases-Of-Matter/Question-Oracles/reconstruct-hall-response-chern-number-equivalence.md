# Oracle For Reconstructing The Hall-Response / Chern-Number Equivalence

- ID: `question_oracle:reconstruct-hall-response-chern-number-equivalence`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for the Lecture Two flagship derivation question.

## Scope
Detailed answer key for the Lecture Two Hall-response equivalence theorem.

## Regime
Topic regression oracle.

## Assumptions
- `The answer must expose both the response-theory spine and the Berry-curvature spine.`

## Representation
Detailed oracle object.

## Source Anchors
- `lecture-two/proof-of-the-equivalence | eqs: mizz, coff, plizz | The answer must explicitly traverse the twist-angle Berry-curvature proof.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Reconstruct The Hall-Response / Chern-Number Equivalence](../Regression-Questions/reconstruct-hall-response-chern-number-equivalence.md)

## Related Units
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Hall-Response / Chern-Number Equivalence Family](../Theorem-Families/hall-response-chern-number-equivalence.md)
- [Hall-Response / Chern-Number Cross-Source Fusion Record](../Source-Fusion-Records/hall-response-chern-number-cross-source-fusion.md)
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Berry-Curvature Trace Equals Projector Commutator](../Proof-Fragments/berry-curvature-trace-equals-projector-commutator.md)
- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)
- [Twisted-Boundary Berry Curvature Reproduces The Hall Level](../Proof-Fragments/twisted-boundary-berry-curvature-reproduces-hall-level.md)

## Prompt
Detailed oracle for regression_question:reconstruct-hall-response-chern-number-equivalence.

## Failure Triggers
- Fail if the answer only quotes the TKNN formula without the response-theory route.
- Fail if the answer omits the many-body twist-angle invariant.
- Fail if the answer never states why the Hall-response coefficient is an integer.

## Mandatory Units
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Berry-Curvature Trace Equals Projector Commutator](../Proof-Fragments/berry-curvature-trace-equals-projector-commutator.md)
- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)
- [Twisted-Boundary Berry Curvature Reproduces The Hall Level](../Proof-Fragments/twisted-boundary-berry-curvature-reproduces-hall-level.md)
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)

## Mandatory Equation Labels
- `murr`
- `coff`
- `plizz`

## Supporting Obligations
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](../Proof-Obligations/large-gauge-holonomy-shift-quantizes-chern-simons-level.md)
- [Chern-Simons Level Produces Quantized Hall Current](../Proof-Obligations/chern-simons-level-produces-quantized-hall-current.md)
- [Filled-Band Berry Curvature Defines The TKNN Invariant](../Proof-Obligations/filled-band-berry-curvature-defines-tknn-invariant.md)
- [Twist-Angle Berry Curvature Equals The Hall Level](../Proof-Obligations/twist-angle-berry-curvature-equals-hall-level.md)
- [Hall Response, Band, And Many-Body Chern Numbers Coincide](../Proof-Obligations/hall-response-band-and-many-body-chern-numbers-coincide.md)

## Equation Contexts
- [Lecture Two Large-Gauge Holonomy Shift Context](../Equation-Contexts/lecture-two-large-gauge-holonomy-shift.md)
- [Lecture Two Hall Current From Chern-Simons Context](../Equation-Contexts/lecture-two-hall-current-from-chern-simons.md)
- [Lecture Two Twist-Angle Berry Curvature Context](../Equation-Contexts/lecture-two-twist-angle-berry-curvature.md)

## Dependency Graph Snapshot
- [Lecture Two Hall-Response / Chern-Number Dependency Graph](../Dependency-Graph-Snapshots/lecture-two-hall-response-chern-number-proof.md)

## Derivation Spine
- Use large gauge invariance on S^2 times S^1 to show the Chern-Simons level k is integral.
- Differentiate the Chern-Simons effective action to obtain the Hall current J_2 = k E_1 / 2pi.
- Define the filled-band Chern number k' from the occupied-state Berry curvature over the Brillouin torus and bridge Tr F to i Tr(P dP wedge dP).
- Write the equivalent occupied-projector formula for the same microscopic integer.
- Compute the twist-angle Berry curvature and integrate it to obtain the many-body invariant \widehat{k}' = k.
- Conclude that k = k' = \widehat{k}'.

## Mandatory Logical Moves
- Justify integrality of k before using it as a response coefficient.
- Keep the response, band, and many-body routes distinct until the final synthesis step.
- Do not quote the projector formula as a black box; connect it to the Berry-curvature trace.
- Use the twist-angle torus as a many-body geometric space, not as the Brillouin torus.

## Common Failure Patterns
- Quoting the final equality without distinguishing what k, k', and \widehat{k}' each mean.
- Skipping the large-gauge quantization step.
- Writing the projector formula with no explanation of why it equals the traced occupied-bundle curvature.
- Naming the TKNN invariant without any explicit occupied-bundle or projector formula.
- Collapsing the twist-angle Berry curvature into the band Berry curvature without explanation.

## Grading Rubric
- Pass requires the three-route derivation, the occupied-projector or Berry-curvature formula for k', and the final synthesis.
- Partial is appropriate if one of the major routes is missing.

## Outgoing Edges
- `oracles` -> [Reconstruct The Hall-Response / Chern-Number Equivalence](../Regression-Questions/reconstruct-hall-response-chern-number-equivalence.md): This oracle records the derivation requirements for the Hall-response / Chern-number question.

## Incoming Edges
- none
