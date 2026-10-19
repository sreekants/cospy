# COLREG Rule 9 — Narrow Channels

| | |
|---|---|
| Legata | `Rule9.legata` |
| Driver | `rules.colreg.rule9.Rule9` (`src/rules/colreg/rule9/Rule9.py`); subscribes to `vessel.overtaken`, `vessel.overtaking` and `vessel.crossing`, prints them, and queues nothing |
| Loaded by | `rules.colreg.yaml`, entry `Rule9` |
| Simulation | Map sea shapes; `LaneDisciplineExaminer` and `SpeedExaminer` (zone rules in `examiner/zones.yaml`) |
| Terms | `OS.Position.Territory`, `[OS.Position, Map.Sea@ShoreLine].MinDistance` and `.Curvature`, `[OS, Map.Sea@TrafficSeparationScheme].Distance`, `OS.Length`, `OS.Intent`; `apply` |
| Tests | none |
| Status | Not judged. Ten clauses, not fed; the territory term cannot see a channel |
| Reviewed | 2026-10-19 |

## How the rule is employed

**In Legata.** The duties of Rule 9 are written as clauses scoped by
`OS.Position.Territory` (narrow channel, fairway, harbour, inland waterway). Several delegate to
Rule 13 or Rule 34 with `apply`. The driver listens to the encounter events but queues nothing,
so no clause is evaluated.

**In the simulation.** Narrow-channel conduct that the simulation does have comes from zone
rules, not COLREG:
- `LaneDisciplineExaminer` scores overtaking where a zone forbids it
  (`lane.overtaking_prohibited`).
- `SpeedExaminer` scores speeding in a zone, with a heavier event when overtaking.
- Zones are map shapes, configured per site in `examiner/zones.yaml` (the Vaniköy–Kanlıca reach
  of the Istanbul Strait is the worked example).

## File-level condition

**Legata.** Three OR'd lines: near a traffic separation scheme
(`Area.ProximityRange`), in a narrow-channel territory, or
`OS.Restriction in ['COLREG.Rule9.*']`.

**Caveats.**
- Not compiled (LEGATA.002).
- `OS.Position.Territory` always resolves to `'Territory.HighSea'`, so no vessel is ever in a
  narrow channel.
- `Area.ProximityRange` is not declared.

## (a) Keep to the starboard side of the channel

> A vessel proceeding along the course of a narrow channel or fairway shall keep as near to the outer
> limit of the channel or fairway which lies on her starboard side as is safe and practicable.

**Legata.** `clause['COLREG.Rule9.a/KeepNearCoast']`: in a channel, fairway or inland waterway,
assures `[OS.Position, Map.Sea@ShoreLine].MinDistance < Sea.Shoreline.SafeDistance`. A comment
proposes 5 × the vessel's width.

**Caveats.**
- The distance is to the nearest shoreline, not to the starboard limit, so keeping to the port
  side passes too.
- `MinDistance` and `Sea.Shoreline.SafeDistance` are not defined.
- Channels have no outer limits in the maps.

## (b) Small and sailing vessels shall not impede

> A vessel of less than 20 metres in length or a sailing vessel shall not impede the passage of a
> vessel which can safely navigate only within a narrow channel or fairway.

**Legata.** `clause['COLREG.Rule9.b/SmallVessel']`: when `(OS.Length < 20) or (OS.Type is
Vessel.Type.Sailing)`, assures `(OS, TS).Distance > Sea.NarrowChannel.SafeDistance`.

**Caveats.**
- `TS` is used but not declared.
- "Can safely navigate only within the channel" is not tested.
- `Sea.NarrowChannel.SafeDistance` is not declared.

## (c) Fishing vessels shall not impede

> A vessel engaged in fishing shall not impede the passage of any other vessel navigating within a
> narrow channel or fairway.

**Legata.** `clause['COLREG.Rule9.c/Fishing']`: when `OS.Operation has
'Vessel.Operation.Fishing'`, assures the same distance as (b).

