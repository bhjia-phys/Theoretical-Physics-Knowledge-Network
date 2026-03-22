# Boundary Anomaly Inflow Requires Chiral Edge Modes

- ID: `theorem:anomaly-inflow-requires-chiral-edge-modes`
- Type: `theorem`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
On a manifold with boundary, the gauge variation of the bulk integer Chern-Simons response cannot be canceled by a purely local boundary counterterm, so anomalous gapless boundary modes are required to absorb the inflow.

## Scope
Source-grade anomaly-inflow theorem reused in the Lecture Three edge-mode family.

## Regime
Integer quantum Hall boundary theory and its continuum anomaly-cancellation story.

## Assumptions
- `The bulk effective action contains an integer-level Chern-Simons term.`
- `The system is defined on a manifold with physical boundary.`

## Representation
Reusable anomaly-inflow theorem linking the bulk Chern-Simons response to mandatory chiral boundary degrees of freedom.

## Source Anchors
- `lecture-two/edge-states-and-anomaly-inflow | eqs: facs | Witten's anomaly-inflow statement for the integer Hall boundary.`
- `paper/anomaly-cancellation | eqs: bulk-topological-variation, inflow-balance | Original source for anomaly inflow and wall-localized chiral zero modes.`

## Mathematical Content
- `kind=display` | `label=facs` | Bulk Chern-Simons action for the integer Hall phase.
$$
I_{\mathrm{bulk}}=\frac{k}{4\pi}\int_{M_2\times\mathbb R}A\wedge \mathrm dA
$$
- `kind=display` | Gauge variation becomes a boundary anomaly that must be canceled by edge degrees of freedom.
$$
\delta_{\Lambda}I_{\mathrm{bulk}}=\frac{k}{4\pi}\int_{\partial M_2\times\mathbb R}\Lambda\,\mathrm dA
$$
- `kind=display` | Callan-Harvey inflow equation equating the edge anomaly with the bulk variation.
$$
\partial_a j^a_{\mathrm{edge}}=-\frac{k}{4\pi}\,\epsilon^{ab}F_{ab},\qquad \delta_{\Lambda}W_{\mathrm{edge}}=-\delta_{\Lambda}I_{\mathrm{bulk}}
$$
- `kind=display` | Net boundary chirality must match the bulk Hall level.
$$
n_+-n_-=k
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `k` | integer Hall-response level multiplying the Chern-Simons action |
| `\Lambda` | gauge parameter whose variation exposes the boundary anomaly |
| `j^a_{\mathrm{edge}}` | boundary chiral current whose divergence carries the edge anomaly |
| `n_+-n_-` | net chirality of boundary gapless modes |

## Dependencies
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)

## Related Units
- [Domain-Wall Edge-Mode Consistency Family](../Theorem-Families/domain-wall-edge-mode-consistency.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](sign-changing-dirac-mass-supports-chiral-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Witten Topological Phases Lecture Two Source Map](../Source-Maps/witten-topological-phases-lecture-two.md)
- [Witten Topological Phases Lecture Three Source Map](../Source-Maps/witten-topological-phases-lecture-three.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)

## Topic Completion Status
`promotion-ready`

## Supporting Regression Questions
- [Show Callan-Harvey Inflow Cancels The Boundary Anomaly](../Regression-Questions/show-callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Derive Boundary Chirality After Doubling And Folding](../Regression-Questions/derive-boundary-chirality-after-doubling-and-folding.md)
- [Separate Local Edge-Mode Proof From Cited-Source Fusion Gap](../Regression-Questions/separate-local-edge-mode-proof-from-cited-source-fusion-gap.md)

## Supporting Oracles
- [Oracle For Showing Callan-Harvey Inflow Cancels The Boundary Anomaly](../Question-Oracles/show-callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Oracle For Deriving Boundary Chirality After Doubling And Folding](../Question-Oracles/derive-boundary-chirality-after-doubling-and-folding.md)
- [Oracle For Separating Local Edge-Mode Proof From Cited-Source Fusion Gap](../Question-Oracles/separate-local-edge-mode-proof-from-cited-source-fusion-gap.md)

## Supporting Regression Runs
- `regression_run:topological-phases-core-2026-03-20-proof-grade-closure`
- `regression_run:topological-phases-core-2026-03-21-leaf-formalization-audit`

## Split Required
`False`

## Recovery Source Refs
- `open_gap:jackiw-rebbi-domain-wall-proof-not-yet-curated`
- `followup_source_task:ingest-callan-harvey-and-jackiw-rebbi-for-edge-mode-proof`
- `conflict_record:continuum-parity-anomaly-is-not-lattice-no-go`

## Failure Modes
- `This continuum anomaly-inflow statement does not by itself prove the separate lattice Nielsen-Ninomiya theorem.`

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.DomainWallEdgeMode`
- Declaration: `anomaly_inflow_requires_chiral_edge_modes`
- Statement kind: `theorem`

### Admissible assumptions

- Work with an integer-level Hall response on a manifold with boundary in the continuum effective theory.
- Treat the local boundary anomaly formula as available input through the Callan-Harvey lemma.

### Lean prerequisites

- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)

### Formalization blockers

- The formal relation between the bulk Hall level and net boundary chirality still needs a reusable index-style wrapper in Lean.
- The current KB still keeps the continuum theorem separate from the lattice regularization story instead of connecting them with a common formal interface.

## Retrieval Hints
- `Use when the answer must explain why a nontrivial bulk Hall term forces chiral boundary modes.`

## Outgoing Edges
- none

## Incoming Edges
- none
