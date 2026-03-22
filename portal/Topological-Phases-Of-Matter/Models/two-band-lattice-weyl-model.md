# Two-Band Lattice Weyl Model

- ID: `model:two-band-lattice-weyl-model`
- Type: `model`
- Domain: `topological-phases-of-matter`
- Subdomain: `toy-models`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
A simple periodic two-band lattice Hamiltonian provides an explicit realization of Weyl nodes on a Brillouin torus and makes the global doubling constraint visible.

## Scope
Lecture One simple examples of periodic band Hamiltonians.

## Regime
Explicit lattice regularization of point-node band structure.

## Assumptions
- `Crystal momentum is periodic.`
- `A minimal two-band effective description is sufficient.`

## Representation
Periodic Bloch Hamiltonian on a Brillouin torus.

## Source Anchors
- `lecture-one/simple-examples-of-band-hamiltonians | eqs: twof | Lecture One gives an explicit periodic Weyl Hamiltonian on the lattice.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Weyl Node](../Concepts/weyl-node.md)
- [Nielsen-Ninomiya Theorem](../Concepts/nielsen-ninomiya-theorem.md)

## Related Units
- [Two-Band Weyl Model With A Tunable Pair](../Equations/two-band-weyl-model-with-tunable-pair.md)
- [Local Weyl Description Does Not Fix Global Lattice Consistency](../Warnings/local-weyl-description-does-not-fix-global-lattice-consistency.md)

## Failure Modes
- `A local continuum toy model is not enough to see the torus-level doubling constraint.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use when an explicit lattice regularization is needed.`

## Outgoing Edges
- `specializes` -> [Two-Band Weyl Model With A Tunable Pair](../Equations/two-band-weyl-model-with-tunable-pair.md): The lattice model is a periodic specialization of the local Weyl-node toy Hamiltonian idea.

## Incoming Edges
- [Two-Band Weyl Model With A Tunable Pair](../Equations/two-band-weyl-model-with-tunable-pair.md) -> `motivates`: The local toy model motivates explicit periodic lattice realizations.
