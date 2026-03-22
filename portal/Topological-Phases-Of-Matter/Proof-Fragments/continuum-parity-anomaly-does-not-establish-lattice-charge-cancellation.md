# Continuum Parity Anomaly Does Not Establish Lattice Charge Cancellation

- ID: `proof_fragment:continuum-parity-anomaly-does-not-establish-lattice-charge-cancellation`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `bridge-objects`
- Canonical Family: `topological-phases/anomaly-vs-lattice-no-go`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
The continuum parity-anomaly and anomaly-inflow story diagnoses the response of a massive Dirac cone or a wall-localized chiral mode, while the lattice Nielsen-Ninomiya theorem is a compact-Brillouin-zone Chern-number and cobordism statement; Haldane's lattice model realizes the former only after the valley contributions combine into an integer lattice invariant.

## Scope
Explicit formula-bearing scope boundary for the Lecture One lattice theorem versus the later parity-anomaly and anomaly-inflow branches.

## Regime
Conceptual and proof-level separation between continuum anomaly language and the lattice no-go theorem.

## Assumptions
- `A single continuum Dirac cone and a compact lattice Brillouin zone answer different questions and live on different state spaces.`
- `The answer must keep motivation, lattice realization, and actual theorem proof distinct.`

## Representation
Scope-boundary proof fragment separating continuum anomaly response statements from the global lattice no-go theorem.

## Source Anchors
- `lecture-two/edge-states-and-anomaly-inflow | Witten uses anomaly inflow as a boundary-consistency argument, not as the Lecture One lattice proof.`
- `paper/chern-insulator-phase | eqs: chern-number-from-valley-masses | Haldane's lattice completion converts local parity-anomaly intuition into an integer Hall invariant after both valleys are included.`
- `paper/anomaly-cancellation | eqs: bulk-topological-variation, inflow-balance | Callan-Harvey explains continuum bulk-boundary consistency, not the compact-BZ proof of zero net lattice chirality.`
- `paper/chern-character-and-cobordism | eqs: cobordism-chern-number-zero | Friedan's theorem proof is a Chern-number and cobordism argument on the spectral bundle over the punctured Brillouin zone.`

## Mathematical Content
- `kind=display` | Continuum parity-anomaly response of one massive Dirac cone.
$$
\Gamma_{\mathrm{odd}}[A]=\frac{\operatorname{sign}m}{2}\,I_{\mathrm{CS}}(A)
$$
- `kind=display` | Callan-Harvey anomaly inflow is a bulk-boundary consistency equation for a continuum wall mode.
$$
\delta_{\Lambda}W_{\mathrm{edge}}=-\delta_{\Lambda}I_{\mathrm{bulk}}
$$
- `kind=display` | `label=chern-number-from-valley-masses` | Haldane's lattice model yields an integer Hall invariant only after combining the two valley contributions.
$$
C=\frac{1}{2}\Bigl(\operatorname{sign}(m_K)-\operatorname{sign}(m_{K'})\Bigr)
$$
- `kind=display` | `label=cobordism-chern-number-zero` | The lattice theorem proves zero net chirality from compact-BZ spectral-bundle topology, not from continuum anomaly response alone.
$$
I_Q = \int_{\partial M} n_\mu F_Q^{0\mu} = 0
$$

## Symbols
- none

## Dependencies
- [A Massive Two Plus One Dimensional Dirac Fermion Induces A Half-Level Chern-Simons Term](../Theorems/half-level-cs-term-from-massive-dirac-fermion.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Haldane Dirac-Mass Signs Determine The Chern Number](haldane-dirac-mass-signs-determine-chern-number.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)

## Related Units
- [Continuum Anomaly To Lattice No-Go](../Bridges/continuum-anomaly-to-lattice-no-go.md)
- [Continuum Parity Anomaly Is Not Lattice No-Go](../Conflict-Records/continuum-parity-anomaly-is-not-lattice-no-go.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)
- [Lecture One Weyl-Node No-Go Proof State](../Proof-States/lecture-one-weyl-node-no-go.md)

## Step Justification
- The half-level Chern-Simons term characterizes the parity-odd response of one continuum Dirac cone, which is not yet a gauge-invariant lattice model.
- Callan-Harvey inflow explains how a boundary chiral anomaly is canceled by a bulk topological term in a continuum domain-wall setup.
- Haldane's lattice realization shows that lattice physics restores an integer invariant by combining both valleys, so the lattice object is already different from a single anomalous cone.
- Friedan's proof of Nielsen-Ninomiya instead computes a compact-Brillouin-zone Chern number of the spectral bundle and sets it to zero by cobordism invariance.

## Retrieval Hints
- `Use when a query risks conflating parity anomaly, anomaly inflow, and the actual lattice no-go proof.`

## Outgoing Edges
- none

## Incoming Edges
- none
