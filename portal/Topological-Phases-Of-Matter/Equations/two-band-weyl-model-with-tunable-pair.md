# Two-Band Weyl Model With A Tunable Pair

- ID: `equation:two-band-weyl-model-with-tunable-pair`
- Type: `equation`
- Domain: `topological-phases-of-matter`
- Subdomain: `toy-models`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
The toy Hamiltonian with off-diagonal p1 plus or minus i p2 and diagonal plus or minus f(p3) realizes Weyl nodes whose creation, motion, and annihilation are controlled by the zeros of f.

## Scope
Lecture One explicit example used to create or annihilate Weyl nodes.

## Regime
Continuum toy model for pairs of Weyl nodes.

## Assumptions
- `Only two bands are retained.`
- `Zeros of f are simple unless one is studying node coalescence.`

## Dependencies
- [Weyl Node](../Concepts/weyl-node.md)

## Related Units
- [Two-Band Lattice Weyl Model](../Models/two-band-lattice-weyl-model.md)
- [Local Weyl Description Does Not Fix Global Lattice Consistency](../Warnings/local-weyl-description-does-not-fix-global-lattice-consistency.md)

## Source Anchors
- `lecture-one/some-examples | eqs: terf, werf | The parameter a in f(p3)=p3^2-a controls pair creation and annihilation.`

## Outgoing Edges
- `motivates` -> [Two-Band Lattice Weyl Model](../Models/two-band-lattice-weyl-model.md): The local toy model motivates explicit periodic lattice realizations.

## Incoming Edges
- [Two-Band Lattice Weyl Model](../Models/two-band-lattice-weyl-model.md) -> `specializes`: The lattice model is a periodic specialization of the local Weyl-node toy Hamiltonian idea.

## Failure Modes
- `This model is local and does not by itself enforce lattice periodicity.`

## Formal Targets
- `aitp-l2`
