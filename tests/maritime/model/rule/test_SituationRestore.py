#!/usr/bin/python
# Filename: test_SituationRestore.py
# Description: Test cases for rules restoring the shared situation after their encounters (COS.007)

import queue, unittest

from maritime.model.rule.COLREG import COLREG
from maritime.model.rule.InlandWaterRule import InlandWaterRule


class Result:
	def __init__(self, error=None):
		self.error	= error


class Automata:
	def __init__(self, fail=False):
		self.fail	= fail
	def evaluate(self, rule_ctxt):
		if self.fail:
			raise RuntimeError( 'automata failed' )
		return Result()


class Resolver:
	def __init__(self):
		self.situations	= []
	def reset(self, ctxt, rule_ctxt):
		self.situations.append( rule_ctxt.situation )


class RuleContext:
	def __init__(self):
		self.situation	= object()
		self.resolver	= Resolver()


def make(cls, fail):
	""" Builds a rule with two queued encounters, bypassing setup()
	Arguments
		cls -- Rule class
		fail -- Whether the automata raises
	Returns
		The rule and its evaluate function
	"""
	rule			= cls.__new__( cls )
	rule.automata	= Automata( fail )
	rule.sitations	= queue.Queue()
	rule.sitations.put( object() )
	rule.sitations.put( object() )
	if cls is COLREG:
		return rule, rule._COLREG__evaluate_rule
	return rule, rule.evaluate_rule


class TestSituationRestore(unittest.TestCase):
	def check(self, cls, fail):
		rule, evaluate	= make( cls, fail )
		rule_ctxt		= RuleContext()
		saved			= rule_ctxt.situation

		if fail:
			with self.assertRaises( RuntimeError ):
				evaluate( None, rule_ctxt )
		else:
			evaluate( None, rule_ctxt )

		self.assertIs( rule_ctxt.situation, saved )
		self.assertIs( rule_ctxt.resolver.situations[-1], saved )

	def test_colreg_restores_after_its_encounters(self):
		self.check( COLREG, False )

	def test_colreg_restores_when_the_automata_raises(self):
		self.check( COLREG, True )

	def test_inland_rule_restores_after_its_encounters(self):
		self.check( InlandWaterRule, False )

	def test_inland_rule_restores_when_the_automata_raises(self):
		self.check( InlandWaterRule, True )


if __name__ == '__main__':
	unittest.main()
