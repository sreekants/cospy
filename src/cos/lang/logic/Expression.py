#!/usr/bin/python
# Filename: Expression.py
# Description: Base class for an decision expression

from cos.core.utilities.Errors import ErrorCode

from abc import ABC, abstractmethod

class Expression(ABC):
	def __init__(self):
		""" Constructor
		"""
		return

	@abstractmethod
	def evaluate( self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		pass

	def result(self, result, value_if_true, value_if_false):
		""" TODO: result
		Arguments
			result -- TODO
			value_if_true -- TODO
			value_if_false -- TODO
		""" 
		if result is None:
			return ErrorCode.ERROR_CONTINUE

		return value_if_true if result else value_if_false

class CompositeExpression(Expression):
	def __init__(self):
		""" Constructor
		"""
		Expression.__init__(self)
		self.components	= []
		return

class UnaryExpression(Expression):
	def __init__(self, lhs):
		""" Constructor
		Arguments
			lhs -- lvalue
		"""
		Expression.__init__(self)
		self.lhs	= lhs
		return

class BinaryExpression(Expression):
	def __init__(self, symbol, lhs, rhs, allow_nulls=False):
		""" Constructor
		Arguments
			lhs -- lvalue
			rhs -- rvalue
		"""
		Expression.__init__(self)
		self.lhs	= lhs
		self.rhs	= rhs
		self.symbol	= symbol

		if allow_nulls == False:
			assert( self.lhs is not None )

		# assert( self.rhs is not None )	# R-value may be a NULL
		return

	def __str__(self)->str:
		""" TODO: __str__
		""" 
		return f'({self.lhs} {self.symbol} {self.rhs})'

if __name__ == "__main__":
	test = Expression()


