# COLREG Rule 9 — Narrow Channels

| | |
|---|---|
| Legata | `Rule9.legata` |
| Driver | `rules.colreg.rule9.Rule9` (`src/rules/colreg/rule9/Rule9.py`); subscribes to `vessel.overtaken`, `vessel.overtaking` and `vessel.crossing`, prints them, and queues nothing |
| Loaded by | `rules.colreg.yaml`, entry `Rule9` |
| Simulation | Map sea shapes; `LaneDisciplineExaminer` and `SpeedExaminer` (zone rules in `examiner/zones.yaml`) |
| Terms | `OS.Position.Territory`, `[OS.Position, Map.Sea@ShoreLine].MinDistance` and `.Curvature`, `[OS, Map.Sea@TrafficSeparationScheme].Distance`, `OS.Length`, `OS.Type`, `OS.Operation`, `OS.Status`, `OS.Intent`, `OS.Signal.ON` |
| Tests | none |
| Status | Not judged. Nine clauses, not fed; the territory term cannot see a channel |
| Reviewed | 2026-10-19 |

## How the rule is employed

**In Legata.** The duties of Rule 9 are written as clauses scoped by
`OS.Position.Territory` (narrow channel, fairway, harbour, inland waterway). The Rule 34 signals
of (e) and (f) are tested directly in `OS.Signal.ON`. The driver listens to the encounter events
but queues nothing, so no clause is evaluated.

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
- `TS` was used but not declared until 2026-10-19.
- "Can safely navigate only within the channel" is not tested.
- `Sea.NarrowChannel.SafeDistance` is not declared.

## (c) Fishing vessels shall not impede

> A vessel engaged in fishing shall not impede the passage of any other vessel navigating within a
> narrow channel or fairway.

**Legata.** `clause['COLREG.Rule9.c/Fishing']`: when `OS.Operation is Vessel.Operation.Fishing`,
assures the same distance as (b). The test was a quoted string until 2026-10-19 and never matched
(LEGATA.033).

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

**Legata.** Three clauses, each on an intent, each assuring the Rule 34 whistle signal in
`OS.Signal.ON`:
- `Rule9.e.i.a`: overtaking → `Sound.Blast.Prolonged.2x.Short.1x` or `.Short.2x` (34(c)(i),
  starboard or port side);
- `Rule9.e.i.b`: overtaken → `Sound.Blast.ProlongedShort.2x` (34(c)(ii), agreement);
- `Rule9.e.i.c`: refusing the overtake (`Manouever.DenyOvertake.*`) → `Sound.Blast.Short.5x`
  (34(d)).

Until 2026-10-19 each used `apply` on Rule 34 clauses that do not exist, and (b) named the
overtaking signal; `apply` did nothing (LEGATA.034–036). (e)(ii) is met by Rule 13, which is fed
for every overtaking encounter; its `apply 'COLREG.Rule13.*'` clause was removed (LEGATA.037).

**In the simulation.** Overtaking is detected by encounter classification (`OTGW`, `OTSO`).
Rule 13 judges it everywhere, channel or not.

**Caveats.**
- No behaviour raises `Manouever.Overtaking.*`, `.Overtaken.*` or `.DenyOvertake.*` intents.
  Classification is not an intent. The conditions should be an overtaking encounter in a channel.
- "Only if the vessel to be overtaken has to take action" is not tested.
- No behaviour sounds a Rule 34 signal (Rule 34).

## (f) Bends and obscured areas

> A vessel nearing a bend or an area of a narrow channel or fairway where other vessels may be obscured
> by an intervening obstruction shall navigate with particular alertness and caution and shall sound
> the appropriate signal prescribed in Rule 34(e).

**Legata.** `clause['COLREG.Rule9.f/TurningBlindspot']`: when `[OS.Position,
Map.Sea@ShoreLine].Curvature > 20`, assures `OS.Signal.ON has 'Sound.Blast.Prolonged.1x'` (the
34(e) prolonged blast). The assurance tested an intent named `Signal` until 2026-10-19
(LEGATA.038).

**Caveats.**
- `Curvature` is not a term, and the threshold has no unit.
- Obstruction is not modelled.

## (g) Avoid anchoring in a narrow channel

> Any vessel shall, if the circumstances of the case admit, avoid anchoring in a narrow channel.

**Legata.** `clause['COLREG.Rule9.g/Anchor']`: in a narrow channel, assures `OS.Status not in
[Vessel.Status.ANCHORED]`. It tested an anchoring intent until 2026-10-19 (LEGATA.039).

**In the simulation.** Anchoring is a trip action. It sets `Status.ANCHORED`.

**Caveats.** No territory is ever a narrow channel.

## Open issues

- A territory or zone term that identifies narrow channels and fairways from the map. The local
  zone rules already name shapes, so Rule 9 could be fed by zone, as the local rules are
  (COLREG.COVERAGE).
- Channel limits, for (a).
- A channel-crossing model, for (d).
- Overtaking-in-a-channel conditions for (e)(i), in place of the intents.
