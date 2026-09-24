<head><link rel="stylesheet" href="https://www.nyun.ca/public/docs/style.css" type="text/css"></head>

# The Co-Simulation Operating System: A Functional Overview

Tools: [coslaunch](../../apps/coslaunch/coslaunch.md) · [cviz](../../apps/cviz/cviz.md) · [costopic](../../apps/costopic/costopic.md) · [cosservice](../../apps/cosservice/cosservice.md) · Data guides: [maps and vessels](../../tools/mapping/MAPGEN.md) · [weather](../../tools/mapping/WEATHERGEN.md)

How COS, a simulator built to test autonomous ships against the rules of the sea, is put
together: what its parts are, what each one does, and why it is built that way. One example runs
through the whole guide. A container ship called *True North* sails through the Türkeli traffic
lanes at the northern mouth of the Bosphorus, in fog, among 33 other vessels. You follow it from
a line in a configuration file to a penalty in a database, and then see how the same run is
repeated a thousand times with the conditions changed.

---

## Contents

* [1. What this document is](#1-what-this-document-is)
* [2. What COS is, and what it isn't](#2-what-cos-is-and-what-it-isnt)
* [3. The central problem: rules speak of situations, simulators produce states](#3-the-central-problem-rules-speak-of-situations-simulators-produce-states)
* [4. Hypotheses, and what the design does not commit to](#4-hypotheses-and-what-the-design-does-not-commit-to)
* [5. Lineage and neighbours](#5-lineage-and-neighbours)
* [6. The overview figure, and how to read this guide](#6-the-overview-figure-and-how-to-read-this-guide)
* [7. One run, end to end](#7-one-run-end-to-end)
* [8. The life of a simulation](#8-the-life-of-a-simulation)
* [9. What COS cannot see](#9-what-cos-cannot-see)
* [10. The kernel](#10-the-kernel)
* [11. The kernel subsystems](#11-the-kernel-subsystems)
* [12. The environment faculty — the world](#12-the-environment-faculty--the-world)
* [13. The actors faculty — the vessels](#13-the-actors-faculty--the-vessels)
* [14. The monitors faculty — situations](#14-the-monitors-faculty--situations)
* [15. The rules faculty — Legata, rules and examiners](#15-the-rules-faculty--legata-rules-and-examiners)
* [16. Talking to a running simulation](#16-talking-to-a-running-simulation)
* [17. From one run to a thousand](#17-from-one-run-to-a-thousand)
* [18. Levels and timescales](#18-levels-and-timescales)
* [19. The parts compared](#19-the-parts-compared)
* [20. Combinations that are not obvious](#20-combinations-that-are-not-obvious)
* [21. One simulator, many waters](#21-one-simulator-many-waters)
* [Appendix A. Glossary](#appendix-a-glossary)
* [Appendix B. Where things live](#appendix-b-where-things-live)

---

## 1. What this document is

Start here if you want to know how COS works. You should already know what a simulation is:
a model of a system, stepped forward in time, whose output you measure. You don't need to know
anything about ships, maritime law or COS itself. Every term is defined where it first appears
and again in [Appendix A](#appendix-a-glossary).

It is **not** a manual, an API reference or a build guide. It describes what the parts are and
how they fit, at the level where you can predict how COS will behave in a case this guide never
mentions. Deeper material lives elsewhere:

| For | Read |
|---|---|
| The research this platform was built for | Sreedharan, Ramachandran, Røsæg and Rokseth, *Safety Assurances in Autonomous Vessels* (ER 2024), `papers/reference/` |
| The rule language, Legata | Sreedharan et al., *Legata*, CS&Law 2025 |
| The risk formalism used in current work | `papers/IEEE-Access/DEFINITIONS.md` |
| Building a location: land, sea, vessels | [`MAPGEN.md`](../../tools/mapping/MAPGEN.md), `tools/mapping/SHIPGEN.md` |
| Generating weather | [`WEATHERGEN.md`](../../tools/mapping/WEATHERGEN.md) |
| Running the programs | the man pages for [coslaunch](../../apps/coslaunch/coslaunch.md), [cviz](../../apps/cviz/cviz.md), [costopic](../../apps/costopic/costopic.md), [cosservice](../../apps/cosservice/cosservice.md) |
| Known defects | [`bugs/INDEX.md`](../../bugs/INDEX.md) |

**About this overview.** Where the ER 2024 paper describes what COS is designed to do, this guide
says so. Where the code does less than the design, the guide says what the code does today, and
points to the bug index. Treat the paper as the direction and this guide as the current position.

---

## 2. What COS is, and what it isn't

COS is not a ship-handling simulator. It has no bridge, no helm and no three-dimensional sea, and
it is not where you train a navigator. Nor is it a collision-avoidance algorithm. It is a
**test ground**: a simulator whose job is to put an autonomous ship's software into many realistic
traffic situations and record, in a database, how well it kept to the rules of the sea.

The name says how it does this. It is an **operating system for simulations**. It has a kernel, a
boot sequence, a process scheduler, messaging between processes, device-like services and a
file store, the same parts a computer's operating system has. The things it schedules are not
programs but pieces of a simulated world: a coastline, a weather front, a ferry, an observer
that notices two ships crossing, a rule that judges them.

The comparison that matters most is with the traditional way of testing collision avoidance.
There, each test case is a short, hand-built encounter: two ships, open sea, a fixed geometry, and
a pass/fail check written into the test itself. COS keeps the knowledge out of the tests. Maps,
vessels, traffic, weather and the rules themselves are **data files**, and the situations that
need judging are **found while the simulation runs**, not scripted in advance. That is what lets
the same software be tested in a harbour, a strait and a fjord without writing new tests.

COS is made of five kinds of parts:

| Part | What it is | Where it lives |
|---|---|---|
| **The kernel** | Boots a simulation from a configuration file, schedules its services, carries messages between them | `src/cos/core` |
| **Faculties** | Plug-in services that make up the world and watch it: environment, actors, monitors, signals, rules | `src/cos`, `src/maritime`, `src/rules`, wired by `config/*.yaml` |
| **Legata** | A small language for writing rules, plus the machinery that checks them against the running simulation | `src/cos/lang/legata`, `config/maritime/regulation` |
| **Tools** | Programs to start, watch and query a simulation | `apps/coslaunch`, `apps/cviz`, `apps/costopic`, `apps/cosservice` |
| **The sweep pipeline** | Generates many variants of a scenario, runs them, and merges their results | `src/cos/cluster`, `src/cos/data/bi`, `templates/cluster` |

<p align="center"><img src="Screenshot-Istanbul.png" alt="The Istanbul scenario in the cviz viewer" width="80%"></p>

*Figure 1. The Istanbul scenario in cviz, the COS viewer. Land is green, water is shaded by depth,
and traffic lanes and zones are drawn as tinted overlays. Every vessel on screen is a service
inside one running COS process.*

---

## 3. The central problem: rules speak of situations, simulators produce states

Every design decision in COS answers one problem. Name it now and the rest of the guide reads as
a list of answers.

**The rules of the sea are written about situations. A simulator only produces states.**

A simulator knows, at each step, where every vessel is, which way it points and how fast it moves.
That is its *state*. The International Regulations for Preventing Collisions at Sea (**COLREG**,
the "rules of the road" for ships) never mention positions. Rule 15 says: *when two power-driven
vessels are crossing so as to involve risk of collision, the vessel which has the other on her own
starboard side shall keep out of the way.* To check that rule, something has to decide that two
vessels are *crossing*, that there is *risk of collision*, and which one is on the other's
*starboard* (right-hand) side. None of those words is a number the simulator holds.

The rules are also vague on purpose. "Safe speed", "in ample time", "so far as practicable" are
judgements a human master makes from experience. The ER 2024 paper puts the gap plainly: the
rules are imprecise, abstract, cross-referencing and full of exceptions, and a machine can only
check precise facts.

COS closes the gap in stages. Each stage turns the output of the stage below into something a
little closer to the words of the rule:

| Stage | Takes | Produces | Done by |
|---|---|---|---|
| Physics | Forces, rudder, engine | Positions, headings, speeds (states) | Vessel behaviours, [§13](#13-the-actors-faculty--the-vessels) |
| Situations | States of pairs of vessels | "Crossing", "head-on", "overtaking", "approach" (situations) | Monitors, [§14](#14-the-monitors-faculty--situations) |
| Terms | A situation and a question | A value for a phrase like "distance to the traffic lane" | Resolvers, [§15](#15-the-rules-faculty--legata-rules-and-examiners) |
| Rules | Terms | Kept or broken, clause by clause | Legata rules, [§15](#15-the-rules-faculty--legata-rules-and-examiners) |
| Scores | Broken clauses | A penalty in a database row | Scorecards and examiners, [§15](#15-the-rules-faculty--legata-rules-and-examiners) |

Read that table as the thesis of COS. The paper borrows the idea from Marvin Minsky's *Society of
Mind*: intelligence comes from many simple agents, each working at its own level of abstraction,
passing results upward. In COS those agents are called **faculties**. When you meet a design choice
that looks odd, such as a rule that never mentions a position, or an observer that does nothing but
label pairs of ships, check it against this table first. It is almost always a stage doing one job.

---

## 4. Hypotheses, and what the design does not commit to

Four hypotheses carry the design, and each is visible in the code.

1. **An autonomous ship should be judged the way a human master is judged.** If machines and people
   share the sea, they should meet the same standard, tested over whole voyages in realistic
   traffic rather than in a handful of staged encounters. This is why COS runs long simulations of
   busy waters and scores everything that happens, instead of testing single manoeuvres.
2. **Small, specialised observers can compose into judgement.** No single piece of COS understands
   COLREG. A monitor labels a crossing; a resolver measures a distance; a rule checks a clause; a
   scorecard prices it. Each faculty is simple, and the chain is what reads the rule.
3. **Knowledge belongs in files, not in code.** Maps, fleets, weather, rule texts and penalties are
   data. Changing the test site, the traffic or the law means changing files, not rebuilding the
   simulator.
4. **Coverage comes from volume.** No finite set of hand-written tests covers every situation, so COS
   is built to run the same scenario many times with its conditions permuted, and to compare the
   results in one database ([§17](#17-from-one-run-to-a-thousand)).

What the design deliberately does **not** commit to matters as much:

- **No single domain.** The kernel knows nothing about ships. Everything maritime lives in
  `src/maritime` and the configuration. The paper names road, rail and air as future domains.
- **No single physics model.** The physics of a vessel is a plug-in behaviour. The one in use today is
  deliberately simple ([§13](#13-the-actors-faculty--the-vessels)).
- **No single jurisdiction.** COLREG applies everywhere, but each site can add its own local rules,
  written in the same language ([§15](#15-the-rules-faculty--legata-rules-and-examiners)).
- **No claim of completeness.** The paper's own lesson is *what you model is what you assure*. A rule
  that is not written, or a term that is not measured, is simply not tested.
- **No real-time guarantee.** A simulation step takes as long as the computer needs. Some timers use
  the wall clock, and that has consequences ([§18](#18-levels-and-timescales)).

---

## 5. Lineage and neighbours

COS is not a clean-sheet design, and knowing what it borrows from lets you skip ahead.

**Simulation-based verification of autonomous ships** is the field it belongs to. The paper
positions COS against the *Open Simulation Platform* (OSP, an industry co-simulation standard for
ship models) and DNV's TestIT work. COS aims to host models like those as plug-ins, and adds
scenario sweeps and rule checking on top.

**Woerner's COLREG metrics** (MIT, 2016–2019) supply the encounter geometry. The thresholds in
`config/evaluator.yaml`, such as the 4,000 m, 1,100 m and 200 m ranges that stage an encounter and the
100 m minimum passing distance, follow that line of work.

**Minsky's *Society of Mind*** is the model for faculties: many small agents, each simple, whose
composition behaves intelligently ([§3](#3-the-central-problem-rules-speak-of-situations-simulators-produce-states)).

**Operating systems** supply the structure: a kernel, a boot sequence, run levels, a scheduler
calling services on a timer, a hierarchical namespace of named objects (like a file system), and
message queues between processes.

**ZeroMQ**, a messaging library, carries requests and events between a running simulation and the
tools that watch it ([§16](#16-talking-to-a-running-simulation)).

**High-performance computing (HPC) clusters** and their **workload managers** (the paper names
SLURM) run the sweep: one task per scenario, many at once ([§17](#17-from-one-run-to-a-thousand)).

**Data warehouses** supply the output format. Results are *facts* (things that happened, with a time
and a value) keyed by *dimensions* (where, which vessel, which scenario), the layout used for
analysis cubes, also called OLAP.

---

## 6. The overview figure, and how to read this guide

```
  config/cos.ini ──(boot)──┐
                           ▼
  ┌──────────────────────────────────────────────────────────────────────┐
  │                      ONE COS PROCESS  (coslaunch)                    │
  │                                                                      │
  │   KERNEL   configuration · object tree · message queue · clock       │
  │      │                                                               │
  │      │ (a) every tick: on_timer()                                    │
  │      ▼                                                               │
  │   ┌──────────────┐  ┌────────────┐  ┌──────────────┐  ┌──────────┐   │
  │   │ ENVIRONMENT  │  │   ACTORS   │  │   MONITORS   │  │  RULES   │   │
  │   │ land · sea   │  │  vessels   │─▶│  situations  │─▶│ Legata   │   │
  │   │ sky · weather│─▶│  behaviour │  │  conduct     │  │ examiners│   │
  │   └──────────────┘  └────────────┘  └──────────────┘  └────┬─────┘   │
  │            (b) topics on the internal message queue        │         │
  │                                                            │ (d)     │
  │   SUBSYSTEMS   World · NetworkManager · DataManager ◀──────┘         │
  └──────────────────┬──────────────────────────────────────┬────────────┘
                     │ (c) RPC :5556 · events :5557         │ (d) every 5 s
                     ▼                                      ▼
          cviz · costopic · cosservice              workingset .s3db
                                                            │ (e) after the sweep
                                                            ▼
                                              merged database → analysis
```

*Figure 2. One COS process, and the five kinds of connection narrated below.*

There are five kinds of connection in that figure, and each one is explained in a section below:

- **(a) Timer calls.** The kernel's runner calls every service once per step.
  [§8](#8-the-life-of-a-simulation), [§10](#10-the-kernel).
- **(b) Internal messages.** Faculties post events such as "vessel.crossing" to named topics, and other
  faculties read them. [§10](#10-the-kernel), [§14](#14-the-monitors-faculty--situations).
- **(c) Outside connections.** Tools send requests to a running simulation on port 5556 and receive its
  event stream on port 5557. [§16](#16-talking-to-a-running-simulation).
- **(d) Recording.** Faculties hand results to the data manager, which writes them to a database file
  every 5 seconds. [§11](#11-the-kernel-subsystems).
- **(e) Merging.** After a sweep, the databases of many runs are merged into one for analysis.
  [§17](#17-from-one-run-to-a-thousand).

**Roadmap.** [§7](#7-one-run-end-to-end) follows one real run through the whole figure before any
box is opened. [§8](#8-the-life-of-a-simulation) and [§9](#9-what-cos-cannot-see) cover how a
simulation starts and stops, and where its view of the world ends. Sections
[10](#10-the-kernel) to [16](#16-talking-to-a-running-simulation) open one box at a time, following
the stages of [§3](#3-the-central-problem-rules-speak-of-situations-simulators-produce-states) from
the world up to the rules. [§17](#17-from-one-run-to-a-thousand) scales one run to many.
[§18](#18-levels-and-timescales) to [§21](#21-one-simulator-many-waters) are synthesis.

---

## 7. One run, end to end

Before opening any box, follow one run all the way through. The numbers here come from a real run
of the running example.

**The running example.** *True North* is a container ship, registered in the Türkeli fleet with the
identifier `bedc897f-512b-45a2-aea4-bcfc248d2a86`. It is the
**vessel under test**: the one whose behaviour is being judged. It follows the trip file
`trip/container.csv` down the Türkeli traffic lanes on a loop, among 33 other vessels. The weather
is fog. The traffic level is `hdta`, high density.

1. **Configure.** A copy of `config/cos.ini` sets the scenario: `COUNTRY=tk`, `LOCATION=turkeli`,
   `WEATHER=foggy`, `TRAFFIC=hdta`, and `RunCycles=1500` steps.
2. **Boot.** `coslaunch.py -config <that file> -port 6556` starts one COS process. The kernel reads
   the file, logs `Loading simulation from …`, and loads the kernel subsystems, then the five
   faculties, then the network services, each from its own YAML file ([§8](#8-the-life-of-a-simulation)).
3. **Build the world.** Builders read the Türkeli map (`land.s3db`, `sea.s3db`), the weather for fog
   (`environment.s3db`) and the fleet (`vessel.s3db`). Vessels whose `scenario=` tag does not match
   `hdta` are left out.
4. **Step.** Every 30 ms or so the runner calls each service. *True North* works out its next position
   from its trip and its ship model and moves.
5. **Notice.** About once a second the situation monitors compare every pair of vessels. In this run
   they logged 10 crossings, 112 head-on encounters, 5 give-way situations and 970 close-approach
   samples, each as a row in a `fact_…` table.
6. **Judge.** Every couple of seconds the rules run. Türkeli has its own local rule, written in
   Legata in `rule/turkeli.legata`. One clause says a vessel in the zone named `Turkeli.TSS.SpeedZone1`
   must have a draft under 10. *Draft* is how deep the hull sits in the water; deep ships are
   restricted in the strait. *True North* entered that zone, and the clause failed.
7. **Price.** The site's scorecard, `rule/score.json`, prices a broken `Turkeli.Bosphorous.DeepDraft`
   clause at 1,000,000 under the concern `Violation.DeepDraft`, for this vessel only.
8. **Record.** The rule hands the data manager a row for the table `fact_ro`: concern, time, the
   vessel's IMO number (9627837), penalty. Every 5 seconds the data manager writes its rows to the
   run's database file.
9. **Stop.** After 1,500 steps, about 58 seconds of wall-clock time, the runner stops, the faculties
   shut down in reverse order, and the last rows are written.

The result: `fact_ro` gained 435 rows. Thirty of them are `Violation.DeepDraft` for *True North*,
1,000,000 each. The other 405 are `Generic` rows with a penalty of 0, from clauses that have no price
on the scorecard.

Two things generalise from that walk. First, **nothing in the run was scripted as a test.** Nobody
wrote "check *True North* at step 400". The encounters were found by monitors, and the violation was
found by a rule that checks every vessel in the zone. Second, **the output is a table, not a
verdict.** A run does not pass or fail. It leaves rows, and the judgement comes from comparing rows
across many runs ([§17](#17-from-one-run-to-a-thousand)).

---

## 8. The life of a simulation

**Configuration.** A simulation is defined by one file, `cos.ini`. Its `[Folders]` section sets the
root folders. Its `[EnvironmentVariables]` section sets the **scenario variables**, the controlled
variables of the experiment: `COUNTRY`, `LOCATION`, `WEATHER`, `TRAFFIC`. From these it builds the
data paths, for example `MAP=$(CONFIG)/map/$(COUNTRY)/$(LOCATION)`. Every other file refers to
those names, so changing four lines moves the whole experiment to a different place and time.

**Boot.** The `[Simulation]` section lists what to load, in three groups:

```ini
[Simulation]
Kernel=Subsystem
Faculties=Environment,Monitors,Signals,Actors,Rules
Services=NetworkServices
```

Each name is another section, which lists YAML files; each YAML file lists Python classes to load.
For example `[Environment]` names `land.yaml`, `sea.yaml`, `sky.yaml` and `weather.yaml`, and
`weather.yaml` names three weather builders. The boot loader reads the lot and creates one object
per entry.

Startup then runs in a fixed order, like the run levels of a computer's operating system:

| Step | What happens |
|---|---|
| 1 | Kernel subsystems are initialised and started (`on_init`, `on_start`) |
| 2 | Every loaded module is started (`on_start`) in load order |
| 3 | Run levels 0 to 4: subsystems, then modules, get `on_run(level)` |
| 4 | The runner thread starts calling `on_timer` on every service, once per step |

Shutdown is the same in reverse: run levels 5 down to 1 (`on_term`), then modules and subsystems stop
(`on_stop`), and the data manager writes whatever it still holds.

**Stepping.** The runner calls `on_timer` on every service registered under `/Services`, then sleeps
30 ms, and repeats. `RunCycles` in `[ProcessManager]` sets how many steps a run lasts. The default,
1,000,000, is effectively "until you stop it".

**Identity.** At boot the kernel turns the scenario name, `SCENARIO=scenario-0:tk/turkeli/foggy/hdta`,
into a number, the first 4 bytes of its SHA-256 hash. That number is the run's **case id**, stored
with every row it writes. In the running example it is 1,002,191,103. The case id is how rows from a
thousand runs are told apart after they are merged.

**In our running example**, the log shows the three groups loading in order (`Loading Kernel:
Subsystem`, `Loading Faculties: …`, `Loading Services: NetworkServices`), and one line near the end
reports `Simulation duration of 1500 steps reached. Stopping simulation.`

---

## 9. What COS cannot see

A simulation only knows what it models. This section is about the edges of that knowledge, because
they decide what a result means. The paper's lesson applies literally: *what you model is what you
assure*.

**An unwritten rule is never broken.** COLREG has 41 rules, and COS loads a module for each (Rule 7 is
switched off). But a rule is only checked when a monitor hands it a situation. Today only Rule 13
(overtaking) and the local rules do that, so a crossing is detected and recorded, yet Rule 15's
clause for crossings is never evaluated. In the running example no COLREG rule raised a violation.

**An unpriced clause costs nothing.** The Türkeli rule has a speed-limit clause, but the scorecard has
no price for it. When it fails, a `Generic` row with a penalty of 0 is written. The 405 zero rows in
[§7](#7-one-run-end-to-end) are exactly this.

**An unmeasured term keeps its default.** Legata reads the world through resolvers
([§15](#15-the-rules-faculty--legata-rules-and-examiners)). Some resolvers return fixed values
today: visibility is always 1.0, and wave height and wind speed seen by the risk network are always
0. A rule or network that depends on them sees clear, calm weather whatever the scenario says.

**Weather is generated more fully than it is used.** Each scenario's weather has wind, current and wave
fields, and regions of fog, rain and snow. Only the wave field changes a result today, through the
capsize check ([§15](#15-the-rules-faculty--legata-rules-and-examiners)). Wind does not yet push
vessels, and nothing reads the fog regions.

**Identical input gives identical output.** Most sites in the repository started as copies of Türkeli,
and every site currently has the same 34 vessels. Where the data behind two scenario levels is the
same, their results will be the same. [`bugs/COS.010`](../../bugs/COS.010.md) measures how often.

**In our running example**, the fog is real data in the database, but *True North*'s penalty came from
its draft, not from the fog. The same run in clear weather would record the same violation.

None of this is hidden. The bug index lists each gap with the work needed to close it. Read a result
together with this section, and ask of any number: *was the thing that produced it actually modelled?*

---

## 10. The kernel

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
answer is the stages of [§3](#3-the-central-problem-rules-speak-of-situations-simulators-produce-states).
Dozens of independent faculties must be loaded from files, started in the right order, find each other
by name and pass results along without knowing about each other. That is exactly the problem an
operating system solves for programs.

**How others do it.** A typical research simulator is one program with a main loop that calls each
model in turn. Adding a model means editing the loop. In COS, adding a model means adding a line to a
YAML file.

**In our example.** *True North* is an object at a path under `/World/Vehicle/Vessel`. Its movement,
the monitors watching it and the rule that fined it are all services the runner calls each step.

---

## 11. The kernel subsystems

**What they do.** Three services that every simulation needs, loaded before any faculty from
`config/subsystem.yaml`.

| Subsystem | Job |
|---|---|
| **World** | Holds the simulated world: the map scale, the vessel range and the collision check |
| **DataManager** | Collects results and writes them to the run's database |
| **NetworkManager** | Hosts the network brokers that tools connect to ([§16](#16-talking-to-a-running-simulation)) |

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

## 12. The environment faculty — the world

**What it does.** Builds the physical world from data files: land, sea, sky and weather.

**What it's made of.** Builders, one per kind of shape, each reading one table of one database:

| Part | Reads | Makes |
|---|---|---|
| Land | `$(MAP)/land.s3db` | Coastlines: the only things vessels collide with |
| Sea | `$(MAP)/sea.s3db` | Areas with meaning: depth, traffic lanes, harbours, legal zones |
| Sky | `$(MAP)/sky.s3db` | Areas of fog and cloud |
| Weather | `config/weather/<country>/<location>/<WEATHER>/environment.s3db` | Wind, current and wave fields; weather regions |

**Sea areas are the vocabulary of the rules.** A traffic lane is a polygon with a type code (303000 for a
*traffic separation scheme*, a sea lane split in two like a dual carriageway) and a name such as
`Turkeli.TSS.North-to-South`. Rules refer to these by name and type. The depth of each area decides
whether a ship runs aground.

**Weather has two layers.** Vector fields of wind, current and waves act on vessels. Regions, polygons
with uniform precipitation, visibility and humidity, describe the air. Both are generated from
`config/weather/profiles.yaml`; [`WEATHERGEN.md`](../../tools/mapping/WEATHERGEN.md) explains how.

**When it runs.** Builders run once at startup. The weather fields update on a timer.

**Why it's built this way.** Keeping the world in databases means a new test site is a new set of files.
[`MAPGEN.md`](../../tools/mapping/MAPGEN.md) lists what a site needs, and what has gone wrong before.

**In our example.** The zone that caught *True North*, `Turkeli.TSS.SpeedZone1`, is one row in Türkeli's
`sea.s3db`. The fog is six regions in `config/weather/tk/turkeli/foggy/environment.s3db`, three of them
fog banks.

---

## 13. The actors faculty — the vessels

**What it does.** Creates the vessels and moves them.

**What it's made of.** Vessel builders read `$(SIMULATION)/vessel.s3db`. Each row is one vessel: name,
identifier, type code (power-driven, sailing and so on), size, starting position, and a **behaviour**,
the Python class that moves it.

| Behaviour | Moves by |
|---|---|
| `ContainerShip`, `Ferry`, `FishingVessel` | Following a trip file of waypoints, with COLREG-aware manoeuvres |
| `BrownianMotionBehavior` | A random walk inside a rectangle, for background traffic |
| `LinearMotionBehavior` | A constant velocity |
| `NavalFleet` | Steering a group of vessels as a flock |

**Traffic levels.** A vessel's `scenario=` tags say which traffic levels it takes part in. With
`TRAFFIC=hdta`, only vessels tagged for `hdta`, and untagged vessels, are created. This is how one
fleet file serves several traffic densities.

**Physics.** Trip followers use a ship model from `config/vehicle/ship/`. The paper describes a
three-degrees-of-freedom manoeuvring model, which tracks forward speed, sideways drift and turn rate.
The model in the code today is simpler. It controls forward speed and turn rate towards the next
waypoint and integrates them in small steps. It does not yet take wind or current into account.

**When it runs.** Every step.

**Why it's built this way.** The vessel under test is a behaviour like any other. To test a real
autonomous-navigation system, you wrap it as a behaviour and give it a row in the fleet file. Nothing
else in COS needs to change.

**In our example.** *True North* is row 101 of Türkeli's fleet, with behaviour `ContainerShip`, trip
`container.csv` (four waypoints, looped) and the ship model `container.yaml`.

---

## 14. The monitors faculty — situations

**What it does.** Watches the vessels and names what is happening between them. This is the second stage
of [§3](#3-the-central-problem-rules-speak-of-situations-simulators-produce-states): states in,
situations out.

**What it's made of.** Two groups of modules:

| Group | File | Detects |
|---|---|---|
| Situations | `config/situation.yaml` | Encounter, crossing, give-way, head-on, overtaking, stand-on, traffic |
| Conduct | `config/conduct.yaml` | Narrow channels, collisions, harbour, obstruction, grounding |

**How an encounter is found.** For each pair of vessels, the monitors compute the geometry: range,
bearing, and the **closest point of approach** (CPA), the smallest distance the two will reach if
neither changes course. The thresholds are in `config/evaluator.yaml`. An encounter is followed in
stages as the range closes through 4,000 m, 1,100 m and 200 m. A pass closer than 100 m is too
close, closer than 50 m is a near miss, and closer than 30 m would most likely have been a collision.
The angles between the two headings decide whether it is head-on, crossing or overtaking.

**What it produces.** Two things for each situation it finds: a row in a `fact_…` table, and an event
on the message queue, such as `vessel.crossing`, for the rules to pick up.

**When it runs.** On a timer set to half a second, which in practice fires about once a second
([§18](#18-levels-and-timescales)).

**Why it's built this way.** Separating "what is happening" from "is it allowed" means a crossing is
detected once, however many rules care about crossings.

**In our example.** In 58 seconds the monitors recorded 10 crossings, 112 head-on encounters,
5 give-way situations and 970 close-approach samples among the 34 vessels.

---

## 15. The rules faculty — Legata, rules and examiners

**What it does.** Judges the situations: which clauses of which rules were kept or broken, and at what
cost. These are the last three stages of
[§3](#3-the-central-problem-rules-speak-of-situations-simulators-produce-states).

**Legata, the rule language.** A rule is written as a text file of clauses. Each clause has a
**condition**, when it applies, and **assure** lines, what must then be true. Here is the Türkeli
clause that caught *True North*:

```
clause['Turkeli.Bosphorous.DeepDraft']:{
    : {
        condition: { : (OS,TrafficSeparationScheme).Name is 'Turkeli.TSS.SpeedZone1' }
        assure:    { : OS.Draft < 10 }
    }
}
```

`OS` is shorthand for *own ship*, the vessel being judged; `TS` is the *target ship*, the other one in
an encounter. Legata files are compiled once, at startup, into a decision tree that the rule's
**automaton**, its checking engine, walks through for each situation.

**Resolvers.** Terms such as `OS.Draft` or `(OS,TS).Distance` are not stored anywhere. A **resolver** works
them out when the automaton asks, by looking into the running simulation. Resolvers are plug-ins listed
in `config/legata.yaml`, one per family of terms: targets, lanes, harbours, economic zones. This is how
a vague word gets a precise meaning: "safe distance in the lane" becomes whatever the lane resolver
computes. The paper calls resolvers *probes* into the simulated world.

**Three kinds of rule.**

| Kind | Loaded from | Checks | Records |
|---|---|---|---|
| COLREG | `config/rules.colreg.yaml`: one module and one Legata file per rule, 41 in all | Situations handed to it by monitors | A log line when a clause fails |
| Local rules | `$(SIMULATION)/rules.yaml`, per site | Every vessel inside the site's named zones | A priced row in `fact_ro` |
| Examiners | `config/rules.examiner.yaml`, `config/rules.risk.yaml` | Specific concerns: approach, berthing, collision, grounding, lane discipline, weather, risk | Their own fact tables |

**Scorecards.** A local rule's `score.json` gives each clause a price, a *concern* (the kind of harm or
breach) and, optionally, the vessels it applies to. A clause without an entry is recorded as `Generic`
with a penalty of 0.

**Two measures of risk.** Current work (the P3 paper) separates two things. **Normative risk**, written
`Ro`, counts rule violations along the path the vessel actually took: the `fact_ro` rows. **Consequential
risk**, written `Rb`, estimates the chance and cost of harm on paths not taken. The risk examiner does
this with a Bayesian network, a probability model of how hazards lead to consequences, loaded from
`config/risk/risk.model.xdsl` and priced per zone and concern in each site's `risk.yaml`. The weather
examiner feeds wave height into a separate capsize network.

**When it runs.** On the evaluator's sample timer, set to 1, which in practice fires about every
2 seconds ([§18](#18-levels-and-timescales)).

**Why it's built this way.** The law changes, and it differs between places. Keeping rules as text, their
vocabulary in resolvers and their prices in scorecards means a lawyer can read a rule, a programmer can
add a term, and an analyst can change a price, each without touching the others' work.

**In our example.** `WaterwayRule` loaded `turkeli.legata` for zones named `Turkeli*`, checked every
vessel in them each time it ran, and priced *True North*'s broken DeepDraft clause from `score.json`:
30 rows, 1,000,000 each.

---

## 16. Talking to a running simulation

**What it does.** Lets other programs watch and question a simulation while it runs.

**How you talk to it.** Two ports, opened by the network broker:

| Port | Kind | Used for |
|---|---|---|
| 5556 (RPC) | Request and reply | Calling a method on an object in the tree, for example "list the services" |
| 5557 (events) | Publish and subscribe | A stream of events: vessel moves, weather updates |

Start a simulation with `-port N` to use N and N+1 instead, so two simulations can run side by side.

**The tools.**

| Tool | Does |
|---|---|
| `coslaunch` | Starts a simulation from a `cos.ini` |
| `cviz` | Draws the map, zones, vessels and weather live, from the event stream |
| `costopic` | Lists topics and reads or posts messages on them |
| `cosservice` | Lists the object tree and describes an object |

Each has a man page ([§1](#1-what-this-document-is)).

**Why it's built this way.** Watching should not change what is watched. The tools run as separate
programs, and `cviz` and `cosservice` only read, so a simulation behaves the same with or without a viewer
attached. `costopic pub` is the exception: it posts a message into the simulation, which is useful for
testing a rule by hand.

**In our example.** The run used `-port 6556`, so it could not clash with a simulation already running on
the default ports. `cviz.py host localhost:6556` would have shown *True North* moving through the lanes.

---

## 17. From one run to a thousand

A single run proves little. The value of COS comes from running the same scenario many times with its
conditions changed, and comparing the results.

**The simulule.** The paper calls one run a **simulule**, a *simulation capsule*: a self-contained
simulation of one combination of conditions, isolated from every other. In the code, a simulule is one
`coslaunch` process started with its own generated configuration folder.

**The pipeline.** Four steps, following the paper:

| Step | Does | In the code |
|---|---|---|
| Scenario generation | Lists every combination of the scenario variables, samples them, and writes one configuration folder per case, plus a task file with one command per line | `ScenarioGenerator`, `templates/cluster/` |
| Cluster run | A workload manager on a computing cluster runs the task file, one simulule per task, many at once | Outside COS (for example SLURM) |
| Aggregation | Renumbers each run's rows into its own block of ids, so they cannot collide, and merges all run databases into one | `cos.data.bi.Builder` |
| Reporting | Analyses the merged facts by dimension: site, weather, traffic, vessel | The OLAP layout in `config/data/` |

**The sweep today.** Sites are read from `config/simulation/`, currently 15. Each is paired with 9 weather
types and 7 traffic levels, giving 945 combinations. Before writing anything, the generator checks that
every combination's simulation folder, map folder and weather databases exist, and refuses to continue
if one is missing. The
paper describes a capacity of 10⁵ to 10⁷ scenarios; the size of a sweep is set by the number of levels
per variable.

**Why it's built this way.** Each simulule shares nothing with the others, so they can run anywhere, in any
order, and a crash loses one case. The case id ([§8](#8-the-life-of-a-simulation)) travels with every row,
so results stay attributable after merging.

**In our example.** *True North* at Türkeli, in fog, at high density, is one of the 945 cases. Its
neighbours in the sweep are the same ship in clear weather, in a hurricane, or in light traffic. The
question the sweep answers is how its penalties change across them.

---

## 18. Levels and timescales

COS acts at several rates, and they are not all measured in the same kind of time.

| Level | Rate | Clock | Decides |
|---|---|---|---|
| Step | Every ~30–40 ms | Wall clock (a 30 ms sleep plus the work) | Vessel movement |
| Situation monitoring | About once a second | Wall clock | Encounters and conduct events |
| Rule evaluation | About every 2 seconds | Wall clock | Violations and penalties |
| Weather update | About every 2 seconds | Wall clock | Rotation of the weather fields |
| Recording | Every 5 seconds | Wall clock | Rows written to disk |
| Run | `RunCycles` steps | Step count | When the simulation stops |
| Sweep | Hours to days | Cluster | Which conditions are compared |

**One consequence to know.** Monitors, rules and weather run on timers measured in real seconds, and
those timers round down to whole seconds. A timer set to 0.5 s fires about once a second; one set to
1 s fires about every 2 seconds. Vessels, by contrast, move once per step. So **the number of times a
rule is checked during a voyage depends on how fast the computer is.** A slower machine takes more
steps per real second of rule timing, and so checks less often per metre sailed. When comparing runs,
compare them on the same kind of machine, or count per step rather than per second.

**In our example.** 1,500 steps took about 58 seconds, roughly 39 ms per step. On a machine twice as fast
the same 1,500 steps would take about half the time, and the rules would run about half as often.

---

## 19. The parts compared

The same questions, asked of every part.

| Part | Knows from | Holds | How you reach it | Keeps its data | Changes a result? |
|---|---|---|---|---|---|
| Kernel | `cos.ini` | Object tree, topics, clock | Object paths, topics | For the run | Only through timing |
| Environment | Map and weather databases | Shapes, fields, regions | `/World/...` | For the run | Yes: land, depth, zones, waves |
| Actors | Fleet database, trip files | Vessels and behaviours | `/World/Vehicle/Vessel` | For the run | Yes: every movement |
| Monitors | Vessel states | Situations | Topics, `fact_…` rows | Rows on disk | Yes: what the rules see |
| Rules | Legata files, scorecards | Clause results, penalties | `fact_ro`, examiner tables | Rows on disk | Yes: the score |
| Data manager | Faculties | Rows in memory | The run database | On disk, every 5 s | No |
| Tools | Ports 5556/5557 | Nothing | Command line | No | No |
| Sweep pipeline | Scenario variables | Folders, task file, merged database | Files | On disk | Decides which runs exist |

Two things the table makes visible. First, **only three parts decide a score**: the world, the vessels and
the rules. Everything else carries, records or displays. Second, **every part that decides a score reads
its knowledge from files.** That is hypothesis 3 of [§4](#4-hypotheses-and-what-the-design-does-not-commit-to)
made concrete: to change what COS tests, you change data.

---

## 20. Combinations that are not obvious

These are places where two mechanisms described separately above combine to do something neither does
alone.

1. **Situations are found, not scripted, so every encounter is tested.** Monitors label every pair of
   vessels on every pass, and rules check every labelled situation. A test that nobody thought to write
   still runs. ([§14](#14-the-monitors-faculty--situations) + [§15](#15-the-rules-faculty--legata-rules-and-examiners))
2. **A zone name is both geography and law.** `Turkeli.TSS.SpeedZone1` is a polygon in a map database and a
   word in a Legata clause. Redrawing the zone changes where the rule applies, without editing the rule.
   ([§12](#12-the-environment-faculty--the-world) + [§15](#15-the-rules-faculty--legata-rules-and-examiners))
3. **Resolvers let vague words grow precise over time.** "Safe distance" starts as a fixed number in a
   resolver and can later become a model, a lookup or a learned function, with no change to the rule
   text. ([§15](#15-the-rules-faculty--legata-rules-and-examiners))
4. **Four scenario variables move the whole experiment.** Because every data path is built from
   `COUNTRY`, `LOCATION`, `WEATHER` and `TRAFFIC`, the sweep generator only has to write four lines per
   case. ([§8](#8-the-life-of-a-simulation) + [§17](#17-from-one-run-to-a-thousand))
5. **The case id makes a thousand databases one.** A hash of the scenario name is stored in every row, so
   merged results can be grouped back into their runs and compared by any variable.
   ([§8](#8-the-life-of-a-simulation) + [§17](#17-from-one-run-to-a-thousand))
6. **The vessel under test is just another vessel.** Because behaviours are plug-ins, an external
   navigation system is tested by putting it in the fleet file. Its penalties are then priced by the same
   scorecards as every other ship. ([§13](#13-the-actors-faculty--the-vessels) + [§15](#15-the-rules-faculty--legata-rules-and-examiners))
7. **A price of 0 is a finding.** `Generic` rows show that a clause failed but nobody decided what it costs.
   Counting them across a sweep lists the clauses whose price still needs to be set.
   ([§9](#9-what-cos-cannot-see) + [§15](#15-the-rules-faculty--legata-rules-and-examiners))

---

## 21. One simulator, many waters

The kernel and faculties are the same everywhere. A site supplies its own map, fleet, weather and,
optionally, local rules.

| Site | What makes it different | Map scale | Local rules |
|---|---|---|---|
| Türkeli (`tk/turkeli`) | Northern mouth of the Bosphorus; traffic lanes, a speed zone and a fuelling depot | 1 m per unit, hand-drawn | Yes: Türkeli, Marmara, Bosphorus |
| Istanbul (`tk/istanbul`) | The strait itself | 1 m per unit, hand-drawn | Yes: the same three |
| Trondheim, Oslo, Bergen, Tautra (`no/…`) | Norwegian fjords and ports, built from open map data | 40 m per unit | No |
| Hormuz (`om/hormuz`) | A strait with one traffic lane from open data | 100 m per unit | No |
| Singapore (`sg/singapore`) | A crowded strait with six traffic-lane shapes | 40 m per unit | No |

**What changes and what doesn't.** Moving the running example from Türkeli to Singapore changes four lines
in `cos.ini`. The kernel, faculties, rule language and tools are untouched. The Türkeli local rule would no
longer load, because Singapore has none yet, so *True North* would be judged by COLREG and the examiners
alone. That is the domain-agnostic design of [§4](#4-hypotheses-and-what-the-design-does-not-commit-to) in
practice, and also its limit: a site is only as well tested as its local rules are written.

---

## Appendix A. Glossary

Every term here is introduced in the body above.

| Term | Meaning |
|---|---|
| **Automaton** | The checking engine of a rule: it walks the compiled clauses of a Legata file for each situation |
| **Behaviour** | The plug-in class that moves a vessel |
| **Builder** | A module that reads a database table at startup and creates world objects from it |
| **Case id** | A number derived from the scenario name, stored in every row a run writes |
| **Clause** | One condition-and-requirement unit of a Legata rule |
| **COLREG** | The International Regulations for Preventing Collisions at Sea: 41 rules for how ships avoid each other |
| **Concern** | The kind of breach or harm a penalty is filed under, for example `Violation.DeepDraft` |
| **CPA** | Closest point of approach: the smallest distance two vessels will reach if neither changes course |
| **Draft** | How deep a ship's hull sits below the waterline |
| **Examiner** | A rule module that scores one concern, such as grounding or weather, into its own table |
| **Fact table** | A database table of events, `fact_…`, each row with a time, a case id and values |
| **Faculty** | A plug-in service at one level of abstraction: environment, actors, monitors, signals, rules |
| **Legata** | The COS rule language |
| **Local rule** | A site-specific rule, loaded from the site's `rules.yaml`, checked against every vessel in its zones |
| **Map unit** | The unit map data is drawn in; each map declares how many metres it is |
| **Monitor** | A faculty that turns vessel states into named situations |
| **Normative risk (`Ro`)** | The priced rule violations along the path a vessel actually took |
| **Consequential risk (`Rb`)** | The estimated cost of harm, from a probability network |
| **Object tree** | The kernel's hierarchy of named objects, addressed by paths like `/World/Vehicle/Vessel` |
| **Resolver** | A plug-in that computes the value of a Legata term from the running simulation |
| **Scenario variables** | `COUNTRY`, `LOCATION`, `WEATHER`, `TRAFFIC`: the controlled variables of a run |
| **Scorecard** | A site's `score.json`: the price and concern for each clause |
| **Simulule** | One self-contained run of one scenario; in the code, one `coslaunch` process |
| **Situation** | A named relation between vessels, or between a vessel and a place: crossing, head-on, in a zone |
| **Step** | One pass of the runner over all services |
| **Sweep** | Many runs of a scenario with its variables permuted |
| **Topic** | A named channel on the kernel's message queue |
| **TSS** | Traffic separation scheme: a sea lane split in two so ships going opposite ways stay apart |
| **Vessel range** | The rectangle vessels are kept inside |
| **Vessel under test** | The ship whose behaviour a scenario is judging |

**A terminology caution.** Four words mean more than one thing in COS, and they are the most common source of
confusion:

- **Rule** is a COLREG rule, a local rule, and a Python module that loads a Legata file. When it matters,
  say which.
- **Situation** is an encounter found by a monitor, and also the object a rule is evaluated against, which
  may be a single vessel in a zone with no other ship involved.
- **Zone** is a sea area in a map database, a row of the risk loss matrix (high seas, territorial waters,
  internal waters, port), and, loosely, a weather region. They are different things.
- **Scenario** is one combination of the scenario variables, and also the `scenario=` tag on a vessel that
  decides which traffic levels include it.

## Appendix B. Where things live

| Subject | Location |
|---|---|
| Design and research context | `papers/reference/ER2024__Safety_Assurances_in_Autonomous_Vessels.pdf` |
| Kernel, runner, boot loader | `src/cos/core/kernel`, `src/cos/core/simulation` |
| Subsystems | `src/cos/subsystem` |
| World building, weather | `src/cos/model`, `config/land.yaml`, `sea.yaml`, `sky.yaml`, `weather.yaml` |
| Vessels and behaviours | `src/maritime/model/vessel`, `src/maritime/behavior`, `config/vessel.yaml` |
| Monitors | `src/maritime/situation`, `src/maritime/conduct`, `config/situation.yaml`, `conduct.yaml`, `evaluator.yaml` |
| Legata compiler and runtime | `src/cos/lang/legata`, `src/cos/model/rule` |
| COLREG rule texts | `config/maritime/regulation/colreg/Rule*.legata` |
| Local rules and scorecards | `config/simulation/<country>/<location>/rules.yaml`, `rule/` |
| Examiners and risk | `src/rules/examiner`, `config/rules.examiner.yaml`, `config/rules.risk.yaml`, `config/risk/` |
| Resolvers | `src/maritime/model/resolver`, `config/legata.yaml` |
| Database layout | `config/data/maritime.xml` |
| Sweep pipeline | `src/cos/cluster/runtime`, `src/cos/data/bi`, `templates/cluster` |
| Tools and man pages | `apps/*/` |
| Site data | `config/map`, `config/simulation`, `config/weather` |
| Known defects | `bugs/INDEX.md` |

<footer class="copyright" />
