# Two-Band Hamiltonian A Plus B Dot Sigma

- ID: `equation:two-band-hamiltonian-d-dot-sigma`
- Type: `equation`
- Domain: `topological-phases-of-matter`
- Subdomain: `weyl-semimetals`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `stable`

## Summary
A generic local two-band Hamiltonian can be written as H(p)=a(p)+b(p).sigma, and after subtracting the scalar part the crossing structure is governed by the vector b(p).

## Scope
Lecture One universal local form for an isolated crossing.

## Regime
Local description near a two-band crossing.

## Assumptions
- `The problem has been reduced to an effective 2x2 Hermitian Hamiltonian.`

## Dependencies
- none

## Related Units
- [Weyl Node](../Concepts/weyl-node.md)
- [Berry Flux Equals Topological Charge](berry-flux-topological-charge.md)

## Source Anchors
- `lecture-one/three-dimensions | eqs: localexp, xpa | The vector b(p) controls both the crossing and its topology.`

## Outgoing Edges
- `explains` -> [Weyl Node](../Concepts/weyl-node.md): The Pauli-vector decomposition is the universal local language for Weyl nodes.

## Incoming Edges
- [Weyl Node](../Concepts/weyl-node.md) -> `depends_on`: The local Weyl-node description is built from the 2x2 Pauli-vector Hamiltonian.

## Failure Modes
- `For more than two relevant bands the local reduction may need a larger matrix block.`

## Formal Targets
- `aitp-l2`
- `lean`
