# COLREG Rule 34 — Manoeuvring and Warning Signals

| | |
|---|---|
| Legata | `Rule34.legata` (text only) |
| Driver | `rules.colreg.rule34.Rule34` (`src/rules/colreg/rule34/Rule34.py`); subscribes to `vessel.overtaking`, and the handler does nothing |
| Loaded by | `rules.colreg.yaml`, entry `Rule34` |
| Simulation | `SignalExaminer` (posts `(intent, situation)` tuples), `NuisanceExaminer`; signal names `Sound.Blast.Short.*`, `Light.Flash.*` |
| Tests | none for the rule |
| Status | Not judged. Deferred (REQ.056 decision); needs a course-change term and intents for manoeuvres |
| Reviewed | 2026-10-19 |

## How the rule is employed

**What exists.**
- **Vocabulary:** `Sound.Blast.Short.1x`, `.2x`, `.3x` (starboard, port, astern) and `.5x`
  (doubt), and the light equivalents `Light.Flash.1x`–`.5x`, all of class `encounter`.
- **`SignalExaminer`** collects, on each change, own ship's declared intent and the encounter
  situation (`(OwnShip,TargetShip).EncounterSituation`). It publishes the pair on
  `/Faculty/Regulation/Rules` as `vessel.signal`. It judges nothing, so that Rule 34 can own the
  judgement.
- **`NuisanceExaminer`** scores an `encounter` signal shown outside an encounter
  (`signal.nuisance`, REQ.036).

**What is missing.**
- Rule 34 does not subscribe to `vessel.signal`.
- No behaviour raises an intent for an alteration of course or astern propulsion. No behaviour
  alters course to avoid collision at all (Rule 8).
- No behaviour sounds a manoeuvring signal. `VesselSignals` leaves `encounter` signals alone
  and never raises them.

So whether a signal accompanied a manoeuvre cannot yet be judged.

## (a) Whistle signals for a manoeuvre, in sight

> When vessels are in sight of one another, a power-driven vessel underway, when manoeuvring as
> authorized or required by these Rules, shall indicate that manoeuvre by the following signals on her
> whistle: one short blast to mean 'I am altering my course to starboard'; two short blasts to mean 'I
> am altering my course to port'; three short blasts to mean 'I am operating astern propulsion'.

**Legata.** None.

**Interpretation needed.**
- A manoeuvre: a course change above a threshold to one side, or astern propulsion (negative
  thrust), detected over time.
- The signal: `Sound.Blast.Short.1x`, `.2x` or `.3x` raised while it lasts.
- In sight: `(OS, TS).Visible`.

**Caveats.** Needs a course-change term (COS.041). Astern propulsion is not modelled; speed only
scales down.

## (b) Light signals

> Any vessel may supplement the whistle signals prescribed in paragraph (a) of this Rule by light
> signals, repeated as appropriate, whilst the manoeuvre is being carried out: (i) one flash … two
> flashes … three flashes …; (ii) the duration of each flash shall be about one second, the interval
> between flashes shall be about one second, and the interval between successive signals shall be not
> less than ten seconds; (iii) the light used for this signal shall, if fitted, be an all-round white
> light, visible at a minimum range of 5 miles …

**Legata.** None.

**Caveats.** Optional. It could be judged only as a mismatch with the whistle signal. Timing is
not modelled (Rule 32).

## (c) Overtaking in a narrow channel

> When in sight of one another in a narrow channel or fairway: (i) a vessel intending to overtake
> another shall in compliance with Rule 9(e)(i) indicate her intention by the following signals on her
> whistle: two prolonged blasts followed by one short blast … two prolonged blasts followed by two short
> blasts …; (ii) the vessel about to be overtaken when acting in accordance with Rule 9(e)(i) shall
> indicate her agreement by the following signal on her whistle: one prolonged, one short, one
> prolonged and one short blast, in that order.

**Legata.** None. Rule 9(d) and (e) `apply` clauses named `COLREG.Rule34.c.i*` and `34.d*`, which
do not exist.

**Caveats.** No vocabulary names exist for these signals. Narrow channels cannot be identified
(Rule 9).

## (d) Doubt: at least five short blasts

> When vessels in sight of one another are approaching each other and from any cause either vessel
> fails to understand the intentions or actions of the other, or is in doubt whether sufficient action
> is being taken by the other to avoid collision, the vessel in doubt shall immediately indicate such
> doubt by giving at least five short and rapid blasts on the whistle. Such signal may be supplemented
> by a light signal of at least five short and rapid flashes.

**Legata.** None.

**Interpretation needed.** "Doubt" could be read as: the stand-on vessel at close quarters while
the give-way vessel has not acted. That needs Rule 17's action measure.

## (e) Bends; (f) whistles more than 100 m apart

> (e) A vessel nearing a bend or an area of a channel or fairway where other vessels may be obscured by
> an intervening obstruction shall sound one prolonged blast. Such signal shall be answered with a
> prolonged blast by any approaching vessel that may be within hearing around the bend or behind the
> intervening obstruction. (f) If whistles are fitted on a vessel at a distance apart of more than 100
> metres, one whistle only shall be used for giving manoeuvring and warning signals.

**Legata.** None.

**Caveats.** Bends and obstructions are not modelled. (f) concerns equipment.

## Open issues

- Deferred by REQ.056. The prerequisites are a course- and speed-change term (COS.041),
  manoeuvre intents raised by behaviours, and a Rule 34 subscriber to `SignalExaminer`'s
  `vessel.signal` posts.
- Vocabulary names for (c) and (e).
