# The packages of `src/`

[← INDEX](INDEX.md) · [kernel](kernel.md) · [extending](extending.md) · [scaffolding](scaffolding.md)

The source tree package by package: what each directory holds, how big it is, and the few classes in
it that you need to know. The dependencies run one way, `rules` → `maritime` → `cos`, and the page
follows them from the bottom up.

<p align="center"><a href="cos-structure.html"><img src="cos-structure.png" alt="COS source structure: packages under src/, the apps and data outside it, and what one coslaunch process runs" width="80%"></a></p>

*Figure 1. The source tree on one page: the four packages under `src/` by size, the apps and data
outside it, stubs drawn dashed, and, in the bottom band, what one `coslaunch` process does at boot and
on every step. Click for the printable A4 version.*

Sizes are lines of Python. The tree has 553 files and 520 classes. This page names the classes that
matter; for any other class, use the generated API pages (`mkdocs serve`, then *Modules*) or search by
name, since every class loaded from configuration lives in a file of the same name.

---

## `cos` — the simulation operating system

25.8k lines, 335 classes. Domain-neutral: nothing in `cos` knows about ships.

| Package | Size | Contents |
|---|---|---|
| `core/kernel` | 3.1k | `Kernel`, `BootLoader`, `Configuration`; the object hierarchy `Object` → `Service` / `Faculty` / `Subsystem` / `CompositeService`; `ObjectManager`, the object tree; `MessageQueue` and `IPCMessage`, the topics; `Logger`; `Device` and `DeviceManager`; `FileSystem` and `BootImage`; the thread pool |
| `core/simulation` | 0.8k | `Simulation`, the kernel singleton; `Runner`, `RunnerThread` and `SimulationClock`, the step loop; `Builder`, database rows to objects; `Actor` and `Behavior`; `CollisionDetector` |
| `core/utilities` | 3.3k | `ActiveRecord`, a small ORM over SQLite; `TransactionalDatabase`; `Tree` and `TreeNode`; `ArgList`; `ThreadPool`; design patterns (`Composite`, `Publisher`, `Flyweight`, …); `GraphDatabase`; `InvertedIndex` |
| `core/network` | 0.7k | `ORPCService` and `ORPCProxy`; ZeroMQ and WebSocket transports |
| `core/service`, `core/api` | 1.9k | The remote API from both ends: services and their client proxies ([communication.md](communication.md#the-remote-api-services-and-proxies)) |
| `core/time`, `core/device` | 0.3k | `Clock`, `Ticker`; `NullDevice` |
| `subsystem/{world,data,network}` | 0.8k | `World`, a composite of the environment services; `DataManager` and `Partition`, the fact tables; `RPCBroker` and `WebSocketBroker` |
| `model/environment` | 1.0k | `Environment`, `Actors`, `Weather` and `WeatherSystem` (wind, current, waves), `Scales` |
| `model/geography` | 1.0k | `Shape` → `Land` / `Sea` / `Sky` and their subtypes; `LandBuilder`, `SeaBuilder`, `SkyBuilder`, `MapBuilder` |
| `model/rule`, `model/resolver` | 1.3k | `Rule`, a faculty; `Automata`, a compiled Legata file; `Context`, the rule context; `Situation`; `RuleSet`; `ScoreCard`; `Resolver` and `CompositeResolver` |
| `model/examiner`, `model/vehicle`, `model/situation` | 0.7k | `Examiner`, `ConcernExaminer`, `Precondition` / `PreconditionSet`; `Vehicle`, `Intent`; `EncounterSituation` |
| `behavior/{motion,control,swarm}` | 2.3k | `MotionBehavior` → linear, Brownian, path, path-following, fleet, prey and predator; hydrodynamic models; boids |
| `lang/{legata,logic,symbol,rebeca}` | 2.7k | Legata: the PLY `Lexer` and `Parser` and the expression nodes; `DecisionTree` and `Decision`; Rebeca actor stubs |
| `math/*`, `physics/force` | 2.4k | Geometry (`Rectangle`, `Vector`, `CPA`, `Distance`), functional (`PID`, `Polynomial`), `Delaunator`, `CPT` |
| `cluster/runtime`, `data/{bi,score}` | 1.0k | `ScenarioGenerator`, `TemplateReplicator`; the database merge `Builder`; score types |
| `ui/{game,gui}`, `tools/cviz` | 2.5k | pygame sprites; the `cviz` viewer (`VirtualWorld`), which watches a simulation over RPC |

**Key classes.**

| Class | Why you need to know it |
|---|---|
| `cos.core.kernel.BootLoader` | Turns `cos.ini` and its manifests into objects; the reason a class must be named after its file |
| `cos.core.kernel.ObjectManager` | The object tree: every component finds every other by path ([the path reference](kernel.md#the-path-reference)) |
| `cos.core.kernel.Object`, `Service`, `Faculty` | The two roots: services are called every step, faculties are driven by a service |
| `cos.core.simulation.Runner` | The step loop: calls `on_timer` on everything under `/Services`, sleeps 30 ms, repeats |
| `cos.core.simulation.Builder` | Base of every builder: reads rows of one type code from a database at boot |
| `cos.core.simulation.Actor`, `cos.behavior.motion.MotionBehavior` | A vehicle's behaviours, and the base class every motion model extends |
| `cos.subsystem.data.DataManager` | Collects `fact_…` rows in memory and writes them every 5 seconds |
| `cos.model.rule.Automata`, `cos.lang.legata.Parser` | Compile a `.legata` file into a decision tree and walk it |
| `cos.model.resolver.CompositeResolver` | Dispatches a Legata term to the resolver that can compute it |
| `cos.model.examiner.Examiner`, `PreconditionSet` | Base of every examiner, and the declaration of what situation a group of terms needs |
| `cos.cluster.runtime.ScenarioGenerator` | Writes one configuration folder per case of a sweep |

---

## `maritime` — the domain layer

7.4k lines, 118 classes. Everything that makes the generic world a sea with ships in it.

| Package | Size | Contents |
|---|---|---|
| `model/vessel` | 0.6k | `Vessel`, which extends `Vehicle`, with its type, operation, status and restriction flags; five subtypes; the vessel `Builder`; `VesselComposer` |
| `model/geography` | 0.5k | 17 legal and traffic zones (exclusive economic zone, traffic separation scheme, lane, harbour, …) extending `cos` `Sea`; the maritime `SeaBuilder`, which registers their type codes |
| `model/resolver` | 1.2k | 17 resolvers: own ship, target ship, target, fleet, sea, land, zone, lane, harbour, … |
| `model/rule`, `model/zone` | 0.8k | `COLREG` and `InlandWaterRule`, the rule bases; the `ZoneAware` mixin, `ZoneRules`, `SpatialZones` |
| `core/situation` | 0.3k | `MaritimeSituation` → `MaritimeEncounterSituation` / `MaritimeConductSituation`; `Maneuver`; encounter types |
| `situation/*`, `conduct/*` | 0.8k | The monitors: crossing, head-on, give-way, overtaking, stand-on, traffic; collision, grounding, harbour, narrow channel, obstruction |
| `regulation/colreg` | 0.5k | `Evaluator`, the service that drives monitors, rules and examiners; its `Resolver` and `API` |
| `regulation/{inland,internal}` | 0.2k | Zone rule classes used by local rules: harbour, inshore traffic, traffic lane, traffic separation scheme, waterway |
| `behavior/vessels` | 0.8k | `PlannedVesselBehavior` and its subclasses (container ship, ferry, fishing vessel, yacht, …); `VesselManeuvers` |
| `device/communication` | 1.1k | AIS, GPS, gyro and magnetic compasses, radar, echosounder |
| `navigation`, `traffic` | 0.5k | `Map`, the spatial query service; route; VTS, port authority, zone allocation |

**Key classes.**

| Class | Why you need to know it |
|---|---|
| `maritime.regulation.colreg.Evaluator` | The one service that calls monitors, rules and examiners ([regulation.md](regulation.md#how-the-evaluator-drives-monitors-rules-and-examiners)) |
| `maritime.model.vessel.Vessel` | The vessel: identity, ship model, status (under way, anchored, aground) and its behaviours |
| `maritime.model.vessel.Builder` | Reads `vessel.s3db`; filters vessels by `scenario=` tag against `TRAFFIC` |
| `maritime.core.situation.MaritimeSituation` | Base of every monitor; posts situations to the rules and records `fact_…` rows |
| `maritime.model.rule.InlandWaterRule` | Base of the zone rules that local rules use: checks every vessel inside zones matching `zonekey=` |
| `maritime.model.zone.ZoneAware` | Mixin that gives an examiner the map shapes under a vessel and zone-local limits |
| `maritime.model.resolver.TargetResolver`, `VesselResolver`, `SeaResolver` | The resolvers behind most own-ship, target-ship and zone terms |
| `maritime.behavior.vessels.PlannedVesselBehavior`, `VesselManeuvers` | Trip following, and the COLREG-aware manoeuvres applied on top of it |
| `maritime.navigation.cartography.Map` | Answers spatial questions: nearest vessels, bodies and zones in an area |

---

## `rules` — regulation content

4.9k lines, 65 classes. Regulation as data plus thin classes: the Legata texts live in `config/`, and the
classes here load and score them.

| Package | Size | Contents |
|---|---|---|
| `colreg/ruleN` | 1.9k | 41 classes, one per COLREG rule, each a `COLREG` subclass paired with `config/maritime/regulation/colreg/RuleN.legata`. Rules 3, 9, 10, 13, 15, 17, 19 and 34 add behaviour; the rest only load their Legata file |
| `examiner/navigation` | 1.3k | Approach, berthing, collision, day-time, extreme weather, grounding, lane discipline, night-time, overtaking, signal, speed |
| `examiner/risk` | 1.3k | `RiskExaminer`, a Bayesian network over pyAgrum; `RiskModel` (loss matrix, bindings, voyage track); the ASV and capsize models |
| `examiner/{environmental,planning,security,inspector}` | 0.3k | Cargo; comfort, economic, plan; customs, zone violation; a test inspector |

**Key classes.**

| Class | Why you need to know it |
|---|---|
| `rules.colreg.rule13.Rule13` | A COLREG rule that reacts to a situation (overtaking) rather than only loading its text |
| `rules.examiner.navigation.NavigationExaminer` | Base of the navigation examiners |
| `rules.examiner.navigation.CollisionExaminer`, `GroundingExaminer` | Worked examples of zone-aware examiners with their own fact tables |
| `rules.examiner.risk.RiskExaminer` | Consequential risk: evidence from resolver terms, gated by preconditions, into a Bayesian network, priced per zone |

---

## `cai` — planning experiments

0.5k lines, 2 classes. RRT, A* and Dijkstra path planners over an image grid. Nothing in `cos`,
`maritime` or `rules` imports it. See [`scaffolding.md`](scaffolding.md).

---

## Layering rules

| Layer | Responsibility | Must not depend on |
|---|---|---|
| `cos` | Kernel, objects, steps, messages, persistence, the rule language, a generic world of shapes and vehicles | `maritime`, `rules` |
| `maritime` | The meaning: vessels, zones, encounters, manoeuvres, the COLREG evaluator | `rules` |
| `rules` | Regulation as data (Legata) plus thin classes and examiners | — |

A new domain, such as road or rail, would sit beside `maritime` and reuse `cos` unchanged. That is the
"no single domain" commitment of [the hypotheses](concepts.md#hypotheses-and-what-the-design-does-not-commit-to).

## Naming conventions

- **One class per file, named after the file,** for anything a manifest loads. The boot loader takes the
  last part of the module path as the class name, and a remote-API proxy takes its target from its own
  class name. Library modules that export several helpers (`Patterns`, `RiskModel`,
  `legata/Expression`) are exempt, because nothing loads them by name.
- **Mirrored names are deliberate.** `World`, `Sea`, `Vessel`, `Topic`, `MQ`, `Timer`, `Port` and `Radar`
  each exist as a client proxy (`core/api`), a remote service (`core/service`) and, where it applies, a
  model class. Import them with an alias: `from cos.core.api.World import World as WorldService`.
- **Some names repeat without being mirrors.** Two `Situation` classes (the data holder in
  `cos.model.rule`, and the faculty in `cos.model.situation`), two `WeatherSystem` classes (the model,
  and a `ui.game` sprite), three `Actor` classes (`core.simulation`, `lang.rebeca`, `maritime.traffic`)
  and two `SailingVessel` classes (a behaviour and a vessel type). Existing code aliases them
  (`Context as RuleContext`). Give new classes distinct names.
