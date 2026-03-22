# Projector Formula for the TKNN Chern Number

- ID: `proof_fragment:projector-formula-for-the-tknn-chern-number`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `berry-geometry`
- Formalization: `draft`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
For the occupied-band projector P(p), the Hall integer is the Brillouin-zone integral of i Tr P [dP, dP] / 2pi, which equals the first Chern class of the occupied bundle.

## Scope
Background proof fragment that turns the bundle-theoretic TKNN definition into an explicit integrand.

## Regime
Finite-rank occupied bundle over a two-dimensional Brillouin torus.

## Assumptions
- `The occupied subspace remains gapped from the empty bands over the whole two-dimensional Brillouin zone.`
- `A smooth local orthonormal frame exists on each patch.`

## Dependencies
- [TKNN Invariant as the First Chern Class of the Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-bundle.md)
- [First Chern Class from Berry Curvature](../Equivalences/first-chern-class-from-berry-curvature.md)

## Related Units
- [The Many-Body Integer hat k' Equals the Band Chern Number k'](../Equivalences/khat-prime-equals-band-chern-number.md)
- [Hall Level Equals the Many-Body Chern Number](../Theorems/hall-level-equals-many-body-chern-number.md)

## Source Anchors
- `kubo-to-integer | Original TKNN quantization argument.`
- `berry-holonomy | Berry holonomy as line-bundle connection.`
- `band-touching-and-sum-rule | Hall integers are precisely the band Chern numbers and obey the band-touching sum rule.`
- `lecture-two/relation-to-band-topology | Witten states the TKNN integer as the first Chern class of the occupied bundle.`

## Outgoing Edges
- none

## Incoming Edges
- none

## Failure Modes
- `If the gap closes, P(p) is not globally smooth and the Chern number can jump.`

## Formal Targets
- `aitp-l2`
