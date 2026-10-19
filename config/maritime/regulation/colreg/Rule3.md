# COLREG Rule 3 — General Definitions

| | |
|---|---|
| Legata | `Rule3.legata` (comments only) |
| Driver | `rules.colreg.rule3.Rule3` (`src/rules/colreg/rule3/Rule3.py`); subscribes to `vessel.aground` and prints it |
| Loaded by | `rules.colreg.yaml`, entry `Rule3` |
| Definitions | `maritime.model.vessel.Vessel` (`Type`, `Operation`, `Status`, `Restriction`), vessel classes in `maritime.model.vessel`, ship models in `vehicle/ship/*.yaml` |
| Terms | `VesselResolver` (`Type`, `Status`, `Operation`, `Restriction`, `Length`, `Width`), `VesselDeclarationsResolver` (enum names), `TargetResolver` (`Visible`, `Visibility`) |
| Tests | none for the rule; the enums are exercised by the Rule 12, 13, 14, 15, 18, 19 and 35 tests |
| Status | Definitions only; nothing to judge. Each definition is a type, an enumeration or a term, described below |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 3 defines the words the other rules use. The simulation carries each definition as one of
three things:

- an **enumeration** on the vessel: `Type`, `Operation`, `Status` or `Restriction`, all `Flag`
  enums in `Vessel.py`;
- a **vessel class** built from `vessel.s3db`, by type code (`maritime.model.vessel.Builder`);
- a **resolver term** that Legata clauses read.

**Enum names in Legata.** A clause names an enum member as `Vessel.<Enum>.<Member>`, either by
the member's own name (`Vessel.Status.RESTRICTED`) or in CamelCase (`Vessel.Type.PowerDriven`).
`VesselDeclarationsResolver` resolves both to the member. Constants that are not enum members
(`Vessel.Collision.PassingDistance`, `Vessel.RestrictedVisibility.Range`) come from
`maritime/regulation/definitions.s3db`.

**Vessel classes, by type code in `vessel.s3db`:**

| Code | Class | `Type` |
|---|---|---|
| 100000 | `PowerDrivenVessel` | `POWER_DRIVEN` |
| 200000 | `SailingVessel` | `SAILING` |
| 300000 | `SeaPlane` | `SEAPLANE` |
| 400000 | `WIG` | `WIG` |
| 800000 | `Fleet` | `FLEET` (a `META_VESSEL`) |

**Operations from the trip plan.** A trip row's action sets the vessel's operation from the row's
waypoint until the next waypoint (`PlannedVesselBehavior.begin_row`), then restores the operation
it had:

| Action | `Operation` | Rule |
|---|---|---|
| `towing(tow length)` | `TOWING`, and `vessel.tow_length` in metres (the action is in map units) | 24(a) |
| `pushing` | `PUSHING` (pushing ahead) | 24(c) |
| `pilotage` | `PILOTAGE` | 29 |
| `flight` | `FLIGHT` (WIG craft taking off, landing or in flight near the surface) | 23(c) |

`FishingVessel` sets `FISHING` itself; a row operation takes precedence over it for the row.

The driver's `on_aground` handler only prints the event. It judges nothing.

## (a) Vessel

> The word 'vessel' includes every description of water craft, including non-displacement craft, WIG
> craft and seaplanes, used or capable of being used as a means of transportation on water.

**Definition.** `maritime.model.vessel.Vessel`, a `Vehicle`. Every built craft is a `Vessel`,
seaplanes and WIG craft included.

**Caveats.** A `Fleet` is a `Vessel` too (`Type.META_VESSEL`). Fleets group vessels for motion
and are not craft. `Vessel.meta()` tells them apart, and `Vessel.afloat()` leaves them out.

## (b) Power-driven vessel

> The term 'power-driven vessel' means any vessel propelled by machinery.

**Definition.** `Type.POWER_DRIVEN` (`0x00000001`), set by the class (`PowerDrivenVessel`).
Legata: `Vessel.Type.PowerDriven`.

**Caveats.** The type is fixed when the vessel is built. A sailing vessel using her engine does
not become power-driven (see (c)).

## (c) Sailing vessel

> The term 'sailing vessel' means any vessel under sail provided that propelling machinery, if
> fitted, is not being used.

