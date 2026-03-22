# Chern-Simons Level Produces Quantized Hall Current

- ID: `proof_obligation:chern-simons-level-produces-quantized-hall-current`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the proof obligation that the same integer k appearing in the Chern-Simons action becomes the observable Hall conductivity when the effective action is differentiated with respect to the background gauge field.

## Scope
Second proof obligation in the Lecture Two theorem chain.

## Regime
Macroscopic response theory.

## Assumptions
- `The current is read from the variation of the effective action.`
- `The background electric field is applied along x_1.`

## Representation
Bounded proof obligation for the response-theory route from k to J_2 = k E_1 / 2pi.

## Source Anchors
- `lecture-two/quantization-of-the-hall-conductivity | eqs: curr, zurr, murr | The functional-derivative step turns the quantized level into the Hall current.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Large-Gauge Holonomy Shift Quantizes The Chern-Simons Level](large-gauge-holonomy-shift-quantizes-chern-simons-level.md)
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [Lecture Two Hall Current From Chern-Simons Context](../Equation-Contexts/lecture-two-hall-current-from-chern-simons.md)

## Related Units
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Lecture Two Hall-Response / Chern-Number Dependency Graph](../Dependency-Graph-Snapshots/lecture-two-hall-response-chern-number-proof.md)

## Pass Conditions
- The answer starts from the effective Chern-Simons action with level k.
- The answer differentiates with respect to the background gauge field to define the induced current.
- The answer derives the transverse Hall current J_2 = k E_1 / 2pi.

## Mandatory Logical Moves
- Write the integer-level effective action.
- Apply the functional derivative definition of current.
- Use the antisymmetric structure of the Chern-Simons term to identify the Hall response.

## Common Failure Patterns
- Quoting the Hall current without showing its origin in the effective action.
- Treating k as a microscopic band invariant before the response-theory step is complete.
- Confusing the electric-field direction with the current direction.

## Grading Rubric
- Full credit requires the variation step and the transverse-current interpretation.
- Partial credit is appropriate if the final current formula is stated but the derivation route is skipped.

## Retrieval Hints
- `Use when the response-theory part of the theorem needs to be reconstructed explicitly.`

## Outgoing Edges
- none

## Incoming Edges
- none
