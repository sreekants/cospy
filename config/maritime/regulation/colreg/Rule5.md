# COLREG Rule 5 — Look-out

| | |
|---|---|
| Legata | `Rule5.legata` |
| Driver | `rules.colreg.rule5.Rule5` (`src/rules/colreg/rule5/Rule5.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule5` |
| Terms | `(OS, TS).TimeToEncounter`, `OS.Intent`, `OS.Restriction`; constants `Vessel.Collision.TimeToEncounter.{AlertRange, VisibleRange}` |
| Tests | `tests/maritime/behavior/vessels/test_TripRows.py` (LookoutTestCase, 3) |
| Status | Not judged in a run: one clause (Sight), not fed. Planned vessels declare the look-out intent while underway (2026-10-19). Radar and Sonar removed (LEGATA.014, LEGATA.015) |
| Reviewed | 2026-10-19 |

## How the rule is employed

**In Legata.** Rule 5 is one clause, Sight. It assures that own ship has declared a look-out
intent while a target is in visible range. The driver feeds nothing, so it is not evaluated.

**In the simulation.** Look-out is part of vessel behaviour, not a declared intent. Each pass, a
vessel behaviour queries the world for the vessels within `behavior.range_visibility` of the
ship model (`b.nearest`). The manoeuvres (`VesselManeuvers.overtaking_distance`,
`crossing_slowdown`, `fishing_slowdown`, `stop_for_safety`) act on that list. Every vessel
therefore keeps a continuous, all-round look-out by the means the simulation has: perfect
knowledge of the other vessels' positions within range. A look-out cannot lapse, so nothing
can breach Rule 5.

## Rule 5

> Every vessel shall at all times maintain a proper look-out by sight and hearing as well as by all
> available means appropriate in the prevailing circumstances and conditions so as to make a full
> appraisal of the situation and of the risk of collision.

**Legata.**
- **file-level condition,** either line:
  - `(OS, TS).TimeToEncounter in Vessel.Collision.TimeToEncounter.AlertRange`;
  - `OS.Restriction in ['COLREG.Rule5.*']`.
- `clause['COLREG.Rule5/Sight']`: with `(OS, TS).TimeToEncounter in VisibleRange`, assures
  `OS.Intent has 'Operation.Lookout.*'`.

**Removed on 2026-10-19.**
- `COLREG.Rule5/Radar` tested radio, not radar, and radar use is Rule 7(b) (LEGATA.014).
- `COLREG.Rule5/Sonar` encoded a requirement COLREG does not contain (LEGATA.015). If sonar
  look-out is wanted, it belongs in a MASS or site rule under its own name.

**Interpretation.** A proper look-out is a declared intent, required whenever a target is in
visible range. "Hearing" and other means are not represented.

**In the simulation.** Look-out is an intent (decided 2026-10-19). `PlannedVesselBehavior`
declares `Operation.Lookout.Sight` on every update while the vessel is underway (status none of
`ANCHORED`, `MOORED`, `FASTENED`, `AGROUND`), since its `move()` queries the vessels in range on
every update; it withdraws the intent otherwise. Behaviours not built on `PlannedVesselBehavior`
(`AnchoredVessel`, fleets) declare none.

`(OS, TS).TimeToEncounter` is the range over the closing speed (the relative velocity along the
line of sight), in seconds, and has no value when the vessels are not closing (LEGATA.004).

**Caveats.**
- Not fed, so never evaluated.
- The intent is declared whenever the behaviour runs, so it records that the query ran, not
  that a target was detected.
- The file-level condition is not compiled (LEGATA.002). Its two lines would be OR'd, and the
  second tests `Restriction`, an enum, against a string pattern.
- Both ranges are still placeholder `NumericRange (0, 10)`, now read as seconds (LEGATA.004).
- The behaviour's look-out is perfect within `range_visibility`, and it ignores visibility,
  darkness and obstruction.
- "Full appraisal of the situation" is not judged.

## Open issues

- Sourced values, in seconds, for `AlertRange` and `VisibleRange`.
- Feed the rule.
