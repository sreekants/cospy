# COLREG Rule 37 — Distress Signals

| | |
|---|---|
| Legata | `Rule37.legata` (text only) |
| Driver | `rules.colreg.rule37.Rule37` (`src/rules/colreg/rule37/Rule37.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule37` |
| Tests | none |
| Status | Not judged. Distress is not modelled |
| Reviewed | 2026-10-19 |

## How the rule is employed

No vessel can be in distress: no status, event or behaviour represents it. The Annex IV signals
are not in the vocabulary. Collision, grounding and capsize are scored by examiners
(`CollisionExaminer`, `GroundingExaminer`, `RiskExaminer`'s capsize model), but none of them puts
a vessel into distress.

## Rule 37

> When a vessel is in distress and requires assistance she shall use or exhibit the signals described in
> Annex IV to these Regulations.

**Legata.** None.

**Caveats.** Annex IV is out of scope. Rule 27(h) relies on the distinction between distress and
not-under-command signals, which the simulation does not need while neither is raised.

## Open issues

- A distress state, for example after grounding or capsize, if search-and-rescue or
  assistance scenarios are added.
