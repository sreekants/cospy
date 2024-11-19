#!/usr/bin/python
# Filename: Rule14.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Head-on Situation
(a) When two power-driven vessels are meeting on reciprocal or nearly reciprocal courses so as to
involve risk of collision each shall alter her course to starboard so that each shall pass on the port
side of the other.
(b) Such a situation shall be deemed to exist when a vessel sees the other ahead or nearly ahead and
by night she could see the masthead lights of the other in a line or nearly in a line and/or both
sidelights and by day she observes the corresponding aspect of the other vessel.
(c) When a vessel is in any doubt as to whether such a situation exists she shall assume that it does
exist and act accordingly.
'''

class Rule14(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule14()