**Definition.** `Type.SAILING` (`0x00000100`), set by the class (`SailingVessel`). Legata:
`Vessel.Type.Sailing`.

**Caveats.**
- "Under sail" and "machinery not being used" are not modelled. A sailing vessel is sailing for
  the whole run, and nothing changes her to power-driven when she motors.
- No sail plan is modelled (see Rule 12(b)).

## (d) Vessel engaged in fishing

> The term 'vessel engaged in fishing' means any vessel fishing with nets, lines, trawls or other
> fishing apparatus which restrict manoeuvrability, but does not include a vessel fishing with
> trolling lines or other fishing apparatus which do not restrict manoeuvrability.

**Definition.** `Operation.FISHING` (`0x00000001`) in `vessel.operation`. Legata:
`Vessel.Operation.Fishing`.

**In the simulation.** The `FishingVessel` behaviour sets its own `mode` to
`Operation.FISHING` on `ioctl('operation.fishing')` and slows near other vessels
(`VesselManeuvers.fishing_slowdown`).

**Caveats.**
- `FishingVessel` sets `vessel.operation` from its `mode` (REQ.059-02): `FISHING` while a
  `fishing(...)` trip action runs or the ioctl is on, `TRANSPORT` otherwise. Other behaviours
  leave it at 0.
- The kind of gear is the ship model's `fishing.gear`: `trawl` or `other` (Rule 26).

## (e) Seaplane

> The word 'seaplane' includes any aircraft designed to manoeuvre on the water.

**Definition.** `Type.SEAPLANE` (`0x00100001`, which includes the power-driven bit), class
`SeaPlane`.

**Caveats.** No scenario has a seaplane, and no rule judges one (Rules 18(e) and 31 are not
applicable in practice).

## (f) Vessel not under command

> The term 'vessel not under command' means a vessel which through some exceptional circumstance is
> unable to manoeuvre as required by these Rules and is therefore unable to keep out of the way of
> another vessel.

**Definition.** `Status.NOT_UNDER_COMMAND` (`0x00000200`). Legata:
`Vessel.Status.NotUnderCommand`.

**Caveats.** Nothing sets it: no behaviour or event calls `vessel.state(Status.NOT_UNDER_COMMAND)`.
It can be set only by a test.

## (g) Vessel restricted in her ability to manoeuvre

> The term 'vessel restricted in her ability to manoeuvre' means a vessel which from the nature of her
> work is restricted in her ability to manoeuvre as required by these Rules and therefore is unable to
> keep out of the way of another vessel. … (i) laying, servicing or picking up a navigation mark,
> submarine cable or pipeline; (ii) dredging, surveying or underwater operations; (iii) replenishment
> or transferring persons, provisions or cargo while underway; (iv) launching or recovery of aircraft;
> (v) mineclearance operations; (vi) a towing operation such as severely restricts the towing vessel
> and her tow in their ability to deviate from their course.

**Definition.** `Status.RESTRICTED` (`0x00001000`), with the cause in `vessel.restriction`.
`Vessel.restrict(r)` sets both.

| (g) | `Restriction` |
|---|---|
| (i) | `SERVICING` |
| (ii) | `DREDGING` (surveying and underwater operations are not separate) |
| (iii) | `TRANSPORTING` |
| (iv) | `LAUNCHING` |
| (v) | `MINE_CLEARANCE` |
| (vi) | `TOWING` |
| — | `OTHER`, `NONE` |

**Caveats.**
- Nothing calls `restrict()`, and the `RestrictedAbilityManeuver` behaviour does not
  (REQ.059-03). So `Status.RESTRICTED` never occurs in a run.
- `Restriction` also holds `DRAUGHT` and `VISIBILITY`, which are not causes under (g). See (h)
  and (l).
- Surveying and underwater operations share `DREDGING`.

## (h) Vessel constrained by her draught

> The term 'vessel constrained by her draught' means a power-driven vessel which because of her
> draught in relation to the available depth and width of navigable water, is severely restricted in
> her ability to deviate from the course she is following.

**Definition.** `Restriction.DRAUGHT`. The draught itself is `vessel.draft` (metres), from the
vessel record or the ship model (`physics.draft`), with bounds checked against `evaluator.yaml`.

