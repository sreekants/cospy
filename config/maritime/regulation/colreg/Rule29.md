# COLREG Rule 29 — Pilot Vessels

| | |
|---|---|
| Legata | `Rule29.legata` (status TODO; no clause) |
| Driver | `rules.colreg.rule29.Rule29` (`src/rules/colreg/rule29/Rule29.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule29` |
| Tests | none |
| Status | Not judged. Pilotage is a trip-row operation (2026-10-19); no clause and no pilot lights yet |
| Reviewed | 2026-10-19 |

## How the rule is employed

A vessel is engaged on pilotage duty for a trip row whose action is `pilotage`: it sets
`Operation.PILOTAGE` until the next waypoint (Rule 3). No behaviour boards or carries a pilot. Lights would be names in the `signal` set (see Rule 20). The white-over-red
all-round lights are not in the vocabulary.

## File-level condition

**Legata.** `OS.Operation is Vessel.Operation.PILOTAGE`. It tested a quoted `PILOT`, not a member,
until 2026-10-19 (LEGATA.003).

**Caveats.** Not compiled (LEGATA.002). There is no clause for it to scope.

## (a) On pilotage duty

> A vessel engaged on pilotage duty shall exhibit: (i) at or near the masthead, two all-round lights in a
> vertical line, the upper being white and the lower red; (ii) when underway, in addition, sidelights
> and a sternlight; (iii) when at anchor, in addition to the lights prescribed in sub-paragraph (i), the
> light, lights or shape prescribed in Rule 30 for vessels at anchor.

**Legata.** None.

## (b) Not on pilotage duty

> A pilot vessel when not engaged on pilotage duty shall exhibit the lights or shapes prescribed for a
> similar vessel of her length.

**Legata.** None.

## Open issues

- The white-over-red all-round lights in the vocabulary, and clauses for (a) on the pattern of
  REQ.057.
- `VesselSignals` rows for pilotage.
