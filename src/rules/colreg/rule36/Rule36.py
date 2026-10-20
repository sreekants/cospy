#!/usr/bin/python
# Filename: Rule36.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from cos.core.kernel.Context import Context
from cos.model.rule.Situation import Situation

'''
Signals to attract Attention
If necessary to attract the attention of another vessel any vessel may make light or
sound signals that cannot be mistaken for any signal authorized elsewhere in these
Rules, or may direct the beam of her searchlight in the direction of the danger, in such
a way as not to embarrass any vessel. Any light to attract the attention of another
vessel shall be such that it can not be mistaken for any aid to navigation. For the
purpose of this Rule the use of high intensity intermittent or revolving lights, such as
stcose lights, shall be avoided.
'''

class Rule36(COLREG):
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
	test = Rule36()


