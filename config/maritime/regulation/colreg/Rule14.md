# COLREG Rule 14 — Head-on Situation

| | |
|---|---|
| Legata | `Rule14.legata` |
| Driver | `rules.colreg.rule14.Rule14` (`src/rules/colreg/rule14/Rule14.py`), its own onset detector (`observe()`, `head_on()`) |
| Loaded by | `rules.colreg.yaml`, entry `Rule14`: `headon.angle=13 headon.range=4000 headon.dcpa=500` |
| Terms | `ColregResolver` (`HeadOn`, `PassingSide`) |
| Tests | `tests/maritime/model/colreg/test_Rule14.py` (14), `tests/rules/colreg/rule14/test_Rule14.py` (3) |
| Status | (a) judged; (b) applied as the onset test; (c) not judged. Judged in a run: 26 encounters, 5 breaches (case 3017189162921500) |
| Reviewed | 2026-10-19 |

## How the rule is fed

`Rule14.feed()` calls `observe()`, its own detector. It is not an `EncounterWatch`.

- **Onset:** `head_on()` holds when:
  - the courses are reciprocal within `headon.angle` (13°);
  - the other vessel is ahead within the same angle;
  - the vessels are closing, within `headon.range` (4 km);
  - the predicted passing distance is under `headon.dcpa` (500 m).
- **Judgement:** the pair is queued once the range opens past the closest approach, marked
  `situation.maneuvers['HeadOn']`.
- **Both vessels:** each vessel of the pair is judged as own ship in its turn.

## (a) Each alters to starboard and passes port to port

> When two power-driven vessels are meeting on reciprocal or nearly reciprocal courses so as to involve
> risk of collision each shall alter her course to starboard so that each shall pass on the port side
> of the other.

**Legata.** `clause['COLREG.Rule14.a']`:
- **condition:** `(OS, TS).HeadOn is true`;
- **assured:** `(OS, TS).PassingSide is 'Port'`.

**Interpretation.** Judged by outcome. At the closest approach the other vessel must be on own
ship's port side, given by the sign of the cross product of own heading with the offset to the
target (`passing_side()`). Altering to port, or standing on into a starboard-to-starboard pass,
both fail.

**In the simulation.** No behaviour alters course for a head-on meeting. The pass happens on
whichever side the vessels' tracks give. The 5 breaches in the run are vessels that passed
starboard to starboard.

**Caveats.**
- Both vessels must be power-driven (a condition in the clause, COS.056). A head-on meeting with a
  sailing vessel, or one not under command, restricted or fishing, is left to Rule 18.
- The alteration to starboard itself is not judged, only the side of the pass. A pass to port
  that needed no alteration complies.
- Passing distance is not judged.
- `PassingSide` is `'Unknown'` when own ship is stopped or exactly in line, which fails the
  assurance.

## (b) When a head-on situation exists

> Such a situation shall be deemed to exist when a vessel sees the other ahead or nearly ahead and by
> night she could see the masthead lights of the other in a line or nearly in a line and/or both
> sidelights and by day she observes the corresponding aspect of the other vessel.

**Legata.** None. It is a definition.

**In the simulation.** `head_on()`, as above. The masthead-light and aspect tests reduce to the
same geometry: reciprocal courses, the other vessel ahead. `classify()` uses the same angle
(`theta_critical_ho`, 13°) for `Encounter.HO`.

**Caveats.** The 13°, 4 km and 500 m thresholds are unvalidated. Rule 14 records no role in the
shared registry, so another watch may also take a head-on pair.

## (c) In doubt, assume head-on

> When a vessel is in any doubt as to whether such a situation exists she shall assume that it does
> exist and act accordingly.

**Legata.** None ("intentional doubt, beyond scope").

**Caveats.** Geometry is exact. Pairs just outside 13° are not head-on, though a mariner in doubt
would treat them so.

## Open issues

- Check the run's 5 breaches case by case.
