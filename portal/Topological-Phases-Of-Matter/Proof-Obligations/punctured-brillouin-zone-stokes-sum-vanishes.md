# Punctured Brillouin-Zone Stokes Sum Vanishes

- ID: `proof_obligation:punctured-brillouin-zone-stokes-sum-vanishes`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Canonical Family: `topological-phases/weyl-node-no-go`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the proof obligation that excising small balls around all isolated nodes and applying Stokes's theorem to a closed form on the punctured Brillouin zone yields vanishing total charge.

## Scope
Second proof obligation in the Lecture One lattice no-go family.

## Regime
Global topological analysis on the punctured Brillouin zone.

## Assumptions
- `The set of isolated nodes is finite.`
- `The relevant form is closed away from the nodes.`

## Representation
Bounded proof obligation for the global Stokes step in the lattice no-go theorem.

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: cl | Witten's punctured-zone Stokes proof of vanishing total charge.`
- `lecture-one/the-berry-connection | eqs: nna | Berry-curvature version of the same zero-sum law.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [The Punctured Brillouin Zone Boundary Sum Vanishes](../Proof-Fragments/punctured-brillouin-zone-boundary-sum.md)
- [Berry Curvature Closedness Repeats The Same Stokes Sum](../Proof-Fragments/berry-curvature-closedness-repeats-stokes-sum.md)

## Related Units
- [Lecture One Weyl-Node No-Go Proof State](../Proof-States/lecture-one-weyl-node-no-go.md)
- [Nielsen-Ninomiya Charge Cancellation](../Theorems/nielsen-ninomiya-charge-cancellation.md)

## Pass Conditions
- The answer defines the punctured Brillouin zone and its boundary spheres.
- The answer explains why the relevant form is closed on the punctured zone.
- The answer applies Stokes's theorem and identifies the boundary integral with the sum of local node charges.

## Mandatory Logical Moves
- Excise small neighborhoods around all isolated nodes.
- State that the remaining manifold has boundary equal to the union of surrounding spheres.
- Apply Stokes's theorem to the closed form and conclude that the total charge vanishes.

## Common Failure Patterns
- Skipping the punctured-zone construction and jumping directly to the final zero-sum formula.
- Invoking Stokes's theorem without stating what closed form is being integrated.

## Grading Rubric
- Full credit requires an explicit punctured-zone Stokes argument.
- Partial credit is appropriate if the answer only quotes the final vanishing sum.

## Retrieval Hints
- `Use when an answer must supply the global lattice step rather than only the local node charge.`

## Outgoing Edges
- none

## Incoming Edges
- none
