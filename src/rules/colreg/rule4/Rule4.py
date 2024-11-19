#!/usr/bin/python
# Filename: Rule4.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Application
Rules in this Section apply in any condition of visibility.
'''

class Rule4(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule4()


