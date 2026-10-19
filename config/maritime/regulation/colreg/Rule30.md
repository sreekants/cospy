# COLREG Rule 30 — Anchored Vessels and Vessels Aground

| | |
|---|---|
| Legata | `Rule30.legata` (status TODO; no clause) |
| Driver | `rules.colreg.rule30.Rule30` (`src/rules/colreg/rule30/Rule30.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule30` |
| Simulation | `Status.ANCHORED` (`Vessel.anchored()`), `Status.AGROUND` (`Vessel.aground()`, grounding conduct) |
| Tests | none |
| Status | Not judged. Text only. `VesselSignals` shows (a), (c) and (d) for container ships, ferries and fishing vessels. REQ.057 (REQ-057-05, open) adds the clauses |
| Reviewed | 2026-10-19 |

## How the rule is employed

**The states are set in a run**, unlike those of Rules 26–28:
- `ANCHORED`: by a trip's anchor action (`PlannedVesselBehavior.anchor()`) and by `AnchoredVessel`;
- `AGROUND`: by the grounding conduct on contact with the seabed (`maritime.conduct.grounding`),
  which also publishes `vessel.aground` (Rule 3's driver prints it).

**Lights and shapes** are names in the `signal` set (see Rule 20). REQ-056-01 adds
`Light.Anchor.Forward`, `Light.Anchor.Aft`, `Light.Deck`, `Shape.Ball.1x`, `Shape.Ball.3x` and
`Light.Allround.Red.2x`. `Light.Allround.White` already exists. `VesselSignals` raises them from
the status, also while the vessel is at anchor and does not move (REQ-059-05). `AnchoredVessel`
does not run it yet (REQ-059-04).

**At rest.** `anchor()` sets the behaviour's velocity to zero, so an anchored vessel is not making
way (Rules 26, 27, 35).

## File-level condition

**Legata.** `OS.State in ['Vessel.State.Anchored', 'Vessel.State.Aground']`.

**Caveats.** Not compiled (LEGATA.002). `OS.State` does not exist. REQ-056-03 decides on
`OS.Status in [Vessel.Status.ANCHORED, Vessel.Status.AGROUND]`.

## (a) At anchor

> A vessel at anchor shall exhibit where it can best be seen: (i) in the fore part, an all-round white
> light or one ball; (ii) at or near the stern and at a lower level than the light prescribed in
> sub-paragraph (i), an all-round white light.

**Legata.** None. REQ-057-05: `Light.Anchor.Forward` and `Light.Anchor.Aft` at night or in
restricted visibility, `Shape.Ball.1x` by day.

**In the simulation.** As planned. A vessel fishing at anchor shows the fishing signals instead
(Rule 26(a)); a restricted vessel the signals of Rule 27(b) only.

## (b) Under 50 m: one all-round white light

> A vessel of less than 50 metres in length may exhibit an all-round white light where it can best be
> seen instead of the lights prescribed in paragraph (a) of this Rule.

**Legata.** None. To be an alternative in (a)'s clause.

**In the simulation.** Not taken: every length shows both anchor lights.

## (c) Deck lights

> A vessel at anchor may, and a vessel of 100 metres and more in length shall, also use the available
> working or equivalent lights to illuminate her decks.

**Legata.** None. REQ-057-05: `Light.Deck` for vessels of 100 m or more.

**In the simulation.** `Light.Deck` only at 100 m or more; the "may" below 100 m is not taken.

## (d) Aground

> A vessel aground shall exhibit the lights prescribed in paragraph (a) or (b) of this Rule and in
> addition, where they can best be seen: (i) two all-round red lights in a vertical line; (ii) three
> balls in a vertical line.

**Legata.** None. REQ-057-05: the anchor lights plus `Light.Allround.Red.2x` at night,
`Shape.Ball.3x` by day.

**In the simulation.** As planned, with no deck lights. Aground outranks every other state.

**Caveats.** The grounding conduct sets `AGROUND` on contact and `UNDERWAY` once the vessel is
free. A vessel touching the seabed for one tick would owe the signals for that tick.

## (e) Under 7 m at anchor; (f) under 12 m aground

> (e) A vessel of less than 7 metres in length, when at anchor, not in or near a narrow channel, fairway
> or anchorage, or where other vessels normally navigate, shall not be required to exhibit the lights or
> shape prescribed in paragraphs (a) and (b) of this Rule. (f) A vessel of less than 12 metres in length,
> when aground, shall not be required to exhibit the lights or shapes prescribed in sub-paragraphs
> (d)(i) and (ii) of this Rule.

**Legata.** None. To be exclusions.

**In the simulation.** Neither exemption is taken: small vessels show the full signals.

**Caveats.** (e)'s "not in or near a narrow channel, fairway or anchorage" cannot be tested,
because the territory term is fixed at high sea (Rule 9).

## Open issues

- REQ-057-05: clauses for (a)–(f), and feed every vessel.
- REQ-059-01, -04: the other behaviours and `AnchoredVessel` show the signals.
- `MOORED` and `FASTENED` are never set; Rule 30 does not cover them anyway. `VesselSignals`
  shows nothing for them.
