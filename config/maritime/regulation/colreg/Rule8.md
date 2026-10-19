# COLREG Rule 8 — Action to Avoid Collision

| | |
|---|---|
| Legata | `Rule8.legata` |
| Driver | `rules.colreg.rule8.Rule8` (`src/rules/colreg/rule8/Rule8.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule8` |
| Simulation | `maritime.behavior.vessels.VesselManeuvers` (avoiding action), `Classification`, `EncounterWatch` |
| Terms | `OS.Intent`, `(OS, TS).Distance`, `(OS, TS).Visible`, `(OS, TS).TimeToEncounter`, `(OS, TS).TimeToClosestApproachPoint`, `OS.AngularVelocity`, `OS.Acceleration`, `OS.MinimumSafe*`; constants `Vessel.Collision.TimeToEncounter.*`, `Vessel.Reaction.AmpleTime` |
| Tests | none |
| Status | Not judged. Six clauses on intents and course or speed change, not fed; the outcome, passing at a safe distance, is judged per encounter by Rules 12–15 and 18 |
| Reviewed | 2026-10-19 |

## How the rule is employed

**Avoiding action in the simulation.** Vessels take action through their behaviour's chain of
manoeuvres (`VesselManeuvers`), applied every movement tick:

- `crossing_slowdown` and `restore_speed` (ferries, yachts, motorboats, sailing vessels): scale
  speed in proportion to the distance to the nearest vessel when it is closer than
  `crossing_fore_min` (ahead) or `crossing_aft_min` (astern), then restore speed gradually.
- `overtaking_distance`: slows when closer than `overtake_lat_min` to a vessel ahead, or
  `tss_min_dist` otherwise.
- `stop_for_safety` (container ships): drops to 5 % speed with any vessel within
  `range_ample_time`, and raises the intent `Speed.SlowdownForTraffic`.
- `fishing_slowdown` (fishing vessels): keeps clear of other vessels' aft.
- `apply_momentum`: blends towards the target velocity with `physics.momentum`, and clamps the
  turn rate to `max_yaw_rate`.

Avoiding action is therefore a speed reduction. No behaviour alters course to avoid
collision: `steer_crossing` and `steer_overtaking` return the velocity unchanged.

**Judgement.** The outcome of Rule 8(d), passing at a safe distance, is judged once per
encounter by the fed encounter rules: `(OS, TS).Distance >= Vessel.Collision.PassingDistance`
(100 m) at the closest approach, in Rules 12, 13, 15 and 18. The Legata clauses of Rule 8 are
never fed.

## File-level condition

**Legata.** `(OS.COLREG.Mode is true) and ((OS, TS).TimeToEncounter in
Vessel.Collision.TimeToEncounter.SituationRange)`.

**Caveats.** Not compiled (LEGATA.002). `OS.COLREG.Mode` is never set, and `SituationRange` is a
placeholder `(0, 10)`.

**TimeToEncounter (2026-10-19).** Every Rule 8 clause compares `(OS, TS).TimeToEncounter`, the
range over the closing speed in seconds, with the `TimeToEncounter` ranges, by `in` or `not in`.
They compared the distance in metres, and `<` or `>` against a range raised (LEGATA.004). The
ranges are still placeholders.

## (a) Positive, in ample time, good seamanship

> Any action to avoid collision shall be taken in accordance with the Rules of this Part and shall, if
> the circumstances of the case admit, be positive, made in ample time and with due regard to the
> observance of good seamanship.

**Legata.** `clause['COLREG.Rule8.a/COLAV']`: within `AlertRange`, assures both
`OS.Intent has 'Manouever.CollisionAvoidance.*'` and `(OS,TS).TimeToClosestApproachPoint >
Vessel.Reaction.AmpleTime` (assurance lines are AND'd).

**Caveats.**
- Only `Decelerate` is raised, by container ships and ferries (see (e)); no course alteration
  intent is.
- `TimeToClosestApproachPoint` is not a term (it is `TCPA`), and `Vessel.Reaction.AmpleTime` is
  not declared.
- When action began is not recorded, so "ample time" cannot be judged (COS.041).

## (b) Readily apparent alterations; no succession of small ones

> Any alteration of course and/or speed to avoid collision, shall, if the circumstances of the case
> admit, be large enough to be readily apparent to another vessel observing visually or by radar; a
> succession of small alterations of course and/or speed should be avoided.

**Legata.** `clause['COLREG.Rule8.b/CourseAlteration']`:
- **condition:** in sight, or within `RadioRange`;
- **excluded:** no turn or no acceleration;
- **assured:** `OS.AngularVelocity > OS.MinimumSafeAngularVelocity` and `OS.Acceleration >
  OS.MinimumSafeAcceleration`, both (assurance lines are AND'd).

**In the simulation.** Speed changes come in proportional, gradual steps, which is a succession
of small alterations by construction.

**Caveats.**
- `AngularVelocity` and the `MinimumSafe*` terms do not resolve.
- An alteration is judged as an instantaneous rate, not as the total change over the manoeuvre.
- Speed reductions have `Acceleration < 0`, so they are excluded.

## (c) Course alteration alone, in good time, substantial

> If there is sufficient sea room, alteration of course alone may be the most effective action to
> avoid a close-quarters situation provided that it is made in good time, is substantial and does not
> result in another close-quarters situation.

**Legata.** `clause['COLREG.Rule8.c/CourseAlteration']`: beyond `SituationRange`, assures `OS.Intent
has 'Manouever.CollisionAvoidance.CloseQuarterAvoidance'`.

**Caveats.**
- This is a permission ("may be"), not a duty, so asserting an intent overstates it.
- No behaviour alters course to avoid collision.
- Sea room is not modelled.

## (d) Pass at a safe distance; check until past and clear

> Action taken to avoid collision with another vessel shall be such as to result in passing at a safe
> distance. The effectiveness of the action shall be carefully checked until the other vessel is
> finally past and clear.

**Legata.** `clause['COLREG.Rule8.d/CourseAlteration']`: the same clause as (c).

**In the simulation.** Judged by the outcome in the encounter rules, as described above:
- Rule 13: the overtaking vessel;
- Rule 15: the give-way vessel when crossing;
- Rules 12 and 18: the vessel that must keep out of the way.

**Caveats.**
- The safe distance is a constant, 100 m (`Vessel.Collision.PassingDistance`), for every vessel
  size and every place.
- "Carefully checked until past and clear" is not judged.
- The (d) clause in the file duplicates (c) and tests an intent.

## (e) Slacken speed or take all way off

> If necessary to avoid collision or allow more time to assess the situation, a vessel shall slacken
> her speed or take all way off by stopping or reversing her means of propulsion.

**Legata.** `clause['COLREG.Rule8.e/Halting']`: within `AlertRange`, assures
`OS.Intent has 'Manouever.CollisionAvoidance.Decelerate'` or `OS.Acceleration <= 0`.

**In the simulation.** The main form of avoiding action (see above). Rule 19(e) judges a speed
reduction in restricted visibility.

`VesselActions.collision_avoidance` (container ships, ferries) declares
`Manouever.CollisionAvoidance.Decelerate` while the behaviour is slowing for another vessel, and
resets it once clear. Slowing means that a separation step the behaviour runs
(`overtaking_distance`, `crossing_slowdown`) is scaling speed below 1, or that `stop_for_safety`
holds `Speed.SlowdownForTraffic`. The intent records the cause, not a measured deceleration: it
stays while the vessel holds a reduced speed.

**Caveats.**
- `OS.Acceleration <= 0` also holds for a vessel at constant speed, so the clause would pass
  without any action.
- "If necessary" is not decided.

## (f) Not to impede

> (i) A vessel which, by any of these Rules, is required not to impede the passage or safe passage of
> another vessel shall, when required by the circumstances of the case, take early action to allow
> sufficient sea room for the safe passage of the other vessel. (ii) A vessel required not to impede
> the passage or safe passage of another vessel is not relieved of this obligation if approaching the
> other vessel so as to involve risk of collision and shall, when taking action, have full regard to
> the action which may be required by the Rules of this part. (iii) A vessel the passage of which is
> not to be impeded remains fully obliged to comply with the rules of this part when the two vessels
> are approaching one another so as to involve risk of collision.

**Legata.** `clause['COLREG.Rule8.f/GiveWayOnPassage']`: the same test as (e).

**Caveats.**
- The clause does not test who must not impede (Rules 9(b)–(d), 10(i)–(j), 18(d)).
- "Impeding" is not defined.

## Open issues

- A course- and speed-change term over the approach (COS.041). It would let (a) "ample time",
  (b) "readily apparent" and (c) be judged on behaviour, not intents.
- Course-alteration manoeuvres: no behaviour turns to avoid collision.
- A safe passing distance scaled by vessel size or place.
- The undeclared terms and constants listed above.
