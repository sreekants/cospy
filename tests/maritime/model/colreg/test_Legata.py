#!/usr/bin/python
# Filename: test_Legata.py
# Description: Test cases for legata operators and clause structure, evaluated through the real resolver (COS.022)

import os, tempfile, unittest

from tests.maritime.model.colreg.colreg_harness import Vessel, Situation, Ctxt, Resolver, Automata, RuleContext


def judge(condition, intents=(), exclude=None)->bool:
	""" Whether a probe clause with this condition is violated; its assurance never holds
	Arguments
		condition -- Legata condition, own ship eastbound with the target 500 m ahead
		intents -- Intents own ship declares
		exclude -- Legata exclusion, or None
	"""
	block	= f"\n        exclude: {{ : {exclude} }}" if exclude else ''
	text	= (f"define:{{ OS: OwnShip, TS: TargetShip }}\nclause['PROBE']:{{\n    :{{\n"
			   f"        condition: {{ : {condition} }}{block}\n        assure: {{ : OS.Intent has 'Never.Set' }}\n    }}\n}}\n")
	f		= tempfile.NamedTemporaryFile( 'w', suffix='.legata', delete=False )
	f.write( text )
	f.close()

	own, target	= Vessel( 'OS', (0.0, 0.0), (1.0, 0.0) ), Vessel( 'TS', (500.0, 0.0), (-1.0, 0.0) )
	for intent in intents:
		own.intent.set( intent )

	ctxt		= Ctxt()
	resolver	= Resolver()
	resolver.init( ctxt, '$(CONFIG)/legata.yaml' )
	automata	= Automata( None )
	automata.load( f.name )
	os.unlink( f.name )

	rule_ctxt	= RuleContext( ctxt, resolver, None, [own, target], None )
	rule_ctxt.situation	= Situation( own, target )
	resolver.reset( ctxt, rule_ctxt )
	return bool( automata.evaluate(rule_ctxt).error )


class OperatorTestCase(unittest.TestCase):
	def test_in_matches_a_scalar_against_an_array(self):
		self.assertTrue( judge("(OS, TS).Position in ['Position.Port', 'Position.Ahead']") )
		self.assertFalse( judge("(OS, TS).Position in ['Position.Astern']") )

	def test_not_in_is_the_complement(self):
		self.assertTrue( judge("(OS, TS).Position not in ['Position.Astern']") )
		self.assertFalse( judge("(OS, TS).Position not in ['Position.Ahead']") )

	def test_has_matches_an_intent_with_wildcards(self):
		self.assertTrue( judge("OS.Intent has 'Manouever.CollisionAvoidance.*'", ['Manouever.CollisionAvoidance.Decelerate']) )
		self.assertTrue( judge("OS.Intent has 'Manouever.CollisionAvoidance.Decelerate'", ['Manouever.CollisionAvoidance.Decelerate']) )
		self.assertFalse( judge("OS.Intent has 'Manouever.CollisionAvoidance.*'") )

	def test_in_matches_an_intent_set_against_an_array(self):
		self.assertTrue( judge("OS.Intent in ['Alert.*', 'Signal.FogHorn']", ['Signal.FogHorn']) )
		self.assertFalse( judge("OS.Intent not in ['*Anchoring*']", ['Operation.Anchoring']) )

	def test_array_elements_may_be_constants(self):
		self.assertTrue( judge("OS.Type in [Vessel.Type.Sailing, Vessel.Type.PowerDriven]") )


class StructureTestCase(unittest.TestCase):
	TRUE, FALSE	= "((OS, TS).Distance > 0)", "((OS, TS).Distance < 0)"

	def test_and_needs_every_term(self):
		self.assertTrue( judge(f"{self.TRUE} and {self.TRUE}") )
		self.assertFalse( judge(f"{self.TRUE} and {self.FALSE}") )
		self.assertFalse( judge(f"{self.FALSE} and {self.TRUE}") )

	def test_or_needs_any_term(self):
		self.assertTrue( judge(f"{self.FALSE} or {self.TRUE}") )
		self.assertFalse( judge(f"{self.FALSE} or {self.FALSE}") )

	def test_nested_terms(self):
		self.assertTrue( judge(f"{self.TRUE} and ({self.FALSE} or {self.TRUE})") )
		self.assertFalse( judge(f"{self.TRUE} and ({self.FALSE} or {self.FALSE})") )

	def test_an_exclusion_that_holds_takes_the_clause_out_of_scope(self):
		self.assertFalse( judge(self.TRUE, exclude=self.TRUE) )
		self.assertTrue( judge(self.TRUE, exclude=self.FALSE) )


if __name__ == '__main__':
	unittest.main()
