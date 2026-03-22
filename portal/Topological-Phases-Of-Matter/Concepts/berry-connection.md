# Berry Connection

- ID: `concept:berry-connection`
- Type: `concept`
- Domain: `topological-phases-of-matter`
- Subdomain: `berry-geometry`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
The Berry connection is the U(1) connection on the line bundle of occupied states over regular momentum space, encoding phase transport of eigenstates along paths.

## Scope
Lecture One U(1) Berry connection for a two-band problem with one filled state.

## Regime
Adiabatic geometry of a gapped band subspace away from bad points.

## Assumptions
- `The occupied state is isolated from the empty state over the region of interest.`
- `A smooth local phase choice exists away from singularities.`

## Representation
Connection one-form on the occupied-state bundle.

## Source Anchors
- `lecture-one/the-berry-connection | eqs: zb | Parallel transport of phase is the defining geometric picture.`

## Mathematical Content
- `label=zb` | Parallel-transport condition along a path; the connection is the object that enforces this phase convention.
$$
\left\langle \psi_p, \frac{\mathrm{d}}{\mathrm{d}s} \psi_p \right\rangle = 0
$$
- Local gauge expression for the Berry connection one-form in a chosen local section.
$$
A = -i\,\langle \psi_p, \mathrm d\psi_p\rangle
$$
- Gauge transformation induced by psi_p -> e^{i\chi(p)} psi_p.
$$
A \mapsto A + \mathrm d\chi
$$
- Curvature of the Berry connection.
$$
F = \mathrm dA
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `\psi_p` | normalized occupied-state wavefunction at momentum p |
| `A` | Berry connection one-form in a local gauge |
| `F` | Berry-curvature two-form |
| `\chi` | local phase redefinition parameter |

## Dependencies
- [Complex Line Bundle Of Filled States](complex-line-bundle-of-filled-states.md)

## Related Units
- [Berry Curvature](berry-curvature.md)
- [Berry Flux Equals Topological Charge](../Equations/berry-flux-topological-charge.md)
- [Berry Curvature Two-Form](../Quantities/berry-curvature-two-form.md)
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)

## Failure Modes
- `At bad points the bundle is singular and the U(1) connection is not globally defined.`

## Formal Targets
- `aitp-l2`
- `lean`

## Retrieval Hints
- `Use for Berry phase, holonomy, or line-bundle questions.`

## Outgoing Edges
- `anchored_in_source` -> [Witten Topological Phases Lecture One Source Map](../Source-Maps/witten-topological-phases-lecture-one.md): The Berry-connection unit is part of the current Lecture One source map.
- `depends_on` -> [Complex Line Bundle Of Filled States](complex-line-bundle-of-filled-states.md): The Berry connection lives on the occupied-state line bundle.

## Incoming Edges
- [Berry Curvature](berry-curvature.md) -> `depends_on`: Curvature is defined from the connection.
