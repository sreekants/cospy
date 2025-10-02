#!/usr/bin/python
# Filename: Resolver_test.py
# Description: Test cases for the Resolver class

from cos.model.rule.Automata import Automata
from cos.model.rule.Context import *
from cos.lang.legata.Expression import *
from cos.model.resolver.Resolver import *
from cos.model.resolver.CompositeResolver import CompositeResolver
from cos.model.resolver.MappingResolver import MappingResolver
from cos.core.kernel.Configuration import Configuration

import unittest

class StateResolver(CompositeResolver):
    def __init__(self):
        CompositeResolver.__init__(self)
        self._variables = self.add(MappingResolver())
        self._constants = self.add(MappingResolver())
        return

    @property
    def constants(self):
        return self._constants

    @property
    def variables(self):
        return self._variables

class AutomataTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.path	= Configuration.resolve_path('$(COS_ROOT)/config/maritime/regulation/colreg/test.k')
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return

	def test_Compile(self):
		a       = Automata(None)
		a.compile( self.path )

		print( "="*40 )
		print( "DUMP" )
		print( "="*40 )
		a.dump()
		a.save( "test.lbo" )
		return


	def test_Load(self):
		a       = Automata(None)
		a.load( "test.lbo" )

		print( "="*40 )
		print( "LOADED DUMP" )
		print( "="*40 )
		a.dump()
		return


	def atest_Evaluate(self):
		a       = Automata(None)
		a.compile( self.path )

		c = StateResolver()
		constants = c.constants
		constants["distance.safe"]       = 100
		constants["distance.visible"]    = 200
		variables = c.variables
		variables["(OwnShip,TargetShip).Distance"]  = 10

		ctxt    = Context(c, None, None)

		# The speed check will cause an error
		variables["OwnShip.Velocity"]       = 130
		result	= a.evaluate(ctxt)
		self.assertEqual(len(result.error), 1)
		print( f"{result}" )

		# The speed check will pass through with no error
		variables["OwnShip.Velocity"]       = 5
		result	= a.evaluate(ctxt)
		self.assertEqual(len(result.error), 0)
		return

if __name__ == '__main__':
    unittest.main()
