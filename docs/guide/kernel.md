# The kernel and its subsystems

[← INDEX](INDEX.md) · [walkthrough](walkthrough.md) · [communication](communication.md) · [extending](extending.md)

The part of COS that knows nothing about ships: it boots a simulation from its configuration,
holds the object tree, carries messages, keeps the clock and records results.

The running example, *True North* in fog at Türkeli, is introduced in [one run, end to end](walkthrough.md#one-run-end-to-end).

---

## The kernel

**What it does.** Starts a simulation from its configuration, holds the named objects that make up the
world, carries messages between them and keeps the clock. It knows nothing about ships.

**What it's made of.** A small set of classes in `src/cos/core/kernel`:

| Part | Job |
|---|---|
| `Configuration` | Reads `cos.ini`, resolves `$(NAME)` variables, finds files |
| `BootLoader` | Loads modules from YAML files and runs startup and shutdown in order |
| `ObjectManager` | A tree of named objects, addressed by path like a file system |
| `MessageQueue` | Named topics that faculties post to and read from |
| `ThreadPool` | Worker threads for services that run in parallel (`NumThreads=4`) |
| `Logger` | The log you see on the console and in `syslog.s3db` |

**The object tree.** Everything in a simulation has a path. Vessels live under `/World/Vehicle/Vessel`,
coastlines under `/World/Land`, the wave field at `/World/Weather/SEA_WAVE`, rules under
`/Faculty/Regulation`, and the services the runner calls under `/Services`. A faculty finds what it
needs by path: the COLREG evaluator asks for everything under `/Faculty/Situation/Maritime` to get its
monitors. `cosservice list` prints this tree from a running simulation.

**The message queue.** Topics are paths too, for example `/Situation/Maritime/Encounter/Crossing` or
`/Faculty/Regulation/Rules/COLREG/Rule13`. A monitor that sees a crossing posts `vessel.crossing` to the
rule topics, and rules that care subscribe to it. Messages wait on a topic until read.
`costopic list` prints the topics of a running simulation.

**When it runs.** Once, at startup, and then continuously through the runner.

**Why it's built this way.** A student might ask why a simulator needs an operating system at all. The
answer is the stages of [the central problem](concepts.md#the-central-problem-rules-speak-of-situations-simulators-produce-states).
Dozens of independent faculties must be loaded from files, started in the right order, find each other
by name and pass results along without knowing about each other. That is exactly the problem an
operating system solves for programs.

**How others do it.** A typical research simulator is one program with a main loop that calls each
model in turn. Adding a model means editing the loop. In COS, adding a model means adding a line to a
YAML file.

**In our example.** *True North* is an object at a path under `/World/Vehicle/Vessel`. Its movement,
the monitors watching it and the rule that fined it are all services the runner calls each step.

---

## The kernel subsystems

**What they do.** Three services that every simulation needs, loaded before any faculty from
`config/subsystem.yaml`.

| Subsystem | Job |
|---|---|
| **World** | Holds the simulated world: the map scale, the vessel range and the collision check |
| **DataManager** | Collects results and writes them to the run's database |
| **NetworkManager** | Hosts the network brokers that tools connect to ([talking to a running simulation](communication.md#talking-to-a-running-simulation)) |

**The world.** Map data is drawn in *map units*, and each map declares how many metres one unit is:
1.0 for hand-drawn maps such as Türkeli, 40 for maps built from open data such as Trondheim, 100 for
Hormuz. Everything is converted to metres when it loads, so the rest of the simulation works in
metres. The world also holds the **vessel range**, the rectangle vessels are kept inside; a vessel that
tries to leave it, or to sail onto land, is stopped.

**The data manager.** Faculties call it with a table name and a row of values. It keeps rows in memory,
one bucket per table, and every 5 seconds writes them to the file named by `storage=` in
`subsystem.yaml`. The file must already contain the tables; their layout is defined in
`config/data/maritime.xml`. Tables are named `fact_…`, one per kind of event: `fact_crossing`,
`fact_head_on`, `fact_approach`, `fact_collision`, `fact_ro` and many more.

**Why it's built this way.** Writing to disk on every event would slow each step. Batching every 5 seconds
keeps the simulation fast, at the cost that a run killed without a clean shutdown loses up to 5 seconds
of rows.

**In our example.** *True North*'s 30 penalty rows were collected in memory and written in batches to
the run's copy of the database.

---

## Inside the kernel

The two sections above describe what the kernel does. This one describes how the code does it, for
readers who will change it.

### The object hierarchy

Every class the kernel loads derives from `Object`, which gives it an identity (type, id, guid) and
a message topic. Its two main specialisations decide where an instance sits in the object tree, and
whether the runner calls it:

```
Object ─┬─ Service    → /Services/<type>/<name>                 called by the runner every step
        │    ├─ Subsystem          World, DataManager, NetworkManager, brokers
        │    ├─ CompositeService   World = Environment + Actors + Weather …
        │    ├─ Builder            reads a database table at boot → /World/...
        │    └─ ORPCService        /Services/API/<Name>, callable from outside
        └─ Faculty    → /Faculty/<category>/<type>/<name>   never called by the runner;
             ├─ Situation → MaritimeSituation   /Faculty/Situation/Maritime/…   driven by the
             ├─ Rule → COLREG, InlandWaterRule  /Faculty/Regulation/Rules/…     COLREG evaluator
             └─ Examiner → ConcernExaminer      /Faculty/Regulation/Examiner/…
```

`Object.initalize` registers each instance at `/<its type path>` when it is loaded. From then on,
components find each other by path, not by import.

### The path reference

These paths are the real interfaces between packages. Renaming a category or a type is a breaking
change even when no import changes.

| Path | Registered by | Read by |
|---|---|---|
| `/Services/<type>/<name>` | every `Service`: subsystems, builders, the COLREG evaluator, brokers | the runner, every step (`on_timer`) |
| `/Services/API/<Name>` | the remote services in `cos.core.service` (`config/api.yaml`) | tools, through the proxies in `cos.core.api` ([communication.md](communication.md)) |
| `/Faculty/Situation/Maritime/…` | situation and conduct monitors (`maritime.situation`, `maritime.conduct`) | `Evaluator.monitor()` |
| `/Faculty/Situation/Incident`, `/Faculty/Situation/Processors` | nothing in the current configuration | `Evaluator.monitor()`, as pre- and post-processing hooks |
| `/Faculty/Regulation/Rules/…` | COLREG rules and local rules (`Rule`) | `Evaluator.evaluate()` |
| `/Faculty/Regulation/Examiner/…` | examiners (`Examiner`) | `Evaluator.evaluate()`, in the same pass as the rules |
| `/World/Land` | `LandBuilder` | the world's collision check, `LandResolver`, the evaluator, zone-aware examiners, `Map` |
| `/World/Sea` | `SeaBuilder` (`cos` and `maritime`) | the evaluator, `SeaResolver`, zone rules and zone-aware examiners, inland rules, `Map` |
| `/World/Sky` | `SkyBuilder` | `Environment` |
| `/World/Vehicle/Vessel` | the vessel `Builder` | `Actors`, the evaluator, `Map`, fleet behaviours, the `Vessel` remote service |
| `/World/Weather/<FIELD>` | `WeatherBuilder` (`WIND_CURRENT`, `SEA_CURRENT`, `SEA_WAVE`) | `Environment`, `Weather`, `ExtremeWeatherExaminer` |

### Boot, in code

```
cos.ini [Simulation]
    Kernel=Subsystem  Faculties=Environment,Monitors,Signals,Actors,Rules  Services=NetworkServices
  → each name is an .ini section → each key names a YAML manifest → packages.modules[] → a class
BootLoader.load_class("a.b.C")  imports module a.b.C and takes its attribute C
  → inst = C(args) ; inst.on_init(ctxt, module)        (registers it in the object tree)
  → on_start for every instance, then on_run at run levels 0–4 ; shutdown mirrors this
```

- `$(CONFIG)`, `$(MAP)`, `$(SIMULATION)`, `$(TRAFFIC)` and the rest come from `cos.ini`
  `[EnvironmentVariables]`, and are expanded in manifest `args`, `config` and `database` fields.
- **The class name must equal the file name.** The loader takes the last component of the module
  path as the class name, so `module: rules.examiner.navigation.GroundingExaminer` loads the class
  `GroundingExaminer` from `GroundingExaminer.py`.
- The resolvers used by Legata are a second registry, `config/legata.yaml`, which the COLREG
  evaluator loads into its `CompositeResolver` ([regulation.md](regulation.md#how-a-term-is-resolved)).

The full map from `cos.ini` sections to manifests is in [support.md](support.md#config--the-simulation-is-data).

### One step, in code

```
RunnerThread (sleeps 30 ms per step) → traverse /Services → on_timer()
  ├─ World / Actors                 → each vessel: Actor.update → Behavior.move
  │                                   → collision check (land polygons + vessel range)
  ├─ Environment / Weather          → wind, current and wave fields
  ├─ COLREG Evaluator
  │    ├─ monitor()   every 0.5 s   → /Faculty/Situation/Incident, …/Maritime, …/Processors
  │    │                              monitors detect situations and post them to the rules
  │    └─ evaluate()  sample timer  → begin · evaluate · end on everything under /Faculty/Regulation:
  │                                   rules walk their automata; examiners score their concerns
  ├─ DataManager                    → queued fact rows written every 5 s, each with the case id
  └─ RPCBroker                      → serves /Services/API/* on the RPC port
```

An exception inside one service's `on_timer` is caught and logged by the runner, and the next
service still runs. A failing service therefore goes quiet instead of stopping the run. Read the log
after every run.
