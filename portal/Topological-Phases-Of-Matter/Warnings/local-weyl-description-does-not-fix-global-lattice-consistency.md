# Local Weyl Description Does Not Fix Global Lattice Consistency

- ID: `warning:local-weyl-description-does-not-fix-global-lattice-consistency`
- Type: `warning`
- Domain: `topological-phases-of-matter`
- Subdomain: `lattice-topology`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
A local Weyl cone only describes the neighborhood of one crossing; it does not by itself guarantee that a globally periodic lattice model exists with the same isolated chirality assignment.

## Scope
Lecture One transition from local Weyl physics to Brillouin-zone constraints.

## Regime
Comparing local continuum models with global lattice realizations.

## Assumptions
- `One starts from a local continuum Hamiltonian.`

## Representation
Misuse warning about extrapolating a local cone to a global lattice model.

## Source Anchors
- `lecture-one/the-nielsen-ninomiya-theorem | The theorem is precisely the obstruction to promoting a lone local chirality into a lattice theory.`
- `lecture-one/simple-examples-of-band-hamiltonians | eqs: twof | Explicit periodic models show multiple nodes rather than a single isolated chirality.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Weyl Node](../Concepts/weyl-node.md)
- [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md)

## Related Units
- [Lattice Weyl Nodes Sum To Zero Net Chirality](../Claims/lattice-weyl-nodes-sum-to-zero-net-chirality.md)
- [Two-Band Lattice Weyl Model](../Models/two-band-lattice-weyl-model.md)

## Failure Modes
- `Ignoring Brillouin-zone compactness leads to false expectations about isolated net chirality.`

## Formal Targets
- `aitp-l2`

## Retrieval Hints
- `Return this whenever a local Weyl Hamiltonian is treated as a complete lattice model.`

## Outgoing Edges
- none

## Incoming Edges
- [Weyl Node](../Concepts/weyl-node.md) -> `warned_by`: A local Weyl-node description should not be mistaken for a full lattice model.
