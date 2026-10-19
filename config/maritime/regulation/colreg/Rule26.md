# COLREG Rule 26 — Fishing Vessels

| | |
|---|---|
| Legata | `Rule26.legata` (status TODO; no clause) |
| Driver | `rules.colreg.rule26.Rule26` (`src/rules/colreg/rule26/Rule26.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule26` |
| Simulation | `FishingVessel` behaviour (`Operation.FISHING` as its `mode`) |
| Tests | none |
| Status | Not judged. Text only. REQ.057 (REQ-057-03, open) adds (b) and (c) |
| Reviewed | 2026-10-19 |

## How the rule is employed

**A fishing vessel** is a vessel whose `operation` is `Operation.FISHING` (Rule 3(d)). The
`FishingVessel` behaviour sets only its own `mode`, not the vessel's operation, so no vessel is
"engaged in fishing" to a rule (REQ-059-02).

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

**Caveats.**
- Trawling and other fishing are not distinguished: there is one `Operation.FISHING`. A gear
  type is needed to choose (b) or (c).
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

**Caveats.** Outlying gear is not modelled, so (c)(ii) cannot be judged.

## (d) Annex II; (e) not engaged in fishing

> (d) The additional signals described in Annex II to these Regulations apply to a vessel engaged in
> fishing in close proximity to other vessels engaged in fishing. (e) A vessel when not engaged in
> fishing shall not exhibit the lights or shapes prescribed in this Rule, but only those prescribed for
> a vessel of her length.

**Legata.** None.

**Caveats.**
- Annex II is out of scope.
- (e) needs the same "only" test as (a).

## Open issues

- REQ-059-02: set `vessel.operation` from the fishing behaviour.
- REQ-057-03: clauses for (b) and (c), and the choice between them (gear type).
- REQ.058: `VesselSignals` raises the fishing lights and shapes.
