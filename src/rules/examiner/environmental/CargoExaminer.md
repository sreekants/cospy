# CargoExaminer

## Synopsis

Checks whether a vessel is carrying a class of payload that the zone it is in does not admit. Scores a violation when the manifest and the zone's restricted list intersect, and reports an absent manifest separately.

## Operation

On each evaluation the examiner confirms its precondition — an own ship in scope — then finds the map shapes enclosing the vessel and merges the zone rules that apply to them. If the merged rules carry no `restricted_cargo` list the zone admits everything and the examiner returns immediately, which keeps the common case cheap. Otherwise it reads the vessel's own manifest from `Vehicle.cargo`, a `ValueSet` built from the vessel's `settings` at construction, and intersects it with the restricted list. A non-empty intersection is scored as `cargo.restricted`, penalised from the scorecard in `config/examiner/zones.yaml`, recorded to `fact_Concern` and published on `/Faculty/Concern/Cargo`. An empty manifest is handled separately as `cargo.undeclared`, because an unconfigured vessel and a genuinely empty hold are indistinguishable here and treating the first as compliant would let a misconfigured vessel pass every cargo rule in the world.

## Features

- Restricted classes are declared per zone in configuration, never in code, so a jurisdiction can be retuned without a rebuild.
- Rules resolve in four layers — map shape `settings`, named zone, `Sea.Type`, then default — so a single reach can override its whole class.
- Accepts the restricted list as either a YAML sequence or a comma-separated string, since map `settings` arrive as strings.
- Distinguishes a barred cargo from an undeclared one, and prices them separately.
- The undeclared report is opt-in via `report.undeclared` in the manifest, so scenarios that legitimately run unladen vessels are not flooded.
- Publishes the carried and restricted sets in the message, so a subscriber can see why it fired without re-deriving it.

## Known limitations

- Fires on every tick a vessel remains in the zone; it has no once-per-episode guard.
- Cargo classes are matched case-sensitively against configuration.
- Has no notion of a permit, though real restricted-cargo regimes are usually conditional rather than absolute.
