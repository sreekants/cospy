# Extending COS

[← INDEX](INDEX.md) · [kernel](kernel.md) · [regulation](regulation.md) · [layers](layers.md) · [support](support.md)

How to add the things COS is built to have more of: examiners, rules, resolvers, vessel behaviours and
locations. Read the first section before any of the recipes; it is the rule that makes the others work.

---

## The one rule: nothing runs until a manifest names it

COS never discovers code. A class runs only if a YAML **manifest** lists it and `cos.ini` names that
manifest ([support.md](support.md#config--the-simulation-is-data) has the full map). Writing a class and
not listing it is the most common reason new code "does nothing", and there is no error to say so.

A manifest entry looks like this:

```yaml
packages:
  modules:
     - name: Grounding                                         # a label for the log
       module: rules.examiner.navigation.GroundingExaminer     # package path + class name
       config: zones=$(CONFIG)/examiner/zones.yaml             # space-separated key=value
```

- **The class name must equal the file name.** The boot loader imports the module path and takes its
  last part as the class name, so `GroundingExaminer` must live in `GroundingExaminer.py`.
- **Faculties** (rules, examiners, monitors) read `config:` as an argument list in `setup()`.
  **Builders** read `args:` in their constructor and `database:` for the file to build from.
- `$(NAME)` variables from `cos.ini` are expanded in `config:`, `args:` and `database:`.
- A load failure is logged as `Failed to load [<module>]: <reason>` and the run continues without that
  module. Search the log for it after adding anything.

Check each change with a short headless run before a sweep ([check your change](#check-your-change)).

---

## Add an examiner

An examiner scores one concern (grounding, speed, weather, …) against every vessel it applies to. It is
driven by the COLREG evaluator, in the same pass as the rules
([regulation.md](regulation.md#how-the-evaluator-drives-monitors-rules-and-examiners)).

1. **Write the class** in `src/rules/examiner/<concern>/<Name>Examiner.py`. Zone-aware examiners mix in
   `ZoneAware`, which supplies the map shapes under a vessel, zone-local limits, a precondition, and a
   priced record of each violation:

   ```python
   from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
   from maritime.model.zone.ZoneAwareness import ZoneAware

   class WakeExaminer(ZoneAware, NavigationExaminer):
       def __init__(self):
           NavigationExaminer.__init__(self)          # registers under /Faculty/Regulation/Examiner/Navigation

       def setup(self, ctxt, config):
           self.init_zones(ctxt, config, requires=['os'])   # needs an own ship in the situation

       def on_start(self, ctxt, config):
           self.cache_shapes(ctxt)                    # the map exists once the world is built

       def evaluate(self, ctxt, rule_ctxt):
           if self.applicable(rule_ctxt) == False:
               return
           vessel = rule_ctxt.situation.os
           shapes, rules, depth = self.survey(vessel)
           # ... decide whether the vessel breaks the concern, then:
           # self.violate(ctxt, vessel, 'wake.speed', zone_name, value=measured)
   ```

2. **Price the event.** `violate()` writes a row to the shared `fact_Concern` table and takes the penalty
   for the event name from the `penalties:` section of `config/examiner/zones.yaml`. Add
   `wake.speed: <penalty>` there, and any zone-local thresholds the examiner reads.
3. **List it** in `config/rules.examiner.yaml`, and in `templates/cluster/config/rules.examiner.yaml` so
   sweeps load it too.

`GroundingExaminer` is a complete, short example to copy. An examiner that needs its own table follows
[add a fact table](#add-a-fact-table) instead of using `violate()`.

## Add a fact table

Results reach disk only through tables the data manager knows. At startup it creates one partition per
table declared in `config/data/maritime.xml`, and copies the template database
`config/data/maritime.s3db` to the working set if the working set does not exist. A push to an
undeclared table is logged as `No such topic` and dropped.

1. Declare the table and its fields in `config/data/maritime.xml`, next to a similar `fact_…` table.
2. Add its `CREATE TABLE` to `config/data/maritime.sql`, and apply it to the template `maritime.s3db`.
3. Add it to `config/data/facts.csv` and `cube.csv`, which list the facts and dimensions for analysis.
4. Delete `config/data/maritime.workingset.s3db` so the next run copies the updated template.
5. Write rows with `ctxt.sim.data.push('fact_<name>', (case_id, time, …))`, in the declared field order.

## Add a local rule

Local rules are site law: they apply to every vessel inside the site's named zones. They need no Python.

1. **Write the Legata file** in `config/simulation/<country>/<location>/rule/<name>.legata`. Each clause
   has a `condition` (when it applies) and `assure` lines (what must then be true). Clause names should be
   unique across the site:

   ```
   clause['Turkeli.SpeedZone.Slow']:{
       : {
           condition: { : (OS,TrafficSeparationScheme).Name is 'Turkeli.TSS.SpeedZone1' }
           assure:    { : OS.Velocity < 0.01 }
       }
   }
   ```

   Use only terms a resolver provides. The own-ship terms in use today include `OS.Velocity`,
   `OS.Draft`, `OS.Cargo` and `OS.Weight`; zone terms take the form `(OS,<ZoneType>).Name`.

2. **Price it** in the site's `rule/score.json`: each clause gets a price, a concern and, optionally, the
   vessels it applies to. An unpriced clause is recorded as `Generic` with a penalty of 0.
3. **List it** in the site's `rules.yaml`. Local rules reuse the zone rule classes; only the configuration
   differs:

   ```yaml
   - name: Istanbul.Turkeli.Zone
     module: maritime.regulation.internal.WaterwayRule
     config: sample.frequency=1 automata=$(SIMULATION)/rule/turkeli.legata scorecard=$(SIMULATION)/rule/score.json zonekey=Turkeli*
   ```

   `zonekey=` selects the sea zones, by name pattern, whose vessels the rule checks. Use
   `InshoreTrafficRule`, `HarbourRule`, `TrafficLaneRule` or `TrafficSeparationSchemeRule` for the other
   zone types.
4. **Check the text** with `tools/colreg/regeval` before running: it compiles every `.legata` file in a
   folder and lists the terms each uses. A term no resolver knows is the usual reason a clause never fails.

## Make a COLREG rule check situations

A COLREG rule class loads its Legata text, but evaluates only the situations handed to it. To make one
act on encounters, subscribe to the monitors' events in `on_start` and queue a situation for each:

```python
from cos.model.rule.Situation import Situation

def on_start(self, ctxt, config):
    COLREG.on_start(self, ctxt, config)
    self.subscribe("vessel.crossing", self.on_crossing)

def on_crossing(self, ctxt, evt):
    self.add_situation(Situation(evt[1], evt[2]))    # own ship, target ship
```

The rule's next evaluation walks its automaton once for every queued situation. `Rule13` is the working
example. The event names the monitors post are in [regulation.md](regulation.md#the-monitors-faculty--situations).

## Add a resolver

A resolver gives Legata a new family of terms, such as `(OwnShip,Map.Land).Distance`.

1. **Write the class**, with the term prefix in the constructor, the current situation captured in
   `reset()`, and one `@simproperty` method per term:

   ```python
   from cos.model.resolver.Resolver import Resolver, simproperty

   class BuoyResolver(Resolver):
       def __init__(self, resolver):
           Resolver.__init__(self, '(OwnShip,Map.Buoy).')
           self.os = None

       def reset(self, ctxt, rulectxt):
           situation = rulectxt.situation
           self.os = situation.os if situation is not None else None

       @simproperty
       def Distance(self):
           if self.os is None:
               return None        # unresolved: the clause cannot be decided
           ...
   ```

2. **Register it** in `config/legata.yaml` (and the template copy):

   ```yaml
   - scope: 'buoy'
     prefix: null
     module: maritime.model.resolver.BuoyResolver
     config:
   ```

Return `None` for a term that cannot be computed rather than a default value. A default makes every
rule that uses the term see the same answer, which is one of the gaps listed in
[what COS cannot see](concepts.md#what-cos-cannot-see). `LandResolver` is a short example.

## Add a vessel behaviour

A behaviour is a plug-in class named in a vessel's `behavior` column in `vessel.s3db`. The column holds
space-separated slots:

| Slot | Updated every step | Use |
|---|---|---|
| `motion=` | yes | how the vessel moves |
| `dynamics=` | yes | the physics model |
| `control.colav=` | yes | collision avoidance |
| `sensor=`, `control.motion=`, `control.dynamics=`, `control.sensor=` | no | created and initialised only |

Each class is constructed as `C(ctxt, config)` and then given `intialize(ctxt, actor, vehicle, config)`.
A motion behaviour extends `cos.behavior.motion.MotionBehavior`, or `PathFollowingMotionBehavior` /
`PlannedVesselBehavior` to reuse trip following, and implements `move(world, t, config)`, returning the
new bounding rectangle and velocity. The world's collision check rejects moves onto land or out of the
vessel range, so a behaviour does not need to test for them.

To put the vessel under test into a scenario, wrap its navigation system as a motion behaviour and give
it a row in the site's `vessel.s3db`. Nothing else in COS changes.

## Add a location

A location is data, not code. Follow [`MAPGEN.md`](../../tools/mapping/MAPGEN.md) for the land and sea
maps and the vessels, [`SHIPGEN.md`](../../tools/mapping/SHIPGEN.md) for traffic and trips, and
[`WEATHERGEN.md`](../../tools/mapping/WEATHERGEN.md) for the weather databases. Optionally add local rules
as above. The sweep generator picks the location up once it has folders under `config/map/`,
`config/simulation/` and `config/weather/`.

---

## Check your change

1. **Run the tests.** `make test`, or `pytest` on the suite that mirrors the package you changed.
2. **Run a short simulation.** Copy `config/cos.ini` to a scratch folder, set `RunCycles=1500` (about
   a minute), point `LogFile`, `MetricsFile` and the data manager's `storage=` at scratch copies, and start
   it on its own ports so it cannot clash with a simulation already running:

   ```bash
   cd apps/coslaunch
   python coslaunch.py -config <scratch>/cos.ini -port 6556
   ```

3. **Read the log.** Look for `Failed to load`, `Runtime error` and `No such topic`. Then query the scratch
   database for the rows you expected.
4. **Only then sweep.** A defect that costs one line in one run costs a thousand runs in a sweep.
