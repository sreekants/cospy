# COLREG Rule 19 — Conduct of Vessels in Restricted Visibility

| | |
|---|---|
| Legata | `Rule19.legata` |
| Driver | `rules.colreg.rule19.Rule19` (`src/rules/colreg/rule19/Rule19.py`) |
| Loaded by | `rules.colreg.yaml`, entry `Rule19` |
| Terms | `ColregResolver` (`SafeSpeed`, `WithinSafeSpeed`, `Paired`, `OnsetSpeed`, `ForwardAtOnset`, `InSightAtOnset`, `SlowedSinceOnset`), `TargetResolver` (`Visibility`), `VesselResolver` (`Status`) |
| Settings | `legata.yaml` colreg resolver `stopping.lengths=15`; `definitions.s3db` `Vessel.RestrictedVisibility.Range` = 2.0 nm; ship model `maneuverability.service_speed` and `steerage_speed` (m/s) |
| Tests | `tests/maritime/model/colreg/test_Rule19.py` (15) |
| Status | (b) safe speed and (e) judged; (b) engines ready, (c) and (d) not judged |
| Reviewed | 2026-10-19 |

## How the rule is fed

The driver feeds two kinds of situation on every rule pass (`Rule19.feed()`):

- **Each vessel under test alone** (`Situation(own, None)`), for (b). A finding repeats on every
  pass while the breach lasts. The rule's finding guards record it once per occurrence: a breach
  that clears for longer than the 10 s release is a new occurrence.
- **Each encounter at risk of collision, once past its closest approach**, for (e). This uses an
  `EncounterWatch` of every encounter type. An encounter begins when the other vessel is within
  4 km (`encounter.range`), the two are closing, and the predicted passing distance is under
  500 m (`encounter.dcpa`). When the encounter begins, the watch records own ship's speed,
  whether the other vessel is forward of her beam, and whether it is in sight. The situation
  is judged on that record once the range opens.

`(OS, TS).Paired` tells the two apart, so (b) is judged once per vessel and not again for each
encounter.

## (a) Application

> This Rule applies to vessels not in sight of one another when navigating in or near an area of
> restricted visibility.

**Legata.** No clause of its own. The scope is a condition in each judged clause, because a
file-level `condition:` block is not compiled (LEGATA.002).

**Interpretation.**
- *Restricted visibility* is the scenario's visibility being under
  `Vessel.RestrictedVisibility.Range` (2 nm): `(OS, TS).Visibility < Vessel.RestrictedVisibility.Range`.
  It is the same test Rule 35 uses.
- *Not in sight* is judged when the encounter begins: the other vessel was further away than the
  visibility (`(OS, TS).InSightAtOnset is false`). A pair that was already in sight is left to
  Section II (Rules 11–18).

**In the simulation.** Visibility is one value per scenario: the midpoint of the `WEATHER`
profile's range in `weather/profiles.yaml` (`TargetResolver`). So every vessel is either in
restricted visibility for the whole run or never.

**Caveats.**
- "In or near an area of restricted visibility" is not modelled. No map has
  restricted-visibility areas, and visibility does not vary with place or time. The original
  test (`Map.Sky@RestrictedVisibility`) was removed.
- Being in sight is judged by distance alone, at the start. A vessel that comes into sight
  later is still judged under (e).
- The 2 nm threshold is a declared constant with no recorded source.

## (b) Safe speed; engines ready

> Every vessel shall proceed at a safe speed adapted to the prevailing circumstances and conditions
> of restricted visibility. A power-driven vessel shall have her engines ready for immediate
> manoeuvre.

**Legata.** `clause['COLREG.Rule19.b']`:
- **condition:** visibility restricted, and `(OS, TS).SafeSpeed > 0`;
- **excluded:** a paired situation, or own ship not underway (anchored, moored, made fast or
  aground);
- **assured:** `(OS, TS).WithinSafeSpeed is true`.

**Interpretation.** A safe speed lets own ship stop within half the visibility, the half-distance
test of seamanship and case law. The stopping distance at speed v is taken as
`k · L · (v / v_s)²`, where:
- L is the ship's length;
- v_s is its service speed;
- k = `stopping.lengths` (15), the IMO upper bound on track reach in a full-astern stop
  (MSC.137(76), 5.3.1).

That gives `SafeSpeed = v_s · √(½ · visibility / (k · L))`, in metres per second. Every vessel
type is judged, not only power-driven ones, because the first sentence applies to every vessel.

**In the simulation.** Own speed is the magnitude of the vessel's velocity. Length comes from the
ship model (`physics.length`), service speed from `maneuverability.service_speed`, and visibility
from the scenario.

**Caveats.**
- **Service speeds are sourced per ship model** (2026-10-19), in m/s, with the source in each
  YAML comment (MAN Energy Solutions propulsion-trend papers, builder datasheets, published
  specifications of the reference vessels). (b) is judged for every ship model. A model without
  one is skipped, with a warning once per model type (LEGATA.052).
- k = 15 is a regulatory upper bound, not the ship's own stopping performance, so the safe speed
  is conservative for a ship that stops better than the limit.
- Assuming stopping distance grows with the square of speed (constant deceleration) is a
  simplification.
