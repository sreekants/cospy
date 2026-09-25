# The Co-Simulation Operating System — Architecture Guide

How COS, a simulator built to test autonomous ships against the rules of the sea, is put together:
what its parts are, what each one does, and why it is built that way. One example runs through the
whole guide. A container ship called *True North* sails through the Türkeli traffic lanes at the
northern mouth of the Bosphorus, in fog, among 33 other vessels. You follow it from a line in a
configuration file to a penalty in a database, and then see how the same run is repeated a thousand
times with the conditions changed.

Start here if you want to know how COS works. You should already know what a simulation is: a model
of a system, stepped forward in time, whose output you measure. You don't need to know anything about
ships, maritime law or COS itself. Every term is defined where it first appears and again in the
[glossary](glossary.md).

This guide is **not** a manual, an API reference or a build guide. It describes what the parts are and
how they fit, at the level where you can predict how COS will behave in a case the guide never
mentions. Where the ER 2024 paper describes what COS is designed to do, the guide says so. Where the
code does less than the design, the guide says what the code does today. Treat the paper as the
direction and this guide as the current position.

---

## File organization

The guide is an overview (this page) plus one page per subject. Links are relative, so the set works
when served as static files.

```
docs/guide/
├── INDEX.md             this overview: §1 the organising idea, §2 the packages of src/,
│                        §3 the top-level layout, §4 where to start, §5 where things live
├── concepts.md          what COS is and isn't · the central problem · hypotheses · lineage ·
│                        what COS cannot see
├── walkthrough.md       the overview figure · one run, end to end · the life of a simulation
├── kernel.md            the kernel and its subsystems · the object tree and its path reference ·
│                        boot and one step, in code
├── world.md             the environment faculty (land, sea, sky, weather) · the actors faculty (vessels)
├── regulation.md        monitors and situations · Legata, rules, resolvers and scorecards · examiners ·
│                        how the evaluator drives them · how a term is resolved
├── communication.md     ports and tools · the remote API: services and proxies · internal messages
├── sweeps.md            from one run to a thousand: scenario generation, case identity, merging
├── synthesis.md         levels and timescales · the parts compared · combinations · many waters
├── layers.md            src/ package by package: sizes, key classes, layering and naming rules
├── support.md           config/, templates/, tests/, tools/, samples/, idl/, papers/
├── extending.md         how to add an examiner, a rule, a resolver, a behaviour or a location
├── scaffolding.md       what exists only as a stub, and what is not wired in
├── glossary.md          every term, and the four words that mean more than one thing
└── cos-structure.html   one-page visual map of the source tree and one run — A4, print-ready
```

## Table of Contents

