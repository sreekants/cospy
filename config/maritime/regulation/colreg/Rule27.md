# COLREG Rule 27 — Vessels Not under Command or Restricted in their Ability to Manoeuvre

| | |
|---|---|
| Legata | `Rule27.legata` (status TODO; no clause) |
| Driver | `rules.colreg.rule27.Rule27` (`src/rules/colreg/rule27/Rule27.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule27` |
| Simulation | `Status.NOT_UNDER_COMMAND`, `Status.RESTRICTED` with `Restriction.*` (Rule 3(f), (g)); `RestrictedAbilityManeuver` behaviour |
| Tests | none |
| Status | Not judged. Text only. REQ.057 (REQ-057-04, open) adds (a) and (b) |
| Reviewed | 2026-10-19 |

## How the rule is employed

**The vessel states exist.** `Status.NOT_UNDER_COMMAND` and `Status.RESTRICTED`, with the cause
in `vessel.restriction`, are set by `Vessel.state()` and `Vessel.restrict()` (Rule 3).

**Nothing sets them.** No behaviour or event calls `state(NOT_UNDER_COMMAND)`. The
`RestrictedAbilityManeuver` behaviour does not call `restrict()` (REQ-059-03).

**Lights and shapes** are names in the `signal` set (see Rule 20). REQ-056-01 adds
`Light.Allround.Red.2x`, `Light.Allround.RedWhiteRed`, `Shape.Ball.2x` and `Shape.BallDiamondBall`.

## File-level condition

**Legata.** `OS.State in ['Vessel.State.Unmanoeuverarble', 'Vessel.State.CommandAbandonded']`.

**Caveats.**
- Not compiled (LEGATA.002).
- `OS.State` and `Vessel.State.*` do not exist. REQ-056-03 decides to use `OS.Status` with
  `Vessel.Status.NotUnderCommand` and `RESTRICTED`.

## (a) Not under command

> A vessel not under command shall exhibit: (i) two all-round red lights in a vertical line where they
> can best be seen; (ii) two balls or similar shapes in a vertical line where they can best be seen;
> (iii) when making way through the water, in addition to the lights prescribed in this paragraph,
> sidelights and a sternlight.

**Legata.** None. REQ-057-04 plans it: `Light.Allround.Red.2x` at night or in restricted
visibility, `Shape.Ball.2x` by day, and sidelights and a sternlight when making way (speed above
`Vessel.MakingWay.Speed`).

## (b) Restricted in her ability to manoeuvre

> A vessel restricted in her ability to manoeuvre, except a vessel engaged in mineclearance operations,
> shall exhibit: (i) three all-round lights in a vertical line where they can best be seen. The highest
> and lowest of these lights shall be red and the middle light shall be white; (ii) three shapes in a
> vertical line where they can best be seen. The highest and lowest of these shapes shall be balls and
> the middle one a diamond; (iii) when making way through the water, a masthead light or lights,
> sidelights and a sternlight in addition to the lights prescribed in sub-paragraph (i); (iv) when at
> anchor, in addition to the lights or shapes prescribed in sub-paragraphs (i) and (ii), the light,
> lights or shape prescribed in Rule 30.

**Legata.** None. REQ-057-04 plans (i)–(iii).

**Caveats.**
- `state()` clears the restriction, so a restricted vessel that anchors loses its RESTRICTED
  status. (b)(iv) cannot hold.
- Mine clearance (`Restriction.PEACE_KEEEPING`) must be excluded.

## (c)–(f) Towing, dredging and underwater, diving, mine clearance

> (c) A power-driven vessel engaged in a towing operation such as severely restricts the towing vessel
> and her tow in their ability to deviate from their course shall, in addition to the lights or shapes
> prescribed in Rule 24(a), exhibit the lights or shapes prescribed in sub-paragraphs (b)(i) and (ii)
> of this Rule. (d) A vessel engaged in dredging or underwater operations, when restricted in her
> ability to manoeuvre, shall exhibit … (e) Whenever the size of a vessel engaged in diving operations
> makes it impracticable to exhibit all lights and shapes prescribed in paragraph (d) … (f) A vessel
> engaged in mineclearance operations shall … exhibit three all-round green lights or three balls …

**Legata.** None. Out of scope for REQ.056–059.

**Caveats.**
- Towing is not modelled (Rule 24).
- The side of an obstruction (d), the diving flag (e) and the mine-clearance 1000 m danger zone
  (f) have no representation.

## (g) Under 12 m; (h) not distress signals

> (g) Vessels of less than 12 metres in length, except those engaged in diving operations, shall not be
> required to exhibit the lights and shapes prescribed in this Rule. (h) The signals prescribed in this
> Rule are not signals of vessels in distress and requiring assistance. Such signals are contained in
> Annex IV to these Regulations.

**Legata.** None. (g) is to be an exclusion in REQ-057-04's clauses. (h) is a definition.

## Open issues

- REQ-059-03: `RestrictedAbilityManeuver` calls `restrict(Restriction.OTHER)`. Something must also
  set `NOT_UNDER_COMMAND`, for example a breakdown event.
- REQ-056-03 and REQ-057-04: clauses on `OS.Status`.
- REQ.058: `VesselSignals` raises the lights and shapes.
- Keep the restriction when a restricted vessel anchors, for (b)(iv).
