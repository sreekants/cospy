# CollisionExaminer

## Synopsis

Values what a collision between two vessels would cost, as the summed worth of the two hulls multiplied by a penalty rate. Publishes the figure so a planner or risk model can weigh an encounter in currency rather than in proximity.

## Operation

The examiner's precondition names both ships, because a collision cost is a property of an encounter and not of a vessel. When an own ship and a target ship are both in scope it resolves `(OwnShip,TargetShip).DCPA` and, if a `report.dcpa` threshold is configured, returns without scoring when the closest approach is further out than that — which keeps distant traffic from generating cost rows. Otherwise it prices each vessel by reading `value`, `hull_value` or `insured_value` from that vessel's own `settings`, falling back to the configured `default_vessel_value` when a hull declares none, and multiplies the sum by `penalty_rate` from the `collision` block of `config/examiner/zones.yaml`. The result is recorded to `fact_Concern` and published on `/Faculty/Concern/Collision` together with the two IMOs, both values, the rate, DCPA and TCPA. It is deliberately an expected cost evaluated over the whole approach rather than a single number at the moment of contact, so a consumer receives a cost curve it can differentiate.

## Features

- Cost model is one line of configuration — `cost = (value(OS) + value(TS)) × penalty_rate` — with no per-pair damage table to maintain.
- Individual hulls can be priced in their own `settings`; the rest take a scenario default.
- An unpriced vessel falls back to a configured value rather than contributing zero, so a collision with an unconfigured ship never looks free.
- `report.dcpa` bounds how wide an encounter has to be before it is costed.
- Publishes both constituent values alongside the total, so a subscriber can see how the figure was reached.
- Carries DCPA and TCPA in the message, letting a consumer distinguish a closing encounter from a receding one even though the cost itself does not.

## Known limitations

- Scores on every tick inside the DCPA threshold, which double-counts an approach badly; it should emit on change or at closest approach.
- The cost ignores TCPA, so a receding vessel is priced the same as a closing one.
- `value()` searches three settings keys in a fixed order and gives no warning when two of them disagree.
