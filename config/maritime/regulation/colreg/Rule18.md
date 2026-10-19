# COLREG Rule 18 — Responsibilities between Vessels

| | |
|---|---|
| Legata | `Rule18.legata` |
| Driver | `rules.colreg.rule18.Rule18` (`src/rules/colreg/rule18/Rule18.py`) |
| Loaded by | `rules.colreg.yaml`, entry `Rule18` (`encounter.dcpa`, `encounter.range` optional) |
| Terms | `VesselResolver` (`Type`, `Status`, `Operation`), `TargetResolver` (`Distance`); constant `Vessel.Collision.PassingDistance` (100 m) |
| Tests | `tests/maritime/model/colreg/test_Rule18.py` (9) |
| Status | (a)–(c) judged; (d)–(f) not applicable. Not yet exercised in a run |
| Reviewed | 2026-10-19 |

## How the rule is fed

`Rule18.feed()` runs an `EncounterWatch` of every encounter type except overtaking (`OTGW`,
`OTSO`, which are Rule 13's: "except where Rules 9, 10 and 13 otherwise require").

- **Onset:** the other vessel is within 4 km, the two are closing, and the predicted passing
  distance is under 500 m.
- **Skips:** a pair classified as no applicable rule, or held by the overtaking watch.
- **Judgement:** the situation is queued once the range opens past the closest approach. The
  watch claims no role.

## (a) Power-driven vessel keeps out of the way

> A power-driven vessel underway shall keep out of the way of: (i) a vessel not under command; (ii) a
> vessel restricted in her ability to manoeuvre; (iii) a vessel engaged in fishing; (iv) a sailing
> vessel.

**Legata.** `clause['COLREG.Rule18.a']`:
- **condition:** `OS.Type is Vessel.Type.PowerDriven`, and the target is not under command,
  restricted, fishing or sailing;
- **excluded:** own ship not under command or restricted; own ship fishing (judged under (c));
  own ship not underway (anchored, moored, made fast, aground);
- **assured:** `(OS, TS).Distance >= Vessel.Collision.PassingDistance`.

**Interpretation.** *Keep out of the way:* passed at 100 m or more at the closest approach.

**Caveats.**
- Nothing sets `NOT_UNDER_COMMAND` or `RESTRICTED`, and `vessel.operation` is never set
  (REQ.059-02, -03). In a run, (a) applies only to power-driven vessels meeting sailing vessels.
- In a crossing, the same vessel is also judged by Rule 15, because the crossing watch does not
  check vessel types.
- Rules 9 and 10 are not fed, so their precedence is not applied.

## (b) Sailing vessel keeps out of the way

> A sailing vessel underway shall keep out of the way of: (i) a vessel not under command; (ii) a
> vessel restricted in her ability to manoeuvre; (iii) a vessel engaged in fishing.

**Legata.** `clause['COLREG.Rule18.b']`: own ship sailing, and the target not under command,
restricted or fishing. Exclusions and assurance as for (a), except fishing.

**Caveats.** Inert in a run, for the same reasons as (a).

## (c) Fishing vessel keeps out of the way

> A vessel engaged in fishing when underway shall, so far as possible, keep out of the way of: (i) a
> vessel not under command; (ii) a vessel restricted in her ability to manoeuvre.

**Legata.** `clause['COLREG.Rule18.c']`: own ship fishing, and the target not under command or
restricted.

**Caveats.**
- "So far as possible" is not tested.
- Inert in a run.

## (d) Constrained by draught

> (i) Any vessel other than a vessel not under command or a vessel restricted in her ability to
> manoeuvre shall, if the circumstances of the case admit, avoid impeding the safe passage of a vessel
> constrained by her draught, exhibiting the signals in Rule 28. (ii) A vessel constrained by her
> draught shall navigate with particular caution having full regard to her special condition.

**Legata.** None. Not applicable.

**Caveats.** "Constrained by draught" is not modelled. `Restriction.DRAUGHT` shares its value with
`TRANSPORTING` and is never set (Rule 3(h)).

## (e) Seaplanes; (f) WIG craft

> (e) A seaplane on the water shall, in general, keep well clear of all vessels and avoid impeding their
> navigation. In circumstances, however, where risk of collision exists, she shall comply with the
> Rules of this Part. (f) (i) A WIG craft shall, when taking off, landing and in flight near the
> surface, keep well clear of all other vessels and avoid impeding their navigation; (ii) a WIG craft
> operating on the water surface shall comply with the Rules of this Part as a power-driven vessel.

**Legata.** None. Not applicable.

**Caveats.** No scenario has seaplanes or WIG craft. Their types include the power-driven bit, so
(a) would judge them as power-driven vessels, which matches (f)(ii).

## Open issues

- Set operation and restriction status from behaviour (REQ.059-02, -03). Until then (b) and (c)
  cannot fire.
- Resolve the Rule 15 / Rule 18(a) overlap.
- Model constrained by draught, for (d).
