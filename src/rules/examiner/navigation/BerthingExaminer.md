# BerthingExaminer

## Synopsis

The berthing counterpart of `GroundingExaminer`: a vessel at or below `berthing_speed` within `berthing_distance` of land that stands closer to the bottom than its draught allows has touched while berthing, in any zone. Scores contact and near miss against the zone's berthing margin.

## Operation

The arithmetic is identical to grounding — under-keel clearance against a configured margin — so this class subclasses `GroundingExaminer` and overrides no methods at all. The difference is carried by redeclared class attributes: `BERTHING` selects the berthing situation, `CONTACT` and `NEAR_MISS` the berthing events, and `TOPIC` and `MESSAGE` the berthing topic. The situation test is shared, so the two examiners are mutually exclusive on any given vessel and pass. The margin is chosen by zone type for both: `berthing_margin` in the `berthing_zones` types, `grounding_margin` elsewhere. Sharing one implementation means a change to the depth model, the clearance formula or the reporting shape lands in both concerns at once.

## Features

- Zero behavioural code: the class is a few names and a constructor.
- The berthing speed and distance are configuration, per zone if needed.
- Its own margin, typically tighter than the seagoing one, since a harbour approach is expected to be close.
- Its own events and IPC topic, so a subscriber can listen for berthing without hearing groundings.
- Inherits every fix and improvement made to `GroundingExaminer` automatically.

## Known limitations

- Inherits the per-tick scoring problem from `GroundingExaminer`.
- Slow and close to land stands in for berthing: nothing sets `Status.MOORED`, and the maps have no berth or quay shapes.
