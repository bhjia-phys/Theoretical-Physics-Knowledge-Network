# Haldane Dirac-Mass Signs Determine The Chern Number

- ID: `proof_fragment:haldane-dirac-mass-signs-determine-chern-number`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
In the Haldane honeycomb model, the two Dirac cones acquire masses m_K = M - 3 sqrt(3) t_2 sin(phi) and m_K prime = M + 3 sqrt(3) t_2 sin(phi); because the two valleys have opposite orientation, the total Chern number is one half of sgn(m_K prime) minus sgn(m_K).

## Scope
Model-specific lattice bridge showing how a concrete condensed-matter Hamiltonian realizes the Hall-response / Chern-number family without Landau levels.

## Regime
Low-energy Dirac analysis of the Haldane Chern insulator on the honeycomb lattice.

## Assumptions
- `The low-energy description near the two honeycomb Dirac points is valid.`
- `The system is half filled and the bulk remains gapped.`

## Representation
Concrete Haldane-model bridge from lattice perturbations to the integer Hall Chern number.

## Source Anchors
- `paper/dirac-mass-criterion | eqs: dirac-mass-at-k-and-k-prime | Archival low-energy mass criterion identifying the two valley masses.`
- `paper/chern-insulator-phase | eqs: chern-number-from-valley-masses | Archival Chern-number formula showing how the valley mass signs determine the Hall phase.`
- `lecture-three/haldanes-model-of-graphene | Witten states that Haldane's perturbation gives masses of the same sign to the Dirac modes and produces the quantum Hall phase.`

## Mathematical Content
- `kind=display` | Effective Dirac masses at the two valleys from sublattice staggering M and complex next-nearest-neighbor hopping t_2 e^{i\phi}.
$$
m_K = M-3\sqrt{3}\,t_2\sin\phi,\qquad m_{K'} = M+3\sqrt{3}\,t_2\sin\phi
$$
- `kind=display` | Total Chern number from the two valleys, whose kinetic terms have opposite orientation.
$$
C = \frac{1}{2}\left(\operatorname{sgn}(m_{K'})-\operatorname{sgn}(m_K)\right)
$$
- `kind=display` | Pure Haldane mass with no sublattice staggering gives the unit Chern-insulator phase.
$$
M=0,\ t_2\sin\phi\neq 0\qquad \Longrightarrow\qquad C=\operatorname{sgn}(t_2\sin\phi)
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `M` | sublattice-staggering (Semenoff) mass |
| `t_2 e^{i\phi}` | complex next-nearest-neighbor hopping that breaks time reversal without net flux per unit cell |
| `C` | first Chern number of the occupied band |

## Dependencies
- [Dirac Point In Two Dimensions](../Concepts/dirac-point-in-2d.md)
- [Parity Anomaly Half Level From Massive Dirac Fermion](parity-anomaly-half-level-from-massive-dirac-fermion.md)

## Related Units
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Hall-Response / Chern-Number Equivalence Family](../Theorem-Families/hall-response-chern-number-equivalence.md)
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Hall-Response / Chern-Number Cross-Source Fusion Record](../Source-Fusion-Records/hall-response-chern-number-cross-source-fusion.md)
- [Witten Topological Phases Lecture Three Source Map](../Source-Maps/witten-topological-phases-lecture-three.md)

## Step Justification
- Linearize the lattice model near K and K prime to identify two massive Dirac cones.
- Use the opposite valley orientation to assign opposite geometric signs to the two half-Dirac contributions.
- Sum the two valley contributions to obtain the Chern-number criterion in terms of the mass signs.

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when an answer must explain the explicit Haldane-model bridge instead of mentioning Haldane only as a citation.`

## Outgoing Edges
- none

## Incoming Edges
- none
