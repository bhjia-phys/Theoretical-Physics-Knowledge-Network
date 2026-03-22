# Lecture Two Hall-Response Symbols

- ID: `notation_map:lecture-two-hall-response-symbols`
- Type: `notation_map`
- Domain: `topological-phases-of-matter`
- Subdomain: `integer-quantum-hall-effect`
- Canonical Family: `topological-phases/hall-response-chern-number`
- Formalization: `candidate`
- Validation: `source-grounded`
- Maturity: `working`

## Summary
This notation map fixes the symbols used in Lecture Two for the Chern-Simons level, Hall current, filled-band Chern number, and twist-angle Berry curvature.

## Scope
Shared notation for the Hall-response / Chern-number equivalence branch.

## Regime
Lecture Two integer quantum Hall response and Berry-curvature notation.

## Assumptions
- `The low-energy response is described by a 2+1-dimensional effective action.`
- `The finite sample has periodic boundary conditions with twist angles alpha_1 and alpha_2.`

## Representation
Shared symbol table for the Hall-response / TKNN / twist-angle branch.

## Source Anchors
- `lecture-two/quantization-of-the-hall-conductivity | eqs: zurr, murr | Hall-response notation centered on the integer level k.`
- `lecture-two/proof-of-the-equivalence | eqs: mizz, coff, plizz | Twist-angle Berry-curvature notation for the many-body Chern number.`

## Mathematical Content
- none

## Symbols
| Symbol | Meaning |
|---|---|
| `k` | integer Chern-Simons level or Hall-response coefficient |
| `k'` | filled-band first Chern number in single-particle band theory |
| `\widehat{k}'` | many-body Chern number over the twist-angle torus |
| `\alpha_1, \alpha_2` | twist angles or flat background holonomies around the two spatial cycles |
| `\widehat{\mathcal F}` | Berry curvature on the twist-angle torus |
| `\mathcal I_{\mathrm{CS}}` | 2+1-dimensional Chern-Simons functional |

## Dependencies
- none

## Related Units
- [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md)
- [Integer Quantum Hall Response Equals Band And Many-Body Chern Number](../Theorems/integer-quantum-hall-response-equals-band-and-many-body-chern-number.md)
- [Large Gauge Invariance Quantizes The Chern-Simons Level](../Proof-Fragments/large-gauge-invariance-quantizes-chern-simons-level.md)
- [Twisted-Boundary Berry Curvature Reproduces The Hall Level](../Proof-Fragments/twisted-boundary-berry-curvature-reproduces-hall-level.md)

## Retrieval Hints
- `Use before answering a Lecture Two derivation question that mixes k, k', and the many-body twist-angle invariant.`

## Outgoing Edges
- `supports` -> [TKNN Invariant As First Chern Class Of The Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-band-bundle.md): The Lecture Two notation map fixes the Hall-response and Berry-curvature symbols used in the TKNN definition.

## Incoming Edges
- none
