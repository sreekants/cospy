# COLREG Rule 13 — Overtaking

| | |
|---|---|
| Legata | `Rule13.legata` |
| Driver | `rules.colreg.rule13.Rule13` (`src/rules/colreg/rule13/Rule13.py`) |
| Loaded by | `rules.colreg.yaml`, entry `Rule13` (`encounter.dcpa`, `encounter.range` optional) |
| Terms | `ColregResolver` (`EncounterSituation`), `TargetResolver` (`Distance`); constant `Vessel.Collision.PassingDistance` (100 m) |
| Simulation | `Classification.classify()` (overtaking angles in `evaluator.yaml`), `EncounterWatch` (role `OTGW`) |
| Tests | `tests/maritime/model/colreg/test_Rule13.py` (5) |
| Status | (a) judged; (b) and (d) met by construction; (c) not judged. Judged in a run: 328 encounters, 0 breaches (case 3017189162921500) |
| Reviewed | 2026-10-19 |

## How the rule is fed

`Rule13.feed()` runs an `EncounterWatch` for `Encounter.OTGW`, own ship overtaking.

- **Onset:** `classify()` names the pair overtaking, the other vessel is within 4 km
  (`encounter.range`), they are closing, and the predicted passing distance is under 500 m
  (`encounter.dcpa`).
- **Role:** the watch claims the role `Overtaking` for the pair in the shared registry
  `EncounterWatch.roles`, so Rules 14 and 15 do not take the same encounter.
- **Judgement:** the situation is queued once the range opens past the closest approach. It
  carries the role recorded at onset (`situation.maneuvers['Overtaking']`).

The driver also subscribes to `vessel.overtaking` and `vessel.crossing`; the handlers do nothing.

## (a) The overtaking vessel keeps out of the way

> Notwithstanding anything contained in the Rules of Part B, Sections I and II any vessel overtaking
> any other shall keep out of the way of the vessel being overtaken.

**Legata.** `clause['COLREG.Rule13.a']`:
- **condition:** `(OS, TS).EncounterSituation is 'Overtaking'`;
- **assured:** `(OS, TS).Distance >= Vessel.Collision.PassingDistance`.

**Interpretation.**
- *Keep out of the way:* passed the other vessel at the passing distance or more at the closest
  approach. Judged by outcome, not by the manoeuvre.
- *Notwithstanding Sections I and II:* the other encounter watches (Rules 12, 15, 18) skip a
  pair already held as overtaking.

**In the simulation.** Overtaking vessels slow down behind the vessel ahead
(`VesselManeuvers.overtaking_distance`, below `overtake_lat_min`). No behaviour steers round to
overtake.

**Caveats.**
- The 100 m passing distance is a constant, the same for every size of vessel.
- Applies to every vessel type, as the rule does.
- No breaches in the run: the behaviours slow down rather than overtake closely.

## (b) Definition of overtaking

> A vessel shall be deemed to be overtaking when coming up with another vessel from a direction more
> than 22.5 degrees abaft her beam, that is, in such a position with reference to the vessel she is
> overtaking, that at night she would be able to see only the sternlight of that vessel but neither of
> her sidelights.

**Legata.** None. It is a definition.

**In the simulation.** `classify()` returns `OTGW` when:
- own ship lies more than 22.5° abaft the other's beam, as seen from the other vessel (a bearing
  between `theta_ot_min` = 112.5° and `theta_ot_max` = 247.5°);
- the other vessel is within `theta_critical_ot` (45°) of own ship's bow;
- own ship is faster.

`OTSO` is the mirror, for the vessel being overtaken.

**Caveats.** The 45° bow sector is an added condition, not in the rule text. Lights are not
used; geometry stands in for "see only the sternlight".

## (c) In doubt, assume overtaking

> When a vessel is in any doubt as to whether she is overtaking another, she shall assume that this is
> the case and act accordingly.

**Legata.** None ("intentional doubt, beyond scope").

**Caveats.** Classification is exact, so a vessel is never in doubt. Pairs near the 112.5°
boundary are classified one way or the other.

## (d) Bearing changes do not end the duty

> Any subsequent alteration of the bearing between the two vessels shall not make the overtaking
> vessel a crossing vessel within the meaning of these Rules or relieve her of the duty of keeping
> clear of the overtaken vessel until she is finally past and clear.

**Legata.** None. Met by construction.

**In the simulation.**
- The role recorded at onset is the one (a) is judged on, whatever the bearing at the closest
  approach.
- The shared role registry stops the crossing watch (Rule 15) from claiming the pair while the
  overtaking encounter lasts.
- Watches of every type (Rules 12, 18, 19) skip a pair held as overtaking.

**Caveats.** "Finally past and clear" is the range starting to open, not a clearance distance.

## Open issues

- Validate the 100 m passing distance, scaled by vessel size or not, and the 4 km and 500 m onset
  thresholds.
- Check the run's encounters case by case for L6 verification.
