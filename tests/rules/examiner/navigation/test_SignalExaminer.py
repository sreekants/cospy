#!/usr/bin/python
# Filename: test_SignalExaminer.py
# Description: Test cases for the SignalExaminer class

import types, unittest

from tests.maritime.model.risk.test_ConcernWeights import source_module

SignalExaminer	= source_module( 'rules.examiner.navigation.SignalExaminer' ).SignalExaminer
Signal			= source_module( 'cos.model.vehicle.Signal' ).Signal

class SignalExaminerTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

class SignalTupleTestCase(unittest.TestCase):
	""" REQ.036: the posted tuple carries the signals shown, apart from the intent """

	def rule_ctxt(self, intent=(), signals=()):
		shown	= Signal()
		for s in signals:
			shown.set( s )
		terms	= { 'OwnShip.Intent': list(intent), 'OwnShip.Signal': shown }
		return types.SimpleNamespace( resolve=terms.get )

	def test_signals_are_one_sorted_token(self):
		r	= self.rule_ctxt( signals=['Sound.Blast.Short.1x', 'Light.Flash.1x'] )
		self.assertEqual( SignalExaminer.signal(r), 'Light.Flash.1x,Sound.Blast.Short.1x' )

	def test_no_signal_is_none(self):
		self.assertIsNone( SignalExaminer.signal(self.rule_ctxt()) )

	def test_intent_and_signal_are_kept_apart(self):
		r	= self.rule_ctxt( intent=['Speed.SlowdownForTraffic'], signals=['Light.Flash.1x'] )
		self.assertEqual( SignalExaminer.intent(r), 'Speed.SlowdownForTraffic' )
		self.assertEqual( SignalExaminer.signal(r), 'Light.Flash.1x' )

if __name__ == '__main__':
    unittest.main()
