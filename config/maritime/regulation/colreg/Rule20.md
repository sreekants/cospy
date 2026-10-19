# COLREG Rule 20 — Application (Part C: Lights and Shapes)

| | |
|---|---|
| Legata | `Rule20.legata` (comments only) |
| Driver | `rules.colreg.rule20.Rule20` (`src/rules/colreg/rule20/Rule20.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule20` |
| Simulation | Signal vocabulary `maritime/signals.yaml`; `vessel.signal` (a `Signal` value set); `VesselSignals` (`src/maritime/behavior/vessels/VesselSignals.py`); `NightTimeExaminer`; `NuisanceExaminer` |
| Tests | none for the rule; vocabulary and examiners have their own tests |
| Status | Application rule; nothing to judge on its own. `VesselSignals` shows lights, shapes and fog signals for container ships, ferries and fishing vessels (REQ.058, REQ.059 partial). Clauses for Rules 23–30 are REQ.057 (open) |
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

**Behaviours show them.** `VesselSignals` runs after each movement tick, also at anchor, for
`ContainerShip`, `Ferry` and `FishingVessel` (REQ-059-01 adds the other behaviours). These are
its interpretations, shared by Rules 23–35:
- **One state per vessel.** A vessel shows the signals of one row of `VesselSignals.TABLE`,
  chosen in this order: aground, not under command, restricted, fishing, anchored, moored,
  sailing, power-driven. The first that holds wins; signals of two rows are never combined.
- **Lights** are shown at night or in restricted visibility, and none otherwise; the option to
  show them "in all other circumstances" is not used.
- **Shapes** are shown by day, in any visibility, and lowered at night.
- **Fog signals** are held in the set for as long as visibility is restricted (Rule 35).
- **Each step replaces its kind.** Showing lights lowers any other `Light.*` name, and so for
  shapes and sounds, except `encounter` signals (Rule 34), which are left alone.
- **Where a rule gives a choice** (a "may", an alternative, a small-vessel exemption), one
  arrangement is fixed; each rule's notes say which.
- **Making way** is the speed the behaviour sets (`dx`) above `Vessel.MakingWay.Speed` (0.25),
  not a speed through the water. An anchored vessel's `dx` is zero.
- **Length** is the ship model's length.
- **Conditions are the rules' own.** Night, visibility and the constants are read once from
  `legata.yaml` (the `target` and `vessel` resolvers), so the vessels and the clauses agree.

**Examiners outside COLREG:**
- `NightTimeExaminer` scores missing lights at night (`night.lights_missing`). The required
  lights are listed per zone in `examiner/zones.yaml` (`required_lights`), and the night window
  is per zone (`night_from`, `night_to`).
- `NuisanceExaminer` scores a signal shown when its class does not allow it
  (`signal.nuisance`): an `encounter` signal outside an encounter, or a fog signal in clear
  visibility outside an encounter.

**What is judged (checked 2026-10-19).**
- **COLREG does not judge lights or shapes.** Rules 23–31 have no fed clauses (REQ.057), so a
  missing or wrong light or shape goes unnoticed by the rules. Only Rule 35 (a)–(c) judges what
  `VesselSignals` raises.
- **`NightTimeExaminer` does not follow the vessel's state.** Its default `required_lights`
  (`Light.Masthead.*`, `Light.Sidelight`, `Light.Sternlight`) apply to every vessel in the zone.
  A vessel lit correctly for its state would be scored as missing lights: at anchor or aground,
  fishing other than trawling, not under command, restricted and stopped, sailing, or power-driven
  under 12 m.
- **`NuisanceExaminer` ignores `navigation` signals,** so lights or shapes for the wrong state
  are not scored either.

## (a) In all weathers

> Rules in this Part shall be complied with in all weathers.

**Legata.** None.

**In the simulation.** No light or shape clause is gated on weather.

## (b) Lights from sunset to sunrise; no other lights

> The Rules concerning lights shall be complied with from sunset to sunrise, and during such times no
> other lights shall be exhibited, except such lights as cannot be mistaken for the lights specified in
> these Rules or do not impair their visibility or distinctive character, or interfere with the keeping
> of a proper look-out.

**Legata.** None. The term `(OS, TS).Night` (REQ-056-05, `TargetResolver`) is true from
`night.from` to `night.to` hours of the simulation's local time (`legata.yaml`, 20 and 6). The
window wraps midnight. It shares its hour test (`Clock.within_hours`) with `NightTimeExaminer`.

**In the simulation.** `VesselSignals` uses the same term on the behaviour's local clock.

**Caveats.**
- Night is a fixed hour window, not sunrise and sunset. That is wrong at high latitudes, such
  as the Trondheimsfjord in summer.
- Two night windows exist: the rules' and the vessels' in `legata.yaml`, and
  `NightTimeExaminer`'s per zone in `examiner/zones.yaml`. They agree only while both say 20–6.
- "No other lights" is judged only for `encounter` and fog signals, by `NuisanceExaminer`.
  Navigation lights for the wrong status are not. `VesselSignals` lowers them by construction.

## (c) Lights by day in restricted visibility

> The lights prescribed by these Rules shall, if carried, also be exhibited from sunrise to sunset in
> restricted visibility and may be exhibited in all other circumstances when it is deemed necessary.

**Legata.** None of its own. Decided (REQ-056-04): restricted visibility is `(OS, TS).Visibility <
Vessel.RestrictedVisibility.Range` (2 nm), as in Rules 19 and 35. Since 2026-10-19 the light
clauses of Rules 23, 24 and 25 apply when `((OS, TS).Night is true) or ((OS, TS).Visibility <
Vessel.RestrictedVisibility.Range)` (LEGATA.008).

**In the simulation.** By day in restricted visibility a vessel shows its lights and its shapes
together.

**Caveats.** Visibility is one value per scenario (Rule 35), so a vessel shows lights everywhere
or nowhere.

## (d) Shapes by day

> The Rules concerning shapes shall be complied with by day.

**Legata.** None of its own. Shape clauses apply when `(OS, TS).Night is false`: since 2026-10-19
the Rule 24 diamond clauses do (LEGATA.008), and REQ.057 adds the shapes of Rules 26, 27 and 30.

**In the simulation.** Day is the complement of the night window; dawn and dusk are not
distinguished. The `Shape.*` names are in the vocabulary (REQ-056-01).

## (e) Annex I

> The lights and shapes specified in these Rules shall comply with the provisions of Annex I to these
> Regulations.

**Legata.** None.

**Caveats.** Annex I (positioning, colour, intensity, shape dimensions) is not modelled.

## Open issues

- REQ.057: clauses for Rules 23–30.
- REQ-059-01: `VesselSignals` in the other vessel behaviours.
- One night window for rules, vessels and `NightTimeExaminer`.
- `NightTimeExaminer` to require the lights of the vessel's state rather than one list per zone.
- Sunrise and sunset by latitude and date.
- "No other lights" for navigation lights, (b).
