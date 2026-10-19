# COLREG Rule 4 — Application (Section I: Conduct of Vessels in Any Condition of Visibility)

| | |
|---|---|
| Legata | `Rule4.legata` (rule text only; status NOT APPLICABLE) |
| Driver | `rules.colreg.rule4.Rule4` (`src/rules/colreg/rule4/Rule4.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule4` |
| Tests | none |
| Status | Not applicable. Application rule; nothing to judge. The invented zero-visibility clause was removed on 2026-10-19 (LEGATA.012) |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 4 says that Rules 4–10 apply in any visibility. It holds no duty of its own. The
simulation applies it by not gating Rules 5–10 on visibility: none of their clauses tests
visibility as a precondition.

`Rule4.legata` holds the rule text and no clause.

## Rule 4

> Rules in this Section apply in any condition of visibility.

**Legata.** None.

**Removed.** Until 2026-10-19 the file held `clause['COLREG.Rule4/ZeroVisibility']`, which was not
COLREG text: in zero visibility near another vessel, decelerate or steer to a safe zone. That
duty belongs to Rules 6 and 19(b) and (e), where reduced visibility is judged. The clause was
never fed, its condition (visibility 0) could not occur, and its terms did not resolve
(LEGATA.012).

## Open issues

- None.
