#!/usr/bin/python
# Filename: Rule2.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Responsibility
(a) Nothing in these Rules shall exonerate any vessel, or the owner, master or crew
thereof, from the consequences of any neglect to comply with these Rules or of the
neglect of any precaution which may be required by the ordinary practice of seamen,
or by the special circumstances of the case.
(b) In construing and complying with these Rules due regard shall be had to all
dangers of navigation and collision and to any special circumstances, including the
limitations of the vessels involved, which may make a departure from these Rules
necessary to avoid immediate danger.
'''

class Rule2(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule2()