**Caveats.** Only the `FishingVessel` behaviour sets `vessel.operation`, and only while fishing
(Rule 26). The other caveats are those of (b).

## (d) Shall not cross so as to impede

> A vessel shall not cross a narrow channel or fairway if such crossing impedes the passage of a vessel
> which can safely navigate only within such channel or fairway. The latter vessel may use the sound
> signal prescribed in Rule 34(d) if in doubt as to the intention of the crossing vessel.

**Legata.** None. The former clause tested overtaking, a copy of (e)(i), and was removed (COS.054).

**Caveats.** Not judged. Crossing a channel needs channel shapes with an axis, a term for a
vessel that can navigate only within the channel, and a measure of impeding.

## (e) Overtaking that needs the other vessel's action

> (i) In a narrow channel or fairway when overtaking can take place only if the vessel to be overtaken
> has to take action to permit safe passing, the vessel intending to overtake shall indicate her
> intention by sounding the appropriate signal prescribed in Rule 34(c)(i). The vessel to be overtaken
> shall, if in agreement, sound the appropriate signal prescribed in Rule 34(c)(ii) and take steps to
> permit safe passing. If in doubt she may sound the signals prescribed in Rule 34(d). (ii) This Rule
> does not relieve the overtaking vessel of her obligation under Rule 13.

**Legata.** Four clauses, each on an intent:
- `Rule9.e.i.a`: overtaking → `apply 'COLREG.Rule34.c.i*'`;
- `Rule9.e.i.b`: overtaken → `apply 'COLREG.Rule34.c.i*'` (it should be 34(c)(ii));
- `Rule9.e.i.c`: refusing the overtake (`Manouever.DenyOvertake.*`) → `apply 'COLREG.Rule34.d*'`;
- `Rule9.e.ii`: overtaking → `apply 'COLREG.Rule13.*'`.

**In the simulation.** Overtaking is detected by encounter classification (`OTGW`, `OTSO`).
Rule 13 judges it everywhere, channel or not.

**Caveats.**
- No behaviour raises `Manouever.Overtaking.*` intents. Classification is not an intent.
- Rule 34 has no clauses, and `apply` is not known to work across rule files.
- "Only if the vessel to be overtaken has to take action" is not tested.

## (f) Bends and obscured areas

> A vessel nearing a bend or an area of a narrow channel or fairway where other vessels may be obscured
> by an intervening obstruction shall navigate with particular alertness and caution and shall sound
> the appropriate signal prescribed in Rule 34(e).

**Legata.** `clause['COLREG.Rule9.f/TurningBlindspot']`: when `[OS.Position,
Map.Sea@ShoreLine].Curvature > 20`, assures `OS.Intent in ['Signal']`.

**Caveats.**
- `Curvature` is not a term.
- The signal should be tested in `OS.Signal` (`Sound.*` from the vocabulary), not in the intent.
- Obstruction is not modelled.

## (g) Avoid anchoring in a narrow channel

> Any vessel shall, if the circumstances of the case admit, avoid anchoring in a narrow channel.

**Legata.** `clause['COLREG.Rule9.g/Anchor']`: in a narrow channel, assures `OS.Intent not in
['*Anchoring*']`.

**In the simulation.** Anchoring is a trip action. It sets `Status.ANCHORED`; it does not raise
an intent.

**Caveats.** It should test `OS.Status is Vessel.Status.ANCHORED`. No territory is ever a narrow
channel.

## Open issues

- A territory or zone term that identifies narrow channels and fairways from the map. The local
  zone rules already name shapes, so Rule 9 could be fed by zone, as the local rules are
  (COLREG.COVERAGE).
- Channel limits, for (a).
- A channel-crossing model, for (d).
- Correct (e)(i)(b), which applies 34(c)(i) where 34(c)(ii) is meant.
- Wait for Rule 34 before relying on `apply`.
