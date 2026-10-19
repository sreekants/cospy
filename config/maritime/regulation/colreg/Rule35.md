# COLREG Rule 35 — Sound Signals in Restricted Visibility

| | |
|---|---|
| Legata | `Rule35.legata` |
| Driver | `rules.colreg.rule35.Rule35` (`src/rules/colreg/rule35/Rule35.py`) |
| Loaded by | `rules.colreg.yaml`, entry `Rule35` |
| Terms | `OwnShipResolver` (`FogSignal`), `TargetResolver` (`Visibility`), `VesselResolver` (`Type`, `Status`, `Operation`, `Velocity`); constants `Vessel.RestrictedVisibility.Range` (2.0 nm), `Vessel.MakingWay.Speed` (0.25) |
| Simulation | Signal vocabulary `Sound.Foghorn*`; `NuisanceExaminer` |
| Tests | `tests/maritime/model/colreg/test_Rule35.py` (8) |
| Status | (a)–(c) judged; (d)–(k) not. REQ.057 (REQ-057-06, open) adds (d) and (g)–(j). Not exercised in a run: no scenario has restricted visibility, and no behaviour sounds fog signals |
| Reviewed | 2026-10-19 |

## How the rule is fed

`Rule35.feed()` adds every vessel under test alone (`Situation(own, None)`) on every pass. A
breach that lasts is recorded once per occurrence by the rule's finding guards (10 s release).

A fog signal is a `Sound.Foghorn*` name in the vessel's `signal` set (see Rules 20 and 32).
`OS.FogSignal` is true when any such name is raised.

No behaviour raises a fog signal yet (REQ.058, REQ.059). Once restricted visibility occurs in a
run, every vessel that the clauses cover would breach.

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

**Caveats.**
- Any fog signal passes, not specifically one prolonged blast.
- The 2-minute interval is not judged.
- The 0.25 making-way speed is unsourced.

## (b) Power-driven, underway and stopped: two prolonged blasts

> A power-driven vessel underway but stopped and making no way through the water shall sound at
> intervals of not more than 2 minutes two prolonged blasts in succession with an interval of about 2
> seconds between them.

**Legata.** `clause['COLREG.Rule35.b']`: as (a), but `OS.Status is Vessel.Status.UNDERWAY` and
`OS.Velocity <= Vessel.MakingWay.Speed`.

**Caveats.** Status is `UNKNOWN` until a vessel first weighs anchor (Rule 3(i)). A stopped vessel
that never anchored is therefore not judged under (b).

## (c) Restricted, sailing, fishing and others: one prolonged, two short

> A vessel not under command, a vessel restricted in her ability to manoeuvre, a vessel constrained by
> her draught, a sailing vessel, a vessel engaged in fishing and a vessel engaged in towing or pushing
> another vessel shall, instead of the signals prescribed in paragraphs (a) or (b) of this Rule sound at
> intervals of not more than 2 minutes three blasts in succession, namely one prolonged followed by two
> short blasts.

**Legata.** `clause['COLREG.Rule35.c']`: restricted visibility; not under command, restricted,
sailing or fishing; and not anchored, moored or aground. Assures `OS.FogSignal is true`.

**Caveats.**
- `FASTENED` is not excluded.
- Constrained by draught, towing and pushing are not modelled (Rules 3(h), 24).
- `NOT_UNDER_COMMAND`, `RESTRICTED` and `vessel.operation` are never set, so in a run (c)
  applies to sailing vessels only.

## (d) Fishing or restricted at anchor

> A vessel engaged in fishing, when at anchor, and a vessel restricted in her ability to manoeuvre when
> carrying out her work at anchor, shall instead of the signals prescribed in paragraph (g) of this Rule
> sound the signal prescribed in paragraph (c) of this Rule.

**Legata.** None. REQ-057-06 plans it.

**Caveats.** `state(ANCHORED)` clears the restriction, so a restricted vessel at anchor cannot be
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

**Caveats.** `Sound.Bell*` does not match `Sound.Foghorn*`, so `OS.FogSignal` does not cover the
bell. The clause must test `OS.Signal`.

## (h) Aground: bell with three strokes

> A vessel aground shall give the bell signal and if required the gong signal prescribed in paragraph
> (g) of this Rule and shall, in addition, give three separate and distinct strokes on the bell
> immediately before and after the rapid ringing of the bell. A vessel aground may in addition sound an
> appropriate whistle signal.

**Legata.** None. REQ-057-06 plans it with `Sound.Bell.Strokes.3x`.

## (i) 12–20 m; (j) under 12 m

> (i) A vessel of 12 metres or more but less than 20 metres in length shall not be obliged to give the
> bell signals prescribed in paragraphs (g) and (h) of this Rule. However, if she does not, she shall
> make some other efficient sound signal at intervals of not more than 2 minutes. (j) A vessel of less
> than 12 metres in length shall not be obliged to give the above-mentioned signals but, if she does
> not, shall make some other efficient sound signal at intervals of not more than 2 minutes.

**Legata.** None. REQ-057-06 plans them as exclusions with an alternative signal.

## (k) Pilot vessel identity signal

> A pilot vessel when engaged on pilotage duty may in addition to the signals prescribed in paragraphs
> (a), (b) or (g) of this Rule sound an identity signal consisting of four short blasts.

**Legata.** None. Pilotage is not modelled (Rule 29).

## Related: fog signals outside restricted visibility

`NuisanceExaminer` scores a `restricted_visibility` signal shown in clear visibility outside an
encounter (`signal.nuisance`).

## Open issues

- REQ.058 and REQ.059: behaviours that sound the fog signals.
- REQ-057-06: (d) and (g)–(j).
- Test the specific signal per clause instead of `FogSignal`.
- Exclude `FASTENED` in (c), and judge (b) for vessels with `UNKNOWN` status.
- Restricted visibility by place and time.
