# COLREG Rule 39 — Definitions (Part F: Verification of Compliance)

| | |
|---|---|
| Legata | `Rule39.legata` (comments only) |
| Driver | `rules.colreg.rule39.Rule39` (`src/rules/colreg/rule39/Rule39.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule39` |
| Tests | none |
| Status | Not applicable. Defines terms of the IMO Member State Audit Scheme |
| Reviewed | 2026-10-19 |

## How the rule is employed

Part F concerns audits of Contracting Parties (States) by the IMO. It places no duty on vessels,
so the simulation defines none of these terms.

The simulation's own "audit" has a different meaning: the audit fields of its fact tables
(`AUDIT_FIELDS`: creation time, audit status, case id, tick) say where and when a record was made. They
are unrelated to Part F.

## (a)–(d)

> (a) Audit means a systematic, independent and documented process for obtaining audit evidence and
> evaluating it objectively to determine the extent to which audit criteria are fulfilled. (b) Audit
> Scheme means the IMO Member State Audit Scheme established by the Organization and taking into account
> the guidelines developed by the Organization. (c) Code for Implementation means the IMO Instruments
> Implementation Code (III Code) adopted by the Organization by resolution A.1070(28). (d) Audit Standard
> means the Code for Implementation.

**Legata.** None.

## Open issues

- None.
