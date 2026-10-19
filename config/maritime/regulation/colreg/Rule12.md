# COLREG Rule 12 — Sailing Vessels

| | |
|---|---|
| Legata | `Rule12.legata` |
| Driver | `rules.colreg.rule12.Rule12` (`src/rules/colreg/rule12/Rule12.py`) |
| Loaded by | `rules.colreg.yaml`, entry `Rule12` (`encounter.dcpa`, `encounter.range` optional) |
| Terms | `ColregResolver` (`Tack`, `TargetTack`, `Windward`), `TargetResolver` (`Distance`), `VesselResolver` (`Type`, `Status`, `Operation`); constant `Vessel.Collision.PassingDistance` (100 m) |
| Simulation | Wind force on each vessel (`actor.motion.forces[WIND_CURRENT]`, set by the weather system) |
| Tests | `tests/maritime/model/colreg/test_Rule12.py` (16) |
| Status | (a), (a)(i)–(iii) judged; (b) not modelled. Not yet exercised in a run |
| Reviewed | 2026-10-19 |

## How the rule is fed

`Rule12.feed()` runs an `EncounterWatch` of every encounter type except overtaking (`OTGW`,
`OTSO`, which are Rule 13's).

- **Onset:** an encounter begins when the other vessel is within 4 km (`encounter.range`), the
  two are closing, and the predicted passing distance is under 500 m (`encounter.dcpa`).
- **Snapshot:** at onset, `Rule12.snapshot()` records each vessel's tack, and whether own ship is
  to windward, from the wind acting on each vessel.
- **Judgement:** the situation is queued once the range opens past the closest approach, and
  judged on the snapshot. A vessel that tacks or bears away to give way keeps the duty she had.

The watch claims no encounter role, so Rules 13–15 keep theirs.

## (a) Two sailing vessels approaching with risk of collision

> When two sailing vessels are approaching one another, so as to involve risk of collision, one of
> them shall keep out of the way of the other as follows;

**Legata.** `clause['COLREG.Rule12.a']`, the symmetric reading:
- **condition:** both vessels sailing, and `(OS, TS).Tack is 'Unknown'`;
- **excluded:** either vessel not under command, restricted or fishing; own ship not underway;
- **assured:** `(OS, TS).Distance >= Vessel.Collision.PassingDistance`.

**Interpretation.**
- *Keep out of the way:* own ship passed at the passing distance or more at the closest
  approach. The same reading is used in Rules 13, 15 and 18.
- When own ship's tack cannot be told (a calm, stopped, or the wind dead ahead or astern), she is
  judged as if she had to keep out of the way.
- A vessel not under command, restricted or fishing is left to Rule 18.

**Caveats.**
- The symmetric reading can flag both vessels in a calm.
- The 100 m passing distance is a constant, the same for every size of vessel.
- Risk of collision is the watch's onset test: 4 km and 500 m, unvalidated.
- Being in sight is not tested (see Rule 11).

## (a)(i) Wind on different sides: port tack keeps clear

> when each has the wind on a different side, the vessel which has the wind on the port side shall
> keep out of the way of the other;

**Legata.** `clause['COLREG.Rule12.a.i']`: both sailing, `Tack is 'Port'` and `TargetTack is
'Starboard'`. Exclusions and assurance as for (a).

**Interpretation.** *Tack* is the side the wind comes over. It is the sign of the cross product
of the vessel's heading with the upwind direction (map y grows south, as in `passing_side()`).

**In the simulation.** The wind vector is the `WIND_CURRENT` force the weather system puts on
each vessel, the direction the wind blows towards. Each vessel's tack uses the wind at its own
position.

## (a)(ii) Same side: windward keeps clear of leeward

> when both have the wind on the same side, the vessel which is to windward shall keep out of the way
> of the vessel which is to leeward;

**Legata.** `clause['COLREG.Rule12.a.ii']`: both sailing, the same known tack, and `Windward is
true`.

**Interpretation.** Own ship is *to windward* when the target lies downwind of her: the offset to
the target has a positive component along the wind vector at own ship.

## (a)(iii) Port tack, other vessel to windward on an unknown tack

> if a vessel with the wind on the port side sees a vessel to windward and cannot determine with
> certainty whether the other vessel has the wind on the port or on the starboard side, she shall keep
> out of the way of the other.

**Legata.** `clause['COLREG.Rule12.a.iii']`: both sailing, `Tack is 'Port'`, `TargetTack is
'Unknown'` and `Windward is false`.

**Interpretation.** "Cannot determine with certainty" becomes "the other vessel's tack is
unknown": she is stopped, or has the wind dead ahead or astern.

**Caveats.** The simulation knows every tack exactly, so (iii) applies only in those edge cases,
not under real uncertainty.

## (b) The windward side is opposite the mainsail

> For the purposes of this Rule the windward side shall be deemed to be the side opposite to that on
> which the mainsail is carried or, in the case of a square-rigged vessel, the side opposite to that on
> which the largest fore-and-aft sail is carried.

**Legata.** None.

**Interpretation.** The windward side is taken from the wind itself, not from the sails.

**Caveats.** No vessel carries a sail plan. Running before the wind with the mainsail out to one
side is judged as `Unknown` here, where (b) would give a tack.

## General caveats

- `SailingVessel` behaviours do not steer by the wind. Whether they give way correctly depends on
  their speed-based separation manoeuvres, not on Rule 12.
- No scenario yet has sailing vessels meeting in wind, so the rule has not been judged in a run.
- Terms return a value, never "unknown": `Windward` is false in a calm. A term returning `None`
  raises `Unresolved variable`.

## Open issues

- Run a scenario with sailing vessels in wind.
- Decide whether the symmetric (a) should flag both vessels.
- Being in sight, per Rule 11.
