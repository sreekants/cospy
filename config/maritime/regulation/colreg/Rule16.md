# COLREG Rule 16 — Action by Give-way Vessel

| | |
|---|---|
| Legata | `Rule16.legata` (status TODO; no clause) |
| Driver | `rules.colreg.rule16.Rule16` (`src/rules/colreg/rule16/Rule16.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule16` |
| Simulation | `VesselManeuvers` (speed-based separation); give-way roles from `Classification` |
| Tests | none |
| Status | Not judged. The outcome, keeping clear, is judged by Rules 12, 13, 15 and 18; "early and substantial" needs a course-change term |
| Reviewed | 2026-10-19 |

## How the rule is employed

**Who gives way.** The give-way vessel is known from encounter classification:
- `OTGW`, overtaking: Rule 13;
- `CRGW`, crossing: Rule 15;
- the keep-out-of-the-way clauses of Rules 12 and 18.

**What the simulation does.** Give-way vessels slow in proportion to proximity
(`crossing_slowdown`, `overtaking_distance`, `stop_for_safety`). They do not alter course.

**What is judged.** Only the outcome, by the rule that gives the duty: passing at
`Vessel.Collision.PassingDistance` (100 m) or more at the closest approach. Whether the action
was *early* and *substantial* is not judged.

## Rule 16

> Every vessel which is directed to keep out of the way of another vessel shall, so far as possible,
> take early and substantial action to keep well clear.

**Legata.** None.

**Interpretation needed.**
- *Early:* when the action began, relative to the onset of the encounter.
- *Substantial:* the size of the change in course or speed.
- *Well clear:* a passing distance above the minimum.

**Caveats.**
- No term measures a course or speed change over an approach (COS.041). The run had 493 give-way
  encounters, none judged under Rule 16.
- Proportional speed changes are gradual by construction. Judged on its own terms, Rule 16 would
  find most give-way action not substantial.

## Open issues

- A course- and speed-change term over the approach (COS.041), then clauses for early,
  substantial and well clear, judged once per give-way encounter with the onset recorded as in
  Rule 12.
- Sourced thresholds for "early" and "substantial".
