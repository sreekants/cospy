# Communication: talking to a running simulation

[← INDEX](INDEX.md) · [kernel](kernel.md) · tools: [coslaunch](../tools/coslaunch.md) · [cviz](../tools/cviz.md) · [costopic](../tools/costopic.md) · [cosservice](../tools/cosservice.md)

How programs outside a simulation watch and question it, and how the parts inside it pass
messages to each other.

The running example, *True North* in fog at Türkeli, is introduced in [one run, end to end](walkthrough.md#one-run-end-to-end).

---

## Talking to a running simulation

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

Each has a man page ([the index](INDEX.md)).

**Why it's built this way.** Watching should not change what is watched. The tools run as separate
programs, and `cviz` and `cosservice` only read, so a simulation behaves the same with or without a viewer
attached. `costopic pub` is the exception: it posts a message into the simulation, which is useful for
testing a rule by hand.

**In our example.** The run used `-port 6556`, so it could not clash with a simulation already running on
the default ports. `cviz.py host localhost:6556` would have shown *True North* moving through the lanes.

---

## The remote API: services and proxies

Every request a tool sends goes to an object in the tree. The objects that accept them are the
**remote services** in `src/cos/core/service`, loaded from `config/api.yaml` and registered at
`/Services/API/<Name>`: `MQ`, `ObjectManager`, `Service`, `Timer`, `Topic`, `Beacon`, `World`,
`Port`, `Radar`, `Sea` and `Vessel`. Each derives from `ORPCService`.

The tools do not build requests by hand. Each remote service has a **client proxy** of the same name
in `src/cos/core/api`, derived from `ORPCProxy`, with one method per remote method. A proxy works out
which object to call from its own class name (`/Services/API/<ClassName>`), and sends the call over
ZeroMQ to the RPC port. `cviz`, `costopic` and `cosservice` are built on these proxies.

The same names therefore exist twice, once on each side, and a third time where there is also a model
class (`World`, `Sea`, `Vessel`). This is deliberate. Import them with an alias, as the tools do:
`from cos.core.api.World import World as WorldService`.

The interface contracts behind the API are in `idl/`, one `.idl` file per service.

## Messages inside the process

Tools use the two ports; faculties inside the process use the kernel's **message queue** instead
([kernel.md](kernel.md#the-kernel)). A monitor posts `vessel.crossing` to the rule topics, and the
rules that care subscribe to it. `costopic` reads the same topics from outside, and `costopic pub`
writes to them.
