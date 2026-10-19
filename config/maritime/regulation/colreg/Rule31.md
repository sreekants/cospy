# COLREG Rule 31 — Seaplanes

| | |
|---|---|
| Legata | `Rule31.legata` (status TODO; no clause) |
| Driver | `rules.colreg.rule31.Rule31` (`src/rules/colreg/rule31/Rule31.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule31` |
| Simulation | `Type.SEAPLANE`, `Type.WIG`; classes `SeaPlane`, `WIG` |
| Tests | none |
| Status | Not applicable. No scenario has seaplanes or WIG craft |
| Reviewed | 2026-10-19 |

## How the rule is employed

The seaplane and WIG types and classes exist (Rule 3(e), (m)), but no scenario builds one. Light
positions and characteristics are not modelled (Rule 20), so "as closely similar as possible"
has nothing to compare.

## Rule 31

> Where it is impracticable for a seaplane or a WIG craft to exhibit lights and shapes of the
> characteristics or in the positions prescribed in the Rules of this Part she shall exhibit lights and
> shapes as closely similar in characteristics and position as is possible.

**Legata.** None.

**Caveats.** An exemption for a special construction, like Rule 1(e). It cannot be judged without
light geometry.

## Open issues

- None until seaplanes or WIG craft appear in a scenario.
