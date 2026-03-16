# Continuum 1D Chiral Fermion Hamiltonian

- ID: `equation:continuum-1d-chiral-fermion-hamiltonian`
- Type: `equation`
- Domain: `topological-phases-of-matter`
- Subdomain: `lecture-one`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `stable`

## Summary
After replacing p-p0 by -i d/dx, the linearized one-dimensional crossing becomes a continuum Hamiltonian H=v integral dx psi* (-i d/dx) psi up to an irrelevant constant shift.

## Scope
Lecture One passage from band dispersion to a chiral continuum field.

## Regime
Long-wavelength effective theory near a one-dimensional crossing.

## Assumptions
- `The constant energy shift can be dropped for low-energy dynamics.`

## Dependencies
- [Linearized Dispersion Near A Fermi Point](linearized-dispersion-near-fermi-point.md)

## Related Units
- [Linearization Gives A 1D Chiral Mode](../Derivations/linearization-gives-1d-chiral-mode.md)

## Source Anchors
- `lecture-one/relativistic-dispersion-in-one-space-dimension | eqs: continuum, constantshift | The constant term is identified as a removable density shift.`

## Outgoing Edges
- `derived_from` -> [Linearized Dispersion Near A Fermi Point](linearized-dispersion-near-fermi-point.md): The continuum Hamiltonian follows from the linearized dispersion after momentum-to-derivative substitution.

## Incoming Edges
- [Linearization Gives A 1D Chiral Mode](../Derivations/linearization-gives-1d-chiral-mode.md) -> `uses`: The derivation ends at the continuum chiral Hamiltonian.

## Failure Modes
- `A single chiral branch is only local; lattice realizations require balancing branches globally.`

## Formal Targets
- `aitp-l2`
