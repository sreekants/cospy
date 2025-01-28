#!/usr/bin/python
# Filename: Rule40.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Application
Contracting Parties shall use the provisions of the Code for Implementation in the
execution of their obligations and responsibilities contained in the present Convention.
'''

class Rule40(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule40()


