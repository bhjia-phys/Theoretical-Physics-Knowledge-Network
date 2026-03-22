# Chern-Simons Action Induces Hall Current

- ID: `derivation_step:chern-simons-action-induces-hall-current`
- Type: `derivation_step`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
Differentiate the integer-level Chern-Simons effective action with respect to the background gauge field to obtain the transverse Hall current J_2 = k E_1 / 2pi.

## Scope
Functional-derivative step from topological action to Hall current.

## Regime
Macroscopic response theory of the integer quantum Hall effect.

## Assumptions
- `The low-energy effective action is dominated by the Chern-Simons term.`
- `The sample lies in the x_1-x_2 plane.`

## Representation
Functional derivative of the Chern-Simons action with respect to the background gauge field.

## Source Anchors
- `lecture-two/quantization-of-the-hall-conductivity | eqs: curr, zurr, murr | Variation of the Chern-Simons action produces the quantized Hall current.`

## Mathematical Content
- `kind=display` | `label=curr` | Definition of the induced current from the effective action.
$$
J_i = -\frac{\delta I_{\mathrm{eff}}}{\delta A_i}
$$
- `kind=display` | `label=zurr` | Effective topological response with integer level k.
$$
I_{\mathrm{eff}} = k\,\mathcal I_{\mathrm{CS}} = \frac{k}{4\pi}\int_{M_3}\epsilon^{ijk}A_i\partial_jA_k
$$
- `kind=display` | `label=murr` | Transverse Hall current induced by an electric field in the x_1 direction.
$$
J_2 = \frac{kF_{01}}{2\pi} = \frac{kE_1}{2\pi}
$$

## Symbols
- none

## Dependencies
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Lecture Two Hall-Response Symbols](../Notation-Maps/lecture-two-hall-response-symbols.md)

## Related Units
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)

## Step Inputs
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)

## Step Justification
- The response current is obtained by differentiating the effective action with respect to the background gauge potential.
- For a 2+1-dimensional sample, the antisymmetric tensor in the Chern-Simons term turns a longitudinal electric field into a transverse current.

## Formal Targets
- `aitp-l2`
- `lean`

## Lean Formalization Plan

- Namespace: `TopologicalPhases.IntegerHall.HallResponseChernNumber`
- Declaration: `chern_simons_action_induces_hall_current`
- Statement kind: `lemma`

### Admissible assumptions

- Treat the effective action as a differentiable functional of the background gauge field.
- Work at the level of formal variational calculus rather than deriving the effective action from a microscopic path integral inside the same lemma.

### Lean prerequisites

- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Lecture Two Hall-Response Symbols](../Notation-Maps/lecture-two-hall-response-symbols.md)

### Formalization blockers

- The repository does not yet provide a formal variational-calculus layer for differential-form actions.
- Sign conventions for epsilon tensors and electric-field components are still carried as source-level notation rather than a reusable formal convention package.

## Retrieval Hints
- `Use when a derivation needs the explicit step from topological response action to Hall conductivity.`

## Outgoing Edges
- `supports` -> [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md): The current derivation turns the quantized Chern-Simons term into the observable Hall response.

## Incoming Edges
- none
