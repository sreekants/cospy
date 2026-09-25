# LaneDisciplineExaminer

## Synopsis

Scores a vessel that overtakes another where the zone forbids overtaking. Two conditions must hold together: the zone must bar the manoeuvre, and the own ship must actually be performing it.

## Operation

With both an own ship and a target ship in scope, the examiner merges the zone rules for the map shapes enclosing the vessel and reads the `overtaking` flag. Absence means permitted — a zone that says nothing about overtaking is not thereby forbidding it — and the flag is accepted as a boolean or as one of several string spellings, because values arriving from a map shape's `settings` are always strings. If the zone does bar it, the examiner asks whether the own ship is overtaking by resolving `(OwnShip,TargetShip).EncounterSituation` and matching it against the `OVERTAKING` tuple, rather than re-deriving the geometry from bearings. That delegation is deliberate: it means this examiner and COLREG rule 13 can never disagree about what counts as overtaking, which is the sort of divergence that makes a compliance report indefensible. A match is scored as `lane.overtaking_prohibited`, recorded to `fact_concern` and published on `/Faculty/Concern/Lane` with both IMOs.

## Features

- Reads the COLREG classification instead of re-deriving it, guaranteeing one reading of "overtaking" across the rule set.
- Zone prohibition is configuration, and can be set on a named reach — the Vanikoy–Kanlica stretch of the Istanbul Strait is the worked example in `zones.yaml`.
- Fails open on an unstated rule, which matches how maritime regulation actually reads.
- Handles the boolean-versus-string mismatch between YAML values and map `settings` values.
- `overtaking()` is a classmethod, so a jurisdiction that classifies overtaking under different names can subclass and redeclare the tuple — and `SpeedExaminer`, which calls it, picks up the same reading.

## Known limitations

- The `OVERTAKING` tuple hard-codes situation spellings that also live in `maritime.core.situation.Types`; it should import them.
- Scores per tick for the length of the manoeuvre rather than once per overtake.
- Does not distinguish beginning an overtake inside a barred zone from being mid-manoeuvre when entering one, which is the more defensible reading of the rule.
