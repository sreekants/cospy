# COLREG Rule 25 — Sailing Vessels Underway and Vessels under Oars

| | |
|---|---|
| Legata | `Rule25.legata` (status TODO) |
| Driver | `rules.colreg.rule25.Rule25` (`src/rules/colreg/rule25/Rule25.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule25` |
| Terms | `OS.Type`, `OS.Operation`, `OS.Signal.ON` |
| Tests | none |
| Status | Not judged. One misnamed clause, not fed. Reworked by REQ.057 (REQ-057-02, open) |
| Reviewed | 2026-10-19 |

## How the rule is employed

Lights are names in a vessel's `signal` set (see Rule 20). Sailing vessels are `Type.SAILING`
(Rule 3(c)). The one clause is never fed. `SailingVessel` does not yet run `VesselSignals`
(REQ-059-01).

**In the simulation.** `VesselSignals` shows the sailing row for a `Type.SAILING` vessel with no
other state (Rule 20): `Light.Sidelight` and `Light.Sternlight` at every length, at night or in
restricted visibility, and no shape.

## File-level condition

**Legata.** `(OS.Type is Vessel.Type.Sailing) or (OS.Operation in ['Vessel.Operation.SAILING',
'Vessel.Operation.OARED'])`.

**Caveats.**
- Not compiled (LEGATA.002).
- `SAILING` and `OARED` are not `Operation` members. Vessels under oars are not modelled.
- Neither underway nor night is tested.

## (a) Sidelights and sternlight

> A sailing vessel underway shall exhibit: (i) sidelights; (ii) a sternlight.

**Legata.** `clause['COLREG.Rule24.a']` (named for Rule 24 by mistake): condition `OS.Type is
Vessel.Type.PowerDriven`, assures `Light.Sidelight` and `Light.Sternlight` (OR'd).

**Caveats.**
- The clause name is wrong (`Rule24.a`, a COS.022 finding).
- The condition tests power-driven where the rule is about sailing vessels, so once the file
  condition were compiled the clause could never apply.
- The OR'd lines pass with one light.

## (b) Combined lantern under 20 m; (c) optional red-over-green

> (b) In a sailing vessel of less than 20 metres in length the lights prescribed in paragraph (a) of
> this Rule may be combined in one lantern carried at or near the top of the mast where it can best be
> seen. (c) A sailing vessel underway may, in addition to the lights prescribed in paragraph (a) of this
> Rule, exhibit at or near the top of the mast, where they can best be seen, two all-round lights in a
> vertical line, the upper being red and the lower green, but these lights shall not be exhibited in
> conjunction with the combined lantern permitted by paragraph (b) of this Rule.

**Legata.** None. Both are options about light arrangement.

**In the simulation.** Neither option is taken: a sailing vessel shows separate sidelights and
sternlight.

**Caveats.** Neither the combined lantern nor the red-over-green lights have vocabulary names, so
(c)'s prohibition cannot be judged.

## (d) Under 7 m and under oars

> (i) A sailing vessel of less than 7 metres in length shall, if practicable, exhibit the lights
> prescribed in paragraph (a) or (b) of this Rule, but if she does not, she shall have ready at hand an
> electric torch or lighted lantern showing a white light which shall be exhibited in sufficient time
> to prevent collision. (ii) A vessel under oars may exhibit the lights prescribed in this Rule for
> sailing vessels, but if she does not, she shall have ready at hand an electric torch or lighted
> lantern showing a white light …

**Legata.** None. REQ-057-02 covers (d) with `Light.Allround.White`.

**In the simulation.** A sailing vessel under 7 m shows the lights of (a); the torch is not
modelled.

## (e) Sail and machinery: cone apex downwards

> A vessel proceeding under sail when also being propelled by machinery shall exhibit forward where it
> can best be seen a conical shape, apex downwards.

**Legata.** None.

**Caveats.** Sailing under power is not modelled (Rule 3(c)), and there is no shape name. A
`Type.SAILING` vessel always shows sailing signals, also when its behaviour motors.

## Open issues

- REQ-057-02: rewrite (a) and (d) for sailing vessels underway at night or in restricted
  visibility, named `COLREG.Rule25.*`, and feed every vessel.
- REQ-059-01: `SailingVessel` runs `VesselSignals`.
