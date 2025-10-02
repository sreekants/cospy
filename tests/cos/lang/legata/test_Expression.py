#!/usr/bin/python
# Filename: Expression_test.py
# Description: Test cases for the Expression class

from cos.model.rule.Automata import *
from cos.model.rule.Context import *
from cos.lang.legata.Expression import *
from cos.lang.legata.Definition import Definition
from cos.model.logic.Decision import Decision
from cos.model.resolver.Resolver import *
from cos.model.resolver.CompositeResolver import CompositeResolver
from cos.model.resolver.MappingResolver import MappingResolver

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

class ExpressionTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):

		txt = "20.0"
		x = txt.isdecimal()
		print(x)

		self.a = Automata(None)
		self.d = self.a.definition
		clause = self.d.add('/', Decision('Decision1'))
		clause.IF( LT('(OS,TS).distance', '20.0') )
		clause.ASSURE( GTE('(OS,TS).distance', 'distance.safe') )

		self.c = StateResolver()
		constants = self.c.constants
		constants["distance.safe"]       = 100
		constants["distance.visible"]    = 200

		print( f"{self.c.resolve(None, 'distance.safe')}" )

		self.ctxt    = Context(self.c, None, None)
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_Error(self):
		variables	= self.c.variables
		variables["(OS,TS).distance"]    = 50
		result	= self.a.evaluate(self.ctxt)
		self.assertEqual(len(result.error), 1)
		print( f"{result}" )
		return

	def test_NoError(self):
		variables	= self.c.variables
		variables["(OS,TS).distance"]    = 150
		result	= self.a.evaluate(self.ctxt)
		self.assertEqual(len(result.error), 0)
		return


if __name__ == '__main__':
    unittest.main()
