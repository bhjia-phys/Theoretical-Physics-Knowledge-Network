# Fermi Velocity

- ID: `quantity:fermi-velocity`
- Type: `quantity`
- Domain: `topological-phases-of-matter`
- Subdomain: `low-energy-kinematics`
- Formalization: `not_started`
- Validation: `source-grounded`
- Maturity: `stable`

## Summary
The Fermi velocity is the slope of the dispersion at a crossing and acts as the effective light-cone speed in the linearized continuum description.

## Scope
Lecture One one-dimensional linearization and its relativistic analogy.

## Regime
Low-energy analysis near a Fermi point.

## Assumptions
- `The dispersion is differentiable at the crossing.`

## Dependencies
- none

## Related Units
- [Linearized Dispersion Near A Fermi Point](../Equations/linearized-dispersion-near-fermi-point.md)
- [Continuum 1D Chiral Fermion Hamiltonian](../Equations/continuum-1d-chiral-fermion-hamiltonian.md)

## Source Anchors
- `lecture-one/relativistic-dispersion-in-one-space-dimension | eqs: dolz | Defined as the derivative of epsilon with respect to momentum at p0.`

## Outgoing Edges
- none

## Incoming Edges
- [Linearized Dispersion Near A Fermi Point](../Equations/linearized-dispersion-near-fermi-point.md) -> `uses`: The linearized dispersion is controlled by the Fermi velocity.

## Failure Modes
- `Vanishing slope invalidates the simple chiral continuum description.`

## Formal Targets
- `aitp-l2`
