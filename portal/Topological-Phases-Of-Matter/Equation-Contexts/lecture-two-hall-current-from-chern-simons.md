# Lecture Two Hall Current From Chern-Simons Context

- ID: `equation_context:lecture-two-hall-current-from-chern-simons`
- Type: `equation_context`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
This equation context records the functional-derivative route from the integer-level Chern-Simons effective action to the transverse Hall current J_2 = k E_1 / 2pi.

## Scope
Equation-level context for the Hall current extracted from the Chern-Simons action.

## Regime
Macroscopic integer quantum Hall response theory.

## Assumptions
- `The topological response dominates the low-energy effective action.`
- `The sample occupies the x_1-x_2 plane.`

## Representation
Equation context for the response-theory step that converts the topological action into the observed Hall conductivity.

## Source Anchors
- `lecture-two/quantization-of-the-hall-conductivity | eqs: curr, zurr, murr | The functional derivative of the Chern-Simons response produces the Hall current.`

## Mathematical Content
- `kind=display` | `label=curr` | Definition of the induced current in the effective-action formalism.
$$
J_i = -\frac{\delta I_{\mathrm{eff}}}{\delta A_i}
$$
- `kind=display` | `label=zurr` | The integer Hall system is governed by an effective Chern-Simons term.
$$
I_{\mathrm{eff}} = k\,\mathcal I_{\mathrm{CS}} = \frac{k}{4\pi}\int_{M_3}\epsilon^{ijk}A_i\partial_jA_k
$$
- `kind=display` | `label=murr` | The longitudinal electric field becomes a transverse Hall current.
$$
J_2 = \frac{kF_{01}}{2\pi} = \frac{kE_1}{2\pi}
$$

## Symbols
| Symbol | Meaning |
|---|---|
| `J_2` | Hall current flowing in the x_2 direction |
| `E_1` | electric field in the x_1 direction |

## Dependencies
- [Lecture Two Hall-Response Symbols](../Notation-Maps/lecture-two-hall-response-symbols.md)

## Related Units
- [Chern-Simons Action Induces Hall Current](../Derivation-Steps/chern-simons-action-induces-hall-current.md)
- [Chern-Simons Level Produces Quantized Hall Current](../Proof-Obligations/chern-simons-level-produces-quantized-hall-current.md)

## Retrieval Hints
- `Use when an answer must show the variation step and not only quote the final conductivity.`

## Outgoing Edges
- none

## Incoming Edges
- none
