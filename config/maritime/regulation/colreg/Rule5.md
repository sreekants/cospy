# COLREG Rule 5 — Look-out

| | |
|---|---|
| Legata | `Rule5.legata` |
| Driver | `rules.colreg.rule5.Rule5` (`src/rules/colreg/rule5/Rule5.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule5` |
| Terms | `(OS, TS).Distance`, `OS.Intent`, `OS.Restriction`; constants `Vessel.Collision.TimeToEncounter.{AlertRange, VisibleRange, RadioRange, SonarRange}` |
| Tests | none |
| Status | Not judged. Three clauses, not fed; their intents are never raised |
| Reviewed | 2026-10-19 |

## How the rule is employed

**In Legata.** Rule 5 is written as three clauses, one per means of look-out (sight, radar,
sonar). Each assures that own ship has declared a look-out intent while a target is in the
range of that means. The driver feeds nothing, so none is evaluated.

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
  - `(OS, TS).Distance in Vessel.Collision.TimeToEncounter.AlertRange`;
  - `OS.Restriction in ['COLREG.Rule5.*']`.
- `clause['COLREG.Rule5/Sight']`: within `VisibleRange`, assures `OS.Intent has
  'Operation.Lookout.*'`.
- `clause['COLREG.Rule5/Radar']`: within `RadioRange`, assures `OS.Intent has
  'Operation.Lookout.Radio*'`.
- `clause['COLREG.Rule5/Sonar']`: within `SonarRange`, assures `OS.Intent has
  'Operation.Lookout.Sonar*'`.

**Interpretation.** A proper look-out is a declared intent per means, required whenever a target
is within that means' range. "Hearing" is not represented.

**In the simulation.** See above: look-out is implicit in each behaviour's nearest-vessel query.

**Caveats.**
- Not fed, so never evaluated.
- No behaviour raises an `Operation.Lookout.*` intent, so once fed every clause would fail for
  every vessel (COS.041).
- The file-level condition is not compiled (LEGATA.002). Its two lines would be OR'd, and the
  second tests `Restriction`, an enum, against a string pattern.
- All ranges are placeholder `NumericRange (0, 10)` compared with metres.
- The behaviour's look-out is perfect within `range_visibility`, and it ignores visibility,
  darkness and obstruction.
- "Full appraisal of the situation" is not judged.

## Open issues

- Decide whether look-out is judged at all, given that the simulation's look-out is perfect. If
  it is, the behaviours must raise look-out intents, which needs declarable intents (COS.041).
- Fix the constant names and give them sourced values.
