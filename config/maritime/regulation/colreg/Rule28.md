# COLREG Rule 28 — Vessels Constrained by their Draught

| | |
|---|---|
| Legata | `Rule28.legata` (status TODO; no clause) |
| Driver | `rules.colreg.rule28.Rule28` (`src/rules/colreg/rule28/Rule28.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule28` |
| Simulation | `Restriction.DRAUGHT`; `vessel.draft` |
| Tests | none |
| Status | Not judged. Optional signals for a state the simulation does not set. Rule 34 and draught are follow-ups of REQ.056 |
| Reviewed | 2026-10-19 |

## How the rule is employed

"Constrained by her draught" is `Restriction.DRAUGHT` (Rule 3(h)). Nothing sets it, and nothing
compares a vessel's draught with the available depth and width of water. The member also shares
its value (`0x100`) with `TRANSPORTING`. Lights would be names in the `signal` set (see Rule 20),
but neither the three red all-round lights nor the cylinder is in the vocabulary.

## Rule 28

> A vessel constrained by her draught may, in addition to the lights prescribed for power-driven
> vessels in Rule 23, exhibit where they can best be seen three all-round red lights in a vertical line,
> or a cylinder.

**Legata.** File-level condition only: `OS.State has 'Vessel.State.Constrained'`. No clause.

**Interpretation.** "May": the signals are optional, so there is no duty to breach. A vessel that
shows them claims the precedence of Rule 18(d).

**Caveats.**
- `OS.State` does not exist (it would be `OS.Restriction`).
- An optional signal could be judged only as a nuisance, shown without the state. That needs the
  state to be set.

## Open issues

- Give `Restriction.DRAUGHT` its own value, and set it from draught against depth (the
  `SeaResolver` depth and `vessel.draft`).
- Add the vocabulary names, if Rule 18(d) is to be judged.
