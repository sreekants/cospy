# COLREG Rule 6 — Safe Speed

| | |
|---|---|
| Legata | `Rule6.legata` (header comment says `COLREG.Rule2`) |
| Driver | `rules.colreg.rule6.Rule6` (`src/rules/colreg/rule6/Rule6.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule6` |
| Terms | `OS.Visibility`, `OS.COLREG.Mode`, `OS.COLREG.Manoeuvrable`, `OS.COLREG.Stoppable`, `[OS.Position, Map.Sea].Draft`; API `add()`, `del()`, `count()`; constants `Situation.Type.*` |
| Tests | none |
| Status | Not judged. Five clauses that set safe-speed factors, not fed; safe speed in restricted visibility is judged by Rule 19(b) |
| Reviewed | 2026-10-19 |

## How the rule is employed

**In Legata.** Rule 6 lists the factors a safe speed must account for. It sets no limit. The
file turns five factors into flags: when a factor holds, the clause adds it to the set
`COLREG.SafeSpeed` on own ship, and `otherwise:` removes it. Another rule could then read the set.
Nothing reads it, and the driver feeds nothing.

**In the simulation.** Speed is governed by vessel behaviour and by zone limits:

- `VesselManeuvers.stop_for_safety` (container ships): with any vessel within
  `behavior.range_ample_time`, the speed drops to 5 % and the vessel raises the intent
  `Speed.SlowdownForTraffic`.
- `crossing_slowdown`, `overtaking_distance` and `fishing_slowdown` scale speed down in
  proportion to the distance to the nearest vessel, below the ship model's separation
  thresholds.
- `SpeedExaminer` scores speed over a zone's `speed_limit` (`examiner/zones.yaml`).
- Rule 19(b) judges a safe speed in restricted visibility: own ship must stop within half the
  visibility.

## Rule 6, opening

> Every vessel shall at all times proceed at a safe speed so that she can take proper and effective
> action to avoid collision and be stopped within a distance appropriate to the prevailing
> circumstances and conditions. In determining a safe speed the following factors shall be among
> those taken into account:

**Legata.** File-level condition `OS.COLREG.Mode is true`: COLREG applies to own ship (as set
by the Rule 1 precedent).

**Caveats.** The file-level condition is not compiled (LEGATA.002), and the Rule 1 mark is never
set.

## (a)(i) The state of visibility

**Legata.** `clause['COLREG.Rule6.a.i/Visibility']`: when `OS.Visibility <
Situation.Type.LowVisibility`, `add(OS, 'COLREG.SafeSpeed', 'LowVisibility')`; otherwise `del`.

**Caveats.**
- `OS.Visibility` is not a vessel term (it is `(OS, TS).Visibility`).
- `Situation.Type.LowVisibility` is not declared.
- Rule 19(b) covers restricted visibility directly.

## (a)(ii) Traffic density

**Legata.** `clause['COLREG.Rule6.a.ii/TrafficDensity']`: when `count(OS,
'COLREG.Vessels.Visible') > Situation.Type.HighTrafficDensity`, add `HighTrafficDensity`;
otherwise `del`.

**Caveats.**
- `count()` has no API entry and would raise.
- `COLREG.Vessels.Visible` is filled by the Rule 11 precedent, which only adds (LEGATA.001).
- `Situation.Type.HighTrafficDensity` is not declared.

## (a)(iii) Manoeuvrability: stopping distance and turning ability

**Legata.** `clause['COLREG.Rule6.a.iii/Manoeuverability']`: when `OS.COLREG.Manoeuvrable is
false` or `OS.COLREG.Stoppable is false` (OR'd lines), add `LowManoeuevrability`; otherwise `del`.

**In the simulation.** Turning is bounded by `maneuverability.max_yaw_rate` (degrees per tick)
and inertia by `physics.momentum`. Stopping distance is modelled only in Rule 19(b), from the
IMO track-reach bound.

**Caveats.** `Manoeuvrable` and `Stoppable` are not resolver terms.

## (a)(iv) Background light at night; (a)(v) wind, sea, current and hazards

**Legata.** None.

**In the simulation.** Wind, sea current and waves act on vessels as forces
(`WIND_CURRENT`, `SEA_CURRENT`, `SEA_WAVE`). `ExtremeWeatherExaminer` scores weather. Neither
speed nor background light is judged against them.

## (a)(vi) Draught in relation to the available depth

**Legata.** `clause['COLREG.Rule6.a.vi/DepthClearance']`: when `[OS.Position, Map.Sea].Draft <
Situation.Type.MinimumDraft`, add `LowDepth`; otherwise `del`.

**In the simulation.** Depth under the keel is `(OwnShip, Map.Sea).Depth` (`SeaResolver`).
`GroundingExaminer` and the grounding conduct handle contact with the seabed.

**Caveats.**
- `[OS.Position, Map.Sea].Draft` is not a term: depth is `Depth`, and draught is `OS.Draft`.
- `Situation.Type.MinimumDraft` is not declared.

## (b)(i)–(vi) Vessels with operational radar

**Legata.** None. The former (b)(i) clause tested water depth, a copy of (a)(vi), and was removed
(COS.053).

**Caveats.** Radar is not modelled: no vessel has radar equipment or a range scale. Judging (b)
needs radar on the ship models and a term for it.

## Open issues

- `otherwise:` is never compiled (LEGATA.001), and `add()`, `del()` and `count()` are broken.
- The `Situation.Type.*` constants are undeclared, and several terms do not exist.
- Decide whether Rule 6 should yield a speed limit, generalising Rule 19(b)'s safe speed to
  every visibility, rather than flags that nothing reads.
