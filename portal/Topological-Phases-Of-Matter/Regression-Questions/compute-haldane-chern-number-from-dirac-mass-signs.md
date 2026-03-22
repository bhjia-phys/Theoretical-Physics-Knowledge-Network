# Compute The Haldane Chern Number From Dirac-Mass Signs

- ID: `regression_question:compute-haldane-chern-number-from-dirac-mass-signs`
- Type: `regression_question`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Tests whether the topic can derive the Haldane-model Chern number from the two valley masses instead of citing the lattice Chern insulator by name only.

## Scope
Bridge-derivation question for the explicit Haldane lattice criterion.

## Regime
Topic regression for the Haldane bridge inside the Lecture Two and Lecture Three hall-response family.

## Assumptions
- `The answer must start from the low-energy graphene valleys rather than jumping directly to the final Hall phase.`

## Representation
Haldane-bridge regression prompt.

## Source Anchors
- `paper/dirac-mass-criterion | eqs: dirac-mass-at-k-and-k-prime | The answer should write the two valley masses explicitly.`
- `paper/chern-insulator-phase | eqs: chern-number-from-valley-masses | The answer should reconstruct the signed valley contribution formula for the Chern number.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Nearest-Neighbor Graphene Hamiltonian](../Definitions/graphene-nearest-neighbor-hamiltonian.md)
- [Graphene Dirac Points Solve 1 + e^{i alpha} + e^{i beta} = 0](../Derivation-Steps/graphene-dirac-point-condition.md)
- [Haldane Dirac-Mass Signs Determine The Chern Number](../Proof-Fragments/haldane-dirac-mass-signs-determine-chern-number.md)

## Related Units
- [Oracle For Computing The Haldane Chern Number From Dirac-Mass Signs](../Question-Oracles/compute-haldane-chern-number-from-dirac-mass-signs.md)

## Prompt
Derive the Haldane-model Chern number from the valley masses at K and K prime, and explain why opposite mass signs produce the anomalous Hall phase.

## Question Family
`derivation`

## Pass Conditions
- The answer writes the valley masses m_K and m_K prime explicitly.
- The answer explains that each massive Dirac cone contributes a half Chern number with opposite valley orientation.
- The answer derives C = 1/2 (sgn(m_K prime) - sgn(m_K)).
- The answer states clearly when the phase is topological and when it is trivial.

## Primary Retrieval Paths
- [Nearest-Neighbor Graphene Hamiltonian](../Definitions/graphene-nearest-neighbor-hamiltonian.md)
- [Graphene Dirac Points Solve 1 + e^{i alpha} + e^{i beta} = 0](../Derivation-Steps/graphene-dirac-point-condition.md)
- [Graphene Lattice Symmetries Protect The Dirac Nodes](../Theorems/graphene-symmetry-protects-dirac-nodes.md)
- [Hemisphere Berry Flux Of A Massive Dirac Hamiltonian Gives Half A Chern Number](../Proof-Fragments/hemisphere-berry-flux-of-massive-dirac-hamiltonian-gives-half-chern-number.md)
- [Haldane Dirac-Mass Signs Determine The Chern Number](../Proof-Fragments/haldane-dirac-mass-signs-determine-chern-number.md)

## Retrieval Hints
- `Use in regression runs to ensure the local Haldane bridge is derivable rather than merely name-dropped.`

## Outgoing Edges
- none

## Incoming Edges
- none
