# Linearized Dispersion Near A Fermi Point

- ID: `equation:linearized-dispersion-near-fermi-point`
- Type: `equation`
- Domain: `topological-phases-of-matter`
- Subdomain: `lecture-one`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `stable`

## Summary
Near an isolated one-dimensional Fermi crossing, the band energy expands linearly as epsilon(p)=epsilon(p0)+v(p-p0)+O((p-p0)^2).

## Scope
Lecture One introduction to low-energy effective chiral modes.

## Regime
Small momentum deviation around a one-dimensional crossing.

## Assumptions
- `The slope at p0 is nonzero.`

## Representation
Taylor expansion of the energy band around a Fermi point.

## Source Anchors
- `lecture-one/relativistic-dispersion-in-one-space-dimension | eqs: dolz | This is the starting point for the emergent relativistic form.`

## Mathematical Content
- none

## Symbols
| Symbol | Meaning |
|---|---|
| `p_0` | momentum where the crossing occurs |
| `v` | Fermi velocity given by d epsilon / d p at p0 |

## Dependencies
- [Fermi Velocity](../Quantities/fermi-velocity.md)

## Related Units
- [Continuum 1D Chiral Fermion Hamiltonian](continuum-1d-chiral-fermion-hamiltonian.md)
- [Linearization Gives A 1D Chiral Mode](../Derivations/linearization-gives-1d-chiral-mode.md)

## Failure Modes
- `Quadratic touching requires a different expansion.`

## Formal Targets
- `aitp-l2`

## Retrieval Hints
- `Use for low-energy continuum approximation near a 1D crossing.`

## Outgoing Edges
- `uses` -> [Fermi Velocity](../Quantities/fermi-velocity.md): The linearized dispersion is controlled by the Fermi velocity.

## Incoming Edges
- [Continuum 1D Chiral Fermion Hamiltonian](continuum-1d-chiral-fermion-hamiltonian.md) -> `derived_from`: The continuum Hamiltonian follows from the linearized dispersion after momentum-to-derivative substitution.
- [Linearization Gives A 1D Chiral Mode](../Derivations/linearization-gives-1d-chiral-mode.md) -> `derived_from`: The derivation starts from the linearized dispersion relation.
