#!/usr/bin/python
# Filename: Expression.py
# Description: Basic logical expressions used in a decision tree

from cos.lang.logic.Expression import *
from cos.lang.symbol.Symbol import *
from cos.core.utilities.Errors import ErrorCode

class ALL(CompositeExpression):
	def __init__(self):
		""" Constructor
		"""
		CompositeExpression.__init__(self)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		for c in self.components:
			result = c.evaluate(ctxt)
			if result in [ErrorCode.S_OK, ErrorCode.S_TRUE, ErrorCode.ERROR_CONTINUE]:
				continue

			if result in [ErrorCode.S_FALSE]:
				return ErrorCode.S_FALSE

			return result

		return ErrorCode.S_TRUE

class ANY(CompositeExpression):
	def __init__(self):
		""" Constructor
		"""
		CompositeExpression.__init__(self)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		for c in self.components:
			result = c.evaluate(ctxt)
			if result in [ErrorCode.S_OK, ErrorCode.S_TRUE]:
				return ErrorCode.S_TRUE

			if result in [ErrorCode.S_FALSE, ErrorCode.ERROR_CONTINUE]:
				continue

			return result

		return ErrorCode.S_FALSE

class NONE(CompositeExpression):
	def __init__(self):
		""" Constructor
		"""
		CompositeExpression.__init__(self)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		for c in self.components:
			result = c.evaluate(ctxt)
			if result in [ErrorCode.S_OK, ErrorCode.S_TRUE]:
				return ErrorCode.S_FALSE

			if result in [ErrorCode.S_FALSE, ErrorCode.ERROR_CONTINUE]:
				continue

			return result

		return ErrorCode.S_TRUE

class ABORT(Expression):
	def __init__(self):
		""" Constructor
		"""
		Expression.__init__(self)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return ErrorCode.E_ABORT

class IS(BinaryExpression):
	def __init__(self, lhs, rhs):
		""" Constructor
		Arguments
			lhs -- lvalue
			lhs -- rvalue
		"""
		BinaryExpression.__init__(self, 'is', lhs, rhs)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.IS(self.lhs, self.rhs), ErrorCode.S_TRUE, ErrorCode.S_FALSE)

class IS_NOT(BinaryExpression):
	def __init__(self, lhs, rhs):
		""" Constructor
		Arguments
			lhs -- lvalue
			lhs -- rvalue
		"""
		BinaryExpression.__init__(self, 'is not', lhs, rhs)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.IS(self.lhs, self.rhs), ErrorCode.S_FALSE, ErrorCode.S_TRUE)


class IN(BinaryExpression):
	def __init__(self, lhs, rhs):
		""" Constructor
		Arguments
			lhs -- lvalue
			lhs -- rvalue
		"""
		BinaryExpression.__init__(self, 'in', lhs, rhs)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.IN(self.lhs, self.rhs), ErrorCode.S_TRUE, ErrorCode.S_FALSE)

	def __str__(self)->str:
		""" TODO: __str__
		""" 
		if isinstance(self.rhs, list) is False:
			return f'({self.lhs} {self.symbol} {self.rhs})'

		argslist = [str(arg) for arg in self.rhs]
		return f"({self.lhs} {self.symbol} [{', '.join(argslist)}])"


class NOT_IN(BinaryExpression):
	def __init__(self, lhs, rhs):
		""" Constructor
		Arguments
			lhs -- lvalue
			lhs -- rvalue
		"""
		BinaryExpression.__init__(self, 'not in', lhs, rhs)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.IN(self.lhs, self.rhs), ErrorCode.S_FALSE, ErrorCode.S_TRUE)


class NOT(UnaryExpression):
	def __init__(self, value):
		""" Constructor
		Arguments
			lhs -- lvalue
		"""
		UnaryExpression.__init__(self, value)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.NOT(self.lhs, self.rhs), ErrorCode.S_TRUE, ErrorCode.S_FALSE)


class GT(BinaryExpression):
	def __init__(self, lhs, rhs):
		""" Constructor
		Arguments
			lhs -- lvalue
			lhs -- rvalue
		"""
		BinaryExpression.__init__(self, '>', lhs, rhs)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.GT(self.lhs, self.rhs), ErrorCode.S_TRUE, ErrorCode.S_FALSE)

class LT(BinaryExpression):
	def __init__(self, lhs, rhs):
		""" Constructor
		Arguments
			lhs -- lvalue
			lhs -- rvalue
		"""
		BinaryExpression.__init__(self, '<', lhs, rhs)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.LT(self.lhs, self.rhs), ErrorCode.S_TRUE, ErrorCode.S_FALSE)


class LTE(BinaryExpression):
	def __init__(self, lhs, rhs):
		""" Constructor
		Arguments
			lhs -- lvalue
			lhs -- rvalue
		"""
		BinaryExpression.__init__(self, '<=', lhs, rhs)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.LTE(self.lhs, self.rhs), ErrorCode.S_TRUE, ErrorCode.S_FALSE)

class GTE(BinaryExpression):
	def __init__(self, lhs, rhs):
		""" Constructor
		Arguments
			lhs -- lvalue
			lhs -- rvalue
		"""
		BinaryExpression.__init__(self, '>=', lhs, rhs)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.GTE(self.lhs, self.rhs), ErrorCode.S_TRUE, ErrorCode.S_FALSE)

class EQ(BinaryExpression):
	def __init__(self, lhs, rhs):
		""" Constructor
		Arguments
			lhs -- lvalue
			lhs -- rvalue
		"""
		BinaryExpression.__init__(self, '==', lhs, rhs)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.EQ(self.lhs, self.rhs), ErrorCode.S_TRUE, ErrorCode.S_FALSE)

class NEQ(BinaryExpression):
	def __init__(self, lhs, rhs):
		""" Constructor
		Arguments
			lhs -- lvalue
			lhs -- rvalue
		"""
		BinaryExpression.__init__(self, '!=', lhs, rhs)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.result(ctxt.NEQ(self.lhs, self.rhs), ErrorCode.S_TRUE, ErrorCode.S_FALSE)

if __name__ == "__main__":
	test = Expression()


