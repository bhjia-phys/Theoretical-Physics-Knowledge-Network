# Single Massive Dirac Fermion Induces Half Level

- ID: `proof_obligation:single-massive-dirac-fermion-induces-half-level`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the proof obligation that one massive 2+1-dimensional Dirac fermion induces the half-level Chern-Simons term (sign m)/2 times I_CS, using Witten's Berry-flux hemisphere argument.

## Scope
First proof obligation in the Lecture Three theorem family.

## Regime
Continuum parity-anomaly derivation.

## Assumptions
- `The Berry-flux derivation of the induced topological term is being used in the continuum theory.`

## Representation
Bounded proof obligation for the half-level anomaly of one massive Dirac fermion.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: uftof, puft, PPP | Witten's hemisphere argument for the half-level parity anomaly.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Lecture Three Parity-Anomaly Half-Level Context](../Equation-Contexts/lecture-three-parity-anomaly-half-level.md)

## Related Units
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Dependency Graph](../Dependency-Graph-Snapshots/lecture-three-domain-wall-edge-mode-proof.md)

## Pass Conditions
- The answer states the massive Dirac Hamiltonian used in the Berry-flux argument.
- The answer explains why the normalized map covers only a hemisphere and therefore contributes half a degree.
- The answer concludes with the induced half-level Chern-Simons term.

## Mandatory Logical Moves
- Write the massive Dirac Hamiltonian.
- Interpret its normalized coefficient vector as a map into the target sphere.
- Use the hemisphere coverage to justify the half-integer level.

## Common Failure Patterns
- Invoking 'parity anomaly' without showing why the level is one half.
- Using the final half-level result without the hemisphere geometry.

## Grading Rubric
- Full credit requires the Berry-flux or hemisphere argument, not only the final formula.
- Partial credit is appropriate if the answer knows the half-level but cannot justify it.

## Retrieval Hints
- `Use when an answer must derive, not merely cite, the half-level anomaly.`

## Outgoing Edges
- none

## Incoming Edges
- none
