#!/usr/bin/python
# Filename: Rule37.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from cos.core.kernel.Context import Context
from cos.model.rule.Situation import Situation

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

	def feed(self, ctxt:Context, rule_ctxt):
		""" Adds every vessel under test on each pass; the finding guards keep one row per episode
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		vessels		= rule_ctxt.vessels or []
		for own in getattr( rule_ctxt, 'subjects', None ) or vessels:
			self.add_situation( Situation(own, None) )
		return



if __name__ == "__main__":
	test = Rule37()


