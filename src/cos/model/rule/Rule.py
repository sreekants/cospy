#!/usr/bin/python
# Filename: Rule.py
# Description: Base class for all rules

from cos.model.rule.Automata import Automata
from cos.model.rule.ScoreCard import ScoreCard
from cos.core.kernel.Faculty import Faculty
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

class Rule(Faculty):
	def __init__(self, type):
		""" Constructor
		Arguments
			type -- Type of the object
		"""
		Faculty.__init__( self, self.category, type )

		self.automata	= None
		self.scorecard	= ScoreCard()
		return

	@property
	def category(self):
		return 'Regulation/Rules'

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		Faculty.on_init(self, ctxt, module)
		config		= ArgList( module.get("config", "") )
		self.setup( ctxt, config )
		return

	def on_start(self, ctxt:Context, config:ArgList):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		return


	def begin(self, ctxt:Context, situation):
		""" Triggers the begining of a sutuation
		Arguments
			ctxt -- Simulation context
			situation -- Situation reference
		"""
		# print( f'begin {self.scope}/{self.id}' )
		return

	def end(self, ctxt:Context, situation):
		""" Triggers the conclusion of a situation
		Arguments
			ctxt -- Simulation context
			situation -- Situation reference
		"""
		# print( f'end {self.scope}/{self.id}' )
		# self.score(ctxt, situation, 'TODO')
		return

	def evaluate(self, ctxt:Context, situation):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			situation -- Situation reference
		"""
		# print( f'evaluate {self.scope}/{self.id}' )
		return

	def score(self, ctxt:Context, situation, event:str):
		""" Scores the rule
		Arguments
			ctxt -- Simulation context
			situation -- Situation reference
		"""
		# print( f'score {self.scope}' )
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the rule, loading its configurations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Overridable implementation
		self.automata	= self.__load_automata( ctxt, config["automata"] )


		self.__load_scorecard( ctxt, config["scorecard"] )
		return

	def data(self, ctxt:Context, situation, values):
		""" Stores a score into the database
		Arguments
			ctxt -- Simulation context
			situation -- Name of the situation. An associated fact_{situation} table must exist in the database
			values -- A tuple of value for each field in the table
		"""
		ctxt.sim.data.push(f'fact_{situation}', values)
		return

	def __load_scorecard(self, ctxt:Context, file)->Automata:
		""" TODO: __load_automata
		Arguments
			ctxt -- Simulation context
			file -- File path
		""" 
		if file is None:
			self.scorecard.reset()
			return
		
		self.scorecard.load(ctxt, ctxt.sim.config.resolve_path(file))
		return
	
	def __load_automata(self, ctxt:Context, file)->Automata:
		""" TODO: __load_automata
		Arguments
			ctxt -- Simulation context
			file -- File path
		""" 
		if file is None:
			return None

		# Resolve the path
		path	= ctxt.sim.config.resolve(file)
		lagata	= Automata(None)

		# Load and compiled legata file
		ctxt.log.info( self.id, f'Loading legata file : {file}' )
		lagata.load( path )
		# lagata.dump()

		return lagata


if __name__ == "__main__":
	test = Rule()


