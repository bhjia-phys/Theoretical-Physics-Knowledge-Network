# Nielsen-Ninomiya Charge Cancellation

- ID: `theorem:nielsen-ninomiya-charge-cancellation`
- Type: `theorem`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Canonical Family: `topological-phases/weyl-node-no-go`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
For a compact lattice Brillouin zone with finitely many isolated Weyl nodes, the sum of their local charges vanishes; in the current KB this statement is explicit both through Witten's punctured-zone Stokes proof and through Friedan's cited spectral-projection / Chern-character route.

## Scope
Lecture One theorem statement that rules out a net uncompensated chirality on the lattice.

## Regime
Global lattice band theory with isolated point nodes.

## Assumptions
- `The Brillouin zone is compact.`
- `Only finitely many isolated point nodes are present.`
- `The local charge of each node is defined either by degree theory or by Berry flux.`

## Representation
Global charge-cancellation theorem on a compact punctured Brillouin zone.

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: wnn, cl | Degree-theoretic derivation of the total-charge sum rule.`
- `lecture-one/the-berry-connection | eqs: nna | Berry-curvature reformulation of the same sum rule.`
- `paper/spectral-projection-chiral-current | eqs: chiral-index-from-low-energy-current | Friedan identifies the total chiral index with the total low-energy chiral charge.`
- `paper/chern-character-and-cobordism | eqs: cobordism-chern-number-zero | Friedan's cited rigorous route identifies the theorem with the vanishing boundary Chern number of the spectral bundle.`

## Mathematical Content
- `kind=display` | `label=cl` | Stokes-theorem sum rule for the total lattice Weyl charge.
$$
\sum_{\alpha} w_\alpha = 0
$$
- `kind=display` | `label=nna` | Berry-curvature version of the same cancellation law.
$$
\sum_{\alpha}\int_{S^2_\alpha}\frac{F}{2\pi}=0
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `w_\alpha` | integer charge of the isolated node labeled by \alpha |
| `F` | Berry curvature of the filled-state line bundle away from bad points |

## Dependencies
- [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md)
- [Pullback Of The Area Form Represents The Local Degree](../Proof-Fragments/pullback-area-form-represents-local-degree.md)
- [The Punctured Brillouin Zone Boundary Sum Vanishes](../Proof-Fragments/punctured-brillouin-zone-boundary-sum.md)
- [Berry Curvature Closedness Repeats The Same Stokes Sum](../Proof-Fragments/berry-curvature-closedness-repeats-stokes-sum.md)
- [Friedan Spectral Projection Localizes The Chiral Current On The Spectrum](../Proof-Fragments/friedan-spectral-projection-localizes-the-chiral-current-on-the-spectrum.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](../Proof-Fragments/friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)
- [Continuum Parity Anomaly Does Not Establish Lattice Charge Cancellation](../Proof-Fragments/continuum-parity-anomaly-does-not-establish-lattice-charge-cancellation.md)

## Related Units
- [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md)
- [Lattice Weyl Nodes Sum To Zero Net Chirality](../Claims/lattice-weyl-nodes-sum-to-zero-net-chirality.md)
- [Weyl-Node No-Go Consistency Family](../Theorem-Families/weyl-node-no-go-consistency.md)
- [Lecture One Weyl-Node No-Go Proof State](../Proof-States/lecture-one-weyl-node-no-go.md)
- [Weyl-Node No-Go Cross-Source Fusion Record](../Source-Fusion-Records/weyl-node-no-go-cross-source-fusion.md)
- [Former Friedan-Level Nielsen-Ninomiya Source Gap (Recovered)](../Open-Gaps/friedan-level-rigorous-nielsen-ninomiya-proof-not-yet-ingested.md)
- [Former Parity-Anomaly Versus Lattice-No-Go Scope Gap (Closed)](../Open-Gaps/parity-anomaly-motivates-but-does-not-prove-lattice-no-go.md)

## Topic Completion Status
`promotion-ready`

## Supporting Regression Questions
- [Prove Nielsen-Ninomiya By Stokes](../Regression-Questions/prove-nielsen-ninomiya-by-stokes.md)
- [Explain The Berry-Flux Version Of The Node Charge](../Regression-Questions/explain-berry-flux-version-of-node-charge.md)
- [Separate Anomaly Intuition From The Lattice Proof](../Regression-Questions/separate-anomaly-intuition-from-lattice-proof.md)

## Supporting Oracles
- [Oracle For Proving Nielsen-Ninomiya By Stokes](../Question-Oracles/prove-nielsen-ninomiya-by-stokes.md)
- [Oracle For The Berry-Flux Version Of The Node Charge](../Question-Oracles/explain-berry-flux-version-of-node-charge.md)
- [Oracle For Separating Anomaly Intuition From The Lattice Proof](../Question-Oracles/separate-anomaly-intuition-from-lattice-proof.md)

## Supporting Regression Runs
- `regression_run:witten-lecture-one-2026-03-21-cited-recovery`
- `regression_run:topological-phases-core-2026-03-21-lecture-one-cited-recovery`

## Split Required
`False`

## Recovery Source Refs
- `open_gap:friedan-level-rigorous-nielsen-ninomiya-proof-not-yet-ingested`
- `open_gap:parity-anomaly-motivates-but-does-not-prove-lattice-no-go`
- `followup_source_task:ingest-friedan-proof-of-nielsen-ninomiya`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when a query asks for the theorem statement itself rather than only the concept summary.`

## Outgoing Edges
- `anchored_in_source` -> [Topological Phases Core Source Network](../Source-Maps/topological-phases-core.md): The Nielsen-Ninomiya theorem is one of the flagship families anchored in the topic-level source network.
- `explains` -> [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md): The theorem unit provides the formal statement underlying the concept note.

## Incoming Edges
- [Berry Curvature Closedness Repeats The Same Stokes Sum](../Proof-Fragments/berry-curvature-closedness-repeats-stokes-sum.md) -> `supports`: The Berry-curvature route independently supports the same theorem.
- [Pullback Of The Area Form Represents The Local Degree](../Proof-Fragments/pullback-area-form-represents-local-degree.md) -> `supports`: The local degree formula supplies the local charge notion used in the theorem.
- [Prove Nielsen-Ninomiya By Stokes](../Regression-Questions/prove-nielsen-ninomiya-by-stokes.md) -> `tests`: The regression question tests whether the theorem proof can be reconstructed explicitly.
- [The Punctured Brillouin Zone Boundary Sum Vanishes](../Proof-Fragments/punctured-brillouin-zone-boundary-sum.md) -> `supports`: The punctured-zone Stokes argument proves the global zero-sum law.
