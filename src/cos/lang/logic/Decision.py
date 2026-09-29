#!/usr/bin/python
# Filename: Decision.py
# Description: Base class for an decision

from cos.lang.logic.Exception import Exception
from cos.lang.logic.Assurance import Assurance
from cos.lang.logic.Expression import Expression
from cos.core.utilities.Errors import ErrorCode
from cos.core.utilities.Tree import TreeNode

from enum import Flag

class DecisionType(Flag):
	TYPE_NULL_OBJECT				= 0x00000000

	TYPE_ROOT_DECISION				= 0x00010000  # Root node of a Decision
	TYPE_BASIC_DECISION				= 0x00000010  # Basic type of Decision
	TYPE_BASIC_CONDITION			= 0x00010010  # Basic condition type
	TYPE_BASIC_PRECONDITION			= 0x00020010  # Basic pre-condition type 
	TYPE_BASIC_POSTCONDITION		= 0x00020010  # Basic post-condition type

class Decision(TreeNode):
	def __init__(self, name:str=None, parent=None, type=DecisionType.TYPE_NULL_OBJECT, ref=None):
		""" Constructor
		Arguments
			name -- Name of the object
			parent -- Parent decision node
			type -- Type of the object
			ref -- Opaque context reference
		"""
		TreeNode.__init__(self, name, parent)
		self.conditions	= []
		self.exceptions	= []
		self.assurances	= []
		self.precedents	= []
		self.trace		= False
		self.type		= type
		self.ref		= ref
		return

	def apply(self, ctxt):
		""" Applies a rule in the decision tree
		Arguments
			ctxt -- Simulation context
		"""
		# Check if any conditions apply; if not, the decision cannot be applied
		if len(self.conditions) == 0:
			condition	= None
		else:
			condition	= self.is_any(ctxt.ctxt, self.conditions)
			if condition is not None:
				if self.trace == True:
					ctxt.ctxt.ctxt.log.trace( 'Logic', f'Applying {self.parent} = {condition}')

				# An exclusion that holds takes the decision out of scope
				if self.is_any(ctxt.ctxt, self.exceptions) is not None:
					return ErrorCode.S_OK

		# Apply all the assurances on the children
		result = self.traverse( Decision.__apply_child, ctxt, 8 )

		if result not in [ErrorCode.S_OK, ErrorCode.S_TRUE, ErrorCode.ERROR_CONTINUE]:
			return result

		if condition is not None:
			# Apply all assurances.
			for assureinfo in self.assurances:
				result = self.__evaluate( ctxt, assureinfo )
				if result not in [ErrorCode.S_OK, ErrorCode.S_TRUE, ErrorCode.ERROR_CONTINUE]:
					# print( f'Assurance failed for decision {self.path}' )
					ctxt.error.append(self)
					return ErrorCode.ERROR_EXCEPTION_IN_SERVICE

		return ErrorCode.S_OK


	def is_any(self, ctxt, expressions):
		""" Checks if any expression is satisfied.
		Arguments
			ctxt -- Simulation context
			expressions -- Expression to evaluate
		"""
		for expinfo in expressions:
			c	= expinfo[0][1]
			result = Decision.evaluate_terms(ctxt, expinfo)
			if result in [ErrorCode.S_OK, ErrorCode.S_TRUE]:
				return c

			if result in [ErrorCode.S_FALSE, ErrorCode.ERROR_CONTINUE]:
				continue

			return None

		return None

	def __evaluate(self, ctxt, assureinfo):
		a	= assureinfo[0][1]
		t   = a[0]
		e	= a[1]

		# TODO: Simplify evaluation logic with polymorphism
		match t:
			case 'function':
				return e.evaluate(ctxt.ctxt)
			
			case 'expression':
				return Decision.evaluate_terms(ctxt.ctxt, e)
		
		if self.trace == True:
			print(f'Evaluating {self.name} assurance expressions:')
		return ErrorCode.S_OK

	@staticmethod
	def evaluate_terms(ctxt, terms):
		""" Evaluates terms as the parser folds them, e.g. [('?', a), ('AND', b)], left to right
		Arguments
			ctxt -- Simulation context
			terms -- (operator, term) pairs; a term is an expression or a nested list of pairs
		Returns
			S_TRUE, S_FALSE, or ERROR_CONTINUE when undecided
		"""
		result	= None
		for operator, term in terms:
			if ((operator == 'AND') and (result is False)) or ((operator == 'OR') and (result is True)):
				continue

			value	= Decision.evaluate_terms(ctxt, term) if isinstance(term, list) else term.evaluate(ctxt)
			value	= { ErrorCode.S_TRUE: True, ErrorCode.S_FALSE: False }.get( value )

			if operator == 'AND':
				result	= False if (value is False) else (None if (result is None) or (value is None) else True)
			elif operator == 'OR':
				result	= True if (value is True) else (None if (result is None) or (value is None) else False)
			else:
				result	= value

		return { True: ErrorCode.S_TRUE, False: ErrorCode.S_FALSE }.get( result, ErrorCode.ERROR_CONTINUE )

	def IF(self, expression):
		""" Adds a condition.
		Arguments
			expression -- Expression to evaluate
		"""
		self.conditions.append(expression)
		return

	def ASSURE(self, expression):
		""" Adds an assurance.
		Arguments
			expression -- Expression to evaluate
		"""
		self.assurances.append(expression)
		return

	def PRECEDENT(self, expression):
		""" Adds a precedent.
		Arguments
			expression -- Expression to evaluate
		"""
		self.precedents.append(expression)
		return

	def EXCEPT(self, expression):
		""" Adds an exception.
		Arguments
			expression -- Expression to evaluate
		"""
		self.exceptions.append(expression)
		return

	@staticmethod
	def __apply_child(ctxt, node:TreeNode):
		""" Internal method to evaluate a child node in a decision tree
		Arguments
			node -- Child node to evaluate
			ctxt -- Simulation context
		"""
		level	= node.level
		result	= node.apply(ctxt)

		# TODO: How to deal with result? Verify.
		if result in [ErrorCode.S_OK, ErrorCode.S_TRUE, ErrorCode.S_FALSE, ErrorCode.ERROR_CONTINUE]:
			return ErrorCode.ERROR_CONTINUE

		return result

	def __str__(self) -> str:
		""" TODO: __str__
		""" 
		return self.path

if __name__ == "__main__":
	test = Decision()


