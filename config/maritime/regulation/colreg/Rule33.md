# COLREG Rule 33 — Equipment for Sound Signals

| | |
|---|---|
| Legata | `Rule33.legata` (text only) |
| Driver | `rules.colreg.rule33.Rule33` (`src/rules/colreg/rule33/Rule33.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule33` |
| Tests | none |
| Status | Not judged. Equipment carriage; vessels carry no sound appliances |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 33 is about equipment, not conduct. Vessels have devices (`Vehicle.devices`, built by
`VesselComposer` from the ship model), but no whistle, bell or gong is defined. A vessel sounds a
signal by raising its name (see Rules 20 and 32), whether or not it carries the appliance.

## (a) Whistle, bell and gong by length

> A vessel of 12 metres or more in length shall be provided with a whistle, a vessel of 20 metres or
> more in length shall be provided with a bell in addition to a whistle, and a vessel of 100 metres or
> more in length shall, in addition, be provided with a gong, the tone and sound of which cannot be
> confused with that of the bell. The whistle, bell and gong shall comply with the specification in
> Annex III to these Regulations. The bell or gong or both may be replaced by other equipment having the
> same respective sound characteristics, provided that manual sounding of the required signals shall
> always be possible.

**Legata.** None.

**Caveats.** If carriage were modelled, it would be a check at build time on the ship model's
devices, not a rule evaluated in a run.

## (b) Under 12 m

> A vessel of less than 12 metres in length shall not be obliged to carry the sound signalling
> appliances prescribed in paragraph (a) of this Rule but if she does not, she shall be provided with
> some other means of making an efficient sound signal.

**Legata.** None.

## Open issues

- None. REQ-057-07 classes Rule 33 as not judged. Carriage could be added as a ship-model
  check, like the draught bounds.
