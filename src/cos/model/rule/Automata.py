#!/usr/bin/python
# Filename: Automata.py
# Description: Impelementation of a rule automata

from cos.model.rule.Context import Context
from cos.lang.legata.Definition import Definition
from cos.lang.legata.Parser import Parser
from cos.lang.logic.Decision import Decision
from cos.lang.logic.DecisionTree import DecisionTree, DecisionType
from cos.core.utilities.Errors import ErrorCode

import os, sys, pickle

class Automata:
	def __init__(self, rule):
		""" Constructor
		Arguments
			rule -- TODO
		""" 
		self.rule		= rule
		self.definition	= Definition()

		self.parser 	= Parser(self, Automata.__evaluate)
		self.parser.build()
		return

	def begin(self, ctxt:Context):
		""" Triggers the begining of a situation
		Arguments
			ctxt -- Simulation context
		"""
		result		= self.definition.traverse( self.__init_node, ctxt, 1 )
		return result

	def evaluate(self, ctxt:Context ):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		""" 
		return self.definition.evaluate(ctxt)


	def compile(self, file:str):
		""" Compiles a file
		Arguments
			file -- File path
		""" 
		with open(file, 'rt') as f:
			codepage = f.read()
			self.parser.parse(codepage, file)
		return

	def load(self, file:str):
		""" Loads the automata from a file
		Arguments
			file -- File path
		""" 
		if file.endswith('.legata'):
			self.compile( file )
			return

		if file.endswith('.lbo'):
			with open(file, 'rb') as fp:
				# TODO: Pickling for simplicity. But the protocol is
				# not necessarily portable or safe
				self.definition	= pickle.load(fp)
				return

		raise Exception( f'Unsupported Legata file format.')

	def save(self, file):
		""" Saves the automata to a binary file
		Arguments
			file -- File path
		""" 
		if file.endswith('.lbo') == False:
			file	+= '.lbo'

		with open(file, 'wb') as fp:
			pickle.dump(self.definition, fp, protocol=pickle.DEFAULT_PROTOCOL)
		return

	def dump(self, args:map=None):
		""" Dumps the automata information to the screen
		""" 
		
		if args is None:
			args	= {'definitions':True}
		
		result	= {}

		if args.get('definitions', False) == True:
			result['definitions'] 	= []
			self.definition.traverse( Automata.__append_node, result['definitions'] )

		return result

	@staticmethod
	def __append_node( result:list, node:Decision ):
		""" Internal callback function to handle dumping a tree node
		Arguments
			ctxt -- Context argument passed to the callback
			node -- Node to process
		"""
		try:
			indent	= ' '*(node.level-1)
			if node.name != 'def':
				result.append( f'{indent}{node.name}' )
				return ErrorCode.ERROR_CONTINUE

			Automata.__append_scope( result, indent, 
						   node.conditions,
						   node.exceptions, 
						   node.assurances )
		except Exception as e:
			print( f'Error transcribing node [{node.path}]: {str(e)}')
		return ErrorCode.ERROR_CONTINUE

	@staticmethod
	def __append_scope( result:list, indent, conditions, exceptions, assurances ):
		for condition in conditions:
			result.append( f'{indent}condition: {Automata.__exprtxt(condition)}' )

		if exceptions is not None:
			for exception in exceptions:
				result.append( f'{indent}condition: {Automata.__exprtxt(exception)}' )

		Automata.__append_actions(result, indent, assurances)
		return

	@staticmethod
	def __append_actions( result:list, indent, actions ):
		try:
			for action in actions:
				opcode	=  action[0][0]
				match opcode:
					case '^':
						result.append( f'{indent} assure: {action[0][1][1]}()' )
					case '?':
						expression	= action[0][1][1]
						result.append( f'{indent} assure: {Automata.__exprtxt(expression[0][1])}' )
					case '*':
						function	= action[0][1][1]
						result.append( f'{indent} assure: {Automata.__fntxt(function)}' )
					case '!':
						apply	= action[0][1]
						result.append( f'{indent} assure: apply {apply}' )
					case '%':
						# TODO: Convert a subclause to an object
						clause	= action[0][1][1]
						result.append( f'{indent} assure: clause [' )
						Automata.__append_clause(result, indent+' ', clause)
						result.append( f'{indent} ]' )
					case _:
						raise RuntimeError( f'Unsupported action type [{opcode}] in [{action[0]}].' )
		except Exception as e:
			raise e
		return

	@staticmethod
	def __append_clause(result:list, indent, clause):
		""" Prints a set of clause
		Arguments
		    indent to construct the clause
			clause -- Clause to the print
		""" 
		Automata.__append_scope( result, indent, 
						clause["conditions"],
						clause["exclusions"], 
						clause["assurances"] )

		return


	@staticmethod
	def __fntxt(expr):
		""" Prings a function
		Arguments
			statements -- TODO
		""" 
		return str(expr)


	@staticmethod
	def __exprtxt(statements):
		""" Prints a set of statements
		Arguments
			statements -- Statements to the print
		""" 
		exprlist	= []
		for s in statements:
			expr	= s[1]
			exprlist.append(str(expr))
		return ' & '.join(exprlist)


	def generate(self, components):
		""" Generates the components of the automata
		Arguments
			components -- Dictionary of components to generate
		""" 

		for c in components['conditions']:
			self.__add_conditions(c)

		for c in components['clauses']:
			self.__add_clause(c)

		for c in components['precedents']:
			self.__add_precedent(c)


		return

	def __add_conditions(self, condition):
		""" Adds a condition to t
		Arguments
			condition -- TODO
		""" 
		# print(f"Generating conditions {condition}...")
		return

	def __add_clause(self, clause):
		""" Adds a close to the list
		Arguments
			clause -- TODO
		""" 
		location	= clause['location']
		try:
			name		= Decision(clause['name'], None, DecisionType.TYPE_BASIC_CONDITION)
			decision	= self.definition.add( '/', name)
			# print(f"{clause['location']} Generating clause {name}...")
			for d in clause['definition']:
				define	= decision.add( Decision('def', None, DecisionType.TYPE_BASIC_DECISION) )
				self.__add_clause_conditions(clause, define, d['conditions'])
				self.__add_clause_assurances(clause, define, d['assurances'])

		except Exception as e:
			print( f'{location} {str(e)}')
			sys.exit(-1)
		return

	def __add_clause_conditions(self, clause, define, conditions):
		""" TODO: __add_clause_conditions
		Arguments
			clause -- TODO
			define -- TODO
			conditions -- TODO
		""" 
		match len(conditions):
			case 0:
				return

			case 1:
				define.IF(conditions[0])
				return

		expr	= conditions[1][0]
		for c in conditions:
			# print(f'condition: {c}')
			define.IF(c)
		return

	def __add_clause_assurances(self, clause, define, assurances):
		""" TODO: __add_clause_assurances
		Arguments
			clause -- TODO
			define -- TODO
			assurances -- TODO
		""" 
		for a in assurances:
			# print(f'assure: {a}')
			define.ASSURE(a)
		return

	def __add_precedent(self, precedent):
		""" TODO: __add_precedents
		Arguments
			clause -- TODO
			define -- TODO
			assurances -- TODO
		""" 
		location	= precedent['location']
		try:
			name		= Decision(precedent['name'], None, DecisionType.TYPE_BASIC_PRECONDITION)
			decision	= self.definition.add( '/', name)
			# print(f"{clause['location']} Generating clause {name}...")
			for d in precedent['definition']:
				define	= decision.add( Decision('def', None, DecisionType.TYPE_BASIC_DECISION) )
				self.__add_clause_conditions(precedent, define, d['conditions'])
				self.__add_clause_assurances(precedent, define, d['assurances'])

		except Exception as e:
			print( f'{location} {str(e)}')
			sys.exit(-1)
		return

	@staticmethod
	def __init_node( ctxt:Context, node:Decision ):
		""" Internal callback function to handle dumping a tree node
		Arguments
			ctxt -- Context argument passed to the callback
			node -- Node to process
		"""
		if node.type != DecisionType.TYPE_BASIC_PRECONDITION:
			return ErrorCode.ERROR_CONTINUE
		
		return DecisionTree.evaluate_node( ctxt, node)

	@staticmethod
	def __evaluate( ctxt, ast ):
		return ctxt.evaluate( ast[0], ast[1] )

	@property
	def symbols(self):
		""" Returns the symbols in the current parse
		"""
		return self.parser.terms
	
if __name__ == "__main__":
	test = Automata(None)
	test.compile("E:\\users\\ntnu\\cospy\\config\\maritime\\regulation\\colreg\\test.legata")
	test.dump()

