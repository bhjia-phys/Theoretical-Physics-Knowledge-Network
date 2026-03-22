# Integer Quantum Hall Response Equals Band And Many-Body Chern Number

- ID: `theorem:integer-quantum-hall-response-equals-band-and-many-body-chern-number`
- Type: `theorem`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
In a gapped integer quantum Hall system, the integer Hall-response level k equals both the source-grade TKNN band Chern number k' and the many-body twist-angle Chern number \widehat{k}'.

## Scope
Canonical theorem family joining Witten Lecture Two, the TKNN band invariant, and the many-body twist-angle formulation.

## Regime
Integer quantum Hall systems with a stable gap.

## Assumptions
- `The two-dimensional system is gapped.`
- `The low-energy response is captured by an integer-level Chern-Simons term.`
- `The many-body ground state remains nondegenerate under adiabatic twists.`

## Representation
Canonical theorem family joining response theory, projector-level band topology, and many-body adiabatic transport.

## Source Anchors
- `lecture-two/quantization-of-the-hall-conductivity | eqs: murr | Macroscopic Hall response coefficient.`
- `lecture-two/relation-to-band-topology | Microscopic filled-band Chern invariant.`
- `lecture-two/proof-of-the-equivalence | eqs: plizz | Many-body twist-angle Chern invariant.`
- `paper/projector-curvature-identity | eqs: occupied-bundle-curvature-form | Original microscopic Hall-conductance invariant, now fused locally through the traced-curvature identity and the occupied-projector formula.`
- `paper/chern-insulator-phase | eqs: chern-number-from-valley-masses | Neighboring lattice realization and parity-anomaly interpretation of the same Hall-response family through the valley-mass Chern-number criterion.`

## Mathematical Content
- `kind=display` | `label=murr` | Macroscopic quantized Hall response.
$$
J_2 = \frac{kE_1}{2\pi}
$$
- `kind=display` | Microscopic filled-band Chern number.
$$
k' = \int_{\mathcal B}\frac{\operatorname{Tr}\,\mathcal F}{2\pi}
$$
- `kind=display` | Equivalent projector formula for the TKNN invariant.
$$
k'=\frac{i}{2\pi}\int_{\mathcal B}\operatorname{Tr}\!\left(P[\partial_{p_1}P,\partial_{p_2}P]\right)\,\mathrm d^2p
$$
- `kind=display` | `label=plizz` | Many-body twist-angle Chern number equals the Hall-response level.
$$
\widehat{k}' = \int_0^{2\pi} d\alpha_1 d\alpha_2\,\frac{\widehat{\mathcal F}}{2\pi} = k
$$
- `kind=display` | Canonical equality of the three integer invariants.
$$
k = k' = \widehat{k}'
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `k` | integer Hall-response level |
| `k'` | single-particle filled-band Chern number |
| `\widehat{k}'` | many-body twist-angle Chern number |

## Dependencies
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Berry-Curvature Trace Equals Projector Commutator](../Proof-Fragments/berry-curvature-trace-equals-projector-commutator.md)
- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md)
- [Twisted-Boundary Berry Curvature Reproduces The Hall Level](../Proof-Fragments/twisted-boundary-berry-curvature-reproduces-hall-level.md)

## Related Units
- [Hall-Response / Chern-Number Equivalence Family](../Theorem-Families/hall-response-chern-number-equivalence.md)
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Hall-Response / Chern-Number Cross-Source Fusion Record](../Source-Fusion-Records/hall-response-chern-number-cross-source-fusion.md)
- [Witten Topological Phases Lecture Two Source Map](../Source-Maps/witten-topological-phases-lecture-two.md)
- [Topological Phases Core Source Network](../Source-Maps/topological-phases-core.md)
- [Haldane Dirac-Mass Signs Determine The Chern Number](../Proof-Fragments/haldane-dirac-mass-signs-determine-chern-number.md)

## Proof Obligations
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

## Topic Completion Status
`promotion-ready`

## Supporting Regression Questions
- [Justify Large-Gauge Quantization Before Hall-Response Equivalence](../Regression-Questions/justify-large-gauge-quantization-before-hall-response-equivalence.md)
- [Reconstruct The Hall-Response / Chern-Number Equivalence](../Regression-Questions/reconstruct-hall-response-chern-number-equivalence.md)
- [Separate Local Lecture Two Proof From Cited-Source Fusion Gap](../Regression-Questions/separate-local-lecture-two-proof-from-cited-source-fusion-gap.md)

