# COLREG Rule 29 — Pilot Vessels

| | |
|---|---|
| Legata | `Rule29.legata` (status TODO; no clause) |
| Driver | `rules.colreg.rule29.Rule29` (`src/rules/colreg/rule29/Rule29.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule29` |
| Tests | none |
| Status | Not judged. Pilotage is not modelled |
| Reviewed | 2026-10-19 |

## How the rule is employed

No vessel is engaged on pilotage duty. `Operation` has no pilot member, and no behaviour boards
or carries a pilot. Lights would be names in the `signal` set (see Rule 20). The white-over-red
all-round lights are not in the vocabulary.

## File-level condition

**Legata.** `OS.Operation has 'Vessel.Operation.PILOT'`.

**Caveats.** Not compiled (LEGATA.002). `PILOT` is not an `Operation` member.

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

- A pilot vessel type or operation, if pilot boats are to appear in scenarios. Then the
  vocabulary name and clauses on the pattern of REQ.057.