**Caveats.**
- `DRAUGHT` has the same value as `TRANSPORTING` (`0x00000100`), so the two cannot be told apart.
  In a Python `Flag`, `DRAUGHT` is an alias of `TRANSPORTING`.
- Nothing sets it, and nothing relates draught to the available depth and width of water to
  decide when a vessel is constrained.
- Rule 18(d) and Rule 28 depend on it and are not judged.

## (i) Underway

> The word 'underway' means that a vessel is not at anchor, or made fast to the shore, or aground.

**Definition.** `vessel.status`:
- `UNDERWAY` (`0x00000100`), set by `Vessel.under_way()`;
- not underway: `ANCHORED` (`anchored()`), `MOORED` (`moored()`), `FASTENED`, `AGROUND`
  (`aground()`).

**In the simulation.**
- A trip's anchor action calls `anchored()`, and the end of the anchor watch calls `under_way()`
  (`PlannedVesselBehavior`). `AnchoredVessel` calls `anchored()`.
- The grounding conduct (`maritime.conduct.grounding`) calls `aground()` on contact with the
  seabed, and `state(UNDERWAY)` once the vessel moves free.
- Rules 12, 18, 19 and 35 read "not underway" as excluding `ANCHORED`, `MOORED`, `FASTENED` and
  `AGROUND`.

**Caveats.**
- A vessel starts as `Status.UNKNOWN` and stays so until she first weighs anchor. Clauses that
  test `is UNDERWAY` therefore miss most vessels, which is why the fed rules exclude the
  not-underway states instead.
- Nothing sets `FASTENED` or `MOORED` today. A berthed vessel stays `UNKNOWN`.
- `state()` clears `restriction`.

## (j) Length and breadth

> The words 'length' and 'breadth' of a vessel mean her length overall and greatest breadth.

**Definition.** Ship model `physics.length` (metres, length overall) and `physics.width`. Terms:
`OS.Length` and `OS.Width`.

**In the simulation.** Each ship model's breadth is sourced and cited in its `width:` comment: PIANC WG235
(2022) beams for the merchant classes, interpolated by deadweight as the draughts are, and builder or
broker figures for the named small craft. `test_Breadth.py` checks that each breadth is cited and lies
between 0 and the length.

**Caveats.** A ship model is a category, not one ship: every vessel of a type has the same
length and breadth.

## (k) In sight of one another

> Vessels shall be deemed to be in sight of one another only when one can be observed visually from
> the other.

**Definition.** `(OS, TS).Visible` (`TargetResolver`): the distance between the vessels is within
the scenario visibility, in nautical miles.

**Caveats.**
- Distance only. Obstruction by land or other vessels, darkness and the height of eye are
  ignored.
- Visibility is one value per scenario.

## (l) Restricted visibility

> The term 'restricted visibility' means any condition in which visibility is restricted by fog, mist,
> falling snow, heavy rainstorms, sandstorms or any other similar causes.

**Definition.** `(OS, TS).Visibility`, in nautical miles, is the midpoint of the scenario `WEATHER`
profile's visibility range (`weather/profiles.yaml`). Visibility is *restricted* below
`Vessel.RestrictedVisibility.Range` (2.0 nm, `definitions.s3db`).

**Caveats.**
- The cause (fog, snow, rain) is not modelled. Neither is variation by place or time.
- The 2 nm threshold is unsourced.
- `Restriction.VISIBILITY` exists but nothing uses it.

## (m) WIG craft

> The term 'Wing-In-Ground (WIG) craft' means a multimodal craft which, in its main operational mode,
> flies in close proximity to the surface by utilizing surface-effect action.

**Definition.** `Type.WIG` (`0x00200001`, which includes the power-driven bit), class `WIG`.

**In the simulation.** The flight phase is a trip row: `flight` sets `Operation.FLIGHT` until the
next waypoint (Rule 23(c)).

**Caveats.** No scenario has a WIG craft.

## Open issues

- Call `restrict()` from `RestrictedAbilityManeuver` (REQ.059-03).
- Something that sets `NOT_UNDER_COMMAND`, `MOORED` and `FASTENED`.
- Give `Restriction.DRAUGHT` its own value.
- Set an initial status (`UNDERWAY`) for vessels that start under way.
- Sailing vessels under power, (c).
