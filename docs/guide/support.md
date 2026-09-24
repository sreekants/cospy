# Outside `src/`: configuration, templates, tests and tools

[← INDEX](INDEX.md) · [kernel](kernel.md) · [extending](extending.md) · [MAPGEN](../../tools/mapping/MAPGEN.md)

Everything in the repository that is not Python source under `src/`. Most of what makes one simulation
different from another lives here, not in code.

---

## `config/` — the simulation is data

A simulation is defined by one file, `config/cos.ini`, and everything it names. Its
`[EnvironmentVariables]` section holds the four **scenario variables** (`COUNTRY`, `LOCATION`,
`WEATHER`, `TRAFFIC`) and builds every data path from them. Its `[Simulation]` section lists what to
load, in three groups, and each name in a group is another section that names YAML **manifests**.
Each manifest lists the Python classes to create ([boot, in code](kernel.md#boot-in-code)).

| Group | Section | Key → manifest | Loads |
|---|---|---|---|
| Kernel | `[Subsystem]` | `Level-0` → `subsystem.yaml` | `NetworkManager`, `DataManager`, `World` |
| Faculties | `[Environment]` | `Land`, `Sea`, `Sky`, `Weather` → `land.yaml`, `sea.yaml`, `sky.yaml`, `weather.yaml` | One builder per shape type, reading `$(MAP)/*.s3db` and the weather database |
| | `[Monitors]` | `Situation`, `Conduct`, `Evaluator` → `situation.yaml`, `conduct.yaml`, `evaluator.yaml` | Situation and conduct monitors; the COLREG evaluator and its thresholds |
| | `[Signals]` | `Beacons`, `Radars`, `PortAuthorities`, `Mapping` → `beacon.yaml`, `radar.yaml`, `port.yaml`, `mapping.yaml` | The `Map` service. The beacon, radar and port-authority manifests are empty |
| | `[Actors]` | `Vessels` → `vessel.yaml` | Vessel builders, one per vessel type, reading `$(SIMULATION)/vessel.s3db` |
| | `[Rules]` | `COLREG`, `MASS`, `LocalRules`, `Competency`, `RiskAssessment` → `rules.colreg.yaml`, `rules.mass.yaml`, `$(SIMULATION)/rules.yaml`, `rules.examiner.yaml`, `rules.risk.yaml` | The 41 COLREG rules; site rules; examiners; the risk examiner. `rules.mass.yaml` is empty |
| Services | `[NetworkServices]` | `Local`, `API` → `network.yaml`, `api.yaml` | The RPC broker; the remote API services |

Two more registries are read by the classes they configure rather than by the boot loader:
`legata.yaml` (the resolvers, read by the COLREG evaluator) and `logger.yaml`.

**The folders under `config/`.**

| Folder | Holds |
|---|---|
| `map/<country>/<location>/` | `land.s3db`, `sea.s3db`, `sky.s3db`, and an optional background image — see [`MAPGEN.md`](../../tools/mapping/MAPGEN.md) |
| `simulation/<country>/<location>/` | `vessel.s3db`, `trip/*.csv`, `formation/*.csv`, the site's `rules.yaml` and `rule/` (Legata files and `score.json`), and `risk.yaml` |
| `weather/<country>/<location>/<WEATHER>/` | `environment.s3db` for each weather type, generated from `weather/profiles.yaml` — see [`WEATHERGEN.md`](../../tools/mapping/WEATHERGEN.md) |
| `maritime/regulation/colreg/` | `Rule1.legata` … `Rule41.legata`, the COLREG texts |
| `vehicle/ship/` | Ship models: container, ferry, fishing vessel, motorboat, simple |
| `examiner/` | `zones.yaml`: zone-local limits and penalties for the zone-aware examiners |
| `risk/` | The risk and capsize Bayesian networks (`.xdsl`) and their evidence bindings |
| `data/` | The results database: layout (`maritime.xml`, `maritime.sql`), dimension and fact definitions, and the working-set database each run writes to |

A location is usable when it has a folder under all three of `map/`, `simulation/` and `weather/`.
`ScenarioGenerator` lists locations from `simulation/` and refuses to generate a case whose map or
weather data is missing ([sweeps.md](sweeps.md)).

---

## `templates/cluster/` — one run's configuration

A copy of the configuration set with `$$COUNTRY$$`, `$$LOCATION$$`, `$$WEATHER$$` and `$$TRAFFIC$$`
tags in place of values. The sweep generator copies it once per case and fills in the tags, so each
simulule gets its own complete configuration folder. Keep it in step with `config/`: a manifest added
to `config/` and not to the template is missing from every sweep.

## `tests/` — the test suites

pytest suites that mirror `src/`: `tests/cos`, `tests/maritime`, `tests/rules`, and `tests/tools`.
Run them with `make test`, which runs pytest with coverage through poetry. Some tests start parts of a
simulation and write output to the current directory, so run them from a scratch folder when working
by hand.

## `tools/` — building data and checking rules

| Tool | Does |
|---|---|
| `mapping/MAPGEN.md`, `SHIPGEN.md`, `WEATHERGEN.md` | Guides for building a location's map, its vessels and trips, and its weather |
| `mapping/kml2map/` | Converts KML (for example from Google Earth) into map polygons, with offset, scale and zone options |
| `mapping/png2map/` | Converts a colour-coded PNG (green land, blue sea) into land and sea polygons |
| `dbtools/` | SQLite utilities: back up, restore and clear a database; load CSV into one; export CSV; copy a database to PostgreSQL |
| `colreg/regeval/` | Compiles every `.legata` file in a folder and reports the rules and terms it finds: a quick check of rule texts without running a simulation |

## `apps/` — the programs

`coslaunch`, `cviz`, `costopic` and `cosservice`, each a thin program over `src/` with its own man page.
What each does is in [communication.md](communication.md#talking-to-a-running-simulation).

## `idl/`, `samples/`, `papers/`, `docs/`, `build/`

| Folder | Holds |
|---|---|
| `idl/` | Interface contracts for the remote API, one per service (`World.idl`, `Vessel.idl`, `Topic.idl`, …) |
| `samples/simulation/` | `minsim`, a minimal simulation, and `openbridge`, a prototype OpenBridge conning display |
| `papers/` | `reference/` (the ER 2024 paper and background) and `IEEE-Access/` (current work, including `DEFINITIONS.md` for the risk formalism) |
| `docs/` | This guide; `taxonomies/` (jurisdiction, protocol, traffic and vessel classifications); `references/` (the consolidated COLREG text); the `mkdocs` site and its generated API pages |
| `build/` | Run output: `syslog.s3db` (the log) and `metrics.s3db` |
