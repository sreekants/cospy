# COLREG Rule 23 — Power-driven Vessels Underway

| | |
|---|---|
| Legata | `Rule23.legata` |
| Driver | `rules.colreg.rule23.Rule23` (`src/rules/colreg/rule23/Rule23.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule23` |
| Terms | `OS.Type`, `OS.Length`, `OS.Velocity`, `OS.Signal.ON`, `OS.Operation`; functions `meters()`, `knot()` |
| Tests | none |
| Status | Not judged. Six clauses, not fed. `VesselSignals` shows the lights for container ships and ferries. Reworked by REQ.057 (open) |
| Reviewed | 2026-10-19 |

## How the rule is employed

Lights are names in a vessel's `signal` set (see Rule 20). Each clause assures that the lights
for own ship's type and length are in `OS.Signal.ON`. The driver feeds nothing (REQ-057-09
requires it to feed every vessel under test).

**In the simulation.** `VesselSignals` shows the power-driven row for a vessel whose state is
none of the others (Rule 20) and whose type is not sailing. Status `UNKNOWN`, before a vessel
first weighs anchor, counts as underway. A fishing vessel not engaged in fishing is power-driven
(Rule 26(e)).

Today, missing lights at night are scored outside COLREG by `NightTimeExaminer`, from the
per-zone `required_lights` in `examiner/zones.yaml`.

## File-level condition

**Legata.** `OS.Operation has 'Vessel.Operation.UNDERWAY'`.

**Caveats.**
- Not compiled (LEGATA.002).
- It tests a status value on the operation term. `UNDERWAY` is a `Status`, not an `Operation`.
- REQ-056-07 decides that underway is to be tested as Rule 3(i) defines it: status none of
  `ANCHORED`, `MOORED`, `FASTENED`, `AGROUND`.
- Night or restricted visibility is not tested (Rule 20(b), (c)). REQ.057 adds `(OS, TS).Night`.

## (a) Masthead lights, sidelights, sternlight

> A power-driven vessel underway shall exhibit: (i) a masthead light forward; (ii) a second masthead
> light abaft of and higher than the forward one; except that a vessel of less than 50 metres in length
> shall not be obliged to exhibit such light but may do so; (iii) sidelights; (iv) a sternlight.

**Legata.**
- `clause['COLREG.Rule23.a']`: power-driven, excluding length under 12 m. Assures, as OR'd
  lines, `Light.Masthead.Forward.1x`, `Light.Sidelight` and `Light.Sternlight`.
- `clause['COLREG.Rule23.a.ii']`: power-driven, excluding length under 50 m. Assures
  `Light.Masthead.Abaft`.

**In the simulation.** From 12 m: `Light.Masthead.Forward.1x`, `Light.Sidelight` and
`Light.Sternlight`. `Light.Masthead.Abaft` is shown only at 50 m or more: the option to show it
below 50 m is not taken. The lights do not depend on making way.

**Caveats.**
- The OR'd assurance lines pass with any one light. They should be one `and`-joined line.
- Vessel length is a ship-model category value.

## (b) Air-cushion vessel

> An air-cushion vessel when operating in the non-displacement mode shall, in addition to the lights
> prescribed in paragraph (a) of this Rule exhibit an all-round flashing yellow light.

**Legata.** `clause['COLREG.Rule23.b']`: `OS.Type is Vessel.Type.AirCushion`, assures
`Light.Flashing.Yellow`.

**Caveats.** `Type` has no `AIR_CUSHION` member, so the term does not resolve. REQ-057-01 takes
(b) out of scope.

## (c) WIG craft

> A WIG craft only when taking off, landing and in flight near the surface shall, in addition to the
> lights prescribed in paragraph (a) of this Rule, exhibit a high intensity all-round flashing red
> light.

**Legata.** `clause['COLREG.Rule23.c']`: `OS.Type is Vessel.Type.WIG`, assures
`Light.Flashing.Red`.

**Caveats.** Flight modes are not modelled, so a WIG craft would need the light at all times. No
scenario has a WIG craft.

## (d) Small power-driven vessels

> (i) A power-driven vessel of less than 12 metres in length may in lieu of the lights prescribed in
> paragraph (a) of this Rule exhibit an all-round white light and sidelights; (ii) a power-driven vessel
> of less than 7 metres in length whose maximum speed does not exceed 7 knots may in lieu of the lights
> prescribed in paragraph (a) of this Rule exhibit an all-round white light and shall, if practicable,
> also exhibit sidelights; (iii) the masthead light or all-round white light on a power-driven vessel of
> less than 12 metres in length may be displaced from the fore and aft centreline …

**Legata.**
- `clause['COLREG.Rule23.d.i']`: power-driven, excluding length over 12 m. Assures
  `Light.Allround.White` or `Light.Sidelight` (OR'd).
- `clause['COLREG.Rule23.d.ii']`: power-driven, excluding length over 7 m *and* speed over 7
  knots. Assures `Light.Allround.White`.
- (iii): none (light position).

**In the simulation.** Under 12 m the alternative of (d)(i) is always taken:
`Light.Allround.White` and `Light.Sidelight`, with no masthead light or sternlight. (d)(ii) is
not distinguished: a vessel under 7 m shows the same lights, sidelights included.

**Caveats.**
- (d)(i) is an alternative ("may in lieu"), but the clause makes it a requirement. A small
  vessel showing the lights of (a) instead would fail.
- (d)(ii) tests the current speed, where the rule means the maximum speed.
- (d)(ii)'s exclusion lets in vessels over 7 m that happen to be slower than 7 knots.

## Open issues

- REQ.057 (REQ-057-01): review (a), (c) and (d) against the text, join the assurances with
  `and`, add the night or restricted-visibility condition, and feed every vessel.
- REQ-059-01: the other power-driven behaviours (Motorboat, Yacht) show the lights.
- The underway test (REQ-056-07).
