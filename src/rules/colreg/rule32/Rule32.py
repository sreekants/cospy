#!/usr/bin/python
# Filename: Rule32.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Rule 32
Definitions
(a) The word 'whistle' means any sound signalling appliance capable of producing the
prescribed blasts and which complies with the specifications in Annex III to these
Regulations.
(b) The term 'short blast' means a blast of about one second's duration.
(c) The term 'prolonged blast' means a blast of from four to six seconds's duration.
'''

class Rule32(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule32()


