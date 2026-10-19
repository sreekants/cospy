# COLREG Rule 1 — Application

| | |
|---|---|
| Legata | `Rule1.legata` |
| Driver | `rules.colreg.rule1.Rule1` (`src/rules/colreg/rule1/Rule1.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule1` |
| Terms | `VesselResolver` (`Position.Territory`, `Mode`); API `set()` |
| Tests | none |
| Status | Not judged. (a) is written as a precedent that is never fed; (b)–(e) are application clauses carried by the simulation's configuration |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 1 says where the Rules apply and what may override them. It holds no duty a vessel can
breach, so it is not judged. The simulation applies it in two ways:

- **COLREG applies everywhere on the map.** Every loaded COLREG rule judges every vessel it is
  fed, wherever the vessel is. Nothing restricts the rule set by territory.
- **Local rules sit beside COLREG.** Special rules made by a harbour, strait or coastal authority
  ((b)–(e)) are written as separate rule sets: `InlandWaterRule` drivers with site-specific
  clauses and the zone rules in `examiner/zones.yaml`. They run alongside the COLREG set and do
  not replace any of its rules.

The driver feeds nothing, so the precedent in `Rule1.legata` is never evaluated.

## (a) Where the Rules apply

> These Rules shall apply to all vessels upon the high seas and in all waters connected therewith
> navigable by seagoing vessels.

**Legata.** `precedent['COLREG.Rule1.a']`:
- **condition:** `OS.Position.Territory in ['Territory.HighSea', 'Territory.Navigable']`;
- **assured:** `set(OS.Mode, 'COLREG', true)`, then `abort`.

**Interpretation.** The precedent marks a vessel as subject to COLREG when it is on the high seas
or in connected navigable waters. Other rules could then test that mark (Rule 7 tests
`OS.COLREG.Mode is true`).

**In the simulation.**
- `OS.Position.Territory` always resolves to `'Territory.HighSea'` (`VesselResolver`), so the
  condition would hold for every vessel.
- In practice the rule set applies to every vessel because it is loaded, not because of this
  mark.

**Caveats.**
- The precedent is never evaluated: `Rule1.py` feeds no situations.
- `set()` ignores its arguments: it stores the first symbol in `vessel.mode` and drops the name
  and value (see LEGATA.001, related observations). The mark could not be read back.
- `OS.Mode` resolves to `vessel.intent`, not `vessel.mode`.
- `Position.Territory` is fixed at high sea, so territory cannot distinguish the high seas from
  inland waters.

## (b) Special rules of local authorities

> Nothing in these Rules shall interfere with the operation of special rules made by an appropriate
> authority for roadsteads, harbours, rivers, lakes or inland waterways connected with the high seas
> and navigable by seagoing vessels. Such special rules shall conform as closely as possible to these
> Rules.

**Legata.** None. A comment says local authorities implement their rules as separate Legata
files.

**In the simulation.**
- Local rules are site rule sets (`InlandWaterRule` drivers and their generated clauses) and the
  per-zone settings in `examiner/zones.yaml`: speed limits, overtaking bans, cargo restrictions.
  Zone examiners such as `SpeedExaminer` and `LaneDisciplineExaminer` judge them.
- Both COLREG and the local rules judge the same vessel. Neither one suspends the other.

**Caveats.**
- There is no precedence between local rules and COLREG. Where a local rule conflicts with a
  COLREG rule, both can record a finding.
- Whether a local rule "conforms as closely as possible" to COLREG is not checked.

## (c) Additional lights and signals for warships, convoys and fishing fleets

> Nothing in these Rules shall interfere with the operation of any special rules made by the
> Government of any State with respect to additional station or signal lights, shapes or whistle
> signals for ships of war and vessels proceeding under convoy, or with respect to additional station
> or signal lights or shapes for fishing vessels engaged in fishing as a fleet. These additional
> station or signal lights, shapes or whistle signals shall, so far as possible, be such that they
> cannot be mistaken for any light, shapes or signal authorized elsewhere under these Rules.

**Legata.** None.

**In the simulation.** Any additional light, shape or sound signal must be a name in the signal
vocabulary, `maritime/signals.yaml`. A rule that names a signal outside that vocabulary is
refused at setup (`COLREG.check_signals()`). A scenario can add State-specific signals there.

**Caveats.**
- No State-specific signals are defined.
- Whether an additional signal "cannot be mistaken" for a COLREG signal is not checked.
- Naval fleets exist (`NavalFleet` behaviour, `Operation.MILITARY`), but no rule or signal treats
  them differently.

## (d) Traffic separation schemes

> Traffic separation schemes may be adopted by the Organization for the purpose of these Rules.

**Legata.** None.

**In the simulation.**
- Traffic separation schemes are map shapes (`TrafficSeparationScheme` in the sea layer). Vessel
  behaviours steer with them (`VesselManeuvers.tss_compliance`, `tss_avoidance`).
- Rule 10 holds the duties inside a scheme.

**Caveats.** Whether a scheme in a map is IMO-adopted is not recorded.

## (e) Vessels of special construction or purpose

> Whenever the Government concerned shall have determined that a vessel of special construction or
> purpose cannot comply fully with the provisions of any of these Rules with respect to the number,
> position, range or arc of visibility of lights or shapes, as well as to the disposition and
> characteristics of sound-signalling appliances, such vessel shall comply with such other provisions
> … as her Government shall have determined to be the closest possible compliance with these Rules in
> respect to that vessel.

**Legata.** None.

**In the simulation.** Not modelled. Lights and shapes are names in the signal vocabulary, with
no position, range or arc of visibility, so there is nothing to vary per vessel.

**Caveats.** An exemption per vessel cannot be declared.

## Open issues

- A territory term that tells the high seas from inland waters, if Rule 1(a) or local rules
  need it.
- Precedence between local rules and COLREG, (b).
- `set()`, `add()` and `del()` ignoring their arguments (LEGATA.001, related observations).
- Whether to remove the unfed precedent, or feed it once something reads the mark.
