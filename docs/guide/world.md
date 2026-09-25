# The world: environment and actors

[← INDEX](INDEX.md) · [kernel](kernel.md) · [regulation](regulation.md) · [MAPGEN](../../tools/mapping/MAPGEN.md) · [WEATHERGEN](../../tools/mapping/WEATHERGEN.md)

The two faculties that make the simulated world: the environment builds land, sea, sky and
weather from data files, and the actors create the vessels and move them. This is the first
stage of [the central problem](concepts.md#the-central-problem-rules-speak-of-situations-simulators-produce-states):
physics in, states out.

The running example, *True North* in fog at Türkeli, is introduced in [one run, end to end](walkthrough.md#one-run-end-to-end).

---

## The environment faculty — the world

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

## The actors faculty — the vessels

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
