#!/usr/bin/python
# Filename: Rule37.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
When a vessel is in distress and requires assistance she shall use or exhibit the signals
described in Annex IV to these Regulations.
'''

class Rule37(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule37()