* [1. The organising idea: an operating system for simulations](#1-the-organising-idea-an-operating-system-for-simulations)
* [2. The packages of `src/`](#2-the-packages-of-src)
* [3. Top-level layout](#3-top-level-layout)
* [4. Where to start](#4-where-to-start)
* [5. Where things live](#5-where-things-live)

The subject pages, in the order they are worth reading:

* [`concepts.md`](concepts.md) — what COS is, and the one problem every part of it answers
* [`walkthrough.md`](walkthrough.md) — one real run, from configuration to penalty
* [`kernel.md`](kernel.md) — the kernel, its subsystems, the object tree, and one step in code
* [`world.md`](world.md) — land, sea, sky, weather and vessels
* [`regulation.md`](regulation.md) — situations, Legata rules, resolvers, scorecards and examiners
* [`communication.md`](communication.md) — ports, tools, and the remote API
* [`sweeps.md`](sweeps.md) — running a scenario a thousand times
* [`synthesis.md`](synthesis.md) — timescales, comparisons, combinations, sites
* [`layers.md`](layers.md) — the source tree, package by package
* [`support.md`](support.md) — everything outside `src/`
* [`extending.md`](extending.md) — adding to COS
* [`scaffolding.md`](scaffolding.md) — ⚠ stubs and unused code
* [`glossary.md`](glossary.md) — the terms

If you read only one of them, make it [`concepts.md`](concepts.md). If you are about to change code,
read [`extending.md`](extending.md) first: a class never runs until a configuration file names it, and
that rule explains most of how COS is put together.

---

## 1. The organising idea: an operating system for simulations

COS is named for what it is. It is structured like a computer's operating system, and the names in
the code are that metaphor, not decoration. The things it schedules are not programs but pieces of a
simulated world: a coastline, a weather front, a ferry, an observer that notices two ships crossing,
a rule that judges them.

| Operating system | COS | Where |
|---|---|---|
| Kernel | `Kernel`: boots a simulation, owns the clock, the object tree and the message queue | `src/cos/core/kernel` |
| Boot loader and run levels | `BootLoader`: loads modules from YAML manifests, then `on_init` → `on_start` → run levels 0–4 | `src/cos/core/kernel/BootLoader.py` |
| Scheduler | `Runner`: calls every service once per step, then sleeps 30 ms | `src/cos/core/simulation/Runner.py` |
| File system namespace | The object tree: every object has a path such as `/World/Vehicle/Vessel` | `ObjectManager` |
| Inter-process messaging | The message queue: named topics that faculties post to and read from | `MessageQueue` |
| System services | Subsystems: `World`, `DataManager`, `NetworkManager` | `src/cos/subsystem` |
| Device drivers | Builders: read a database at boot and create world objects | `src/cos/model/geography`, `src/maritime/model/vessel` |
| Processes | Faculties: environment, actors, monitors, signals, rules | `src/cos`, `src/maritime`, `src/rules` |
| One run of a batch job | A *simulule*: one `coslaunch` process with its own configuration | [`sweeps.md`](sweeps.md) |

The one borrowing that is not from operating systems is the word **faculty**. It comes from Minsky's
*Society of Mind*: many small agents, each simple and each working at its own level of abstraction,
whose composition behaves intelligently. That idea is the thesis of COS, and
[`concepts.md`](concepts.md#the-central-problem-rules-speak-of-situations-simulators-produce-states)
explains it.

Four ordinary words mean more than one thing in COS, and they are the most common source of
confusion: **rule**, **situation**, **zone** and **scenario**. The [glossary](glossary.md) says which
meaning is which.

---

<iframe src="cos-structure.html" title="COS — one-page source structure" style="width:100%; height:1140px; border:none;"></iframe>

## 2. The packages of `src/`

`src/` holds four top-level packages. The dependencies run one way: `rules` → `maritime` → `cos`.
Sizes count lines of Python. The full treatment of each package is in [`layers.md`](layers.md).

| Package | Classes | Role | Status |
|---|---|---|---|
| [`cos`](layers.md#cos--the-simulation-operating-system) | 335 | The domain-neutral simulation OS: kernel, object tree, tick loop, messaging, persistence, Legata, a generic world of shapes and vehicles | ok |
| [`maritime`](layers.md#maritime--the-domain-layer) | 118 | The maritime domain: vessels, sea zones, encounters, manoeuvres, the COLREG evaluator | navigation and traffic are scaffolding |
| [`rules`](layers.md#rules--regulation-content) |  65 | Regulation content: 41 COLREG rule classes and the examiners | ⚠ 33 rule classes and 9 examiners are stubs |
| [`cai`](layers.md#cai--planning-experiments) |  2 | Path-planning experiments (RRT, A*, Dijkstra) | ⚠ not used by COS |

A module existing is not evidence that a feature exists. See [`scaffolding.md`](scaffolding.md).

---

## 3. Top-level layout

| Directory | Purpose |
|---|---|
| `src/` | All Python source, in the four packages above. The only place you edit code |
| `apps/` | The four programs: `coslaunch`, `cviz`, `costopic` and `cosservice`. Their man pages are in `docs/tools/` |
| `config/` | `cos.ini`, the YAML manifests that say what to load, Legata rule texts, and per-location data under `map/`, `simulation/` and `weather/` |
| `templates/cluster/` | The configuration template the sweep generator copies once per case |
| `tests/` | pytest suites mirroring `src/`: `tests/cos`, `tests/maritime`, `tests/rules` |
| `tools/` | Location and weather generators (`mapping/`), database utilities (`dbtools/`), a rule evaluator (`colreg/`) |
| `idl/` | Interface contracts for the remote API, one `.idl` per service |
| `samples/` | Standalone examples: a minimal simulation (`minsim`) and an OpenBridge conning-display prototype |
| `papers/` | The research the platform serves: the ER 2024 paper and current work |
| `docs/` | This guide, the tools' man pages (`docs/tools/`), taxonomies, references, and the generated API pages (`mkdocs`) |
| `build/` | Run output: the system log and metrics databases |

Details of each are in [`support.md`](support.md).

---

## 4. Where to start

| Goal | Go to |
|---|---|
| Understand what COS is for | [`concepts.md`](concepts.md) |
| See one run from start to finish | [`walkthrough.md`](walkthrough.md#one-run-end-to-end) |
| Run a simulation or watch one | [`communication.md`](communication.md) and the man page for [coslaunch](../tools/coslaunch.md) |
| Understand what happens in one step | [`kernel.md`](kernel.md#one-step-in-code) |
| Find which class owns a path such as `/World/Sea` | [`kernel.md`](kernel.md#the-path-reference) |
| Build a new location | [`MAPGEN.md`](../../tools/mapping/MAPGEN.md), then [`SHIPGEN.md`](../../tools/mapping/SHIPGEN.md) and [`WEATHERGEN.md`](../../tools/mapping/WEATHERGEN.md) |
| Write or change a rule | [`regulation.md`](regulation.md#the-rules-faculty--legata-rules-and-examiners), then [`extending.md`](extending.md#add-a-local-rule) |
| Add an examiner, a resolver or a vessel behaviour | [`extending.md`](extending.md) |
| Run a sweep | [`sweeps.md`](sweeps.md) |
| Interpret a result | [`concepts.md`](concepts.md#what-cos-cannot-see) and [`synthesis.md`](synthesis.md#levels-and-timescales) |
| Find out why a module has no effect | [`scaffolding.md`](scaffolding.md) |
| Look up a class | [`layers.md`](layers.md), or the generated API pages (`mkdocs serve`, then *Modules*) |

---

## 5. Where things live

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
| Remote API | `src/cos/core/service`, `src/cos/core/api`, `config/api.yaml`, `idl/` |
| Database layout | `config/data/maritime.xml` |
| Sweep pipeline | `src/cos/cluster/runtime`, `src/cos/data/bi`, `templates/cluster` |
| Tools and man pages | `apps/*/`, `docs/tools/` |
| Site data | `config/map`, `config/simulation`, `config/weather` |

**Further reading.**

| For | Read |
|---|---|
| The research this platform was built for | Sreedharan, Ramachandran, Røsæg and Rokseth, *Safety Assurances in Autonomous Vessels* (ER 2024), `papers/reference/` |
| The rule language, Legata | Sreedharan et al., *Legata*, CS&Law 2025 |
| The risk formalism used in current work | `papers/IEEE-Access/DEFINITIONS.md` |
| Building a location: land, sea, vessels | [`MAPGEN.md`](../../tools/mapping/MAPGEN.md), [`SHIPGEN.md`](../../tools/mapping/SHIPGEN.md) |
| Generating weather | [`WEATHERGEN.md`](../../tools/mapping/WEATHERGEN.md) |
| Running the programs | the man pages for [coslaunch](../tools/coslaunch.md), [cviz](../tools/cviz.md), [costopic](../tools/costopic.md), [cosservice](../tools/cosservice.md) |
