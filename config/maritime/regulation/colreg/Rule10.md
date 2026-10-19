# COLREG Rule 10 — Traffic Separation Schemes

| | |
|---|---|
| Legata | `Rule10.legata` |
| Driver | `rules.colreg.rule10.Rule10` (`src/rules/colreg/rule10/Rule10.py`); subscribes to `vessel.crossing` and queues nothing |
| Loaded by | `rules.colreg.yaml`, entry `Rule10` |
| Simulation | Map shapes `TrafficSeparationScheme` (sea layer); lane settings in `location.yaml` `sea.tss`; `Map.in_tss()`; `VesselManeuvers.tss_avoidance`; site-generated local clauses |
| Terms | `TSS` (`OwnShip.TrafficSeparationScheme`, `TSSResolver`), `TSS.*`, `[OS, Map.Sea@TrafficSeparationScheme].Distance`, `OS.Intent`, `OS.Status`, `OS.Operation`, `OS.Length`, `OS.Type`, `TS.Type`; `continue` |
| Tests | none |
| Status | Not judged as COLREG. Thirteen clauses, not fed; the TSS model behind them is incomplete. Behaviours follow the lanes; local site clauses cover parts of (b)(i), (e) and (g) |
| Reviewed | 2026-10-19 |

## How the rule is employed

**In the simulation.** Traffic separation schemes are map shapes. Vessel behaviours use them in
two ways:

- `tss_compliance` (container ships, ferries, yachts, motorboats) would turn the heading towards
  the lane bearing when it is off by more than `behavior.tss_angle_tol` (30°). It never does:
  `Map.get_tss_bearing()` is a stub that returns `None`, so lane direction is not enforced.
- `tss_avoidance` (sailing and fishing vessels): a vessel that drifts into a scheme is put back
  where it was and given a random new heading. These vessels keep out of schemes by
  construction.

**Local clauses.** Site-generated local rules (60 clauses at 5 sites) cover parts of (b)(i),
(e) and (g) as zone clauses. As committed they cannot run: their zone keys are empty and shapes
are missing (COLREG.COVERAGE).

**Lane settings.** Each location's `location.yaml` holds them under `sea.tss`: a default
`safe_distance`, an optional `separation_distance`, and per lane its `safe_heading`. Map databases
hold no zone settings. `ZoneResolver` reads them through `Location.lane()` as `TSS.SafeDistance`,
`TSS.SafeHeading` and `TSS.SeparationDistance`, each 0 when the location sets none.

**In Legata.** The clauses assume a full TSS model: lanes, separation zones and lines, entry and
exit zones, safe headings and speeds. The resolver provides about 5 of the roughly 12 properties
used. The driver queues nothing.

## (a) Application

> This Rule applies to traffic separation schemes adopted by the Organization and does not relieve
> any vessel of her obligation under any other rule.

