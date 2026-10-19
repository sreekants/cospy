# COLREG Rule 21 — Definitions (Lights)

| | |
|---|---|
| Legata | `Rule21.legata` (comments only) |
| Driver | `rules.colreg.rule21.Rule21` (`src/rules/colreg/rule21/Rule21.py`), constructor only |
| Loaded by | `rules.colreg.yaml`, entry `Rule21` |
| Definitions | Signal vocabulary `maritime/signals.yaml` |
| Tests | none for the rule |
| Status | Definitions only; nothing to judge |
| Reviewed | 2026-10-19 |

## How the rule is employed

Rule 21 defines each kind of light by colour, position and arc. The simulation defines lights
only as **names in the signal vocabulary**, each of class `navigation`. Showing a name stands for
showing a correctly fitted light (see Rule 20). Colour, arc and position are not modelled.

| Rule 21 | Vocabulary name | Note |
|---|---|---|
| (a) Masthead light | `Light.Masthead.Forward.1x`, `Light.Masthead.Forward.2x`, `Light.Masthead.Abaft` | Forward light, two in a line (Rule 24), second abaft (Rule 23(a)(ii)) |
| (b) Sidelights | `Light.Sidelight` | Both sides as one name; a combined lantern is not distinct |
| (c) Sternlight | `Light.Sternlight` | |
| (d) Towing light | `Light.TowingLight` | |
| (e) All-round light | `Light.Allround.White` | REQ-056-01 adds `Light.Allround.GreenWhite`, `RedWhite`, `Red.2x`, `RedWhiteRed` |
| (f) Flashing light | `Light.Flashing.Yellow`, `Light.Flashing.Red` | Rule 23(b), (c) |

## (a)–(f)

> (a) 'Masthead light' means a white light placed over the fore and aft centreline of the vessel
> showing an unbroken light over an arc of the horizon of 225 degrees … (b) 'Sidelights' means a green
> light on the starboard side and a red light on the port side each showing an unbroken light over an
> arc of the horizon of 112.5 degrees … (c) 'Sternlight' means a white light placed as nearly as
> practicable at the stern showing an unbroken light over an arc of the horizon of 135 degrees … (d)
> 'Towing light' means a yellow light having the same characteristics as the 'sternlight' … (e)
> 'All-round light' means a light showing an unbroken light over an arc of the horizon of 360 degrees.
> (f) 'Flashing light' means a light flashing at regular intervals at a frequency of 120 flashes or
> more per minute.

**Legata.** None.

**Caveats.**
- Arcs are not modelled, so which lights another vessel can see from its bearing is not derived.
  Rules 13(b) and 14(b) use geometry instead (bearing sectors that match the arcs: 22.5° abaft the
  beam, and dead ahead).
- Red and green sidelights are one name. A vessel cannot show only one of them.

## Open issues

- Light arcs, if a rule needs another vessel's view of own ship's lights.
