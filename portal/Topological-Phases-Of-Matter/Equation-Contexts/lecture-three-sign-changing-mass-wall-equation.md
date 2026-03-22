# Lecture Three Sign-Changing Mass Wall Context

- ID: `equation_context:lecture-three-sign-changing-mass-wall-equation`
- Type: `equation_context`
- Domain: `topological-phases-of-matter`
- Subdomain: `edge-modes`
- Canonical Family: `topological-phases/domain-wall-edge-mode`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
This equation context records the folding step that converts the boundary problem for two opposite-mass fermions into one Dirac equation on all of space with a sign-changing mass profile.

## Scope
Equation-level context for the sign-changing-mass Dirac equation.

## Regime
Folded continuum boundary analysis.

## Assumptions
- `The boundary condition can be encoded by folding the two half-space problems into one whole-space problem.`

## Representation
Equation context for the folded sign-changing-mass problem.

## Source Anchors
- `lecture-three/more-on-edge-states-of-the-integer-quantum-hall-effect | eqs: plift, ulift, nuft, obeys, gift | The boundary gluing is rewritten as one Dirac equation with a sign-changing mass.`

## Mathematical Content
- `kind=display` | `label=plift` | Boundary condition gluing the two opposite-mass fermions.
$$
\left.\psi'\right|_{x_1=0}=\gamma_1\left.\psi\right|_{x_1=0}
$$
- `kind=display` | `label=ulift` | The two bulk equations before folding.
$$
\left(\slashed{\partial}-m\right)\psi=0,\qquad \left(\slashed{\partial}+m\right)\psi'=0
$$
- `kind=display` | `label=gift` | Folded whole-space Dirac equation with a sign-changing mass profile.
$$
\left(\slashed{\partial}-m\,\operatorname{sign}(x_1)\right)\widehat\psi = 0
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `x_1` | coordinate normal to the boundary |
| `\widehat\psi` | folded spinor defined on all of space |

## Dependencies
- [Lecture Three Edge-Mode Symbols](../Notation-Maps/lecture-three-edge-mode-symbols.md)

## Related Units
- [Normalizable Domain-Wall Zero Mode Requires Mass Sign Change](../Proof-Fragments/normalizable-domain-wall-zero-mode-requires-mass-sign-change.md)
- [Boundary Folding Produces Sign-Changing Mass Dirac Equation](../Proof-Obligations/boundary-folding-produces-sign-changing-mass-dirac-equation.md)

## Retrieval Hints
- `Use when the answer must show how the boundary problem becomes a domain-wall problem.`

## Outgoing Edges
- none

## Incoming Edges
- none
