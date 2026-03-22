# Hall Response, Band, And Many-Body Chern Numbers Coincide

- ID: `proof_obligation:hall-response-band-and-many-body-chern-numbers-coincide`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the synthesis obligation that the macroscopic Hall-response coefficient k, the band invariant k', and the many-body twist-angle invariant \widehat{k}' all encode the same quantized integer in the gapped integer Hall system.

## Scope
Final synthesis obligation for the equality k = k' = \widehat{k}'.

## Regime
Flagship Lecture Two theorem synthesis.

## Assumptions
- `The response-theory, band-theory, and many-body constructions are all applied in the same gapped phase.`
- `The ground state stays nondegenerate under adiabatic twists.`

## Representation
Final synthesis obligation that makes the Lecture Two family reusable as one theorem.

## Source Anchors
- `lecture-two/relation-to-band-topology | Band-theory side of the equality.`
- `lecture-two/proof-of-the-equivalence | eqs: plizz | Many-body side of the equality and its identification with k.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](large-gauge-holonomy-shift-quantizes-chern-simons-level.md)
- [Chern-Simons Level Produces Quantized Hall Current](chern-simons-level-produces-quantized-hall-current.md)
- [Filled-Band Berry Curvature Defines The TKNN Invariant](filled-band-berry-curvature-defines-tknn-invariant.md)
- [Twist-Angle Berry Curvature Equals The Hall Level](twist-angle-berry-curvature-equals-hall-level.md)
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md)
- [Lecture Two Twist-Angle Berry Curvature Context](../Equation-Contexts/lecture-two-twist-angle-berry-curvature.md)

## Related Units
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Hall-Response / Chern-Number Equivalence Family](../Theorem-Families/hall-response-chern-number-equivalence.md)

## Pass Conditions
- The answer states what k, k', and \widehat{k}' each mean.
- The answer explains why k is the response coefficient, k' the band invariant, and \widehat{k}' the many-body invariant.
- The answer concludes with the equality k = k' = \widehat{k}' without erasing which route produced each quantity.

## Mandatory Logical Moves
- Carry the response-theory route to the integer k.
- Carry the microscopic band-topology route to k'.
- Carry the twist-angle Berry-curvature route to \widehat{k}'.
- Fuse the three routes into one canonical equality.

## Common Failure Patterns
- Giving only one side of the equality.
- Using the final formula without distinguishing the three meanings of the symbols.
- Skipping the bridge from the many-body invariant back to the Hall-response level.

## Grading Rubric
- Full credit requires all three routes and the final synthesis.
- Partial credit is appropriate if the answer reconstructs only two of the three routes.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.HallResponseChernNumber`
- Declaration: `hall_response_band_and_many_body_chern_numbers_coincide`
- Statement kind: `theorem`

### Admissible assumptions

- The response coefficient, band invariant, and twist-angle invariant are all computed in the same gapped phase.
- The ground state stays nondegenerate during the twist-angle deformation.

### Lean prerequisites

- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](large-gauge-holonomy-shift-quantizes-chern-simons-level.md)
- [Chern-Simons Level Produces Quantized Hall Current](chern-simons-level-produces-quantized-hall-current.md)
- [Filled-Band Berry Curvature Defines The TKNN Invariant](filled-band-berry-curvature-defines-tknn-invariant.md)
- [Twist-Angle Berry Curvature Equals The Hall Level](twist-angle-berry-curvature-equals-hall-level.md)
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md)

### Formalization blockers

- The twist-angle Berry-curvature formalization still needs a clean geometric interface between many-body parameter space and the Hall-response coefficient.

## Retrieval Hints
- `Use when the answer must recover the full theorem rather than one local lemma.`

## Outgoing Edges
- none

## Incoming Edges
- none
