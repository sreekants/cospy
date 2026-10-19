# COLREG Rule 35 — Sound Signals in Restricted Visibility

| | |
|---|---|
| Legata | `Rule35.legata` |
| Driver | `rules.colreg.rule35.Rule35` (`src/rules/colreg/rule35/Rule35.py`) |
| Loaded by | `rules.colreg.yaml`, entry `Rule35` |
| Terms | `OwnShipResolver` (`FogSignal`), `TargetResolver` (`Visibility`), `VesselResolver` (`Type`, `Status`, `Operation`, `Velocity`); constants `Vessel.RestrictedVisibility.Range` (2.0 nm), `Vessel.MakingWay.Speed` (0.25) |
| Simulation | Signal vocabulary `Sound.Foghorn*`, `Sound.Bell*`, `Sound.Gong`; `VesselSignals.fog_signals`; `NuisanceExaminer` |
| Tests | `tests/maritime/model/colreg/test_Rule35.py` (8) |
| Status | (a)–(c) judged; (d)–(k) not. REQ.057 (REQ-057-06, open) adds (d) and (g)–(j). Container ships, ferries and fishing vessels sound fog signals; not exercised in a run, as no scenario has restricted visibility |
| Reviewed | 2026-10-19 |

## How the rule is fed

`Rule35.feed()` adds every vessel under test alone (`Situation(own, None)`) on every pass. A
breach that lasts is recorded once per occurrence by the rule's finding guards (10 s release).

A fog signal is a `Sound.Foghorn*` name in the vessel's `signal` set (see Rules 20 and 32).
`OS.FogSignal` is true when any such name is raised.

**In the simulation.** `VesselSignals.fog_signals` raises the signal for the vessel's state
(Rule 20) while the scenario visibility is under `Vessel.RestrictedVisibility.Range`, and lowers
it otherwise. The signal is a name held in the set, not a timed blast: it stands for sounding at
the prescribed interval. `SailingVessel`, `Motorboat`, `Yacht`, `RestrictedAbilityManeuver` and
`AnchoredVessel` do not run it yet (REQ-059-01, -04), so they would breach once restricted
visibility occurs.

**Checked against the behaviour** (2026-10-19, in the COLREG test harness, not in a run). For
each `VesselSignals` state, the sound it raises in fog satisfies (a)–(c), and without it the
vessel breaches the clause for its state. Anchored, aground and fishing at anchor are not judged
either way, as (d), (g) and (h) have no clauses. Whether the behaviour raises the signal before
the rule reads it in a live tick is untested: no scenario has restricted visibility.

## Opening: in or near restricted visibility, by day or night

> In or near an area of restricted visibility, whether by day or night, the signals prescribed in this
> Rule shall be used as follows:

**Legata.** In each clause: `(OS, TS).Visibility < Vessel.RestrictedVisibility.Range`.

**Interpretation.** Restricted visibility is the scenario visibility (the midpoint of the
`WEATHER` profile range) under 2 nm.

**Caveats.**
- "In or near an area" is not modelled: visibility is one value per scenario.
- The 2 nm threshold is unsourced.

## (a) Power-driven, making way: one prolonged blast

> A power-driven vessel making way through the water shall sound at intervals of not more than 2 minutes
> one prolonged blast.

**Legata.** `clause['COLREG.Rule35.a']`:
- **condition:** restricted visibility, power-driven, `OS.Velocity > Vessel.MakingWay.Speed`;
- **excluded:** not under command, restricted, sailing or fishing (they owe (c));
- **assured:** `OS.FogSignal is true`.

**In the simulation.** `Sound.Foghorn.Prolonged.1x` while the behaviour's speed (`dx`) is above
`Vessel.MakingWay.Speed`, at every length.

**Caveats.**
- Any fog signal passes, not specifically one prolonged blast.
- The 2-minute interval is not judged.
- The 0.25 making-way speed is unsourced.
- Making way is the behaviour's speed, not the speed through the water.

## (b) Power-driven, underway and stopped: two prolonged blasts

> A power-driven vessel underway but stopped and making no way through the water shall sound at
> intervals of not more than 2 minutes two prolonged blasts in succession with an interval of about 2
> seconds between them.

**Legata.** `clause['COLREG.Rule35.b']`: as (a), but underway as Rule 3(i) defines it (status none
of `ANCHORED`, `MOORED`, `FASTENED`, `AGROUND`) and `OS.Velocity <= Vessel.MakingWay.Speed`.

**Interpretation.** Underway is tested by exclusion because a vessel's status stays `UNKNOWN`
until it first weighs anchor.

**Caveats.** As (a): any fog signal passes, so a stopped vessel sounding one prolonged blast
complies.

**In the simulation.** `Sound.Foghorn.Prolonged.2x` at or below the making-way speed. An
anchored vessel, with zero speed, sounds (g) instead.

## (c) Restricted, sailing, fishing and others: one prolonged, two short

> A vessel not under command, a vessel restricted in her ability to manoeuvre, a vessel constrained by
> her draught, a sailing vessel, a vessel engaged in fishing and a vessel engaged in towing or pushing
> another vessel shall, instead of the signals prescribed in paragraphs (a) or (b) of this Rule sound at
> intervals of not more than 2 minutes three blasts in succession, namely one prolonged followed by two
> short blasts.

