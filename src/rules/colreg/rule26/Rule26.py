#!/usr/bin/python
# Filename: Rule26.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Fishing Vessels
(a) A vessel engaged in fishing, whether underway or at anchor, shall exhibit only the
lights and shapes prescribed in this COLREG.
(b) A vessel when engaged in trawling, by which is meant the dragging through the
water of a dredge net or other apparatus used as a fishing appliance, shall exhibit:
(i) two all-round lights in a vertical line, the upper being green and the lower
white, or a shape consisting of two cones with their apexes together in a
vertical line one above the other;
(ii) a masthead light abaft of and higher than the all-round green light; a vessel
of less than 50 metres in length shall not be obliged to exhibit such a light but
may do so;
(iii) when making way through the water, in addition to the lights prescribed in
this paragraph, sidelights and a sternlight.
(c) A vessel engaged in fishing, other than trawling, shall exhibit:
(i) two all-round lights in a vertical line, the upper being red and the lower white,
or a shape consisting of two cones with apexes together in a vertical line one
above the other;
(ii) when there is outlying gear extending more than 150 metres horizontally
from the vessel, an all-round white light or a cone apex upwards in the
direction of the gear;
(iii) when making way through the water, in addition to the lights prescribed in
this paragraph, sidelights and a sternlight.
(d) The additional signals described in Annex II to these Regulations apply to a vessel
engaged in fishing in close proximity to other vessels engaged in fishing.
(e) A vessel when not engaged in fishing shall not exhibit the lights or shapes
prescribed in this Rule, but only those prescribed for a vessel of her length.
'''

class Rule26(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule26()


