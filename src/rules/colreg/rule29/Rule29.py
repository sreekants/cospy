#!/usr/bin/python
# Filename: Rule29.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Pilot Vessels
(a) A vessel engaged on pilotage duty shall exhibit:
(i) at or near the masthead, two all-round lights in a vertical line, the upper
being white and the lower red;
(ii) when underway, in addition, sidelight and a sternlight;
(iii) when at anchor, in addition to the lights prescribed in subparagraph (i), the
light, lights or shape prescribed in Rule 30 for vessels at anchor.
(b) A pilot vessel when not engaged on pilotage duty shall exhibit the lights or shapes
prescribed for a similar vessel of her length.
'''

class Rule29(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule29()


