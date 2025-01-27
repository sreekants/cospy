#!/usr/bin/python
# Filename: Rule23.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Power-driven Vessels underway
(The new paragraph (c) shall enter into force on 29 November
2003, as amended by Resolution A.919(22))
(a) A power-driven vessel underway shall exhibit:
(i) a masthead light forward;
(ii) a second masthead light abaft of and higher than the forward one; except that
a vessel of less than 50 meters in length shall not be obliged to exhibit such
light but may do so;
(iii) sidelights;
(iv) a sternlight.
(b) An air-cushion vessel when operating in the non-displacement mode shall, in
addition to the lights prescribed in paragraph (a) of this Rule exhibit an all-round
flashing yellow light.
(c) A WIG craft only when taking off, landing and in flight near the surface shall, in
addition to the lights prescribed in paragraph (a) of this Rule, exhibit a high intensity
all-round flashing red light.
(d)
(i) A power-driven vessel of less than 12 meters in length may in lieu of the lights
prescribed in paragraph (a) of this Rule exhibit an all-round white light and
sidelights:
(ii) a power-driven vessel of less than 7 meters in length whose maximum speed
does not exceed 7 knots may in lieu of the lights prescribed in paragraph (a) of
this Rule exhibit an all-round white light and shall, if practicable, also exhibit
sidelights;
(iii) the masthead light or all-round white light on a power-driven vessel of less
than 12 meters in length may be displaced from the fore and aft centreline of
the vessel if centreline fitting is not practicable, pcosided that the sidelights are
combined in one lantern which shall be carried on the fore and aft centreline of
the vessel or located as nearly as practicable in the same fore and aft line as
the masthead light or the all-round white light.
'''

class Rule23(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule23()


