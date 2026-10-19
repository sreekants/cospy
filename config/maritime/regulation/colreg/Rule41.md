# COLREG Rule 41 — Verification of Compliance

| | |
|---|---|
| Legata | `Rule41.legata` (comments only) |
| Driver | `rules.colreg.rule41.Rule41` (`src/rules/colreg/rule41/Rule41.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule41` |
| Tests | none |
| Status | Not applicable. Periodic IMO audits of Contracting Parties |
| Reviewed | 2026-10-19 |

## How the rule is employed

Not represented in the simulation. Rule 41 concerns the IMO auditing States. It is not about
verifying the compliance of vessels.

COS verifies vessel compliance in its own way:
- COLREG rules and examiners record findings to the ledger;
- `ViolationInspector` writes them to the fact tables;
- coverage of each COLREG rule is tracked by level (`L0`–`L6`) outside the configuration.

None of this is Rule 41.

## (a)–(d)

> (a) Every Contracting Party shall be subject to periodic audits by the Organization in accordance with
> the audit standard to verify compliance with and implementation of the present Convention. (b) The
> Secretary-General of the Organization shall have responsibility for administering the Audit Scheme …
> (c) Every Contracting Party shall have responsibility for facilitating the conduct of the audit and
> implementation of a programme of actions to address the findings … (d) Audit of all Contracting Parties
> shall be: (i) based on an overall schedule developed by the Secretary-General …; and (ii) conducted at
> periodic intervals …

**Legata.** None.

## Open issues

- None.