- Traffic density, sea state and manoeuvrability are not taken into account, though they are
  among the "prevailing circumstances".
- "Engines ready for immediate manoeuvre" is not judged: no behaviour sets `Vessel.Engine.ON`, so
  judging it would flag every power-driven vessel.
- A breach is a speed over the bound on any pass. A short excursion counts as much as a long one.

## (c) Due regard when applying Section I

> Every vessel shall have due regard to the prevailing circumstances and conditions of restricted
> visibility when complying with the Rules of Section I of this Part.

**Legata.** None. The clause is a comment.

**Interpretation.** A general duty that qualifies Rules 4–10. It is judged through those rules,
not on its own.

**Caveats.**
- Rules 5–10 are not fed yet (COS.022), so nothing judges it today.
- The original clause (`assure: abort` on an unresolved `OS.Situation` term) was removed.

## (d) Radar alone: avoiding action, and course alterations to avoid

> A vessel which detects by radar alone the presence of another vessel shall determine if a
> close-quarters situation is developing and/or risk of collision exists. If so, she shall take
> avoiding action in ample time, provided that when such action consists of an alteration of course,
> so far as possible the following shall be avoided: (i) an alteration of course to port for a
> vessel forward of the beam, other than for a vessel being overtaken; (ii) an alteration of course
> towards a vessel abeam or abaft the beam.

**Legata.** None. The clause is a comment.

**Interpretation.** It would need four things:
- detection by radar alone;
- a test for whether a close-quarters situation is developing;
- that the action came in ample time;
- the direction of any course change, relative to the other vessel's bearing.

**Caveats.**
- Not judged. There is no course- or speed-change term (COS.041), and the original assurance
  tested `OS.Manouever`, which no behaviour sets. Once fed, it would have flagged every
  encounter.
- Detection is not modelled by sensor: `(OS, TS).Detect` lists the target's signals, not how own
  ship detected it.
- "Ample time" has no source. `Vessel.Collision.TimeToEncounter.*` are placeholder ranges
  `(0, 10)`.

## (e) Fog signal or close quarters forward of the beam: reduce speed

> Except where it has been determined that a risk of collision does not exist, every vessel which
> hears apparently forward of her beam the fog signal of another vessel, or which cannot avoid a
> close-quarters situation with another vessel forward of her beam, shall reduce her speed to the
> minimum at which she can be kept on her course. She shall if necessary take all her way off and in
> any event navigate with extreme caution until danger of collision is over.

**Legata.** `clause['COLREG.Rule19.e']`:
- **condition:** visibility restricted, `(OS, TS).ForwardAtOnset is true`, and
  `(OS, TS).InSightAtOnset is false`;
- **excluded:** `(OS, TS).OnsetSpeed <= 0`, or own ship not underway;
- **assured:** `OS.Velocity <= OS.SteerageSpeed`. Until 2026-10-19 it assured
  `SlowedSinceOnset`, so any reduction complied (LEGATA.053).

**Interpretation.**
- *Risk of collision* (the "except where" clause) is the encounter watch's own test. An encounter
  begins only when the vessels are closing, within 4 km, with a predicted passing distance under
  500 m.
- *Forward of her beam:* the other vessel bore less than 90° from own ship's course at the start.
- *Reduce her speed to the minimum at which she can be kept on her course:* at the closest
  approach own ship is no faster than her ship model's `steerage_speed`. A ship model without one
  is not judged.
- An own ship already stopped at the start has no way to take off and is not judged.
- Each encounter is judged once, after the closest approach, on what held at its start. A
  vessel is not flagged before she has had time to react, and each encounter is one finding.

**In the simulation.** The start is recorded by `Rule19.snapshot()`. Speed at the closest
approach is own ship's speed on the pass after the range starts to open.

**Caveats.**
- The steerage speed is 4 knots (2.06 m/s) for the merchant ship and ferry models: the midpoint
  of the "3.5–4.5 knots" manoeuvring speed in MAN's *Basic Principles of Ship Propulsion*. The tug,
  AUV, yachts and motorboat have no sourced steerage speed and are not judged under (e).
- No behaviour slows to steerage speed in fog, so every judged vessel that does not stop will
  breach (e) in a run with restricted visibility.
- Taking all way off "if necessary" and navigating "with extreme caution" are not judged.
- The fog-signal trigger is not modelled separately. Only container ships, ferries and fishing
  vessels sound fog signals (Rule 35), and the encounter trigger stands in for it: both need the other vessel forward of
  the beam at risk of collision. A fog signal heard from a vessel not at risk is not judged.
- The 4 km range and 500 m passing distance are unvalidated constants, shared with Rules 12, 15
  and 18.
- Speed is compared at two moments only. A vessel that slowed and then sped up again before
  the closest approach can still fail, and one that slowed only at the last moment complies.
- Not exercised in a run: no scenario has restricted visibility yet.

## Open issues

- Steerage speeds for the tug, AUV, yacht and motorboat models (for (e)).
- A course-change term (COS.041), for (d) and for whether the action in (e) came in time.
- Something that sets `Vessel.Engine.ON` (engines ready, (b)).
- Per-area or time-varying visibility (for (a)).
- LEGATA.002, after which the scope could move to a file-level condition.
