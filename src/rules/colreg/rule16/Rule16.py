#!/usr/bin/python
# Filename: Rule16.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Action by Give-way Vessel
Every vessel which is directed to keep out of the way of another vessel shall, so far as possible, take
early and substantial action to keep well clear.
'''

class Rule16(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule16()


