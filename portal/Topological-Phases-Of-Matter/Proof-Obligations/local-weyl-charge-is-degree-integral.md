# Local Weyl Charge Is A Degree Integral

- ID: `proof_obligation:local-weyl-charge-is-degree-integral`
- Type: `proof_obligation`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Canonical Family: `topological-phases/weyl-node-no-go`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Discharge the proof obligation that the charge of an isolated Weyl node is the degree integral of the normalized coefficient map on a small surrounding sphere.

## Scope
First proof obligation in the Lecture One lattice no-go family.

## Regime
Local topological analysis near one Weyl node.

## Assumptions
- `A two-band crossing is isolated and enclosed by a small sphere in momentum space.`

## Representation
Bounded proof obligation for the local topological charge of one Weyl node.

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | eqs: nwn, wnn | Witten's degree-theory definition of the local node charge.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Weyl Node As An Isolated Three-Dimensional Two-Band Crossing](../Definitions/weyl-node-as-isolated-three-dimensional-two-band-crossing.md)
- [Pullback Of The Area Form Represents The Local Degree](../Proof-Fragments/pullback-area-form-represents-local-degree.md)
- [Winding Number As The Degree Of S2 To S2](../Equations/winding-number-as-s2-to-s2-degree.md)

## Related Units
- [Lecture One Weyl-Node No-Go Proof State](../Proof-States/lecture-one-weyl-node-no-go.md)
- [Weyl-Node No-Go Consistency Family](../Theorem-Families/weyl-node-no-go-consistency.md)

## Pass Conditions
- The answer defines the normalized coefficient map on a small sphere around the node.
- The answer writes the degree integral or equivalent pullback-area-form formula for the local charge.
- The answer explains why the resulting integer is stable under smooth deformations that keep the node isolated.

## Mandatory Logical Moves
- Choose a small sphere surrounding one isolated bad point.
- Normalize the local coefficient vector to a map into S^2.
- Integrate the pulled-back normalized area form to obtain the integer charge.

## Common Failure Patterns
- Naming chirality without giving the surrounding-sphere degree formula.
- Using Berry flux without connecting it to the local degree map.

## Grading Rubric
- Full credit requires an explicit local degree formula.
- Partial credit is appropriate if the answer only states that the charge is an integer.

## Retrieval Hints
- `Use when an answer must justify the local integer attached to one Weyl node before the global sum rule.`

## Outgoing Edges
- none

## Incoming Edges
- none
