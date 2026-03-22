# Edge Mode Restores Consistency With Integer Bulk Response

- ID: `proof_obligation:edge-mode-restores-consistency-with-integer-bulk-response`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the synthesis obligation that the chiral wall mode derived from the sign-changing mass supplies the boundary degree of freedom required by the doubled integer Hall system once one mass sign has been flipped.

## Scope
Final synthesis obligation connecting the local wall mode back to the bulk response story.

## Regime
Final synthesis of the Lecture Three theorem family.

## Assumptions
- `The bulk discussion is the doubled integer Hall system built from opposite-mass Dirac fermions.`

## Representation
Final synthesis obligation for the Lecture Three boundary-mode theorem.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: plof, uftof, gift, trogg | Witten's conceptual closure of the edge-mode consistency argument.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Single Massive Dirac Fermion Induces Half Level](single-massive-dirac-fermion-induces-half-level.md)
- [Doubling Cancels Parity Anomaly Before Boundary Sign Flip](doubling-cancels-parity-anomaly-before-boundary-sign-flip.md)
- [Boundary Folding Produces Sign-Changing Mass Dirac Equation](boundary-folding-produces-sign-changing-mass-dirac-equation.md)
- [Domain-Wall Ansatz Imposes Chiral Boundary Equation](domain-wall-ansatz-imposes-chiral-boundary-equation.md)
- [Normalizable Wall Mode Requires Mass Sign Change](normalizable-wall-mode-requires-mass-sign-change.md)

## Related Units
- [Lecture Three Domain-Wall Edge-Mode Proof State](../Proof-States/lecture-three-domain-wall-edge-mode.md)
- [Sign-Changing Dirac Mass Supports Chiral Edge Mode](../Theorems/sign-changing-dirac-mass-supports-chiral-edge-mode.md)
- [Domain-Wall Edge-Mode Cross-Source Fusion Record](../Source-Fusion-Records/domain-wall-edge-mode-cross-source-fusion.md)

## Pass Conditions
- The answer explains the doubled starting point and the boundary sign flip.
- The answer reconstructs the wall mode locally.
- The answer connects that wall mode back to the consistent integer Hall boundary story.

## Mandatory Logical Moves
- Start from the doubled anomaly-free bulk system.
- Introduce the boundary sign flip and obtain the wall equation.
- Derive the localized chiral mode.
- Explain why that mode is the missing boundary excitation of the integer Hall system.

## Common Failure Patterns
- Stopping at the local wall-mode derivation without reconnecting it to the bulk consistency story.
- Confusing this continuum synthesis with the separate lattice Nielsen-Ninomiya theorem.

## Grading Rubric
- Full credit requires both the local derivation and the bulk-boundary consistency interpretation.
- Partial credit is appropriate if the wall mode is derived but never tied back to the integer Hall response.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.DomainWallEdgeMode`
- Declaration: `edge_mode_restores_consistency_with_integer_bulk_response`
- Statement kind: `theorem`

### Admissible assumptions

- The doubled bulk system starts anomaly-free before one mass sign is flipped.
- The boundary-folding and normalizability lemmas have already been discharged separately.

### Lean prerequisites

- [Single Massive Dirac Fermion Induces Half Level](single-massive-dirac-fermion-induces-half-level.md)
- [Doubling Cancels Parity Anomaly Before Boundary Sign Flip](doubling-cancels-parity-anomaly-before-boundary-sign-flip.md)
- [Boundary Folding Produces Sign-Changing Mass Dirac Equation](boundary-folding-produces-sign-changing-mass-dirac-equation.md)
- [Domain-Wall Ansatz Imposes Chiral Boundary Equation](domain-wall-ansatz-imposes-chiral-boundary-equation.md)
- [Normalizable Wall Mode Requires Mass Sign Change](normalizable-wall-mode-requires-mass-sign-change.md)

### Formalization blockers

- The boundary zero-mode formalization still needs reusable lemmas for the folded Dirac operator and chiral projection.

## Retrieval Hints
- `Use when the answer must close the loop between parity anomaly, domain wall, and integer Hall consistency.`

## Outgoing Edges
- none

## Incoming Edges
- none
