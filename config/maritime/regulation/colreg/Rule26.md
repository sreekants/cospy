# COLREG Rule 26 — Fishing Vessels

| | |
|---|---|
| Legata | `Rule26.legata` (status TODO; no clause) |
| Driver | `rules.colreg.rule26.Rule26` (`src/rules/colreg/rule26/Rule26.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule26` |
| Simulation | `FishingVessel` behaviour (sets `vessel.operation`); `VesselSignals`; ship model `fishing.gear` |
| Tests | none |
| Status | Not judged. Text only. `VesselSignals` shows (b) or (c) for fishing vessels. REQ.057 (REQ-057-03, open) adds the clauses |
| Reviewed | 2026-10-19 |

## How the rule is employed

**A fishing vessel** is a vessel whose `operation` is `Operation.FISHING` (Rule 3(d)). The
`FishingVessel` behaviour sets it from its `mode` every tick (REQ-059-02): `FISHING` while a
`fishing(...)` trip action runs or `ioctl('operation.fishing')` is on, and `TRANSPORT` otherwise.

**Lights and shapes** are names in the `signal` set (see Rule 20). The fishing lights and the
cones are added by REQ-056-01: `Light.Allround.GreenWhite` (trawling), `Light.Allround.RedWhite`
(other fishing), `Shape.Cones.ApexTogether`.

## File-level condition

**Legata.** `OS.Operation has 'Vessel.Operation.FISHING'`.

**Caveats.** Not compiled (LEGATA.002). There is no clause for it to scope.

## (a) Only the lights and shapes of this Rule

> A vessel engaged in fishing, whether underway or at anchor, shall exhibit only the lights and shapes
> prescribed in this Rule.

**Legata.** None.

**In the simulation.** Fishing outranks anchored, so a vessel fishing at anchor shows only the
fishing signals, not the anchor light or ball. `VesselSignals` lowers every other `Light.*` and
`Shape.*` name, so "only" holds by construction.

**Caveats.** "Only" would need a test that no other status lights are shown. `NuisanceExaminer`
covers only `encounter` and fog signals.

## (b) Trawling

> A vessel when engaged in trawling … shall exhibit: (i) two all-round lights in a vertical line, the
> upper being green and the lower white, or a shape consisting of two cones with their apexes together
> in a vertical line one above the other; (ii) a masthead light abaft of and higher than the all-round
> green light; a vessel of less than 50 metres in length shall not be obliged to exhibit such a light
> but may do so; (iii) when making way through the water, in addition to the lights prescribed in this
> paragraph, sidelights and a sternlight.

**Legata.** None. REQ-057-03 plans it.

**In the simulation.** `VesselSignals` shows (b) for a vessel whose `Operation` is `FISHING` and
whose ship model has `fishing.gear: trawl`: `Light.Allround.GreenWhite`, `Light.Masthead.Abaft` at
50 m or more only, sidelights and a sternlight when making way, and `Shape.Cones.ApexTogether` by
day. Status outranks fishing in one order: aground, not under command and restricted show their own
signals; a vessel fishing at anchor shows the fishing signals (Rule 35(d)).

**Caveats.**
- Trawling and other fishing share one `Operation.FISHING`; the ship model's `fishing.gear`
  (`trawl` or `other`, default `other`) chooses (b) or (c), so every vessel of a model fishes alike.
- "Making way" has a constant, `Vessel.MakingWay.Speed` (0.25), declared in `definitions.s3db`
  and unsourced.

## (c) Fishing other than trawling

> A vessel engaged in fishing, other than trawling, shall exhibit: (i) two all-round lights in a
> vertical line, the upper being red and the lower white, or a shape consisting of two cones with apexes
> together in a vertical line one above the other; (ii) when there is outlying gear extending more than
> 150 metres horizontally from the vessel, an all-round white light or a cone apex upwards in the
> direction of the gear; (iii) when making way through the water, in addition to the lights prescribed
> in this paragraph, sidelights and a sternlight.

**Legata.** None. REQ-057-03 plans it.

**In the simulation.** The default for `fishing.gear`: `Light.Allround.RedWhite`, sidelights and a
sternlight when making way, and `Shape.Cones.ApexTogether` by day. `FishingVessel` sets
`Operation.FISHING` while a `fishing(...)` trip action runs or `ioctl('operation.fishing')` is in
effect.

**Caveats.** Outlying gear is not modelled, so (c)(ii) is neither shown nor judged.

## (d) Annex II; (e) not engaged in fishing

> (d) The additional signals described in Annex II to these Regulations apply to a vessel engaged in
> fishing in close proximity to other vessels engaged in fishing. (e) A vessel when not engaged in
> fishing shall not exhibit the lights or shapes prescribed in this Rule, but only those prescribed for
> a vessel of her length.

**Legata.** None.

**In the simulation.** When the fishing walk ends the operation returns to `TRANSPORT` and the
next tick replaces the fishing signals with the power-driven ones, so (e) holds by construction.

**Caveats.**
- Annex II is out of scope.
- (e) needs the same "only" test as (a).

## Open issues

- REQ-057-03: clauses for (b) and (c), choosing between them by `fishing.gear`.
- Outlying gear, (c)(ii).
- Gear per trip rather than per ship model.
