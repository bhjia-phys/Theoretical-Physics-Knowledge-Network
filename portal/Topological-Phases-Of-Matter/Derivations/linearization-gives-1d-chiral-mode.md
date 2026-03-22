# Linearization Gives A 1D Chiral Mode

- ID: `derivation:linearization-gives-1d-chiral-mode`
- Type: `derivation`
- Domain: `topological-phases-of-matter`
- Subdomain: `lecture-one`
- Canonical Family: ``
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Linearizing the dispersion around a one-dimensional Fermi crossing and replacing momentum deviation by -i d/dx yields a continuum chiral Hamiltonian whose sign of velocity fixes the branch direction.

## Scope
Lecture One derivation from local band data to chiral continuum field theory.

## Regime
One-dimensional low-energy effective theory.

## Assumptions
- `The crossing is simple with nonzero slope.`
- `Long-wavelength continuum approximation is valid.`

## Representation
Low-energy derivation from Taylor expansion plus momentum-to-derivative substitution.

## Source Anchors
- `lecture-one/relativistic-dispersion-in-one-space-dimension | eqs: dolz, continuum | This is the first continuum reduction in Lecture One.`

## Mathematical Content
- none

## Symbols
- none

## Dependencies
- [Linearized Dispersion Near A Fermi Point](../Equations/linearized-dispersion-near-fermi-point.md)
- [Continuum 1D Chiral Fermion Hamiltonian](../Equations/continuum-1d-chiral-fermion-hamiltonian.md)
- [Fermi Velocity](../Quantities/fermi-velocity.md)

## Related Units
- [Local Weyl Description Does Not Fix Global Lattice Consistency](../Warnings/local-weyl-description-does-not-fix-global-lattice-consistency.md)

## Failure Modes
- `A single chiral branch is only a local low-energy description, not a global lattice theory.`

## Formal Targets
- `aitp-l2`

## Retrieval Hints
- `Use when a query asks how a band crossing becomes a relativistic chiral mode.`

## Outgoing Edges
- `derived_from` -> [Linearized Dispersion Near A Fermi Point](../Equations/linearized-dispersion-near-fermi-point.md): The derivation starts from the linearized dispersion relation.
- `uses` -> [Continuum 1D Chiral Fermion Hamiltonian](../Equations/continuum-1d-chiral-fermion-hamiltonian.md): The derivation ends at the continuum chiral Hamiltonian.

## Incoming Edges
- none