**Legata.** File-level condition, two OR'd lines: `[OS, Map.Sea@TrafficSeparationScheme].Distance
in Area.ProximityRange`, or `OS.Restriction in ['COLREG.Rule10.*']`.

**Caveats.**
- Not compiled (LEGATA.002).
- `Area.ProximityRange` is not declared.
- Whether a scheme is IMO-adopted is not recorded.

## (b)(i) Proceed in the lane, in the direction of flow

**Legata.** `clause['COLREG.Rule10.b.i']`: with `TSS is not empty`, assures both
`OS.Position in TSS.Area` and `OS.Heading in TSS.SafeHeading` (assurance lines are AND'd). A
restricted vessel on a `SAFETY` or `SERVICE` operation is excluded ((k), (l)). The speed and
separation lines were removed on 2026-10-19: they are not in Rule 10(b)(i) (LEGATA.040).

**In the simulation.** Lane direction is not enforced (`get_tss_bearing()` returns `None`). Each lane's
heading is `TSS.SafeHeading`, from `location.yaml`.

**Caveats.** Most `TSS.*` terms do not resolve (LEGATA.007).

## (b)(ii) Keep clear of separation lines and zones

**Legata.** `clause['COLREG.Rule10.b.ii']`: distance to `TSS.SeparationZone` and
`TSS.SeparationLine` above `TSS.SeparationDistance`. The (k) and (l) exclusions apply.

**Interpretation.** The clearance is per location, optionally per lane, from `location.yaml`
`sea.tss.separation_distance`.

**Caveats.**
- No location sets a separation distance, so the term is 0 and the clause holds trivially.
- Separation zones are shapes (305000) in some maps. Separation lines are not shapes, and
  `TSS.SeparationZone` and `TSS.SeparationLine` are not terms.

## (b)(iii) Join and leave at the termination, or at a small angle

**Legata.** `Rule10.b.iii/EnterTrafficSeparationScheme` and `/ExitTrafficSeparationScheme`: on the
intents `TrafficSeparationScheme.Enter` and `.Exit`, near the entry or exit zone, with the
heading in `TSS.SafeZone.EntryHeading` or `ExitHeading`.

**In the simulation.** `VesselActions.tss_lane` (container ships) declares
`TrafficSeparationScheme.Enter` on a leg that starts outside a scheme and whose next waypoint is
inside one, and `.Exit` on a leg from inside to a waypoint outside. Inside is `Map.in_tss()` on
the vessel's rectangle, now and moved to the next waypoint; the path between is not tested. A
leg that passes through a scheme between two waypoints outside it declares neither. Without a
next waypoint neither is declared.

**Caveats.** Entry and exit zones are not modelled.

## (c) Avoid crossing lanes; cross at right angles

**Legata.** `clause['COLREG.Rule10.c']`: on the intent `TrafficSeparationScheme.Crossing`, heading
relative to the lane in `range(87.5, 92.5)`. An exit-zone distance line, unrelated to crossing,
was removed on 2026-10-19 (LEGATA.041). `abs()` and `range()` evaluate since the same date
(LEGATA.005, LEGATA.006).

**In the simulation.** `VesselActions.tss_crossing` (ferries) declares
`TrafficSeparationScheme.Crossing` for as long as the ferry is inside a scheme. A ferry is taken
to cross whatever its heading; ferries do not declare Enter or Exit.

**Caveats.**
- Any ferry movement inside a scheme counts as crossing, including one along a lane.
- The ±2.5° band is unsourced. The rule says "as nearly as practicable".

## (d) Inshore traffic zones

**Legata.**
- `Rule10.d.i`: in an inshore traffic zone, without a destination or emergency intent, only
  vessels under 20 m (`OS.Length < 20`), sailing (`OS.Type`) or fishing (`OS.Operation`). The
  length and sailing tests could never match until 2026-10-19 (LEGATA.042).
- `Rule10.d.ii`: with such an intent, `continue`.

**Caveats.**
- "When she can safely use the appropriate traffic lane" is not tested.
- No map has inshore traffic zones, and the destination and emergency intents are not raised.

## (e) Separation zones: enter only in emergency or to fish

**Legata.** `clause['COLREG.Rule10.e']`: in a scheme, assures `OS.Position not in
TSS.SeparationZone`, excluding a vessel crossing, joining or leaving (the TSS intents), one with
an emergency intent, one engaged in fishing, and the (k) and (l) operations. It replaced
`Rule10.e.i` on 2026-10-19, which only granted the exceptions with a `clear` that did nothing
(LEGATA.043).

**Caveats.**
- Crossing a separation line is not tested: lines are not shapes.
- `TSS.SeparationZone` is not a term (LEGATA.007).

## (f) Particular caution near terminations

**Legata.** `Rule10.f`: a condition with no assurance (a TODO).

**Caveats.** "Particular caution" is not defined.

## (g) Avoid anchoring in or near a scheme

**Legata.** `Rule10.g`: near a scheme (`AvoidRange`), assures `OS.Status not in
[Vessel.Status.ANCHORED]`.

**In the simulation.** Anchoring is a trip action that sets `Status.ANCHORED`.

**Caveats.** `Area.TrafficSeparationScheme.AvoidRange` is not declared.

## (h) Not using a scheme: avoid it by a wide margin

**Legata.** `Rule10.h`: a vessel outside a scheme and not declaring
`TrafficSeparationScheme.Enter` keeps the distance to the scheme above `SafeZoneClearance`. Until
2026-10-19 it tested the distance only once the vessel was already outside the range, so it could
not fail (LEGATA.045).

**In the simulation.** `tss_avoidance` keeps sailing and fishing vessels out of schemes.

**Caveats.**
- The constants are not declared.
- "Using" a scheme is read as being in it or declaring entry. "Near it" is not tested, so the
  margin applies at any distance; it holds trivially far away.

## (i) Fishing; (j) under 20 m or sailing: not to impede lane traffic

**Legata.** `Rule10.i` (`OS.Operation is Vessel.Operation.Fishing`) and `Rule10.j` (under 20 m or
sailing, towards a power-driven target): assure a distance to the target above
`SafeSmallVesselClearance` and `TSS.SmallVessel.SafeDistance`. On 2026-10-19 (i)'s fishing test
became a constant, and (j) gained sailing vessels, the power-driven target and a length test that
matches (LEGATA.046, LEGATA.047).

**Caveats.**
- "Impeding" is reduced to a distance.
- The target is not tested for following a lane.
- The constants are not declared.

## (k) Restricted vessel maintaining safety; (l) restricted vessel laying or servicing a cable

**Legata.** No clause of their own since 2026-10-19. A restricted vessel engaged in a `SAFETY` or
`SERVICE` operation is excluded from (b)(i), (b)(ii) and (e): lane direction and separation zones,
"to the extent necessary". The former clauses used `clear` and `abort`, which did nothing, and
quoted strings that never matched (LEGATA.048, LEGATA.049).

**Caveats.**
- `Status.RESTRICTED` is never set (REQ.059-03).
- `SERVICE` covers navigation marks and pipelines too, not only cables.

## Open issues

- A TSS model: lanes with direction, separation zones and lines, entry and exit zones, and
  inshore zones. Then terms for each (COS.022 follow-up).
- Feed by zone, as the local rules do. Then decide how the local clauses and these clauses
  share (b)(i), (e) and (g).
