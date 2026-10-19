# GroundingExaminer

## Synopsis

Detects a vessel standing into water too shallow for its draught when it is not berthing. Scores contact with the seabed and near misses as separate events.

## Operation

The examiner requires an own ship in scope, then collects the map shapes enclosing the vessel's position and merges their zone rules. It first asks whether it is answerable at all: a vessel at or below `berthing_speed` within `berthing_distance` of land is berthing and is left to `BerthingExaminer`; every other vessel is judged here, in any zone. It then takes the shallowest `nominal_depth` among the enclosing shapes — shallowest rather than mean, because a vessel grounds on the shallowest thing beneath it — and computes under-keel clearance as depth less draught less the vessel's own `underkeel_clearance` allowance. The margin is `berthing_margin` in the zone types listed under `berthing_zones` and `grounding_margin` elsewhere. A clearance above it passes silently; at or below it the examiner scores `grounding.contact` when the clearance has gone negative and the lighter `grounding.margin` when it has not. The finding is penalised from the scorecard, written to `fact_concern` and published on `/Faculty/Concern/Grounding`.

## Features

- Reads depth from the map's own `Sea.nominal_depth` rather than a separate bathymetry source, so it works with any scenario that builds sea shapes.
- Separates contact from near miss, so a scorecard can price an averted grounding differently from an actual one.
- The margin is per zone and overridable down to an individual map shape's `settings`.
- Berthing and grounding are told apart by speed and distance to land, both configuration, so a contact mid-fjord is a grounding even in internal waters.
- Returns cleanly when the map reports no depth, rather than treating an unknown depth as zero.
- Shares its entire implementation with `BerthingExaminer`, which redeclares six class attributes and nothing else, so the two cannot drift apart as the depth model improves.

## Known limitations

- Scores on every tick the clearance stays low, so one grounding becomes many rows; it needs the once-per-episode guard `NightTimeExaminer` has.
- `nominal_depth` ignores tide and squat, though `Vessel` already carries `squat` and `motion_allowance`.
- No hysteresis, so a vessel oscillating at the margin alternates between contact and near miss.
