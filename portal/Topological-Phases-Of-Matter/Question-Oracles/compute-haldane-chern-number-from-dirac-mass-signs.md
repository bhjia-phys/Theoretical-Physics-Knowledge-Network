# Oracle For Computing The Haldane Chern Number From Dirac-Mass Signs

- ID: `question_oracle:compute-haldane-chern-number-from-dirac-mass-signs`
- Type: `question_oracle`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Detailed oracle for the Haldane bridge question that reconstructs the Chern number from the two valley masses.

## Scope
Detailed answer key for the Haldane valley-mass criterion.

## Regime
Topic regression oracle.

## Assumptions
- `The answer must use the local graphene-to-Haldane bridge rather than quoting a final phase diagram.`

## Representation
Detailed oracle object.

## Source Anchors
- `paper/dirac-mass-criterion | eqs: dirac-mass-at-k-and-k-prime | The answer must write the two valley masses.`
- `paper/chern-insulator-phase | eqs: chern-number-from-valley-masses | The answer must reconstruct the Chern-number criterion from the valley contributions.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Compute The Haldane Chern Number From Dirac-Mass Signs](../Regression-Questions/compute-haldane-chern-number-from-dirac-mass-signs.md)

## Related Units
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)
- [Hall-Response / Chern-Number Cross-Source Fusion Record](../Source-Fusion-Records/hall-response-chern-number-cross-source-fusion.md)
- [Nearest-Neighbor Graphene Hamiltonian](../Definitions/graphene-nearest-neighbor-hamiltonian.md)
- [Graphene Dirac Points Solve 1 + e^{i alpha} + e^{i beta} = 0](../Derivation-Steps/graphene-dirac-point-condition.md)
- [Graphene Lattice Symmetries Protect The Dirac Nodes](../Theorems/graphene-symmetry-protects-dirac-nodes.md)
- [Hemisphere Berry Flux Of A Massive Dirac Hamiltonian Gives Half A Chern Number](../Proof-Fragments/hemisphere-berry-flux-of-massive-dirac-hamiltonian-gives-half-chern-number.md)
- [Haldane Dirac-Mass Signs Determine The Chern Number](../Proof-Fragments/haldane-dirac-mass-signs-determine-chern-number.md)

## Prompt
Detailed oracle for regression_question:compute-haldane-chern-number-from-dirac-mass-signs.

## Failure Triggers
- Fail if the answer never writes the masses at K and K prime.
- Fail if the answer never explains why opposite mass signs give nonzero Chern number.

## Mandatory Units
- [Nearest-Neighbor Graphene Hamiltonian](../Definitions/graphene-nearest-neighbor-hamiltonian.md)
- [Graphene Dirac Points Solve 1 + e^{i alpha} + e^{i beta} = 0](../Derivation-Steps/graphene-dirac-point-condition.md)
- [Graphene Lattice Symmetries Protect The Dirac Nodes](../Theorems/graphene-symmetry-protects-dirac-nodes.md)
- [Hemisphere Berry Flux Of A Massive Dirac Hamiltonian Gives Half A Chern Number](../Proof-Fragments/hemisphere-berry-flux-of-massive-dirac-hamiltonian-gives-half-chern-number.md)
- [Haldane Dirac-Mass Signs Determine The Chern Number](../Proof-Fragments/haldane-dirac-mass-signs-determine-chern-number.md)
- [Lecture Two Hall-Response / Chern-Number Proof State](../Proof-States/lecture-two-hall-response-chern-number.md)

## Mandatory Equation Labels
- `dirac-mass-at-k-and-k-prime`
- `chern-number-from-valley-masses`

## Derivation Spine
- Start from the graphene Dirac points and identify the two low-energy valleys.
- Write the two valley masses m_K = M - 3 sqrt(3) t_2 sin(phi) and m_K prime = M + 3 sqrt(3) t_2 sin(phi).
- Use the massive Dirac half-Chern contribution together with the opposite orientation of the two valleys.
- Sum the two valley contributions to obtain C = 1/2 (sgn(m_K prime) - sgn(m_K)).
- State explicitly which sign patterns give the trivial phase and which give the anomalous Hall phase.

## Mandatory Logical Moves
- Do not skip the passage from graphene valleys to Haldane masses.
- Explain why the two half-Chern contributions subtract rather than add.
- Identify the topological phase by the relative sign of the two masses.

## Common Failure Patterns
- Quoting the final Chern-number formula with no explanation of the two valley contributions.
- Ignoring the opposite orientation of the K and K prime cones.
- Treating the Haldane phase as topological for any nonzero mass without checking the relative signs.

## Grading Rubric
- Pass requires the explicit mass formulas, the half-cone logic, and the final signed Chern-number criterion.
- Partial is appropriate if the answer remembers the criterion but hides the valley-orientation reasoning.

## Outgoing Edges
- none

## Incoming Edges
- none
