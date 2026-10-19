# COLREG Rule 36 — Signals to Attract Attention

| | |
|---|---|
| Legata | `Rule36.legata` (text only) |
| Driver | `rules.colreg.rule36.Rule36` (`src/rules/colreg/rule36/Rule36.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule36` |
| Simulation | Signal vocabulary; `NuisanceExaminer` |
| Tests | none |
| Status | Not judged. A permission with conditions; no attention signals are defined |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 36 permits signals to attract attention, provided they cannot be mistaken for other
signals. Any signal a vessel shows must be a name in the vocabulary (see Rule 20). No
attention-signal or searchlight name is defined, so a vessel cannot make one.

## Rule 36

> If necessary to attract the attention of another vessel any vessel may make light or sound signals
> that cannot be mistaken for any signal authorized elsewhere in these Rules, or may direct the beam of
> her searchlight in the direction of the danger, in such a way as not to embarrass any vessel. Any
> light to attract the attention of another vessel shall be such that it cannot be mistaken for any aid
> to navigation. For the purpose of this Rule the use of high intensity intermittent or revolving
> lights, such as strobe lights, shall be avoided.

**Legata.** None.

**Interpretation.** If attention signals were added, they would get a vocabulary class of their
own. `NuisanceExaminer` could then score their use with no other vessel at risk.

**Caveats.**
- "Cannot be mistaken" holds by construction: every name is distinct.
- Searchlights and strobes are not modelled.

## Open issues

- None. REQ-057-07 classes Rule 36 as not judged.
