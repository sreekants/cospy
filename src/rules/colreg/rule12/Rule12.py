#!/usr/bin/python
# Filename: Rule12.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Sailing Vessels
(a) When two sailing vessels are approaching one another, so as to involve risk of collision, one of
them shall keep out of the way of the other as follows;
(i) when each has the wind on a different side, the vessel which has the wind on the port
side shall keep out of the way of the other;
(ii) when both have the wind on the same side, the vessel which is to windward shall keep
out of the way of the vessel which is to leeward;
(iii) if a vessel with the wind on the port side sees a vessel to windward and cannot
determine with certainty whether the other vessel has the wind on the port or on the
starboard side, she shall keep out of the way of the other.
(b) For the purposes of this Rule the windward side shall be deemed to be the side opposite to that
on which the mainsail is carried or, in the case of a square-rigged vessel, the side opposite to that on
which the largest fore-and-aft sail is carried.
'''

class Rule12(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule12()


