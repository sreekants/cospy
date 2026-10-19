# COLREG Rule 10 — Traffic Separation Schemes

| | |
|---|---|
| Legata | `Rule10.legata` |
| Driver | `rules.colreg.rule10.Rule10` (`src/rules/colreg/rule10/Rule10.py`); subscribes to `vessel.crossing` and queues nothing |
| Loaded by | `rules.colreg.yaml`, entry `Rule10` |
| Simulation | Map shapes `TrafficSeparationScheme` (sea layer); lane settings in `location.yaml` `sea.tss`; `Map.in_tss()`; `VesselManeuvers.tss_avoidance`; site-generated local clauses |
| Terms | `TSS` (`OwnShip.TrafficSeparationScheme`, `TSSResolver`), `TSS.*`, `[OS, Map.Sea@TrafficSeparationScheme].Distance`, `OS.Intent`, `OS.Status`, `OS.Operation`, `OS.Length`; `clear`, `abort`, `continue` |
| Tests | none |
| Status | Not judged as COLREG. Fifteen clauses, not fed; the TSS model behind them is incomplete. Behaviours follow the lanes; local site clauses cover parts of (b)(i), (e) and (g) |
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

**Legata.** `clause['COLREG.Rule10.b.i']`: with `TSS is not empty`, four OR'd assurances:
- `OS.Position in TSS.Area`;
- `OS.Heading in TSS.SafeHeading`;
- `OS.Velocity <= TSS.SafeVelocity`;
- `(OS,TS).Distance >= TSS.SafeDistance`.

**In the simulation.** Lane direction is not enforced (`get_tss_bearing()` returns `None`). Each lane's
heading is `TSS.SafeHeading`, from `location.yaml`.

**Caveats.**
- The lines are OR'd, so any one of them passes the clause.
- The speed and distance tests are not in Rule 10(b)(i).
- Most `TSS.*` terms do not resolve.

## (b)(ii) Keep clear of separation lines and zones

**Legata.** `clause['COLREG.Rule10.b.ii']`: distance to `TSS.SeparationZone` and
`TSS.SeparationLine` above `TSS.SeparationDistance`.

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
relative to the lane in `range(87.5, 92.5)`.

**In the simulation.** `VesselActions.tss_crossing` (ferries) declares
`TrafficSeparationScheme.Crossing` for as long as the ferry is inside a scheme. A ferry is taken
to cross whatever its heading; ferries do not declare Enter or Exit.

**Caveats.**
- Any ferry movement inside a scheme counts as crossing, including one along a lane.
- The ±2.5° band is unsourced. The rule says "as nearly as practicable".

## (d) Inshore traffic zones

**Legata.**
- `Rule10.d.i`: in an inshore traffic zone, without a destination or emergency intent, only
  vessels under 20 m, sailing or fishing.
- `Rule10.d.ii`: with such an intent, `continue`.

**Caveats.**
- Sailing is tested as an `Operation`; it is a `Type`.
- No map has inshore traffic zones, and the destination and emergency intents are not raised.

## (e) Separation zones: enter only in emergency or to fish

**Legata.** `Rule10.e.i`: in the separation zone, with an emergency intent or while fishing,
`clear` (clears the findings).

**Caveats.**
- The clause only clears. Nothing asserts the prohibition itself.
- `vessel.operation` is never set.

## (f) Particular caution near terminations

**Legata.** `Rule10.f`: a condition with no assurance (a TODO).

**Caveats.** "Particular caution" is not defined.

## (g) Avoid anchoring in or near a scheme

**Legata.** `Rule10.g`: near a scheme (`AvoidRange`), assures `OS.Status not in
[Vessel.Status.ANCHORED]`.

**In the simulation.** Anchoring is a trip action that sets `Status.ANCHORED`.

**Caveats.** `Area.TrafficSeparationScheme.AvoidRange` is not declared.

## (h) Not using a scheme: avoid it by a wide margin

**Legata.** `Rule10.h`: outside `SafeRange`, assures the distance to the scheme is above
`SafeZoneClearance`.

**In the simulation.** `tss_avoidance` keeps sailing and fishing vessels out of schemes.

**Caveats.** The constants are not declared. Whether a vessel is "using" a scheme is not
modelled.

## (i) Fishing; (j) under 20 m or sailing: not to impede lane traffic

**Legata.** `Rule10.i` (fishing) and `Rule10.j` (length under 20 m): assure a distance to the
target above `SafeSmallVesselClearance` or `TSS.SmallVessel.SafeDistance`.

**Caveats.**
- (j) omits sailing vessels.
- "Impeding" is reduced to a distance.
- `TS` is used without the lane-following test.
- The constants are not declared.

## (k) Restricted vessel maintaining safety; (l) restricted vessel laying or servicing a cable

**Legata.** `Rule10.k` and `Rule10.l`: a restricted vessel engaged in `SAFETY` or `SERVICE`,
`clear` and `abort`.

**Caveats.**
- `Status.RESTRICTED` is never set (REQ.059-03).

## Open issues

- A TSS model: lanes with direction, separation zones and lines, entry and exit zones, and
  inshore zones. Then terms for each (COS.022 follow-up).
- Feed by zone, as the local rules do. Then decide how the local clauses and these clauses
  share (b)(i), (e) and (g).
- Join the OR'd (b)(i) lines with `and`.
