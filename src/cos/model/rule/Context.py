		#!/usr/bin/python
# Filename: Context.py
# Description: Implementation of the Context class

from cos.model.rule.Situation import Situation
from cos.lang.symbol.Symbol import Symbol, SymbolType
from cos.core.kernel.Context import Context as KernelContext

class Context:
	def __init__(self, ctxt:KernelContext, resolver, world, vessels, api):
		""" Constructor
		Arguments
			resolver -- Reference to the resolver
			world -- Reference ot the simulation world
			vessels -- List of ships in the environment
		"""
		self.ctxt		= ctxt
		self.resolver	= resolver
		self.vessels	= vessels			# Vessels to be included in motion analysis
		self.bodies		= None				# Rigid bodies to be included in obstruction analysis
		self.world		= world

		self.situation	= Situation()
		self.encounters	= []
		self.api		= api
		return

	def resolve_tuple(self, lhs, rhs):
		""" Resolves the tuple to values
		Arguments
			lhs -- lvalue of the expression (variable name)
			rhs -- rvalue of the expression
		""" 
		lhs	= self.resolve(lhs)
		rhs	= self.resolve(rhs)
		if lhs is None or rhs is None:
			return (False, lhs, rhs)

		return (True, lhs, rhs)

	# Evaluation of expressions in the context of the situation
	def IS(self, lhs, rhs, match_all:bool=False):
		""" operator IS
		Arguments
			lhs -- lvalue of the expression (variable name)
			rhs -- rvalue of the expression
			match_all -- Flag to match all values
		"""
		result, lhs, rhs	= self.resolve_tuple(lhs, rhs)
		if result == False:
			return None
		
		return True if lhs == rhs else False

	def IN(self, lhs, rhs, match_all:bool=False):
		""" operator IN
		Arguments
			lhs -- lvalue of the expression (variable name)
			rhs -- rvalue of the expression (an array)
			match_all -- Flag to match all values
		"""
		if (lhs is None) or (lhs is None):
			raise RuntimeError("Unexpected NULL object in expression evaluation.") 
		
		result, lhs, rhs	= self.resolve_tuple(lhs, rhs)
		if result == False:
			return None

		if match_all == False:
			return True if lhs in rhs else False
		
		for x in lhs:
			if x not in rhs:
				return False
			
		return True

	def LT(self, lhs, rhs, convert=None):
		""" operator LT
		Arguments
			lhs -- lvalue of the expression (variable name)
			rhs -- rvalue of the expression
			convert -- Flag to enable automatic conversion
		"""
		result, lhs, rhs	= self.resolve_tuple(lhs, rhs)
		if result == False:
			return None
		return True if lhs<rhs else False

	def GT(self, lhs, rhs, convert=None):
		""" operator GT
		Arguments
			lhs -- lvalue of the expression (variable name)
			rhs -- rvalue of the expression
			convert -- Flag to enable automatic conversion
		"""
		result, lhs, rhs	= self.resolve_tuple(lhs, rhs)
		if result == False:
			return None
		return True if lhs>rhs else False

	def GTE(self, lhs, rhs, convert=None):
		""" operator GTE
		Arguments
			lhs -- lvalue of the expression (variable name)
			rhs -- rvalue of the expression
			convert -- Flag to enable automatic conversion
		"""
		result, lhs, rhs	= self.resolve_tuple(lhs, rhs)
		if result == False:
			return None
		return True if lhs>=rhs else False

	def LTE(self, lhs, rhs, convert=None):
		""" operator LTE
		Arguments
			lhs -- lvalue of the expression (variable name)
			rhs -- rvalue of the expression
			convert -- Flag to enable automatic conversion
		"""
		result, lhs, rhs	= self.resolve_tuple(lhs, rhs)
		if result == False:
			return None
		return True if lhs<=rhs else False

	def EQ(self, lhs, rhs, convert=None):
		""" operator EQ
		Arguments
			lhs -- lvalue of the expression (variable name)
			rhs -- rvalue of the expression
			convert -- Flag to enable automatic conversion
		"""
		result, lhs, rhs	= self.resolve_tuple(lhs, rhs)
		if result == False:
			return None
		return True if lhs == rhs else False

	def NEQ(self, lhs, rhs, convert=None):
		""" operator NEQ
		Arguments
			lhs -- lvalue of the expression (variable name)
			rhs -- rvalue of the expression
			convert -- Flag to enable automatic conversion
		"""
		result, lhs, rhs	= self.resolve_tuple(lhs, rhs)
		if result == False:
			return None
		return True if lhs!=rhs else False

	def resolve(self, expr):
		""" Resolve an expression
		Arguments
			expr -- Expression
		"""
		if isinstance(expr, SymbolType):
			expr	= expr.value

		if isinstance(expr, int) or isinstance(expr, float) or isinstance(expr, list):
			return expr

		return self.resolver.resolve(self, expr)

	def evaluate(self, method, args):
		""" Evaluates an API method
		Arguments
			method -- Method to call
			args -- Arguments to the method
		"""
		return self.api(self, method, args)

if __name__ == "__main__":
	test = Context()


