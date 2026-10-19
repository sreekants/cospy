# COLREG Rule 23 — Power-driven Vessels Underway

| | |
|---|---|
| Legata | `Rule23.legata` |
| Driver | `rules.colreg.rule23.Rule23` (`src/rules/colreg/rule23/Rule23.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule23` |
| Terms | `OS.Type`, `OS.Status`, `OS.Operation`, `OS.Length`, `OS.MaxSpeed`, `OS.Signal.ON`, `(OS, TS).Night`, `(OS, TS).Visibility`; function `knot()` |
| Tests | `tests/maritime/model/colreg/test_Rule23.py` (13) |
| Status | Not judged in a run: five clauses, not fed. Clauses corrected 2026-10-19 (LEGATA.058, 061, 062). `VesselSignals` shows the lights for container ships and ferries. Feeding is REQ-057-09 |
| Reviewed | 2026-10-19 |

## How the rule is employed

Lights are names in a vessel's `signal` set (see Rule 20). Each clause assures that the lights
for own ship's type and length are in `OS.Signal.ON`. The driver feeds nothing (REQ-057-09
requires it to feed every vessel under test).

**Shared by every clause.**
- **Underway** is Rule 3(i): status none of `ANCHORED`, `MOORED`, `FASTENED`, `AGROUND`. Status
  `UNKNOWN`, before a vessel first weighs anchor, counts as underway.
- **The Rule 20 window:** lights are judged at night (`(OS, TS).Night`) or in restricted
  visibility (`(OS, TS).Visibility < Vessel.RestrictedVisibility.Range`), not by day in clear
  visibility (LEGATA.008).
- **Vessels with lights of their own are excluded:** not under command, restricted, or engaged in
  fishing. They show the lights of Rules 26 and 27 instead, and Rule 26(a) says "only".
- Assurance lines are AND'd, so every light on its own line is needed.

**In the simulation.** `VesselSignals` shows the power-driven row for a vessel whose state is
none of the others (Rule 20) and whose type is not sailing. A fishing vessel not engaged in
fishing is power-driven (Rule 26(e)).

Today, missing lights at night are also scored outside COLREG by `NightTimeExaminer`, from the
per-zone `required_lights` in `examiner/zones.yaml` (see Rule 20).

## File-level condition

**Legata.** Underway, as above. It tested `OS.Operation has 'Vessel.Operation.UNDERWAY'`, a status
written as an operation string, until 2026-10-19 (LEGATA.003).

**Caveats.** Not compiled (LEGATA.002). Each clause therefore repeats the underway test.

## (a) Masthead lights, sidelights, sternlight

> A power-driven vessel underway shall exhibit: (i) a masthead light forward; (ii) a second masthead
> light abaft of and higher than the forward one; except that a vessel of less than 50 metres in length
> shall not be obliged to exhibit such light but may do so; (iii) sidelights; (iv) a sternlight.

**Legata.**
- `clause['COLREG.Rule23.a']`: power-driven, underway, in the Rule 20 window, excluding length
  under 12 m. Assures `Light.Masthead.Forward.1x`, `Light.Sidelight` and `Light.Sternlight`.
- `clause['COLREG.Rule23.a.ii']`: the same, excluding length under 50 m. Assures
  `Light.Masthead.Abaft`.

**In the simulation.** From 12 m: `Light.Masthead.Forward.1x`, `Light.Sidelight` and
`Light.Sternlight`. `Light.Masthead.Abaft` is shown only at 50 m or more: the option to show it
below 50 m is not taken. The lights do not depend on making way.

**Caveats.** Vessel length is a ship-model category value.

## (b) Air-cushion vessel

> An air-cushion vessel when operating in the non-displacement mode shall, in addition to the lights
> prescribed in paragraph (a) of this Rule exhibit an all-round flashing yellow light.

**Legata.** None. Not applicable: `Type` has no air-cushion member, and no scenario has an
air-cushion vessel.

**Removed.** `clause['COLREG.Rule23.b']` tested `Vessel.Type.AirCushion`. The constant does not
resolve, and the error stopped every clause of Rule 23 from being judged, so the clause was
removed on 2026-10-19 (LEGATA.059). It also lacked the non-displacement condition and the 23(a)
lights. Adding the type would bring it back.

## (c) WIG craft

> A WIG craft only when taking off, landing and in flight near the surface shall, in addition to the
> lights prescribed in paragraph (a) of this Rule, exhibit a high intensity all-round flashing red
> light.

**Legata.** `clause['COLREG.Rule23.c']`: `OS.Type is Vessel.Type.WIG` and `OS.Operation is
Vessel.Operation.FLIGHT`, in the Rule 20 window. Assures `Light.Flashing.Red` and the 23(a) lights.

**In the simulation.** The flight phase is a trip row: the action `flight` sets `Operation.FLIGHT`
from its waypoint to the next (Rule 3, LEGATA.060).

**Caveats.**
- A WIG craft on the water is `Type.WIG`, not `Type.POWER_DRIVEN`, so 23(a) does not judge it,
  although Rule 18(f)(ii) treats it as power-driven there.
- No scenario has a WIG craft.

## (d) Small power-driven vessels

> (i) A power-driven vessel of less than 12 metres in length may in lieu of the lights prescribed in
> paragraph (a) of this Rule exhibit an all-round white light and sidelights; (ii) a power-driven vessel
> of less than 7 metres in length whose maximum speed does not exceed 7 knots may in lieu of the lights
> prescribed in paragraph (a) of this Rule exhibit an all-round white light and shall, if practicable,
> also exhibit sidelights; (iii) the masthead light or all-round white light on a power-driven vessel of
> less than 12 metres in length may be displaced from the fore and aft centreline …

**Legata.**
- `clause['COLREG.Rule23.d.i']`: power-driven, underway, in the Rule 20 window, under 12 m, not a
  vessel (d)(ii) covers. Assures the 23(a) lights *or* `Light.Allround.White` with
  `Light.Sidelight`.
- `clause['COLREG.Rule23.d.ii']`: under 7 m with a maximum speed (`OS.MaxSpeed`, from the ship
  model) not over 7 knots. Assures the 23(a) lights *or* `Light.Allround.White`.
- (iii): none (light position).

Until 2026-10-19 (LEGATA.061, LEGATA.062):
- (d)(i) required the alternative, so a small vessel showing the 23(a) lights breached.
- A vessel of exactly 12 m fell under both (a) and (d)(i).
- (d)(ii)'s exclusion was inverted: every slow vessel, a 300 m tanker included, had to show an
  all-round white light.

**Interpretation.** Each paragraph accepts its own lights or the fuller set. A vessel (d)(ii)
covers is judged by (d)(ii) only. A vessel under 7 m whose ship model has no maximum speed is
judged under (d)(i). "Shall, if practicable, also exhibit sidelights" is not judged:
practicability is not modelled.

**In the simulation.** Under 12 m the alternative of (d)(i) is always taken:
`Light.Allround.White` and `Light.Sidelight`, with no masthead light or sternlight. (d)(ii) is
not distinguished: a vessel under 7 m shows the same lights, sidelights included, which both
clauses accept.

**Caveats.** `max_speed` is sourced (m/s) where a source states one: general cargo, tanker, car
carrier, fast ferry, tug, motorboat and yachts. The only model under 7 m is the AUV, which has
none.

## Open issues

- Feed every vessel (REQ-057-09).
- REQ-059-01: the other power-driven behaviours (Motorboat, Yacht) show the lights.
