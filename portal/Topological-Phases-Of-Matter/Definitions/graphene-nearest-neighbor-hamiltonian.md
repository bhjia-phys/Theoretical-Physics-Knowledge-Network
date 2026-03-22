# Nearest-Neighbor Graphene Hamiltonian

- ID: `definition:graphene-nearest-neighbor-hamiltonian`
- Type: `definition`
- Domain: `topological-phases-of-matter`
- Subdomain: `haldane-model`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
The spinless nearest-neighbor honeycomb model has Bloch Hamiltonian H=t[[0,1+e^{-i alpha}+e^{-i beta}],[1+e^{i alpha}+e^{i beta},0]], which is the lattice starting point for Witten's Haldane-model bridge to quantized Hall response.

## Scope
Reusable lattice starting point for the Haldane realization of the integer Hall family.

## Regime
Honeycomb-lattice band theory before the Haldane mass is turned on.

## Assumptions
- `The model is the spinless nearest-neighbor tight-binding problem on the honeycomb lattice.`
- `No symmetry-breaking mass term has yet been added.`

## Representation
Definition of the unperturbed graphene Bloch Hamiltonian in the A/B sublattice basis.

## Source Anchors
- `lecture-three/haldanes-model-of-graphene | eqs: hham | Witten's explicit graphene Hamiltonian used to motivate the Haldane branch.`
- `paper/main-result | Original lattice realization of anomalous Hall response without Landau levels.`

## Mathematical Content
- `kind=display` | `label=hham` | Nearest-neighbor graphene Hamiltonian in the A/B sublattice basis.
$$
H=t\begin{pmatrix} 0 & 1+e^{-i\alpha}+e^{-i\beta} \\ 1+e^{i\alpha}+e^{i\beta} & 0 \end{pmatrix}
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `H` | single-particle Bloch Hamiltonian of the spinless nearest-neighbor graphene model |
| `t` | nearest-neighbor hopping amplitude |
| `\alpha` | first Brillouin-zone angle controlling one relative hopping phase |
| `\beta` | second Brillouin-zone angle controlling the second relative hopping phase |

## Dependencies
- none

## Related Units
- [Graphene Dirac Points Solve 1 + e^{i alpha} + e^{i beta} = 0](../Derivation-Steps/graphene-dirac-point-condition.md)
- [Graphene Lattice Symmetries Protect The Dirac Nodes](../Theorems/graphene-symmetry-protects-dirac-nodes.md)
- [Lecture Two TKNN / Haldane Archival Enrichment Remains To Be Curated](../Open-Gaps/lecture-two-tknn-equivalence-proof-not-yet-curated.md)
- [Witten Topological Phases Lecture Three Source Map](../Source-Maps/witten-topological-phases-lecture-three.md)

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when the Haldane branch needs the explicit lattice Hamiltonian rather than only the words 'graphene model'.`

## Outgoing Edges
- none

## Incoming Edges
- none
