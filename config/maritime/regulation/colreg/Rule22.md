# COLREG Rule 22 — Visibility of Lights

| | |
|---|---|
| Legata | `Rule22.legata` |
| Driver | `rules.colreg.rule22.Rule22` (`src/rules/colreg/rule22/Rule22.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule22` |
| Terms | `OS.Length`, `OS.Equipment.*.Range`; functions `meters()`, `miles()` |
| Tests | none |
| Status | Not judged. Four clauses on light equipment that no resolver provides; not fed |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 22 sets the minimum range of each light by vessel length. It is an equipment standard, not
conduct. The simulation has no light equipment: a light is a name in the signal vocabulary, with
no intensity or range (see Rule 20). The clauses are never fed.

## (a)–(c) Minimum ranges by length

> The lights prescribed in these Rules shall have an intensity as specified in Section 8 of Annex I to
> these Regulations so as to be visible at the following minimum ranges: (a) In vessels of 50 metres or
> more in length: a masthead light, 6 miles; a sidelight, 3 miles; a sternlight, 3 miles; a towing light,
> 3 miles; a white, red, green or yellow all-round light, 3 miles. (b) In vessels of 12 metres or more in
> length but less than 50 metres in length: a masthead light, 5 miles; except that where the length of
> the vessel is less than 20 metres, 3 miles; a sidelight, 2 miles; a sternlight, 2 miles; a towing
> light, 2 miles; a white, red, green or yellow all-round light, 2 miles. (c) In vessels of less than 12
> metres in length: a masthead light, 2 miles; a sidelight, 1 mile; a sternlight, 2 miles; a towing
> light, 2 miles; a white, red, green or yellow all-round light, 2 miles.

**Legata.**
- `clause['COLREG.Rule22.a']`: `OS.Length > meters(50)`.
- `clause['COLREG.Rule22.b.Large']`: `OS.Length in range(meters(20), meters(50))`.
- `clause['COLREG.Rule22.b.Small']`: `OS.Length in range(meters(12), meters(20))`.
- `clause['COLREG.Rule22.c']`: `OS.Length < meters(12)`.

Each assures `OS.Equipment.<Light>.Range >= miles(n)` for the masthead, side, stern, towing and
signal (all-round) lights. The lines are OR'd.

**Interpretation.** Each vessel's fitted lights would carry a range, compared with the minimum
for its length.

**Caveats.**
- `OS.Equipment.*` is not a term, and ship models have no light equipment.
- The assurance lines are OR'd, so meeting any one minimum would pass the clause.
- (a) tests `> 50`, where the rule says 50 m *or more*.
- `meters()` and `miles()` are not known to be Legata functions.
- Vessel length is `physics.length` from the ship model, which is a category value, not the
  individual vessel's length.

## (d) Inconspicuous, partly submerged vessels or objects being towed

> In inconspicuous, partly submerged vessels or objects being towed: a white all-round light, 3 miles.

**Legata.** None.

**Caveats.** Towed objects are not modelled.

## Open issues

- Decide whether Rule 22 is in scope. It concerns equipment certification, and REQ-057-07
  classes it as not judged. If it is, light equipment with a range must be added to the ship
  models.