**Legata.** `clause['COLREG.Rule35.c']`: restricted visibility; not under command, restricted,
sailing or fishing; and underway as Rule 3(i) defines it. Assures `OS.FogSignal is true`.

**In the simulation.** `Sound.Foghorn.Prolonged.Short.2x` for the not under command,
restricted, trawling, fishing and sailing rows, whether making way or not.

**Caveats.**
- Any fog signal passes: a sailing or fishing vessel sounding the power-driven
  `Sound.Foghorn.Prolonged.1x` complies.
- Constrained by draught, towing and pushing are not modelled (Rules 3(h), 24).
- `NOT_UNDER_COMMAND` and `RESTRICTED` are never set (REQ-059-03), so in a run (c) applies to
  sailing and fishing vessels only.

## (d) Fishing or restricted at anchor

> A vessel engaged in fishing, when at anchor, and a vessel restricted in her ability to manoeuvre when
> carrying out her work at anchor, shall instead of the signals prescribed in paragraph (g) of this Rule
> sound the signal prescribed in paragraph (c) of this Rule.

**Legata.** None. REQ-057-06 plans it.

**In the simulation.** A vessel fishing at anchor sounds `Sound.Foghorn.Prolonged.Short.2x`, not the
bell (`VesselSignals`).

**Caveats.**
- Not judged: (c) excludes vessels at anchor, and (d) has no clause, so a vessel fishing at
  anchor that sounds nothing, or rings the bell, is not caught.
- `state(ANCHORED)` clears the restriction, so a restricted vessel at anchor cannot be
  recognised (Rule 27(b)(iv)).

## (e) Towed vessel; (f) composite unit

> (e) A vessel towed or if more than one vessel is towed the last vessel of the tow, if manned, shall at
> intervals of not more than 2 minutes sound four blasts in succession, namely one prolonged followed by
> three short blasts … (f) When a pushing vessel and a vessel being pushed ahead are rigidly connected in
> a composite unit they shall be regarded as a power-driven vessel and shall give the signals prescribed
> in paragraphs (a) or (b) of this Rule.

**Legata.** None. Towing is not modelled.

## (g) At anchor: bell, and gong for 100 m or more

> A vessel at anchor shall at intervals of not more than one minute ring the bell rapidly for about 5
> seconds. In a vessel of 100 metres or more in length the bell shall be sounded in the forepart of the
> vessel and immediately after the ringing of the bell the gong shall be sounded rapidly for about 5
> seconds in the after part of the vessel. A vessel at anchor may in addition sound three blasts in
> succession, namely one short, one prolonged and one short blast …

**Legata.** None. REQ-057-06 plans it with `Sound.Bell` and `Sound.Gong` (REQ-056-01).

**In the simulation.** `Sound.Bell` at every length, and `Sound.Gong` as well at 100 m or more.
The optional short-prolonged-short warning is not sounded.

**Caveats.**
- Not judged: with no clause, a vessel at anchor without the bell or the gong is not caught.
- `Sound.Bell*` does not match `Sound.Foghorn*`, so `OS.FogSignal` does not cover the bell.
  The clause must test `OS.Signal`.

## (h) Aground: bell with three strokes

> A vessel aground shall give the bell signal and if required the gong signal prescribed in paragraph
> (g) of this Rule and shall, in addition, give three separate and distinct strokes on the bell
> immediately before and after the rapid ringing of the bell. A vessel aground may in addition sound an
> appropriate whistle signal.

**Legata.** None. REQ-057-06 plans it with `Sound.Bell.Strokes.3x`.

**In the simulation.** `Sound.Bell` and `Sound.Bell.Strokes.3x`, with `Sound.Gong` at 100 m or
more. The optional whistle signal is not sounded.

**Caveats.** Not judged: with no clause, a vessel aground without the bell, the strokes or the
gong is not caught.

## (i) 12–20 m; (j) under 12 m

> (i) A vessel of 12 metres or more but less than 20 metres in length shall not be obliged to give the
> bell signals prescribed in paragraphs (g) and (h) of this Rule. However, if she does not, she shall
> make some other efficient sound signal at intervals of not more than 2 minutes. (j) A vessel of less
> than 12 metres in length shall not be obliged to give the above-mentioned signals but, if she does
> not, shall make some other efficient sound signal at intervals of not more than 2 minutes.

**Legata.** None. REQ-057-06 plans them as exclusions with an alternative signal.

**In the simulation.** `VesselSignals` rings the bell (and gives the strokes aground) at every
length, which (i) and (j) allow, so no alternative signal is modelled.

## (k) Pilot vessel identity signal

> A pilot vessel when engaged on pilotage duty may in addition to the signals prescribed in paragraphs
> (a), (b) or (g) of this Rule sound an identity signal consisting of four short blasts.

**Legata.** None. Pilotage is not modelled (Rule 29).

## Related: fog signals outside restricted visibility

`NuisanceExaminer` scores a `restricted_visibility` signal shown in clear visibility outside an
encounter (`signal.nuisance`).

## Open issues

- REQ-059-01, -04: the other behaviours sound the fog signals.
- REQ-057-06: (d) and (g)–(j).
- Test the specific signal per clause instead of `FogSignal`.
- A run with restricted visibility, to confirm the signals are raised before the rule reads them.
- Restricted visibility by place and time.
