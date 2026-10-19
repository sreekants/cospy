# COLREG Rule 15 — Crossing Situation

| | |
|---|---|
| Legata | `Rule15.legata` |
| Driver | `rules.colreg.rule15.Rule15` (`src/rules/colreg/rule15/Rule15.py`) |
| Loaded by | `rules.colreg.yaml`, entry `Rule15` (`encounter.dcpa`, `encounter.range` optional) |
| Terms | `ColregResolver` (`EncounterSituation`, `AheadOfTarget`), `TargetResolver` (`Distance`); constant `Vessel.Collision.PassingDistance` (100 m) |
| Simulation | `Classification.classify()` (crossing angles in `evaluator.yaml`), `EncounterWatch` (role `CRGW`) |
| Tests | `tests/maritime/model/colreg/test_Rule15.py` (7) |
| Status | Judged: keep clear, and cross astern. Judged in a run: 702 encounters, 8 breaches (case 3017189162921500) |
| Reviewed | 2026-10-19 |

## How the rule is fed

`Rule15.feed()` runs an `EncounterWatch` for `Encounter.CRGW`, own ship giving way in a crossing.

- **Onset:** `classify()` names the pair a crossing with the other vessel on own ship's starboard
  side, within 4 km, closing, with a predicted passing distance under 500 m.
- **Role:** the watch claims the role `GiveWay` in the shared registry, so a pair that began as
  overtaking stays with Rule 13.
- **Judgement:** the situation is queued once the range opens past the closest approach. It
  carries the role and the target's last course under way (`ts_course`).

## Rule 15

> When two power-driven vessels are crossing so as to involve risk of collision, the vessel which has
> the other on her own starboard side shall keep out of the way and shall, if the circumstances of the
> case admit, avoid crossing ahead of the other vessel.

**Legata.**
- `clause['COLREG.Rule15/KeepClear']`: `EncounterSituation is 'GiveWay'`, assures `(OS,
  TS).Distance >= Vessel.Collision.PassingDistance`.
- `clause['COLREG.Rule15/CrossAstern']`: `EncounterSituation is 'GiveWay'`, assures `(OS,
  TS).AheadOfTarget is false`.

**Interpretation.**
- *The other on her own starboard side:* `classify()` gives `CRGW` when the courses cross by more
  than `theta_critical_ho` (13°), and:
  - the target's bearing from own ship is between `theta_critical_cr` (−10°) and 112.5°;
  - own ship's bearing from the target is between −112.5° and 10°.
- *Keep out of the way:* passed at 100 m or more at the closest approach.
- *Avoid crossing ahead:* at the closest approach own ship is abaft the other's beam. A target
  stopped since then keeps the course it last held under way.

**In the simulation.** Give-way vessels slow when another vessel comes within
`crossing_fore_min` ahead or `crossing_aft_min` astern (`crossing_slowdown`). No behaviour alters
course to starboard to pass astern.

**Caveats.**
- Both vessels must be power-driven (a condition in each clause, COS.056), and neither may be
  not under command, restricted or engaged in fishing (exclusions since 2026-10-19, LEGATA.050,
  LEGATA.051). A crossing with such a vessel, or with a sailing vessel, is left to Rule 18(a).
- "If the circumstances of the case admit" is not tested: crossing ahead is a breach whatever
  the circumstances.
- The 100 m passing distance, and the 4 km and 500 m onset thresholds, are unvalidated.
- The stand-on vessel's duties are Rule 17's, not judged.

## Open issues

- Check the run's 8 breaches case by case.
