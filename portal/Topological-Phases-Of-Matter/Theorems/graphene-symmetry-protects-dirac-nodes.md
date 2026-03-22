# Graphene Lattice Symmetries Protect The Dirac Nodes

- ID: `theorem:graphene-symmetry-protects-dirac-nodes`
- Type: `theorem`
- Domain: `topological-phases-of-matter`
- Subdomain: `haldane-model`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Reflection and rotational symmetries of the honeycomb lattice keep the two graphene Dirac nodes pinned and at the same energy; only symmetry-breaking perturbations can turn them into masses and open the Haldane route to quantized Hall response.

## Scope
Reusable theorem-level statement of why graphene has protected Dirac points before the Haldane mass is introduced.

## Regime
Honeycomb-lattice symmetry analysis prior to opening a topological gap.

## Assumptions
- `The starting model is the nearest-neighbor honeycomb Hamiltonian.`
- `Perturbations preserve the lattice symmetries until the Haldane mass mechanism is discussed explicitly.`

## Representation
Theorem-level symmetry statement for the graphene precursor of the Haldane model.

## Source Anchors
- `lecture-three/haldanes-model-of-graphene | eqs: hham, theq, omeq | Witten's symmetry-based explanation of why the two Dirac nodes persist before the Haldane perturbation.`
- `paper/main-result | Original condensed-matter realization in which suitable symmetry breaking gaps the paired Dirac cones into a Chern insulator.`

## Mathematical Content
- `kind=display` | `label=hham` | Symmetry-constrained nearest-neighbor graphene Hamiltonian.
$$
H=t\begin{pmatrix} 0 & 1+e^{-i\alpha}+e^{-i\beta} \\ 1+e^{i\alpha}+e^{i\beta} & 0 \end{pmatrix}
$$
- `kind=display` | `label=theq` | Band-touching condition selecting the Dirac nodes.
$$
1+e^{i\alpha}+e^{i\beta}=0
$$
- `kind=display` | `label=omeq` | The two symmetry-related Dirac-point locations.
$$
e^{i\alpha}=\frac{1}{2}\left(-1\pm\sqrt{-3}\right)=e^{-i\beta}
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `H` | graphene Bloch Hamiltonian near half filling |
| `\alpha,\beta` | Brillouin-zone angles locating the two graphene Dirac points |

## Dependencies
- [Nearest-Neighbor Graphene Hamiltonian](../Definitions/graphene-nearest-neighbor-hamiltonian.md)
- [Graphene Dirac Points Solve 1 + e^{i alpha} + e^{i beta} = 0](../Derivation-Steps/graphene-dirac-point-condition.md)

## Related Units
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Hall-Response / Chern-Number Cross-Source Fusion Record](../Source-Fusion-Records/hall-response-chern-number-cross-source-fusion.md)
- [Lecture Two TKNN / Haldane Archival Enrichment Remains To Be Curated](../Open-Gaps/lecture-two-tknn-equivalence-proof-not-yet-curated.md)
- [Witten Topological Phases Lecture Three Source Map](../Source-Maps/witten-topological-phases-lecture-three.md)

## Failure Modes
- `This theorem by itself does not yet give the explicit Haldane mass term or the full lattice Chern-number calculation.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when the Haldane branch needs the explicit statement of what protects the ungapped graphene cones and what must be broken to gap them.`

## Outgoing Edges
- none

## Incoming Edges
- none
