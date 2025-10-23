#!/usr/bin/python
# Filename: Symbol.py
# Description: Implementation of the symbolic types used in a decison

from enum import Enum
from abc import ABC, abstractmethod

class Type(Enum):
	"""Types of symbols."""
	NULL			= 0  # A named variable
	VARIABLE		= 1  # A named variable
	STRING			= 2
	FLOAT			= 3
	INTEGER			= 4
	LIST			= 5
	RANGE			= 6

	OPERATOR		= 100
	FUNCTION		= 300


class SymbolType(ABC):
	def __init__(self, type:Type, value):
		""" Constructor
		Arguments
			type -- Type of the object
			value -- Value of the symbol
		""" 
		self.value	= value
		return

	def __str__(self) -> str:
		""" TODO: __str__
		""" 
		return self.tostring()

	@abstractmethod
	def tostring(self) -> str:
		""" A string representation of the object
		"""
		pass

class Symbol:
	class Variable(SymbolType):
		def __init__(self, value:str):
			""" Constructor
			Arguments
				value -- Value of the symbol
			""" 
			SymbolType.__init__(self, Type.VARIABLE, value)
			return

		def tostring(self) -> str:
			""" TODO: tostring
			""" 
			return self.value


	class Float(SymbolType):
		def __init__(self, value:float):
			""" Constructor
			Arguments
				value -- Value of the symbol
			""" 
			SymbolType.__init__(self, Type.FLOAT, value)
			return

		def tostring(self) -> str:
			""" TODO: tostring
			""" 
			return str(self.value)

	class Integer(SymbolType):
		def __init__(self, value:int):
			""" Constructor
			Arguments
				value -- Value of the symbol
			""" 
			SymbolType.__init__(self, Type.INTEGER, value)
			return

		def tostring(self) -> str:
			""" TODO: tostring
			""" 
			return str(self.value)

	class String(SymbolType):
		def __init__(self, value:str):
			""" Constructor
			Arguments
				value -- Value of the symbol
			""" 
			SymbolType.__init__(self, Type.STRING, value)
			return

		def tostring(self) -> str:
			""" TODO: tostring
			""" 
			return f'\"{self.value}\"'


	class List(SymbolType):
		def __init__(self, args=None):
			""" Constructor
			Arguments
				args -- List of arguments
			""" 
			SymbolType.__init__(self, Type.LIST, [])
			if args is not None:
				for a in args:
					self.value.append(a)
			return

		def IN(self, value) -> bool:
			return True if (value in self.value) else False

		def tostring(self) -> str:
			""" TODO: tostring
			""" 
			parts   = [ str(p) for p in self.value ]
			return f"[{','.join(parts)}]"

		def append(self, arg):
			""" TODO: append
			Arguments
				arg -- TODO
			""" 
			self.value.append(arg)
			return self

	class Operator(SymbolType):
		def __init__(self, op):
			""" Constructor
			Arguments
				op -- TODO
			""" 
			SymbolType.__init__(self, Type.OPERATOR, op)
			return

		def tostring(self) -> str:
			""" TODO: tostring
			""" 
			return str(self.value)

		def evaluate(self, ctxt):
			""" Evaluates the expression
			Arguments
				ctxt -- Simulation context
			"""
			return self.value.evaluate(ctxt)


	class Range(SymbolType):
		def __init__(self, min, max):
			""" Constructor
			Arguments
				min -- TODO
				max -- TODO
			""" 
			SymbolType.__init__(self, Type.RANGE, (min,max) )
			return

		def IN(self, value) -> bool:
			return True if (self.value[0]<= value)  and (self.value[1]>= value) else False

		def BETWEEN(self, value) -> bool:
			return True if (self.value[0]< value)  and (self.value[1]> value) else False
		
		def tostring(self) -> str:
			""" TODO: tostring
			""" 
			return f'[{self.value[0]}:{self.value[1]}]'

	class Function(SymbolType):
		def __init__(self, name, args, evaluator):
			""" Constructor
			Arguments
				name -- Name of the object
				args -- List of arguments
				evaluator -- Evaluation handler
			""" 
			SymbolType.__init__(self, Type.FUNCTION, (name, args))
			self.eval	= evaluator
			return

		def tostring(self) -> str:
			""" TODO: tostring
			""" 
			argslist = [str(arg) for arg in self.value[1]]
			return f"{self.value[0]}({', '.join(argslist)})"
		
		def evaluate(self, ctxt):
			return self.eval(ctxt, self.value)

if __name__ == "__main__":
	test = SymbolType()

