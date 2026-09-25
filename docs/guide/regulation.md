# Regulation: situations, rules and examiners

[← INDEX](INDEX.md) · [world](world.md) · [kernel](kernel.md) · [extending](extending.md)

How states become judgements: monitors name situations, Legata rules check clauses against them,
resolvers supply the terms the rules use, and scorecards and examiners price the result.

The running example, *True North* in fog at Türkeli, is introduced in [one run, end to end](walkthrough.md#one-run-end-to-end).

---

## The monitors faculty — situations

**What it does.** Watches the vessels and names what is happening between them. This is the second stage
of [the central problem](concepts.md#the-central-problem-rules-speak-of-situations-simulators-produce-states): states in,
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
([levels and timescales](synthesis.md#levels-and-timescales)).

**Why it's built this way.** Separating "what is happening" from "is it allowed" means a crossing is
detected once, however many rules care about crossings.

**In our example.** In 58 seconds the monitors recorded 10 crossings, 112 head-on encounters,
5 give-way situations and 970 close-approach samples among the 34 vessels.

---

## The rules faculty — Legata, rules and examiners

**What it does.** Judges the situations: which clauses of which rules were kept or broken, and at what
cost. These are the last three stages of
[the central problem](concepts.md#the-central-problem-rules-speak-of-situations-simulators-produce-states).

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
2 seconds ([levels and timescales](synthesis.md#levels-and-timescales)).

**Why it's built this way.** The law changes, and it differs between places. Keeping rules as text, their
vocabulary in resolvers and their prices in scorecards means a lawyer can read a rule, a programmer can
add a term, and an analyst can change a price, each without touching the others' work.

**In our example.** `WaterwayRule` loaded `turkeli.legata` for zones named `Turkeli*`, checked every
vessel in them each time it ran, and priced *True North*'s broken DeepDraft clause from `score.json`:
30 rows, 1,000,000 each.

---

## How the evaluator drives monitors, rules and examiners

The COLREG evaluator (`maritime.regulation.colreg.Evaluator`) is the one service that calls the
faculties on this page. On each of its ticks it builds a fresh rule context, which holds the
resolver, the world, the vessels and the API, and makes two kinds of pass:

| Pass | Timer | Calls | In order |
|---|---|---|---|
| `monitor()` | 0.5 s | every monitor under `/Faculty/Situation/…` | incident hooks, maritime situations and conduct, processor hooks |
| `evaluate()` | the evaluator's `sample.frequency` | every faculty under `/Faculty/Regulation/…`, both rules and examiners | `begin` on all, then `evaluate` on all, then `end` on all |

Examiners are therefore not a separate stage: they sit next to the rules in the object tree
(`/Faculty/Regulation/Examiner/…`) and run in the same pass, each deciding for itself, through its
own timer and preconditions, whether it has anything to score.

## How a term is resolved

A Legata clause refers to terms such as `(OwnShip,TargetShip).DCPA` or `OS.Draft`. When an
automaton needs one, the rule context asks the evaluator's `CompositeResolver`. It picks a resolver
from `config/legata.yaml` by the term's prefix and property name. The resolver reads the **current
situation** in the rule context: the own ship, the target ship, the fleet and the zone that a monitor
or rule has put there. It computes the value from the live objects under `/World`.

Two consequences follow. A term is only as good as its resolver, so a resolver that returns a fixed
value makes every rule that uses it see that value ([what COS cannot see](concepts.md#what-cos-cannot-see)).
And the situation is shared: whatever set it last decides what the next term is about. That makes the
order of monitors, rules and examiners part of the meaning of a result.

Adding a resolver, a rule or an examiner is described in [extending.md](extending.md).
