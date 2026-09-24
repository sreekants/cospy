# Scaffolding: stubs, empty manifests and unused code

[← INDEX](INDEX.md) · [layers](layers.md) · [extending](extending.md)

A class or a directory existing is not evidence that a feature exists. This page lists what is in the
tree but does not yet do anything, so that a result is not read as covering it. Each item is a place
where work can be added; [extending.md](extending.md) says how.

---

## COLREG rule classes that only load their text

`src/rules/colreg/` has one class for each of the 41 COLREG rules. **33 of them are six-line classes**
that load their Legata file and nothing more. A rule's clauses are only evaluated against situations
the rule is handed, and handing them over is code: the rule must subscribe to the monitors' events and
queue a situation for each ([make a COLREG rule check situations](extending.md#make-a-colreg-rule-check-situations)).

| Rules with code of their own | Rules that only load their text |
|---|---|
| 3, 9, 10, 13, 15, 17, 19, 34 | 1, 2, 4–8, 11, 12, 14, 16, 18, 20–33, 35–41 |

Of the eight with code, only Rule 13 queues situations for its automaton today. A COLREG clause that
nothing hands a situation to never fails, whatever happens at sea
([what COS cannot see](concepts.md#what-cos-cannot-see)).

## Examiners with no evaluation

Nine of the 19 examiners are stubs whose `evaluate` returns without doing anything:

| Examiner | Package |
|---|---|
| `ApproachExaminer`, `OvertakingExaminer`, `DayTimeExaminer` | `rules/examiner/navigation` |
| `ComfortExaminer`, `EconomicExaminer`, `PlanExaminer` | `rules/examiner/planning` |
| `CustomsExaminer`, `ZoneViolationExaminer` | `rules/examiner/security` |
| `TestInspector` | `rules/examiner/inspector` |

Seven of them are the same 24-line template with a different name. All except `TestInspector` are
listed in `config/rules.examiner.yaml`, so eight stub examiners load and run in every evaluation pass,
and record nothing.

## Empty manifests

These manifests are named in `cos.ini` but list no modules, so their faculty group loads nothing from
them:

| Manifest | Section | Would load |
|---|---|---|
| `config/beacon.yaml` | `[Signals]` `Beacons` | beacons |
| `config/radar.yaml` | `[Signals]` `Radars` | shore radars |
| `config/port.yaml` | `[Signals]` `PortAuthorities` | port authorities |
| `config/rules.mass.yaml` | `[Rules]` `MASS` | rules for maritime autonomous surface ships |

## Disabled manifest entries still load

Two manifest entries carry `enable: False`: `Rule7` in `rules.colreg.yaml`, and `WebSocketBroker` in
`network.yaml`. The boot loader does not read that flag: `BootLoader.load_modules` creates every entry
it finds. Both are therefore loaded. The only code that honours `enable` is the sweep generator, when it
checks which weather databases a case needs. To leave a module out of a run, delete or comment out its
entry.

## Monitor hooks with nothing in them

The COLREG evaluator's `monitor()` pass runs three groups: `/Faculty/Situation/Incident`, then
`/Faculty/Situation/Maritime`, then `/Faculty/Situation/Processors`. No module registers under the first
or the last, so only the maritime monitors run. The two hooks are there for incident detectors and for
post-processors of detected situations.

## Packages nothing uses

| Package | Contents | Used by |
|---|---|---|
| `src/cai/` | RRT, A* and Dijkstra path planners | nothing |
| `src/cos/lang/rebeca/` | Actor-language stubs (`Actor`, `IPCPort`, `Service`) | nothing |
| `src/cos/math/fem/` | A mesh class | nothing |
| `src/maritime/navigation/route/` | `Route`, one method | nothing |
| `src/maritime/traffic/` | VTS, port authority, zone allocation, captain | only an adapter in `PreyBehavior` |

## Resolved terms with fixed values

Some resolvers return a constant instead of a measurement: visibility is always 1.0, and the wave height
and wind speed seen by the risk network are always 0. Rules and networks that use them see clear, calm
weather whatever the scenario says. The weather itself is generated in full; it is the path from the
weather to these terms that is not built ([what COS cannot see](concepts.md#what-cos-cannot-see)).
