# Twisted-Boundary Berry Curvature Reproduces The Hall Level

- ID: `proof_fragment:twisted-boundary-berry-curvature-reproduces-hall-level`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Treat the twist angles alpha_1 and alpha_2 as adiabatic parameters, read the Berry connection from the one-derivative effective action, and integrate the resulting curvature over the twist-angle torus to recover the Hall-response level k.

## Scope
Key proof fragment in Witten's Lecture Two many-body version of the TKNN formula.

## Regime
Many-body adiabatic transport on the twist-angle torus.

## Assumptions
- `The many-body ground state stays nondegenerate as the twist angles vary.`
- `The excitation gap remains finite in the large-volume limit relevant for the response measurement.`

## Representation
Many-body Berry-curvature proof fragment on the twist-angle torus.

## Source Anchors
- `lecture-two/proof-of-the-equivalence | eqs: mizz, roff, coff, plizz | The Hall-response level is re-derived as the Berry curvature on the twist-angle torus.`

## Mathematical Content
- `kind=display` | `label=mizz` | One-derivative term in the reduced action for the twist angles.
$$
I' = -\frac{k}{2\pi}\int dt\,\alpha_1\frac{d\alpha_2}{dt}
$$
- `kind=display` | `label=roff` | Berry connection on the twist-angle torus.
$$
\nabla = \left(\frac{\partial}{\partial \alpha_1},\frac{\partial}{\partial \alpha_2}+i\frac{k\alpha_1}{2\pi}\right)
$$
- `kind=display` | `label=coff` | Constant Berry curvature determined by the Hall-response level.
$$
\widehat{\mathcal F}_{\alpha_1\alpha_2} = -i\left[\frac{D}{D\alpha_1},\frac{D}{D\alpha_2}\right] = \frac{k}{2\pi}
$$
- `kind=display` | `label=plizz` | Many-body Chern number equals the Hall-response level.
$$
\widehat{k}' = \int_0^{2\pi} d\alpha_1 d\alpha_2\,\frac{\widehat{\mathcal F}}{2\pi} = k
$$

## Symbols
- none

## Dependencies
- [Lecture Two Hall-Response Symbols](../Notation-Maps/lecture-two-hall-response-symbols.md)
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)

## Related Units
- [Band And Many-Body Chern Numbers Agree Under Twisted Boundary Conditions](../Equivalences/band-and-many-body-chern-numbers-agree-under-twisted-boundary-conditions.md)
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)

## Step Justification
- The twist angles are adiabatic parameters defined modulo 2pi, so they form a torus.
- In the adiabatic limit the Berry connection is read from the one-time-derivative part of the action.
- Integrating the constant Berry curvature over the full twist-angle torus gives the many-body Chern number.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.HallResponseChernNumber`
- Declaration: `twisted_boundary_berry_curvature_reproduces_hall_level`
- Statement kind: `lemma`

### Admissible assumptions

- Work on the twist-angle torus for a gapped nondegenerate many-body ground state bundle.
- Use the effective-action extraction of the Berry connection as a permitted wrapper input rather than formalizing the full microscopic adiabatic theorem here.

### Lean prerequisites

- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [Lecture Two Hall-Response Symbols](../Notation-Maps/lecture-two-hall-response-symbols.md)

### Formalization blockers

- The repository does not yet provide a formal interface for many-body ground-state bundles over twist-angle parameter spaces.
- The extraction of Berry connection from the one-derivative effective action is still represented as a physics wrapper step rather than a lower-level formal theorem.

## Retrieval Hints
- `Use when a question asks for the many-body twist-angle route rather than only the single-particle band formula.`

## Outgoing Edges
- `supports` -> [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md): The twist-angle Berry-curvature proof shows that the many-body invariant reproduces the Hall level.

## Incoming Edges
- none
