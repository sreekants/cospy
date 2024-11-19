#!/usr/bin/python
# Filename: Rule5.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Look-out
Every vessel shall at all times maintain a proper look-out by sight and hearing as well as by all
available means appropriate in the prevailing circumstances and conditions so as to make a full
appraisal of the situation and of the risk of collision.
'''

class Rule5(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule5()


