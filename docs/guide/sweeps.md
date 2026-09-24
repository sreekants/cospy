# Sweeps: from one run to a thousand

[← INDEX](INDEX.md) · [walkthrough](walkthrough.md) · [synthesis](synthesis.md)

A single run proves little. This page covers how COS runs the same scenario many times with its
conditions changed, and how the results are brought together.

The running example, *True North* in fog at Türkeli, is introduced in [one run, end to end](walkthrough.md#one-run-end-to-end).

---

## From one run to a thousand

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
order, and a crash loses one case. The case id ([the life of a simulation](walkthrough.md#the-life-of-a-simulation)) travels with every row,
so results stay attributable after merging.

**In our example.** *True North* at Türkeli, in fog, at high density, is one of the 945 cases. Its
neighbours in the sweep are the same ship in clear weather, in a hurricane, or in light traffic. The
question the sweep answers is how its penalties change across them.
