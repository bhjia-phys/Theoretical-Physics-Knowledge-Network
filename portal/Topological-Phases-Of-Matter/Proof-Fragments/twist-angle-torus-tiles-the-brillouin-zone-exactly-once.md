# Twist-Angle Torus Tiles the Brillouin Zone Exactly Once

- ID: `proof_fragment:twist-angle-torus-tiles-the-brillouin-zone-exactly-once`
- Type: `proof_fragment`
- Domain: `topological-phases-of-matter`
- Subdomain: `many-body-band-equivalence`
- Formalization: `draft`
- Validation: `source-grounded`
- Maturity: `seed`

## Summary
Summing over discrete crystal momenta and integrating the twist angles over 0 <= alpha_i < 2pi is exactly the same as integrating over the full Brillouin zone.

## Scope
Key counting step in Witten's proof that the twist-angle Chern number equals the band Chern number.

## Regime
Finite periodic sample used in the many-body to band-theory equivalence argument.

## Assumptions
- `The finite system has periodicities L_1 and L_2 with discrete momenta p_i = (2 pi s_i + alpha_i)/L_i.`
- `The integrand is periodic in the Brillouin zone.`

## Dependencies
- [Many-Body Twist-Angle Chern Number](../Definitions/many-body-twist-angle-chern-number.md)
- [TKNN Invariant as the First Chern Class of the Filled-Band Bundle](../Definitions/tknn-invariant-as-first-chern-class-of-filled-bundle.md)

## Related Units
- [The Many-Body Integer hat k' Equals the Band Chern Number k'](../Equivalences/khat-prime-equals-band-chern-number.md)

## Source Anchors
- `lecture-two/proof-of-the-equivalence | Witten's finite-size reorganization argument.`

## Outgoing Edges
- none

## Incoming Edges
- none

## Failure Modes
- `If the finite-size momentum set does not uniformly sample the Brillouin zone, the reorganization identity fails.`

## Formal Targets
- `aitp-l2`
