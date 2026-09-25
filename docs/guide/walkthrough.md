# Walkthrough: one run, end to end

[← INDEX](INDEX.md) · [concepts](concepts.md) · [kernel](kernel.md) · [glossary](glossary.md)

One COS process on one figure, then one real run followed from a configuration file to a penalty
in a database, then the life cycle every run goes through.

---

## The overview figure

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
  │   │ land · sea   │─>│  vessels   │─>│  situations  │─>│ Legata   │   │
  │   │ sky · weather│  │  behaviour │  │  conduct     │  │ examiners│   │
  │   └──────────────┘  └────────────┘  └──────────────┘  └────┬─────┘   │
  │            (b) topics on the internal message queue        │         │
  │                                                            │ (d)     │
  │   SUBSYSTEMS   World · NetworkManager · DataManager <──────┘         │
  └──────────────────┬──────────────────────────────────────┬────────────┘
                     │ (c) RPC :5556 · events :5557         │ (d) every 5 s
                     ▼                                      ▼
          cviz · costopic · cosservice              workingset .s3db
                                                            │ (e) after the sweep
                                                            ▼
                                              merged database → analysis
```

*Figure 1. One COS process, and the five kinds of connection narrated below.*

There are five kinds of connection in that figure, and each one is explained on another page:

- **(a) Timer calls.** The kernel's runner calls every service once per step.
  [the life of a simulation](#the-life-of-a-simulation), [the kernel](kernel.md#the-kernel).
- **(b) Internal messages.** Faculties post events such as "vessel.crossing" to named topics, and other
  faculties read them. [the kernel](kernel.md#the-kernel), [the monitors](regulation.md#the-monitors-faculty--situations).
- **(c) Outside connections.** Tools send requests to a running simulation on port 5556 and receive its
  event stream on port 5557. [talking to a running simulation](communication.md#talking-to-a-running-simulation).
- **(d) Recording.** Faculties hand results to the data manager, which writes them to a database file
  every 5 seconds. [the kernel subsystems](kernel.md#the-kernel-subsystems).
- **(e) Merging.** After a sweep, the databases of many runs are merged into one for analysis.
  [sweeps](sweeps.md).

The source tree behind the figure, package by package, is drawn on one page in
[`cos-structure.html`](cos-structure.html) and described in [layers.md](layers.md).

**Reading on.** The next two sections follow one real run through the whole figure, then
cover how a simulation starts and stops. The boxes are opened one page at a time, from the
world up to the rules: [kernel.md](kernel.md), [world.md](world.md),
[regulation.md](regulation.md) and [communication.md](communication.md).
[sweeps.md](sweeps.md) scales one run to many, and [synthesis.md](synthesis.md) pulls the
parts together.

---

## One run, end to end

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
   faculties, then the network services, each from its own YAML file ([the life of a simulation](#the-life-of-a-simulation)).
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
across many runs ([sweeps](sweeps.md)).

---

## The life of a simulation

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
