# COLREG Rule 24 — Towing and Pushing

| | |
|---|---|
| Legata | `Rule24.legata` |
| Driver | `rules.colreg.rule24.Rule24` (`src/rules/colreg/rule24/Rule24.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule24` |
| Terms | `OS.Type`, `OS.Operation`, `OS.Length`, `OS.Trait`, `OS.Signal.ON`; `apply` |
| Tests | none |
| Status | Not judged. Five clauses on operations the simulation does not have; not fed. Out of scope for REQ.056–059 (towing is a follow-up) |
| Reviewed | 2026-10-19 |

## How the rule is employed

Towing and pushing are not modelled. `Operation` has no towing, pushing, pushed or towed members,
and `Restriction.TOWING` exists but nothing sets it. No vessel tows another, and no tow length or
composite unit is represented. The clauses follow the same pattern as Rule 23 (lights as names in
`OS.Signal.ON`, see Rule 20) and are never fed.

## File-level condition

**Legata.** `OS.Operation in ['Vessel.Operation.TOWING', 'Vessel.Operation.PUSHING',
'Vessel.Operation.PUSHED']`.

**Caveats.** Not compiled (LEGATA.002). None of the three is an `Operation` member.

## (a) Power-driven vessel towing

> A power-driven vessel when towing shall exhibit: (i) instead of the light prescribed in Rule
> 23(a)(i) or (a)(ii), two masthead lights in a vertical line. When the length of the tow, measuring
> from the stern of the towing vessel to the after end of the tow exceeds 200 metres, three such lights
> in a vertical line; (ii) sidelights; (iii) a sternlight; (iv) a towing light in a vertical line above
> the sternlight; (v) when the length of the tow exceeds 200 metres, a diamond shape where it can best
> be seen.

**Legata.** `clause['COLREG.Rule24.a']`: power-driven. Assures `Light.Masthead.Forward.2x`,
`Light.Sidelight`, `Light.Sternlight` and `Light.TowingLight`, and a nested clause:
`OS.Length > meters(200)` → `Light.Diamond`.

**Caveats.**
- The 200 m test is on the vessel's length, not the length of the tow.
- The three masthead lights for a long tow are missing.
- A nested clause inside `assure:` is not known to compile.
- The diamond is a shape and applies by day, not with the lights.

## (b) Composite unit

> When a pushing vessel and a vessel being pushed ahead are rigidly connected in a composite unit they
> shall be regarded as a power-driven vessel and exhibit the lights prescribed in Rule 23.

**Legata.** `clause['COLREG.Rule24.b']`: power-driven and `PUSHED`, `apply 'COLREG.Rule23*'`.

## (c) Pushing ahead or towing alongside

> A power-driven vessel when pushing ahead or towing alongside, except in the case of a composite
> unit, shall exhibit: (i) instead of the light prescribed in Rule 23(a)(i) or (a)(ii), two masthead
> lights in a vertical line; (ii) sidelights; (iii) a sternlight.

**Legata.** `clause['COLREG.Rule24.c']`: power-driven and `PUSHING`, excluding `OS.Trait has
'Vessel.Trait.CompositeUnit'`. Assures the masthead lights, sidelights and sternlight.

**Caveats.** `OS.Trait` is not a term.

## (d) Also Rule 23(a)(ii)

> A power-driven vessel to which paragraph (a) or (c) of this Rule applies shall also comply with Rule
> 23(a)(ii).

**Legata.** `clause['COLREG.Rule24.d']`: power-driven, `apply 'COLREG.Rule23*'`.

**Caveats.** The clause applies all of Rule 23, not only (a)(ii), and to every power-driven
vessel the file-level condition admits.

## (e) Vessel or object being towed

> A vessel or object being towed, other than those mentioned in paragraph (g) of this Rule, shall
> exhibit: (i) sidelights; (ii) a sternlight; (iii) when the length of the tow exceeds 200 metres, a
> diamond shape where it can best be seen.

**Legata.** `clause['COLREG.Rule24.e']`: `OS.Operation has 'Vessel.Operation.TOWED'`. Assures
sidelights, a sternlight, and a nested diamond for length over 200 m.

## (f)–(i) Groups, submerged objects, impracticable cases

> (f) Provided that any number of vessels being towed alongside or pushed in a group shall be lighted as
> one vessel … (g) An inconspicuous, partly submerged vessel or object, or combination of such vessels or
> objects being towed, shall exhibit … (h) Where from any sufficient cause it is impracticable for a
> vessel or object being towed to exhibit the lights or shapes prescribed in paragraph (e) or (g) …
> (i) Where from any sufficient cause it is impracticable for a vessel not normally engaged in towing
> operations to display the lights prescribed in paragraph (a) or (c) …

**Legata.** None (TODOs).

## Open issues

- A towing model: who tows whom, tow length, composite units. Then `Operation` (or
  `Restriction`) members and terms for it. This is listed as a follow-up of REQ.056.
- Until then, Rule 24 stays not applicable.
