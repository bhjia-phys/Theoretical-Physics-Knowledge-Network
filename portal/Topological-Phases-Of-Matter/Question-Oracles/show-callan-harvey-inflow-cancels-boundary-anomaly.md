# Oracle For Showing Callan-Harvey Inflow Cancels The Boundary Anomaly

- ID: `question_oracle:show-callan-harvey-inflow-cancels-boundary-anomaly`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for the Callan-Harvey bridge question that asks for the explicit bulk-plus-boundary cancellation equation.

## Scope
Detailed answer key for the explicit Callan-Harvey cancellation equation.

## Regime
Topic regression oracle.

## Assumptions
- `The answer must show the matching of coefficients between the bulk variation and the edge anomaly.`

## Representation
Detailed oracle object.

## Source Anchors
- `lecture-two/edge-states-and-anomaly-inflow | eqs: facs | The answer must state the bulk Chern-Simons response.`
- `paper/anomaly-cancellation | eqs: bulk-topological-variation, inflow-balance | The answer must write the explicit cancellation between the boundary anomaly and the bulk variation.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Show Callan-Harvey Inflow Cancels The Boundary Anomaly](../Regression-Questions/show-callan-harvey-inflow-cancels-boundary-anomaly.md)

## Related Units
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Domain-Wall Edge-Mode Cross-Source Fusion Record](../Source-Fusion-Records/domain-wall-edge-mode-cross-source-fusion.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](../Theorems/anomaly-inflow-requires-chiral-edge-modes.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Prompt
Detailed oracle for regression_question:show-callan-harvey-inflow-cancels-boundary-anomaly.

## Failure Triggers
- Fail if the answer never writes the cancellation equation.
- Fail if the answer claims the bulk Chern-Simons term is gauge invariant by itself on a manifold with boundary.

## Mandatory Units
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](../Theorems/anomaly-inflow-requires-chiral-edge-modes.md)
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)

## Mandatory Equation Labels
- `facs`
- `bulk-topological-variation`
- `inflow-balance`

## Derivation Spine
- Write the bulk response I_bulk = (k / 4pi) integral A wedge dA.
- Compute its gauge variation delta_Lambda I_bulk = (k / 4pi) integral_boundary Lambda dA.
- Write the boundary anomaly of the chiral edge mode through either its anomalous divergence or the variation delta_Lambda W_edge.
- Match the coefficients to show delta_Lambda W_edge = - delta_Lambda I_bulk.
- Conclude that gauge invariance is restored only for the combined bulk-plus-boundary system.

## Mandatory Logical Moves
- Keep the bulk variation and the edge anomaly as separate contributions until the final cancellation step.
- State explicitly that a local boundary counterterm built only from background fields does not replace the chiral edge mode.
- Use the same Hall level k on both sides of the cancellation equation.

## Common Failure Patterns
- Saying only that anomaly inflow happens without writing the cancellation equation.
- Writing the bulk variation but not the edge anomaly, or vice versa.
- Treating the edge mode as optional after the bulk Chern-Simons term is present.

## Grading Rubric
- Pass requires the explicit bulk variation, the explicit edge anomaly, and the final cancellation equation.
- Partial is appropriate if the answer has the right idea but leaves one side of the balance schematic.

## Outgoing Edges
- none

## Incoming Edges
- none
