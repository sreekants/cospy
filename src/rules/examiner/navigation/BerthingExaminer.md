# BerthingExaminer

## Synopsis

The inland counterpart of `GroundingExaminer`: a vessel in internal waters, a harbour or a waterway that stands closer to the bottom than its draught allows has berthed, whether or not it meant to. Scores contact and near miss against the zone's berthing margin.

## Operation

The arithmetic is identical to grounding — under-keel clearance against a configured margin — so this class subclasses `GroundingExaminer` and overrides no methods at all. The difference is carried entirely by six redeclared class attributes: `ZONES` points at `berthing_zones` instead of `grounding_zones`, `MARGIN` at `berthing_margin`, `CONTACT` and `NEAR_MISS` at the berthing events, and `TOPIC` and `MESSAGE` at the berthing topic. The inherited scorer reads all six through `self`, so ordinary attribute lookup routes a berthing instance to berthing configuration without a single conditional. Because `berthing_zones` lists the inland `Sea.Type` values and `grounding_zones` the seagoing ones, the two examiners are mutually exclusive on any given vessel and neither needs to know the other exists. Sharing one implementation means a change to the depth model, the clearance formula or the reporting shape lands in both concerns at once.

## Features

- Zero behavioural code: the class is six names and a constructor.
- Inland zone types are configuration, so the berthing/grounding boundary moves per jurisdiction without a code change.
- Its own margin, typically tighter than the seagoing one, since a harbour approach is expected to be close.
- Its own events and IPC topic, so a subscriber can listen for berthing without hearing groundings.
- Inherits every fix and improvement made to `GroundingExaminer` automatically.

## Known limitations

- Inherits the per-tick scoring problem from `GroundingExaminer`.
- Does not distinguish an intentional berthing from running aground in shallow water, though `Vessel.moored()` already exists to tell them apart.
