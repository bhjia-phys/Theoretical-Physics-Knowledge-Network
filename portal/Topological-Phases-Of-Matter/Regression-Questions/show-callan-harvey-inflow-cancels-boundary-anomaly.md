# Show Callan-Harvey Inflow Cancels The Boundary Anomaly

- ID: `regression_question:show-callan-harvey-inflow-cancels-boundary-anomaly`
- Type: `regression_question`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Tests whether the topic can write the explicit bulk-plus-boundary anomaly-cancellation equation instead of mentioning anomaly inflow only as a slogan.

## Scope
Bridge-derivation question for the anomaly-inflow side of the Lecture Three family.

## Regime
Topic regression for the explicit Callan-Harvey inflow bridge.

## Assumptions
- `The answer must exhibit both the bulk gauge variation and the edge anomaly.`

## Representation
Callan-Harvey bridge regression prompt.

## Source Anchors
- `lecture-two/edge-states-and-anomaly-inflow | eqs: facs | The answer should start from the bulk Chern-Simons response.`
- `paper/anomaly-cancellation | eqs: bulk-topological-variation, inflow-balance | The answer should write the explicit cancellation between the edge anomaly and bulk inflow.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](../Theorems/anomaly-inflow-requires-chiral-edge-modes.md)

## Related Units
- [Oracle For Showing Callan-Harvey Inflow Cancels The Boundary Anomaly](../Question-Oracles/show-callan-harvey-inflow-cancels-boundary-anomaly.md)

## Prompt
Show explicitly how the Callan-Harvey bulk inflow cancels the boundary gauge anomaly of the chiral edge mode.

## Question Family
`derivation`

## Pass Conditions
- The answer writes the bulk Chern-Simons term and its boundary gauge variation.
- The answer writes the anomalous divergence or effective-action variation of the edge mode.
- The answer shows that delta W_edge = - delta I_bulk.
- The answer explains that the combined system is gauge invariant only after both bulk and edge contributions are included.

## Primary Retrieval Paths
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](../Theorems/anomaly-inflow-requires-chiral-edge-modes.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Retrieval Hints
- `Use in regression runs to ensure anomaly inflow is available as an explicit equation chain.`

## Outgoing Edges
- none

## Incoming Edges
- none
