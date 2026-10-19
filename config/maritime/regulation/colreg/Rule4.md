# COLREG Rule 4 — Application (Section I: Conduct of Vessels in Any Condition of Visibility)

| | |
|---|---|
| Legata | `Rule4.legata` |
| Driver | `rules.colreg.rule4.Rule4` (`src/rules/colreg/rule4/Rule4.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule4` |
| Terms | `OS.Visibility`, `(OS, TS).Distance`, `OS.Intent`, `OS.Velocity`; constants `Vessel.Collision.TimeToEncounter.AlertRange`, `Vessel.Velocity.ReducedSpeed` |
| Tests | none |
| Status | Not judged. Application rule; the clause in the file is an addition, not COLREG text, and is never fed |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 4 says that Rules 4–10 apply in any visibility. It holds no duty of its own. The
simulation applies it by not gating Rules 5–10 on visibility: none of their clauses tests
visibility as a precondition.

The driver feeds nothing, so `Rule4.legata` is never evaluated.

## Rule 4

> Rules in this Section apply in any condition of visibility.

**Legata.** The rule text itself has no clause. The file instead adds
`clause['COLREG.Rule4/ZeroVisibility']`, which is not COLREG text:
- **file-level condition:** `OS.Visibility <= 0`;
- **condition:** `(OS, TS).Distance < Vessel.Collision.TimeToEncounter.AlertRange`;
- **assured,** either of:
  - `OS.Intent has 'Manouever.CollisionAvoidance.Decelerate'` and
    `OS.Velocity <= Vessel.Velocity.ReducedSpeed`;
  - `OS.Intent has 'Manoeuverer.Course.SafeZone'`.

**Interpretation.** The added clause reads, in zero visibility, "slow down or steer to safety near
another vessel". That duty belongs to Rules 6 and 19, not Rule 4.

**Caveats.**
- Not fed, so never evaluated.
- The file-level condition is not compiled (LEGATA.002), so the clause would apply in any
  visibility once fed.
- `OS.Visibility` is not a vessel term: visibility is `(OS, TS).Visibility`.
- `TS` is used but not declared.
- `AlertRange` is a placeholder range `(0, 10)` compared with metres.
- `Vessel.Velocity.ReducedSpeed` is not declared in `definitions.s3db`.
- Container ships and ferries declare `Decelerate` (Rule 8(e)); no behaviour sets the safe-zone
  intent, and `'Manoeuverer.Course.SafeZone'` is misspelled.
- The two assurance lines are OR'd.

## Open issues

- Decide whether to move the zero-visibility clause to Rule 19 or delete it (COLREG.COVERAGE).