## Supporting Oracles
- [Oracle For Large-Gauge Quantization Before Hall-Response Equivalence](../Question-Oracles/justify-large-gauge-quantization-before-hall-response-equivalence.md)
- [Oracle For Reconstructing The Hall-Response / Chern-Number Equivalence](../Question-Oracles/reconstruct-hall-response-chern-number-equivalence.md)
- [Oracle For Separating Local Lecture Two Proof From Cited-Source Fusion Gap](../Question-Oracles/separate-local-lecture-two-proof-from-cited-source-fusion-gap.md)

## Supporting Regression Runs
- `regression_run:topological-phases-core-2026-03-20-proof-grade-closure`
- `regression_run:topological-phases-core-2026-03-21-leaf-formalization-audit`

## Split Required
`False`

## Recovery Source Refs
- `open_gap:lecture-two-tknn-equivalence-proof-not-yet-curated`
- `followup_source_task:ingest-tknn-and-haldane-for-lecture-two-equivalence`

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.HallResponseChernNumber`
- Declaration: `integer_quantum_hall_response_eq_band_and_many_body_chern_number`
- Statement kind: `theorem`

### Admissible assumptions

- Work in a gapped two-dimensional U(1)-conserving Hall phase with a nondegenerate ground state under adiabatic twists.
- Treat the response, band, and many-body constructions as three presentations of the same phase rather than as independent systems.

### Lean prerequisites

- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Projector Formula For The TKNN Chern Number](../Proof-Fragments/projector-formula-for-the-tknn-chern-number.md)
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md)

### Formalization blockers

- The common Lean-side wrapper relating response theory, Bloch bundles, and many-body twist bundles is still missing.
- The Haldane-model realization and the thermodynamic-limit bridge are still maintained as neighboring explanatory units rather than as local formal sublemmas.

## Formal-Theory Guardrails

- Formal theory role: `trusted_target`
- Statement graph role: `target_statement`
- Prerequisite closure status: `closed`

### Statement graph parents

- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md)

### Statement graph children

- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)

## Faithfulness Review

- Status: `reviewed`
- Strategy: Keep the target theorem equal to the shared integer relation k = k' = khat', and treat the Haldane branch only as a neighboring realization rather than as an extra conjunct inside the theorem.
- Notes: The KB expands the proof spine into obligations and fragments but does not alter the source theorem statement.

## Comparator Audit

- Status: `passed`

### Comparator risks

- Do not weaken the theorem into only a band statement or only a many-body statement; all three integers must remain present.

## Provenance And Attribution

- Provenance kind: `mixed`

### Attribution requirements

- Retain attribution to Witten for the theorem statement and to TKNN for the projector-level band invariant used in the proof route.

## Retrieval Hints
- `Use when a query asks for the flagship theorem behind Lecture Two rather than only one side of the equivalence.`

## Outgoing Edges
- `anchored_in_source` -> [Topological Phases Core Source Network](../Source-Maps/topological-phases-core.md): The Hall-response theorem is one of the flagship families anchored in the topic-level source network.
- `anchored_in_source` -> [Witten Topological Phases Lecture Two Source Map](../Source-Maps/witten-topological-phases-lecture-two.md): The flagship Hall-response theorem is part of the Lecture Two source map.

## Incoming Edges
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md) -> `supports`: The current derivation turns the quantized Chern-Simons term into the observable Hall response.
- [Reconstruct The Hall-Response / Chern-Number Equivalence](../Regression-Questions/reconstruct-hall-response-chern-number-equivalence.md) -> `tests`: The regression question tests whether the Hall-response theorem can be reconstructed explicitly.
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md) -> `supports`: Large gauge invariance supplies the integer quantization of the Hall-response level.
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md) -> `supports`: The many-body twisted-boundary equivalence closes the equality between microscopic and macroscopic invariants.
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md) -> `supports`: The TKNN definition provides the microscopic Chern-number side of the Hall-response theorem.
- [Ingest TKNN And Haldane For The Lecture Two Equivalence](../Followup-Source-Tasks/ingest-tknn-and-haldane-for-lecture-two-equivalence.md) -> `routes_to`: The TKNN/Haldane recovery task is meant to re-enter the canonical Hall-response theorem family.
- [Twisted-Boundary Berry Curvature Reproduces The Hall Level](../Proof-Fragments/twisted-boundary-berry-curvature-reproduces-hall-level.md) -> `supports`: The twist-angle Berry-curvature proof shows that the many-body invariant reproduces the Hall level.
