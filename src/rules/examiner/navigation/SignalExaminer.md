# SignalExaminer

## Synopsis

Collates what a vessel means to do with what is happening around it, and posts the pair where COLREG rule 34 can hear it. It deliberately makes no judgement of its own.

## Operation

Rule 34 governs manoeuvring and warning signals, and it cannot be judged from either half alone: a single short blast is correct when altering to starboard and wrong when altering to port. So this examiner gathers rather than decides. It resolves `OwnShip.Intent` — a `ValueSet`, rendered as a sorted comma-joined token — and `(OwnShip,TargetShip).EncounterSituation`, and publishes the resulting `(intent, situation)` tuple to the topic the rule set listens on, by default `/Faculty/Regulation/Rules`, the same topic `MaritimeSituation.regulate()` posts regulation events to. The vessel is notified directly as well, so a bridge model can raise the signal without subscribing to the regulation topic. The tuple is posted only when it changes from what was last posted for that vessel, because rule 34 is about the signal accompanying a manoeuvre: a steady state is not a signalling event, and republishing it every tick would drown the queue. Keeping the judgement in rule 34 rather than here keeps one reading of the rule in one place.

## Features

- Publishes an observation, not a verdict, so the rule that owns the interpretation keeps it.
- Change-triggered rather than periodic, which matches the semantics of a manoeuvring signal and keeps the queue quiet.
- Both the topic and the message name are configurable from the `signal` block of `zones.yaml`.
- Notifies the vessel as well as the topic, so a bridge model needs no subscription to the regulation feed.
- Carries own and target IMO plus the zone, so a listener has the full context without re-resolving anything.
- Fires on either half alone: an intent with no encounter, or an encounter with no declared intent, is still published.

## Known limitations

- The `posted` map of last-seen tuples grows without bound over a long scenario.
- Nothing currently subscribes to `vessel.signal` on `/Faculty/Regulation/Rules`, so the examiner is write-only until rule 34 is implemented.
- `intent()` joins a `ValueSet` into a comma-separated string that rule 34 must then parse apart again; passing the collection through would be cleaner.
