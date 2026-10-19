# COLREG Rule 2 — Responsibility

| | |
|---|---|
| Legata | `Rule2.legata` (comments only) |
| Driver | `rules.colreg.rule2.Rule2` (`src/rules/colreg/rule2/Rule2.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule2` |
| Terms | none |
| Tests | none |
| Status | Not judged. No clause; the general duty is approximated by the examiners, as described below |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 2 is a general duty of good seamanship, plus a permission to depart from the Rules to avoid
immediate danger. Neither can be judged clause by clause: a breach of Rule 2 is always a breach
of something more specific. The simulation spreads the duty across its examiners, which judge
seamanship outside COLREG:

- `CollisionExaminer`, `GroundingExaminer` and `BerthingExaminer`: the consequences of neglect.
- `RiskExaminer`: the risk taken, assessed over time.
- `SpeedExaminer`, `LaneDisciplineExaminer`, `ExtremeWeatherExaminer`, `NightTimeExaminer` and
  the zone examiners: the precautions of ordinary practice in a zone.

## (a) No exoneration from neglect

> Nothing in these Rules shall exonerate any vessel, or the owner, master or crew thereof, from the
> consequences of any neglect to comply with these Rules or of the neglect of any precaution which
> may be required by the ordinary practice of seamen, or by the special circumstances of the case.

**Legata.** None. A TODO comment proposes including the practice files `practice.sailing`,
`practice.steering` and `practice.navigation`.

**Interpretation.** Every finding, from a COLREG rule or an examiner, is recorded against the
vessel and scored. Complying with one rule never offsets a finding under another.

**In the simulation.**
- Findings go to the ledger (`Ledger.post`). `ViolationInspector` writes them to the fact tables
  (`Ro`, `Rl`, `Rw`, the violation assessment).
- COLREG findings are priced by prefix in `examiner/zones.yaml` (`penalties: COLREG`).

**Caveats.**
- "Ordinary practice of seamen" is not a rule set. The three `practice.*.legata` files exist in
  this folder but are not included or loaded.
- The COLREG penalty is a flat placeholder (`COLREG: 50.0`, unsourced).

## (b) Due regard to dangers; departure to avoid immediate danger

> In construing and complying with these Rules due regard shall be had to all dangers of navigation
> and collision and to any special circumstances, including the limitations of the vessels involved,
> which may make a departure from these Rules necessary to avoid immediate danger.

**Legata.** None. A TODO comment proposes including the situation files `situation.visibility`,
`situation.traffic` and `situation.weather`.

**Interpretation.**
- *Departure* would excuse a breach of another rule when complying would have caused immediate
  danger.
- *Limitations of the vessels* are partly carried by vessel status: a vessel not under command or
  restricted keeps out of the way of no one (Rules 12 and 18 exclude it).

**In the simulation.** No finding is excused. The encounter classification
(`Encounter.EncounterStage`: no risk, risk of collision, close quarters, immediate danger)
exists, but no rule reads the stage to excuse a departure.

**Caveats.**
- A justified departure is still scored as a breach of the rule departed from.
- The three `situation.*.legata` files exist but are not included or loaded.
- Vessel limitations beyond status (draught, manoeuvrability) are not considered.

## Open issues

- Decide whether the `practice.*` and `situation.*` files become rule sets, and how a
  departure under (b) is recognised.
- A source for the COLREG penalty.
