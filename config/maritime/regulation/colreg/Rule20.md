# COLREG Rule 20 — Application (Part C: Lights and Shapes)

| | |
|---|---|
| Legata | `Rule20.legata` (comments only) |
| Driver | `rules.colreg.rule20.Rule20` (`src/rules/colreg/rule20/Rule20.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule20` |
| Simulation | Signal vocabulary `maritime/signals.yaml`; `vessel.signal` (a `Signal` value set); `NightTimeExaminer`; `NuisanceExaminer` |
| Tests | none for the rule; vocabulary and examiners have their own tests |
| Status | Application rule; nothing to judge on its own. When lights and shapes are required is decided for Rules 23–31 by REQ.056–059 (open) |
| Reviewed | 2026-10-19 |

## How lights and shapes are implemented

These mechanisms are shared by Rules 20–31 and 33–37.

- **A light, shape or sound signal is a name** in the vocabulary, `maritime/signals.yaml`: for
  example `Light.Masthead.Forward.1x`, `Light.Sidelight` or `Sound.Foghorn.Prolonged.1x`. Each
  name has a class that says when it may be shown:
  - `navigation`: lights and shapes, by status and time;
  - `restricted_visibility`: fog signals;
  - `encounter`: manoeuvring and warning signals.
- **A vessel shows a signal** by adding its name to its `signal` value set:
  `Vehicle.raise_signal(name)` and `lower_signal(name)`; `is_signaled(pattern)` tests it.
- **Clauses read the set** as `OS.Signal` or `OS.Signal.ON` (`VesselResolver`), for example
  `OS.Signal.ON has 'Light.Sidelight'`.
- **Names are checked.** `COLREG.check_signals()` refuses at setup any clause that names a
  signal outside the vocabulary, and `Signal.configure()` loads the vocabulary for the vessels.
- **Lights have no geometry.** Position, arc, colour and range (Annex I, Rules 21 and 22) are
  not modelled. A name stands for a correctly fitted light.

Nothing raises navigation lights or shapes yet: `VesselSignals.py` is an empty class. REQ.058
(the `VesselSignals` behaviour) and REQ.059 (behaviours that call it) are open.

**Examiners outside COLREG:**
- `NightTimeExaminer` scores missing lights at night (`night.lights_missing`). The required
  lights are listed per zone in `examiner/zones.yaml` (`required_lights`), and the night window
  is per zone (`night_from`, `night_to`).
- `NuisanceExaminer` scores a signal shown when its class does not allow it
  (`signal.nuisance`): an `encounter` signal outside an encounter, or a fog signal in clear
  visibility outside an encounter.

## (a) In all weathers

> Rules in this Part shall be complied with in all weathers.

**Legata.** None.

**In the simulation.** No light or shape clause is gated on weather.

## (b) Lights from sunset to sunrise; no other lights

> The Rules concerning lights shall be complied with from sunset to sunrise, and during such times no
> other lights shall be exhibited, except such lights as cannot be mistaken for the lights specified in
> these Rules or do not impair their visibility or distinctive character, or interfere with the keeping
> of a proper look-out.

**Legata.** None. The decided design (REQ-056-05) adds a term `(OS, TS).Night`, true between
`night.from` and `night.to` hours (`legata.yaml`, defaults 20 and 6). It shares its hour test with
`NightTimeExaminer`.

**Caveats.**
- Night is a fixed hour window, not sunrise and sunset. That is wrong at high latitudes, such
  as the Trondheimsfjord in summer.
- "No other lights" is judged only for `encounter` and fog signals, by `NuisanceExaminer`.
  Navigation lights for the wrong status are not.

## (c) Lights by day in restricted visibility

> The lights prescribed by these Rules shall, if carried, also be exhibited from sunrise to sunset in
> restricted visibility and may be exhibited in all other circumstances when it is deemed necessary.

**Legata.** None. Decided (REQ-056-04): restricted visibility is `(OS, TS).Visibility <
Vessel.RestrictedVisibility.Range` (2 nm), as in Rules 19 and 35.

## (d) Shapes by day

> The Rules concerning shapes shall be complied with by day.

**Legata.** None. Shape clauses are to apply when `(OS, TS).Night` is false (REQ.057).

**Caveats.** No shape names are in the vocabulary yet. REQ-056-01 adds `Shape.*`.

## (e) Annex I

> The lights and shapes specified in these Rules shall comply with the provisions of Annex I to these
> Regulations.

**Legata.** None.

**Caveats.** Annex I (positioning, colour, intensity, shape dimensions) is not modelled.

## Open issues

- REQ.056–059: the night term, signal names, clauses for Rules 23–30, and behaviours that show
  the lights.
- Sunrise and sunset by latitude and date.
- "No other lights" for navigation lights, (b).
