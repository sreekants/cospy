# COLREG Rule 7 — Risk of Collision

| | |
|---|---|
| Legata | `Rule7.legata` |
| Driver | `rules.colreg.rule7.Rule7` (`src/rules/colreg/rule7/Rule7.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule7`, **`enable: False`** |
| Simulation | `maritime.regulation.colreg.Classification`, `maritime.regulation.colreg.Encounter`, `maritime.model.rule.EncounterWatch`, `TargetResolver` (`DCPA`, `TCPA`, `OnCollisionCourse`), `RiskExaminer` |
| Tests | none for the rule; classification and watch through the Rule 12–15, 18 and 19 tests |
| Status | Disabled. Risk of collision is determined by the simulation, not judged as a duty |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 7 tells a vessel how to determine risk of collision. The simulation determines it for every
vessel instead, so it can decide when the encounter rules apply:

- **Encounter classification.** The situation module `Encounter` (`situation.yaml`) pairs every
  vessel with each other vessel within `r_colregs_2_max` (4 km). It classifies each pair with
  `classify()`, using bearings and courses and the angles in `evaluator.yaml`: head-on,
  overtaking (give-way or stand-on), crossing (give-way or stand-on), or no applicable rule.
  Pairs that are not closing get no applicable rule. Each class is published as a manoeuvre
  event (`vessel.crossing`, `vessel.overtaking`, `vessel.standon`, `vessel.giveway`).
- **Risk at onset.** `EncounterWatch.at_risk()` judges risk of collision for the fed rules
  (12–15, 18, 19): the vessels are closing, within range, and the predicted passing distance
  (DCPA) is under 500 m.
- **Terms.** `(OS, TS).DCPA`, `TCPA` and `OnCollisionCourse` (closing with DCPA ≤
  `collision.dcpa`, 100 m in `legata.yaml`).
- **Risk over time.** `RiskExaminer` evaluates the probability of collision per assessment from
  a Bayesian network.

The Legata clauses would judge whether own ship had raised alert intents. They are disabled
(COS.047): with nothing raising those intents they recorded nothing.

## (a) Use all available means; if in doubt, risk exists

> Every vessel shall use all available means appropriate to the prevailing circumstances and
> conditions to determine if risk of collision exists. If there is any doubt such risk shall be deemed
> to exist.

**Legata.**
- `clause['COLREG.Rule7.a.Alert']`: within `AlertRange`, assures `OS.Intent in
  ['Alert.SituationAvoidance', 'Alert.CollisionAvoidance']`.
- `clause['COLREG.Rule7.a.Situation']`: within `SituationRange`, assures `OS.Intent has
  'Alert.CollisionAvoidance'`.

**Interpretation.** Determining risk is shown by raising an alert intent.

**In the simulation.** Risk is computed exactly from true positions and velocities (CPA), so it
is never in doubt.

**Caveats.**
- No behaviour raises an `Alert.*` intent.
- `AlertRange` and `SituationRange` are placeholder ranges `(0, 10)` compared with metres.

## (b) Proper use of radar

> Proper use shall be made of radar equipment if fitted and operational, including long-range
> scanning to obtain early warning of risk of collision and radar plotting or equivalent systematic
> observation of detected objects.

**Legata.** `clause['COLREG.Rule7.b']`: when `OS.Capability has 'Equipment.Radar*'`, assures
`OS.Intent has 'Operation.Lookout.Radio*'`.

**Caveats.** Radar is not modelled, and `OS.Capability` is not a term.

## (c) No assumptions on scanty information

> Assumptions shall not be made on the basis of scanty information, especially scanty radar
> information.

**Legata.** None (TODO).

**Caveats.** Not judgeable: the simulation has complete information.

## (d)(i) Compass bearing does not appreciably change

> Such risk shall be deemed to exist if the compass bearing of an approaching vessel does not
> appreciably change;

**Legata.** `clause['COLREG.Rule7.d.i']`: within `AlertRange` and `(TS, OS).Heading.Gradient <
Vessel.Collision.Heading.Collide`, assures `OS.Intent has 'Alert.CollisionAvoidance'`.

**In the simulation.** Equivalent to a small DCPA while closing: `EncounterWatch.at_risk()` and
`OnCollisionCourse`.

**Caveats.** `Heading.Gradient` and `Vessel.Collision.Heading.Collide` are not defined.

## (d)(ii) Risk despite bearing change: large vessels, tows, close range

> such risk may sometimes exist even when an appreciable bearing change is evident, particularly when
> approaching a very large vessel or a tow or when approaching a vessel at close range.

**Legata.** `clause['COLREG.Rule7.d.ii']`, three OR'd lines:
- a large target (`TS.Weight in Vessel.Class.LargeVessel`);
- own ship towing (`OS.Operation has 'Vessel.Operation.TOWING'`);
- within `SituationRange`.

Each assures `Alert.CollisionAvoidance`.

**In the simulation.** The DCPA test does not depend on vessel size, and DCPA is measured
between vessel positions, not hull outlines.

**Caveats.**
- `Vessel.Class.LargeVessel` is not declared.
- Towing is a `Restriction`, not an `Operation`.

## Open issues

- File-level condition `OS.COLREG.Mode is true` and `Environment.Scenario has
  'Risk.Collision'`: not compiled (LEGATA.002), and neither term is set.
- Decide whether Rule 7 stays disabled, with the simulation's determination of risk documented
  as its implementation, or is judged on intents once COS.041 makes intents declarable.
- The 4 km, 500 m and 100 m thresholds are unvalidated.
