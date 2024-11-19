#!/usr/bin/python
# Filename: Rule11.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Application
Rules in this Section apply to vessels in sight of one another.
'''

class Rule11(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule11()


