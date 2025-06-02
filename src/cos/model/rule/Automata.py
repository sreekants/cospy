#!/usr/bin/python
# Filename: Automata.py
# Description: Impelementation of a rule automata

from cos.model.rule.Definition import Definition
from cos.model.rule.Context import Context
from cos.model.rule.Parser import Parser
from cos.model.logic.Decision import Decision
from cos.model.logic.DecisionTree import DecisionTree, DecisionType
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

	def dump(self, args:map):
		""" Dumps the automata information to the screen
		""" 

		if args.get('definitions', False) == True:
			self.definition
			result = []
			self.definition.traverse( Automata.__append_node, result )
			print( '\n'.join(result) )

		return

	@staticmethod
	def __append_node( result:list, node:Decision ):
		""" Internal callback function to handle dumping a tree node
		Arguments
			ctxt -- Context argument passed to the callback
			node -- Node to process
		"""
		indent	= ' '*(node.level-1)
		if node.name != 'def':
			result.append( f'{indent}{node.name}' )
			return ErrorCode.ERROR_CONTINUE

		for statements in node.conditions:
			result.append( f'{indent}condition: {Automata.__exprtxt(statements)}' )

		Automata.__append_actions(result, indent, node.assurances)
		return ErrorCode.ERROR_CONTINUE

	@staticmethod
	def __append_actions( result:list, indent, actions ):
		for action in actions:
			result.append( Automata.__append_action(list, indent, action) )
		return

	@staticmethod
	def __append_action( result:list, indent, action ):
		part	= action[0]
		opcode	= part[0]
		match opcode:
			case '^':
				return f'{indent} assure: {action[0][1][1]}()'
			case '?':
				statements	= action[0][1][1]
				return f'{indent} assure: {Automata.__exprtxt(statements[0][1])}'
			case '*':
				statements	= action[0][1][1]
				return f'{indent} assure: {Automata.__fntxt(statements)}'
			case '!':
				statements	= action[0][1][1]
				return f'{indent} assure: apply {action[0][1]}'
			case '{':
				return f'{indent} assure: {Automata.__clause_to_text(result, indent, part[1][1])}'
			case _:
				raise RuntimeError( f'Unsupported action type [{opcode}] in [{action[0]}].' )
		return

	@staticmethod
	def __clause_to_text(result, indent, clause):
		return 'CLAUSE'
	
	@staticmethod
	def __fntxt(expr):
		""" TODO: __exprtxt
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
	test = Automata()

