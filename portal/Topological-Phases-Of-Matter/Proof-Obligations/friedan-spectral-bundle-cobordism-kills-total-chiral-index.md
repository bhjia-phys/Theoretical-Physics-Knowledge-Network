# Friedan Spectral-Bundle Cobordism Kills Total Chiral Index

- ID: `proof_obligation:friedan-spectral-bundle-cobordism-kills-total-chiral-index`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Canonical Family: `topological-phases/weyl-node-no-go`
- Formalization: `candidate`
- Validation: `cross-checked`
- Maturity: `working`

## Summary
Discharge the proof obligation that Friedan's spectral-projection current identifies the lattice chiral index with the boundary Chern number of the spectral bundle, and therefore cobordism invariance forces the total chiral index to vanish.

## Scope
Third proof obligation in the Lecture One lattice no-go family.

## Regime
Characteristic-class reformulation of the lattice theorem.

## Assumptions
- `The occupied spectral subspaces form a finite-rank bundle over the punctured Brillouin zone.`

## Representation
Bounded proof obligation for Friedan's rigorous cited route to the lattice no-go theorem.

## Source Anchors
- `paper/spectral-projection-chiral-current | eqs: chiral-index-from-low-energy-current | Friedan identifies the low-energy chiral index with the total current charge.`
- `paper/chern-character-and-cobordism | eqs: spectral-bundle-curvature, cobordism-chern-number-zero | The current is reinterpreted as the top Chern character of the spectral bundle on the punctured Brillouin zone.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Friedan Spectral Projection Localizes The Chiral Current On The Spectrum](../Proof-Fragments/friedan-spectral-projection-localizes-the-chiral-current-on-the-spectrum.md)
- [Friedan Chiral Index Is The Chern Number Of The Spectral Bundle Boundary](../Proof-Fragments/friedan-chiral-index-is-the-chern-number-of-the-spectral-bundle-boundary.md)

## Related Units
- [Lecture One Weyl-Node No-Go Proof State](../Proof-States/lecture-one-weyl-node-no-go.md)
- [Weyl-Node No-Go Cross-Source Fusion Record](../Source-Fusion-Records/weyl-node-no-go-cross-source-fusion.md)

## Pass Conditions
- The answer writes the lattice chiral index as the total low-energy chiral charge.
- The answer identifies the spectral bundle W and its natural connection or curvature.
- The answer states that the index is a boundary Chern number and explains why cobordism invariance forces it to vanish.

## Mandatory Logical Moves
- Construct or name the charge-filtered spectral projection S(p).
- Interpret the resulting current as the top Chern character of the spectral bundle.
- Use the fact that the punctured Brillouin zone boundary bounds a manifold to conclude that the boundary Chern number is zero.

## Common Failure Patterns
- Mentioning Friedan only as a citation without the spectral bundle or cobordism argument.
- Treating the cited route as merely another slogan for the Stokes proof without explaining the characteristic-class reformulation.

## Grading Rubric
- Full credit requires the spectral-bundle and cobordism interpretation.
- Partial credit is appropriate if the answer cites Friedan but cannot explain the Chern-number reformulation.

## Retrieval Hints
- `Use when an answer must justify why the cited Friedan route counts as a rigorous recovery rather than a placeholder citation.`

## Outgoing Edges
- none

## Incoming Edges
- none
