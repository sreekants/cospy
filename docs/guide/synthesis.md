# Synthesis: timescales, comparisons and combinations

[← INDEX](INDEX.md) · [concepts](concepts.md) · [glossary](glossary.md)

The parts described on the other pages, seen together: the rates they run at, the same questions
asked of each, what they do in combination, and what changes from one site to another.

The running example, *True North* in fog at Türkeli, is introduced in [one run, end to end](walkthrough.md#one-run-end-to-end).

---

## Levels and timescales

COS acts at several rates, and they are not all measured in the same kind of time.

| Level | Rate | Clock | Decides |
|---|---|---|---|
| Step | A 30 ms sleep plus the motion work | Simulated clock: one tick is `SpeedUp × DeltaT` simulated seconds (default 1, REQ.032) | Vessel movement |
| Situation monitoring | Every 0.5 simulated seconds, on the latest tick | Simulated clock | Encounters and conduct events |
| Rule evaluation | Every `sample.frequency` simulated seconds, on the latest tick | Simulated clock | Violations and penalties |
| Weather update | Every `Sample.Rate` simulated seconds | Simulated clock | Rotation of the weather fields |
| Recording | Every 5 seconds | Wall clock | Rows written to disk |
| Run | `RunCycles` steps | Step count | When the simulation stops |
| Sweep | Hours to days | Cluster | Which conditions are compared |

**One consequence to know.** With `[ProcessManager] Affinity` set, vessels move on one thread and the
monitors and rules run on a second, each pass judging the latest tick and skipping the ticks that went
by during the previous pass. Motion never waits for the rules. So **the number of ticks the rules judge
during a voyage depends on how fast the computer is.** Every row records the `tick` it was judged on
and its time in simulated seconds, so rows from different machines line up on simulated time, but a
faster machine records more of them. The runner logs each pass's lag in ticks.

---

## The parts compared

The same questions, asked of every part.

| Part | Knows from | Holds | How you reach it | Keeps its data | Changes a result? |
|---|---|---|---|---|---|
| Kernel | `cos.ini` | Object tree, topics, clock | Object paths, topics | For the run | Only through timing |
| Environment | Map and weather databases | Shapes, fields, regions | `/World/...` | For the run | Yes: land, depth, zones, waves |
| Actors | Fleet database, trip files | Vessels and behaviours | `/World/Vehicle/Vessel` | For the run | Yes: every movement |
| Monitors | Vessel states | Situations | Topics, `fact_…` rows | Rows on disk | Yes: what the rules see |
| Rules | Legata files, scorecards | Clause results, penalties | `fact_concern`, examiner tables | Rows on disk | Yes: the score |
| Data manager | Faculties | Rows in memory | The run database | On disk, every 5 s | No |
| Tools | Ports 5556/5557 | Nothing | Command line | No | No |
| Sweep pipeline | Scenario variables | Folders, task file, merged database | Files | On disk | Decides which runs exist |

Two things the table makes visible. First, **only three parts decide a score**: the world, the vessels and
the rules. Everything else carries, records or displays. Second, **every part that decides a score reads
its knowledge from files.** That is hypothesis 3 of [the hypotheses](concepts.md#hypotheses-and-what-the-design-does-not-commit-to)
made concrete: to change what COS tests, you change data.

---

## Combinations that are not obvious

These are places where two mechanisms described separately above combine to do something neither does
alone.

1. **Situations are found, not scripted, so every encounter is tested.** Monitors label every pair of
   vessels on every pass, and rules check every labelled situation. A test that nobody thought to write
   still runs. ([the monitors](regulation.md#the-monitors-faculty--situations) + [the rules faculty](regulation.md#the-rules-faculty--legata-rules-and-examiners))
2. **A zone name is both geography and law.** `Turkeli.TSS.SpeedZone1` is a polygon in a map database and a
   word in a Legata clause. Redrawing the zone changes where the rule applies, without editing the rule.
   ([the environment faculty](world.md#the-environment-faculty--the-world) + [the rules faculty](regulation.md#the-rules-faculty--legata-rules-and-examiners))
3. **Resolvers let vague words grow precise over time.** "Safe distance" starts as a fixed number in a
   resolver and can later become a model, a lookup or a learned function, with no change to the rule
   text. ([the rules faculty](regulation.md#the-rules-faculty--legata-rules-and-examiners))
4. **Four scenario variables move the whole experiment.** Because every data path is built from
   `COUNTRY`, `LOCATION`, `WEATHER` and `TRAFFIC`, the sweep generator only has to write four lines per
   case. ([the life of a simulation](walkthrough.md#the-life-of-a-simulation) + [sweeps](sweeps.md))
5. **The case id makes a thousand databases one.** A hash of the scenario name is stored in every row, so
   merged results can be grouped back into their runs and compared by any variable.
   ([the life of a simulation](walkthrough.md#the-life-of-a-simulation) + [sweeps](sweeps.md))
6. **The vessel under test is just another vessel.** Because behaviours are plug-ins, an external
   navigation system is tested by putting it in the fleet file. Its penalties are then priced by the same
   scorecards as every other ship. ([the actors faculty](world.md#the-actors-faculty--the-vessels) + [the rules faculty](regulation.md#the-rules-faculty--legata-rules-and-examiners))
7. **A missing price is a finding.** A failed clause with no price is named in the run log
   (`Unpriced clause … failed`) rather than recorded. Collecting those lines across a sweep lists the
   clauses whose price still needs to be set.
   ([what COS cannot see](concepts.md#what-cos-cannot-see) + [the rules faculty](regulation.md#the-rules-faculty--legata-rules-and-examiners))

---

## One simulator, many waters

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
alone. That is the domain-agnostic design of [the hypotheses](concepts.md#hypotheses-and-what-the-design-does-not-commit-to) in
practice, and also its limit: a site is only as well tested as its local rules are written.
