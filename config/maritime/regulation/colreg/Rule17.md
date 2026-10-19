# COLREG Rule 17 — Action by Stand-on Vessel

| | |
|---|---|
| Legata | `Rule17.legata` (status TODO; no clause) |
| Driver | `rules.colreg.rule17.Rule17` (`src/rules/colreg/rule17/Rule17.py`); subscribes to `vessel.giveway`, `vessel.standon` and `vessel.crossing`, and the handlers do nothing |
| Loaded by | `rules.colreg.yaml`, entry `Rule17` |
| Simulation | Stand-on roles from `Classification` (`CRSO`, `OTSO`); `VesselManeuvers` |
| Tests | none |
| Status | Not judged. Needs a course- and speed-change term |
| Reviewed | 2026-10-19 |

## How the rule is employed

**Who stands on.** The stand-on vessel is known from encounter classification: `CRSO` (crossing)
and `OTSO` (being overtaken). The situation modules publish `vessel.standon` and
`vessel.giveway`.

**What the simulation does.** Behaviours do not distinguish stand-on from give-way. The same
proximity slowdowns (`crossing_slowdown`, `stop_for_safety`) act on both vessels, so a stand-on
vessel usually slows too, contrary to (a)(i).

## (a)(i) Keep course and speed

> Where one of two vessels is to keep out of the way the other shall keep her course and speed.

**Legata.** None.

**Interpretation needed.** Course and speed held within a tolerance from onset to the closest
approach.

**Caveats.** No course- or speed-change term (COS.041). Once one exists, most stand-on vessels
would breach (a)(i), because of the shared slowdown behaviour. The run had 702 stand-on
crossings, none judged.

## (a)(ii) May act when the give-way vessel is not acting

> The latter vessel may however take action to avoid collision by her manoeuvre alone, as soon as it
> becomes apparent to her that the vessel required to keep out of the way is not taking appropriate
> action in compliance with these Rules.

**Legata.** None.

**Caveats.** A permission. Judging it needs the give-way vessel's action over time, and a test for
when its absence became apparent.

## (b) Must act when collision cannot be avoided by the give-way vessel alone

> When, from any cause, the vessel required to keep her course and speed finds herself so close that
> collision cannot be avoided by the action of the give-way vessel alone, she shall take such action as
> will best aid to avoid collision.

**Legata.** None.

**Interpretation needed.** A close-quarters threshold (DCPA and TCPA), past which the stand-on
vessel must act. `EncounterStage.STAGE4` (immediate danger) exists in `Types.py` but is not
computed.

## (c) Not to alter to port for a vessel on her port side

> A power-driven vessel which takes action in a crossing situation in accordance with sub-paragraph
> (a)(ii) of this Rule to avoid collision with another power-driven vessel shall, if the circumstances
> of the case admit, not alter course to port for a vessel on her own port side.

**Legata.** None.

**Caveats.** Needs the direction of the course change. No behaviour alters course in a crossing.

## (d) The give-way vessel is not relieved

> This Rule does not relieve the give-way vessel of her obligation to keep out of the way.

**Legata.** None.

**In the simulation.** Met by construction: Rules 13 and 15 judge the give-way vessel whatever the
stand-on vessel does.

## Open issues

- A course- and speed-change term (COS.041), then clauses for (a)(i), (b) and (c).
- Stand-on behaviour: keep course and speed in `VesselManeuvers` for `CRSO`/`OTSO` roles, so
  that the behaviours obey the rule they will be judged on.
- A close-quarters or immediate-danger stage for (b).
