# Glossary

[← INDEX](INDEX.md)

Every term used across the guide. Each is also defined where it first appears.

---

## Terms

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
