		#!/usr/bin/python
# Filename: Context.py
# Description: Implementation of the Context class

from cos.model.rule.Situation import Situation
from cos.lang.symbol.Symbol import Symbol, SymbolType
from cos.core.kernel.Context import Context as KernelContext

import fnmatch, math, statistics

# Unit functions convert to the base units terms resolve to: metres and metres per second
UNITS	= {
	'meters'	: 1.0,
	'miles'		: 1852.0,				# Nautical miles
	'feets'		: 0.3048,
	'knot'		: 1852.0 / 3600.0,
	'kmph'		: 1.0 / 3.6,
	'nmphtokmph': 1.852,
}

MATH	= {
	'abs'		: lambda args: abs( args[0] ),
	'min'		: lambda args: min( args ),
	'max'		: lambda args: max( args ),
	'floor'		: lambda args: math.floor( args[0] ),
	'mean'		: lambda args: statistics.mean( args ),
	'std'		: lambda args: statistics.pstdev( args ),
	'count'		: lambda args: len( args[0] ),
}

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
		self.subjects	= vessels			# Own-ship side of each pair: the vessels under test
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

		if isinstance(rhs, Symbol.Range) or isinstance(rhs, Symbol.AngularRange):
			return rhs.IN(lhs)

		if isinstance(rhs, list) == False:
			return True if lhs in rhs else False

		# Array elements arrive as unresolved symbols
		rhs		= [ self.resolve(x) if isinstance(x, SymbolType) else x for x in rhs ]

		# A set (e.g. an intent) matches when any of its members does
		values	= list(lhs) if isinstance(lhs, (list, tuple, set)) else [lhs]
		if match_all == False:
			return any( Context.match(v, r) for v in values for r in rhs )

		return all( any(Context.match(v, r) for r in rhs) for v in values )

	@staticmethod
	def match(value, pattern)->bool:
		""" Whether a value matches an array element, with shell wildcards for strings
		Arguments
			value -- Value from the subject
			pattern -- Array element
		"""
		if isinstance(value, str) and isinstance(pattern, str):
			return fnmatch.fnmatchcase( value, pattern )

		return value == pattern

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
		# Handle constants
		if isinstance(expr, Symbol.Float) or isinstance(expr, Symbol.Integer) or isinstance(expr, Symbol.String):
			return expr.value

		if isinstance(expr, Symbol.Range):
			return Symbol.Range(self.resolve(expr.value[0]), self.resolve(expr.value[1]))

		if isinstance(expr, Symbol.AngularRange):
			return Symbol.AngularRange(self.resolve(expr.value[0]), self.resolve(expr.value[1]))

		if isinstance(expr, Symbol.Function):
			return self.call( expr )

		if isinstance(expr, SymbolType):
			expr	= expr.value

		if isinstance(expr, int) or isinstance(expr, float) or isinstance(expr, list):
			return expr

		return self.resolver.resolve(self, expr)

	def call(self, function):
		""" Value of a unit or math function used as an operand, e.g. meters(20) or abs(x)
		Arguments
			function -- Symbol.Function
		Returns
			The value, or None when an argument does not resolve
		"""
		name, args	= function.value
		if (name not in UNITS) and (name not in MATH):
			return function.evaluate( self )

		values	= [ self.resolve(a) for a in (args or []) ]
		if any( v is None for v in values ):
			return None

		if (len( values ) != 1) and (name not in ('min', 'max', 'mean', 'std')):
			raise RuntimeError( f'{name}() takes one argument, got {len(values)}' )

		if name in UNITS:
			return float( values[0] ) * UNITS[name]

		return MATH[name]( values )

	def evaluate(self, method, args):
		""" Evaluates an API method
		Arguments
			method -- Method to call
			args -- Arguments to the method
		"""
		return self.api(self, method, args)

if __name__ == "__main__":
	test = Context()


