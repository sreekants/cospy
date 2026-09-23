# SpeedExaminer

## Synopsis

Penalises a vessel exceeding the speed limit of the zone it is in. Scores a heavier, separate event when the limit is broken while overtaking.

## Operation

The precondition names only the own ship, because a speed limit applies whether or not another vessel is present; the overtaking aggravation is tested afterwards and needs a target. The examiner merges the zone rules for the shapes enclosing the vessel and reads `speed_limit`, returning immediately when the zone is unrestricted, then resolves `OwnShip.Velocity` and compares it against the limit plus a configured `tolerance` of slack. On a breach it asks whether the vessel is also overtaking, delegating to `LaneDisciplineExaminer.overtaking()` so that both examiners read the same COLREG classification, and selects `speed.limit_exceeded_overtaking` or plain `speed.limit_exceeded` accordingly. Note the deliberate asymmetry with lane discipline: overtaking need not be prohibited in this zone for the aggravation to apply, because speeding in order to get past another vessel is worse even where overtaking itself is allowed. The excess over the limit is carried into the record as the finding's value, and the whole assessment is published on `/Faculty/Concern/Speed`.

## Features

- Two distinct events let the scorecard price ordinary speeding and speeding-to-overtake differently, without this examiner deciding by how much.
- Speed limits are per zone and overridable down to an individual map shape.
- A configurable tolerance absorbs sensor noise around the limit.
- The excess is recorded as a quantity, so a downstream analysis can weight by severity even though the penalty itself is flat.
- Shares the overtaking test with `LaneDisciplineExaminer`, so the two can never disagree.
- Reports whether the aggravation applied in the published message, not only in the event name.

## Known limitations

- Imports `LaneDisciplineExaminer` purely for one classmethod, coupling two examiners; `overtaking()` would sit better on `NavigationExaminer`.
- The penalty is flat regardless of how far over the limit the vessel is, though the excess is already carried.
- No dwell requirement, so a single-tick GPS spike scores a violation.
