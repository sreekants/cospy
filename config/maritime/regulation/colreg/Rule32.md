# COLREG Rule 32 — Definitions (Sound Signals)

| | |
|---|---|
| Legata | `Rule32.legata` (comments only) |
| Driver | `rules.colreg.rule32.Rule32` (`src/rules/colreg/rule32/Rule32.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule32` |
| Definitions | Signal vocabulary `maritime/signals.yaml` (`Sound.*`) |
| Tests | none |
| Status | Definitions only; nothing to judge |
| Reviewed | 2026-10-19 |

## How the rule is employed

Sound signals are **names in the signal vocabulary**, raised into a vessel's `signal` set like
lights (see Rule 20). A name stands for the whole signal: the count and kind of blasts are in the
name, not timed.

| Rule 32 | In the simulation |
|---|---|
| (a) Whistle | Not an appliance. Whistle signals are the `Sound.Blast.*` and `Sound.Foghorn.*` names |
| (b) Short blast, about 1 s | Encoded in names: `Sound.Blast.Short.1x` to `.5x` |
| (c) Prolonged blast, 4–6 s | Encoded in names: `Sound.Foghorn.Prolonged.1x`, `.2x`, `Sound.Foghorn.Prolonged.Short.2x` |

REQ-056-01 adds `Sound.Bell`, `Sound.Bell.Strokes.3x` and `Sound.Gong` (Rule 35(g), (h)).

## (a)–(c)

> (a) The word 'whistle' means any sound signalling appliance capable of producing the prescribed blasts
> and which complies with the specifications in Annex III to these Regulations. (b) The term 'short
> blast' means a blast of about one second's duration. (c) The term 'prolonged blast' means a blast of
> from four to six seconds' duration.

**Legata.** None.

**Caveats.**
- Durations and intervals are not modelled. A signal is either raised or not, so the
  "at intervals of not more than 2 minutes" of Rule 35 reduces to "raised".
- Hearing range is not modelled: any vessel can "hear" any signal.
- `OS.FogSignal` matches `Sound.Foghorn*`, which is any fog signal, not the one the vessel owes
  (Rule 35). It does not match the bell or gong.

## Open issues

- Timed signals, if the intervals of Rules 34 and 35 are to be judged.
