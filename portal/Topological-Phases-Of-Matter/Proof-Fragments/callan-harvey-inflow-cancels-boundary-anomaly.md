# Callan-Harvey Inflow Cancels The Boundary Anomaly

- ID: `proof_fragment:callan-harvey-inflow-cancels-boundary-anomaly`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
For a wall-localized chiral mode, the anomalous boundary current divergence is exactly canceled by the gauge variation of the bulk Chern-Simons response, so the combined bulk-plus-boundary system is gauge invariant.

## Scope
Archival Callan-Harvey fragment making the inflow-cancellation equation explicit inside the Lecture Three edge-mode family.

## Regime
Continuum anomaly-inflow analysis for integer quantum Hall boundaries and domain walls.

## Assumptions
- `A chiral wall or edge mode is present on the boundary.`
- `The bulk effective action contains the corresponding integer Chern-Simons response term.`

## Representation
Explicit bulk-plus-boundary anomaly-cancellation identity behind the edge-mode consistency story.

## Source Anchors
- `paper/anomaly-cancellation | eqs: bulk-topological-variation, inflow-balance | Archival anomaly-cancellation mechanism for wall-localized chiral zero modes.`
- `lecture-two/edge-states-and-anomaly-inflow | eqs: facs | Witten states the bulk Chern-Simons term whose boundary variation must be canceled.`

## Mathematical Content
- `kind=display` | Bulk Chern-Simons response term.
$$
I_{\mathrm{bulk}}=\frac{k}{4\pi}\int_{M} A\wedge \mathrm{d}A
$$
- `kind=display` | Gauge variation of the bulk response becomes a boundary term.
$$
\delta_{\Lambda} I_{\mathrm{bulk}}=\frac{k}{4\pi}\int_{\partial M}\Lambda\,\mathrm{d}A
$$
- `kind=display` | Boundary anomaly of the chiral mode is exactly canceled by bulk inflow.
$$
\partial_a j^a_{\mathrm{edge}}=-\frac{k}{4\pi}\,\epsilon^{ab}F_{ab},\qquad \delta_{\Lambda}W_{\mathrm{edge}}=-\delta_{\Lambda}I_{\mathrm{bulk}}
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `k` | integer Hall-response level |
| `j^a_{\mathrm{edge}}` | boundary chiral current |
| `W_{\mathrm{edge}}` | effective action of the boundary chiral mode |

## Dependencies
- [Parity Anomaly Half Level From Massive Dirac Fermion](parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](../Theorems/jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)

## Related Units
- [Boundary Anomaly Inflow Requires Chiral Edge Modes](../Theorems/anomaly-inflow-requires-chiral-edge-modes.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Domain-Wall Edge-Mode Cross-Source Fusion Record](../Source-Fusion-Records/domain-wall-edge-mode-cross-source-fusion.md)

## Step Justification
- Compute the gauge variation of the bulk Chern-Simons response and note that it localizes on the boundary.
- Identify the wall-localized chiral mode as the only place where a boundary gauge anomaly can live.
- Match the boundary anomaly coefficient to the bulk variation so the combined system is gauge invariant.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.DomainWallEdgeMode`
- Declaration: `callan_harvey_inflow_cancels_boundary_anomaly`
- Statement kind: `lemma`

### Admissible assumptions

- Work with an integer-level bulk Chern-Simons response on a manifold with boundary and a chiral edge theory living on that boundary.
- Treat the anomaly coefficient of the chiral boundary mode as a permitted lower-level input.

### Lean prerequisites

- [Parity Anomaly Half Level From Massive Dirac Fermion](parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Jackiw-Rebbi Zero Mode For A Sign-Changing Dirac Mass](../Theorems/jackiw-rebbi-zero-mode-for-sign-changing-dirac-mass.md)

### Formalization blockers

- The current KB does not yet provide a Lean-side interface for gauge variation of the Chern-Simons action on manifolds with boundary.
- The boundary chiral anomaly formula is still imported as physics background rather than as a formal theorem in the same library.

## Retrieval Hints
- `Use when an answer must show the exact Callan-Harvey cancellation equation rather than only saying 'anomaly inflow'.`

## Outgoing Edges
- none

## Incoming Edges
- none
