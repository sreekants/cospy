#!/usr/bin/python
# Filename: Rule21.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Definitions
(a) 'Masthead light' means a white light placed over the fore and aft centerline of the
vessel showing an unbroken light over an arc of the horizon of 225 degrees and so
fixed as to show the light from right ahead to 22.5 degrees abaft the beam on either
side of the vessel.
(b) 'Sidelights' means a green light on the starboard side and a red light on the port
side each showing an unbroken light over an arc of the horizon of 112.5 degrees and
so fixed as to show the light from right ahead to 22.5 degrees abaft the beam on its
respective side. In a vessel of less than 20 meters in length the sidelights may be
combined in one lantern carried on the fore and aft centreline of the vessel.
(c) 'Sternlight' means a white light placed as nearly as practicable at the stern
showing an unbroken light over an arc of the horizon of 135 degrees and so fixed as
to show the light 67.5 degrees from right aft on each side of the vessel.
(d) 'Towing light' means a yellow light having the same characteristics as the
'sternlight' defined in paragraph(c) of this COLREG.
(e) 'All round light' means a light showing an unbroken light over an arc of the horizon
of 360 degrees.
(f) 'Flashing light' means a light flashing at regular intervals at a frequency of 120
flashes or more per minute.
'''

class Rule21(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule21()


