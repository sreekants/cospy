# NightTimeExaminer

## Synopsis

Verifies that a vessel is showing the navigation lights her zone requires once the simulation clock reads night. Scores the lights she is missing, once per vessel per night.

## Operation

The examiner reads the hour from `ctxt.sim.now()`, accepting either a `datetime` or a seconds-from-midnight scalar, and tests it against the `night_from`/`night_to` window in the merged zone rules. That window normally wraps midnight, so the test is a disjunction rather than a range; when the clock leaves the window the examiner clears its record of who has been reported, which is what makes the finding once-per-night rather than once-per-scenario. Inside the window it takes `required_lights` from configuration — a list, or a comma-separated string when it arrives from a map shape's `settings` — and compares it against the lights the vessel is showing, read from the vessel's `operation` `ValueSet`, the same property set a bridge model raises signals into. Any required light not present is collected, and a non-empty set is scored as `night.lights_missing` with the count as the finding's value. A vessel with no `operation` set at all is treated as showing nothing rather than as compliant, because an absent set and a dark ship are indistinguishable from here.

## Features

- The required light set is configuration per zone, since it differs by vessel type and jurisdiction and COLREG part C is exactly the sort of list a scenario designer needs to vary.
- Handles the midnight-wrapping night window correctly, including the boundary hours.
- Once per vessel per night, so an unlit ship is one finding rather than one per tick.
- Accepts either a datetime clock or a numeric one without configuration.
- Reports both the required set and the missing subset, so the finding is actionable without re-deriving it.
- Treats an unconfigured vessel as unlit rather than compliant, so a misconfiguration surfaces instead of hiding.

## Known limitations

- `self.reported` is cleared by the first vessel seen in daylight, so vessels evaluated later in the same tick lose their record.
- When the clock is not a `datetime`, treating it as seconds-from-midnight is a guess about the simulation's time base.
- Sunrise and sunset are latitude- and date-dependent, and a fixed hour window will be wrong for the Trondheimsfjord scenarios.
