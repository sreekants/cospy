# RiskExaminer

## Synopsis

Wraps the ASV risk network of Kristensen et al. (2025) as a COS examiner, scoring the probability of each hazardous event and the expected economic loss it implies. It always scores and always records; publishing is advisory, and a vessel model may subscribe to the assessment or ignore it entirely.

## Operation

At startup the examiner loads a Bayesian network from `config/risk/risk.model.xdsl` and its bindings from `risk.model.yaml`, where evidence terms are organised into five named groups — `collision`, `target`, `environment`, `at_sea` and `auv_operation`. On each evaluation it walks the groups, and for each one asks `resolvable()` whether the current situation carries the attributes that group's terms require: a term such as `(OwnShip,TargetShip).DCPA` is a fact about an encounter, not about the world, so asking for it with no target ship in scope is a category error rather than a missing observation. Groups whose precondition fails are skipped whole, so an unresolved term always means "applicable but unobserved" and the corresponding node simply keeps its prior. Surviving terms are resolved, discretized into network states and set as evidence; inference then yields the three hazard marginals, their exact joint, and the expected loss per cross-cutting concern from the Table A.5 cost values. Each assessment is charged against a per-vessel `VoyageTrack` that weights the increment by the probability of having reached that point intact and charges only once per distinct risk picture, then published on `/Faculty/Risk/Assessment` and written unconditionally to `fact_Rb`.

## Features

- Group-gated bindings make each family of evidence declare the situation it depends on, separating inapplicable terms from unobserved ones.
- Hazard probabilities are combined with the exact joint from the network, never by summing the marginals as eq. (14) of the source paper does.
- Expected losses are summed across consequence nodes, which is valid unconditionally and correct physically — one collision can damage both vessels and harm a person.
- Cumulative voyage cost is survival-weighted, so an exposure later in a voyage is only charged if the vessel got there.
- Charges once per distinct evidence configuration, so a ten-minute encounter sampled at 1 Hz is not counted six hundred times.
- Recording is unconditional and publishing advisory, which gives a natural controlled experiment: the same scenario with a vessel subscribing and not subscribing is comparable on cumulative cost.
- The eq. (14) sum is still recorded alongside the exact joint, so the divergence between them is queryable across a whole sweep.
- `Rl` is written as a single MATLAB matrix literal, `[a, b; c, d];`, rows being spatial zones and columns concerns. The fact schema is therefore fixed: a territory that adds a concern or a zone changes the shape of the literal and nothing else — no column to add, no warehouse schema to regenerate.
- Every valuation is USD, declared once in `RiskModel.CURRENCY` rather than stored per row, so two territories cannot disagree about what a stored number means.

## Known limitations

These are live defects, not design trade-offs.

- **Four of the five binding groups never fire.** `resolvable()` misspells `environment` as `enviroment`; the `at_sea` branch returns `False` before its real test, leaving the code below unreachable; `target` matches no branch at all; and `auv_operation` requires `situation.fleet`, which nothing in the tree ever assigns. Only `collision` can contribute evidence.
- **The situation is not owned by this examiner.** `RuleContext` is constructed with an empty `Situation`, and only `COLREG.__evaluate_rule` populates it — mutating the shared context in a loop and never restoring it. Since `rules.risk.yaml` loads after `rules.colreg.yaml`, this examiner inherits whichever encounter the last COLREG rule left behind.
- **The per-vessel loop does not vary the evidence.** `observe()` takes a vessel and ignores it, resolving against the shared situation, so N vessels each accumulate the same exposure.
- ~~`risk.model.yaml` binds `auv_asv_depth`, which is not a node in the network.~~ Removed 2026-09-26 (COS.006); folding AUV depth into the link distance is REQ.034. A binding to an absent node is dropped at load, and `test_Bindings` holds the shipped bindings to the network.
- No resolver is registered for any `Map.*` or `Fleet` prefix in `config/legata.yaml`, so those terms cannot resolve even once the gating is fixed.
- The class comment still describes registration under `/Faculty/Situation/Processors` and being driven by `Evaluator.monitor()`; it is now a `Regulation/Examiner` driven by `Evaluator.evaluate()`.
- Conditional probability tables are placeholders apart from the four static priors of Table A.6.
- A serialized `Rl` carries no axis labels in the row. The zone and concern order is logged once at startup by `__load_matrix`, and editing that order part way through a sweep makes earlier matrices undecodable.
- `Rl` is no longer sliceable in SQL. A query that wants loss by concern across a sweep must deserialize every row in application code; only the `RiskAssessment` rollup stays dimensional.
