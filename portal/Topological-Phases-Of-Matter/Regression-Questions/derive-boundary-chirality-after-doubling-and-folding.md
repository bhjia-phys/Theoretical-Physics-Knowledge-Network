# Derive Boundary Chirality After Doubling And Folding

- ID: `regression_question:derive-boundary-chirality-after-doubling-and-folding`
- Type: `regression_question`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Tests whether the topic can reconstruct the Lecture Three proof in the correct order from half-level anomaly, to anomaly cancellation by doubling, to the folded sign-changing-mass equation, and finally to the chiral boundary mode.

## Scope
Proof-focused regression prompt for the doubled continuum edge-mode derivation.

## Regime
Topic regression for the Lecture Three flagship proof.

## Assumptions
- `The answer must preserve the proof order and not jump straight to the wall ansatz.`

## Representation
Lecture Three proof-order regression prompt.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: uftof, quft, gift, zoggg, trogg | The answer should reconstruct the entire local proof in order.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Dependency Graph](../Dependency-Graph-Snapshots/lecture-three-domain-wall-edge-mode-proof.md)

## Related Units
- [Oracle For Deriving Boundary Chirality After Doubling And Folding](../Question-Oracles/derive-boundary-chirality-after-doubling-and-folding.md)

## Prompt
Reconstruct in detail how Witten goes from the half-level parity anomaly of one massive Dirac fermion, to anomaly cancellation by doubling, to the folded sign-changing-mass Dirac equation, and finally to the chiral boundary mode.

## Question Family
`derivation`

## Pass Conditions
- The answer derives the half-level anomaly and its cancellation by doubling.
- The answer explains the folding step to the sign-changing-mass equation.
- The answer derives the chiral boundary equation and localized wall profile.
- The answer preserves the order of the proof.

## Primary Retrieval Paths
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Lecture Three Domain-Wall Edge-Mode Dependency Graph](../Dependency-Graph-Snapshots/lecture-three-domain-wall-edge-mode-proof.md)
- [Lecture Three Parity-Anomaly Half-Level Context](../Equation-Contexts/lecture-three-parity-anomaly-half-level.md)
- [Lecture Three Sign-Changing Mass Wall Context](../Equation-Contexts/lecture-three-sign-changing-mass-wall-equation.md)
- [Lecture Three Chiral Wall-Mode Context](../Equation-Contexts/lecture-three-chiral-wall-mode.md)

## Outgoing Edges
- none

## Incoming Edges
- none
