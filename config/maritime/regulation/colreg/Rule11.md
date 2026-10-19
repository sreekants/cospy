# COLREG Rule 11 — Application (Section II: Conduct of Vessels in Sight of One Another)

| | |
|---|---|
| Legata | `Rule11.legata` |
| Driver | `rules.colreg.rule11.Rule11` (`src/rules/colreg/rule11/Rule11.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule11` |
| Terms | `(OS, TS).Visibility`, `(OS, TS).Visible`; API `add()`, `del()`; constant `Vessel.Visibility.VisibleRange` |
| Tests | none |
| Status | Application rule. The precedent is not fed. Rules 12–18 are judged without an in-sight test, except Rule 19(e), which leaves vessels in sight to Section II |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 11 limits Rules 12–18 to vessels in sight of one another. In the simulation:

- **Rules 12–15 and 18 do not test being in sight.** They judge every encounter at risk that
  their watch classifies, in any visibility.
- **Rule 19(e) applies only to pairs not in sight when the encounter begins**
  (`(OS, TS).InSightAtOnset is false`). In restricted visibility, a pair beyond the visibility
  is judged under Rule 19 *and* under Rules 12–18.
- **Being in sight is distance only:** `(OS, TS).Visible`, the distance within the scenario
  visibility (Rule 3(k)).

The precedent in `Rule11.legata` would keep a set of vessels in sight for Rule 6(a)(ii). It is
never fed.

## Rule 11

> Rules in this Section apply to vessels in sight of one another.

**Legata.** `precedent['COLREG.Rule11.VesselInSight']`:
- **condition:** `(OS, TS).Visibility in Vessel.Visibility.VisibleRange`;
- **assured:** `add(OS, 'COLREG.Vessels.Visible', TS)` and the reverse;
- **otherwise:** `del` both.

**Interpretation.** Each pair in sight is recorded in a per-vessel set that later rules can count
or test.

**Caveats.**
- Not fed, so never evaluated.
- `otherwise:` is never compiled (LEGATA.001), so the set would only grow.
- `add()` and `del()` ignore their arguments (LEGATA.001, related observations).
- The condition tests the scenario's visibility, not the distance between the two vessels:
  every pair would be "in sight" whenever visibility is within `(0, 10000)` nm.
- `TS` is used but not declared.
- Not judging the encounter rules for vessels out of sight double-judges a restricted-visibility
  encounter under Rules 12–18 and 19.

## Open issues

- Decide whether Rules 12–15 and 18 should apply only to vessels in sight, with
  `InSightAtOnset is true` as Rule 19 has it, so that Sections II and III do not overlap.
- Use `(OS, TS).Visible` in place of the precedent, or delete the precedent.
