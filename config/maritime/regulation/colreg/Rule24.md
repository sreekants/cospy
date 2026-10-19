# COLREG Rule 24 — Towing and Pushing

| | |
|---|---|
| Legata | `Rule24.legata` |
| Driver | `rules.colreg.rule24.Rule24` (`src/rules/colreg/rule24/Rule24.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule24` |
| Terms | `OS.Type`, `OS.Operation`, `OS.Length`, `OS.TowLength`, `OS.Signal.ON`, `(OS, TS).Night`, `(OS, TS).Visibility` |
| Tests | `tests/maritime/model/colreg/test_Rule24.py` (6) |
| Status | Not judged in a run: eight clauses, not fed. Towing and pushing are trip-row operations (2026-10-19), so (a), (c) and (d) apply to them; (b) composite units and (e) towed vessels are not modelled |
| Reviewed | 2026-10-19 |

## How the rule is employed

**Towing and pushing are trip-row operations** (Rule 3). The action `towing(tow length)` sets
`Operation.TOWING` and the tow length, `pushing` sets `Operation.PUSHING`, each until the next
waypoint. `OS.TowLength` is the tow length in metres, 0 when not towing. The tow itself is not a
vessel: nothing is towed or pushed, so (b) composite units and (e) towed vessels have no vessel to
judge. The clauses follow the same pattern as Rule 23 (lights as names in `OS.Signal.ON`, see
Rule 20) and are never fed.

**Shared by every clause.**
- Each clause tests the operation it is about. (a), (c) and (d) test `Vessel.Operation.TOWING` or
  `PUSHING`. (b) and (e) still test quoted `PUSHED` and `TOWED` strings, which match no member,
  so they apply to no vessel (LEGATA.003). Until 2026-10-19, (a) and (d) tested only
  "power-driven", so fed, they would have demanded towing lights of every power-driven vessel.
- Lights are judged in the Rule 20 window (night or restricted visibility), shapes by day
  (LEGATA.008).
- The diamond is `Shape.Diamond` (it was `Light.Diamond`).
- A nested clause inside `assure:` passed without being evaluated. The compiler now refuses one,
  so the diamond paragraphs are clauses of their own.

## File-level condition

**Legata.** `OS.Operation in [Vessel.Operation.TOWING, Vessel.Operation.PUSHING]`.

**Caveats.** Not compiled (LEGATA.002). Each clause repeats its operation test.

## (a) Power-driven vessel towing

> A power-driven vessel when towing shall exhibit: (i) instead of the light prescribed in Rule
> 23(a)(i) or (a)(ii), two masthead lights in a vertical line. When the length of the tow, measuring
> from the stern of the towing vessel to the after end of the tow exceeds 200 metres, three such lights
> in a vertical line; (ii) sidelights; (iii) a sternlight; (iv) a towing light in a vertical line above
> the sternlight; (v) when the length of the tow exceeds 200 metres, a diamond shape where it can best
> be seen.

**Legata.**
- `clause['COLREG.Rule24.a']`: power-driven and towing, in the Rule 20 window. Assures
  `Light.Sidelight`, `Light.Sternlight` and `Light.TowingLight`.
- `clause['COLREG.Rule24.a.i']`: the same, with `OS.TowLength <= 200`. Assures
  `Light.Masthead.Forward.2x`.
- `clause['COLREG.Rule24.a.i/LongTow']`: the same, with `OS.TowLength > 200`. Assures
  `Light.Masthead.Forward.3x`.
- `clause['COLREG.Rule24.a.v']`: power-driven and towing, by day, `OS.TowLength > 200`. Assures
  `Shape.Diamond`.

**Interpretation.** By day in restricted visibility a long tow owes both the lights and the
diamond (Rule 20(c), (d)).

**Caveats.** `VesselSignals` has no towing row, so a towing vessel shows the power-driven lights
and would breach (a) once fed.

## (b) Composite unit

> When a pushing vessel and a vessel being pushed ahead are rigidly connected in a composite unit they
> shall be regarded as a power-driven vessel and exhibit the lights prescribed in Rule 23.

**Legata.** `clause['COLREG.Rule24.b']`: power-driven and `PUSHED`, in the Rule 20 window.
Assures the Rule 23(a) lights directly: `Light.Masthead.Forward.1x`, `Light.Sidelight` and
`Light.Sternlight`. It used `apply 'COLREG.Rule23*'` until 2026-10-19, which did nothing and would
have applied every Rule 23 clause, the small-craft ones too (LEGATA.064).

**Caveats.** The condition should be a rigidly connected composite unit, not a pushed vessel.
`OS.Trait` is not a term.

## (c) Pushing ahead or towing alongside

> A power-driven vessel when pushing ahead or towing alongside, except in the case of a composite
> unit, shall exhibit: (i) instead of the light prescribed in Rule 23(a)(i) or (a)(ii), two masthead
> lights in a vertical line; (ii) sidelights; (iii) a sternlight.

**Legata.** `clause['COLREG.Rule24.c']`: power-driven and `Vessel.Operation.PUSHING`, in the Rule
20 window. Assures `Light.Masthead.Forward.2x`, sidelights and a sternlight. The composite-unit
exclusion (`OS.Trait`) was removed on 2026-10-19: the term does not resolve, so it would have
stopped Rule 24 evaluating for any pushing vessel. `pushing` is pushing ahead, not a composite
unit.

**Caveats.** Towing alongside is not a trip action, so it is not tested (LEGATA.065).

## (d) Also Rule 23(a)(ii)

> A power-driven vessel to which paragraph (a) or (c) of this Rule applies shall also comply with Rule
> 23(a)(ii).

**Legata.** `clause['COLREG.Rule24.d']`: power-driven, towing or pushing, 50 m or more, in the
Rule 20 window. Assures `Light.Masthead.Abaft`, Rule 23(a)(ii). It applied all of Rule 23 to every
power-driven vessel with an `apply` that did nothing until 2026-10-19 (LEGATA.066).

## (e) Vessel or object being towed

> A vessel or object being towed, other than those mentioned in paragraph (g) of this Rule, shall
> exhibit: (i) sidelights; (ii) a sternlight; (iii) when the length of the tow exceeds 200 metres, a
> diamond shape where it can best be seen.

**Legata.**
- `clause['COLREG.Rule24.e']`: towed, in the Rule 20 window. Assures sidelights and a sternlight.
- `clause['COLREG.Rule24.e.iii']`: towed, by day, over 200 m. Assures `Shape.Diamond`.

**Caveats.** The 200 m test uses the towed vessel's own length, not the length of the tow
(LEGATA.067).

## (f)–(i) Groups, submerged objects, impracticable cases

> (f) Provided that any number of vessels being towed alongside or pushed in a group shall be lighted as
> one vessel … (g) An inconspicuous, partly submerged vessel or object, or combination of such vessels or
> objects being towed, shall exhibit … (h) Where from any sufficient cause it is impracticable for a
> vessel or object being towed to exhibit the lights or shapes prescribed in paragraph (e) or (g) …
> (i) Where from any sufficient cause it is impracticable for a vessel not normally engaged in towing
> operations to display the lights prescribed in paragraph (a) or (c) …

**Legata.** None (TODOs).

## Open issues

- Towed vessels and composite units, for (b) and (e), and towing alongside, for (c).
- `VesselSignals` rows for towing and pushing.
- Feed the rule.
