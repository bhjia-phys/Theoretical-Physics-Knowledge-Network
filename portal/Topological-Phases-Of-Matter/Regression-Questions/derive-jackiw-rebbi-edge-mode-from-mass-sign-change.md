# Derive The Jackiw-Rebbi Edge Mode From Mass Sign Change

- ID: `regression_question:derive-jackiw-rebbi-edge-mode-from-mass-sign-change`
- Type: `regression_question`
- Domain: `topological-phases-of-matter`
- Subdomain: `regression`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Tests whether the topic can derive the chiral boundary mode from the sign-changing Dirac mass and explain how that mode fits the parity-anomaly consistency story.

## Scope
Flagship Lecture Three derivation question for the topological-phases topic suite.

## Regime
Topic regression for the Lecture Three boundary-mode branch.

## Assumptions
- `The answer must distinguish the continuum edge-mode derivation from the separate lattice no-go theorem.`

## Representation
Lecture Three flagship regression prompt.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: gift, zoggg, trogg | The answer should reconstruct the wall-mode derivation and connect it to the doubled parity-anomaly setup.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Jackiw-Rebbi Domain-Wall Zero Mode](../Definitions/jackiw-rebbi-domain-wall-zero-mode.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Related Units
- [Oracle For Deriving The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Question-Oracles/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md)

## Prompt
Derive the chiral boundary mode supported by a sign-changing Dirac mass and explain why it makes the doubled integer Hall system consistent.

## Question Family
`derivation`

## Pass Conditions
- The answer explains why a single massive Dirac fermion carries a half-level parity anomaly.
- The answer shows how the boundary problem is rewritten as a sign-changing-mass Dirac equation.
- The answer writes the localized ansatz and the reduced boundary Dirac equation.
- The answer writes the bulk-plus-boundary anomaly-cancellation equation rather than mentioning anomaly inflow only as a slogan.
- The answer explains why the resulting chiral edge mode restores consistency with the integer bulk response.

## Primary Retrieval Paths
- [Parity Anomaly Half Level From Massive Dirac Fermion](../Proof-Fragments/parity-anomaly-half-level-from-massive-dirac-fermion.md)
- [Callan-Harvey Inflow Cancels The Boundary Anomaly](../Proof-Fragments/callan-harvey-inflow-cancels-boundary-anomaly.md)
- [Jackiw-Rebbi Domain-Wall Zero Mode](../Definitions/jackiw-rebbi-domain-wall-zero-mode.md)
- [Domain-Wall Ansatz Reduces To Boundary Dirac Equation](../Derivation-Steps/domain-wall-ansatz-reduces-to-boundary-dirac-equation.md)
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)

## Retrieval Hints
- `Use in topic regression runs to test whether the Lecture Three edge-mode story is derivable rather than only cited.`

## Outgoing Edges
- `tests` -> [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md): The regression question tests whether the edge-mode theorem can be reconstructed explicitly.

## Incoming Edges
- [Oracle For Deriving The Jackiw-Rebbi Edge Mode From Mass Sign Change](../Question-Oracles/derive-jackiw-rebbi-edge-mode-from-mass-sign-change.md) -> `oracles`: This oracle records the derivation requirements for the Jackiw-Rebbi edge-mode question.
