#!/usr/bin/python
# Filename: Rule28.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Vessel constrained by their draught
A vessel constrained by her draught may, in addition to the lights prescribed for
power-driven vessels in rule 23, exhibit where they can best be seen three all-round
red lights in a vertical line, or a cylinder.
'''

class Rule28(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule28()


