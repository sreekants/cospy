#!/usr/bin/python
# Filename: Rule31.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Seaplanes
(This Rule shall enter into force on 29 November 2003, as
amended by Resolution A.919(22))
Where it is impracticable for a seaplane or a WIG craft to exhibit lights and shapes of the
characteristics or in the positions prescribed in the Rules of this Part she shall exhibit
lights and shapes as closely similar in characteristics and position as is possible.
'''

class Rule31(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule31()


