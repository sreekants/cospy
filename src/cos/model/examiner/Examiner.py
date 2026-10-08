#!/usr/bin/python
# Filename: Examiner.py
# Description: Base class for all rules

from cos.model.rule.Automata import Automata
from cos.model.rule.ScoreCard import ScoreCard
from cos.core.kernel.Faculty import Faculty
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList
from cos.model.examiner.Examination import Examination, ExaminationType, EXAMINATION

class Examiner(Faculty):
	def __init__(self, type):
		""" Constructor
		Arguments
			type -- Type of the object
		"""
		Faculty.__init__( self, self.category, type )

		self.automata		= None
		self.scorecard		= ScoreCard()
		self.examinations	= {}		# ExaminationType -> handler(ctxt, body)
		self.subscribe( EXAMINATION, self.on_examination )
		self.handle_examination( ExaminationType.EPOCH_EPISODE, self.on_epoch_episode )
		return

	@property
	def category(self):
		return 'Practice/Examiners'

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		# Set up before registering, so an examiner whose setup fails is never
		# reached by the rule evaluator half-initialized. BootLoader logs the error.
		config		= ArgList( module.get("config", "") )
		self.setup( ctxt, config )
		Faculty.on_init(self, ctxt, module)
		return

	def on_start(self, ctxt:Context, config:ArgList):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		return


	def handle_examination(self, type:ExaminationType, handler):
		""" Registers the handler for one type of examination
		Arguments
			type -- Examination type
			handler -- Callable(ctxt, body)
		"""
		if getattr( self, 'examinations', None ) is None:
			# Examiners built without __init__, e.g. in tests
			self.examinations	= { ExaminationType.EPOCH_EPISODE: self.on_epoch_episode }
		self.examinations[type]	= handler
		return

	def on_examination(self, ctxt:Context, examination:Examination):
		""" Examines what an examination carries; any other type is ignored
		Arguments
			ctxt -- Simulation context
			examination -- Examination received on a subscribed topic
		"""
		handler	= (getattr( self, 'examinations', None ) or {}).get( getattr(examination, 'type', None) )
		if handler is None:
			return

		# A failing examiner must not stop delivery to the others
		try:
			handler( ctxt, examination.body )
		except Exception as e:
			ctxt.log.error( self.id, f'{examination.type.name}: {e}' )
		return

	def on_epoch_episode(self, ctxt:Context, episode):
		""" Closes the examiner's own periods at the end of an epoch
		Arguments
			ctxt -- Simulation context
			episode -- Ended EpochEpisode
		"""
		self.end( ctxt, episode.context )
		return

	def end(self, ctxt:Context, rule_ctxt):
		""" Ends whatever the examiner keeps open across situations
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context of the pass that ended the epoch
		"""
		return

	# No score() here: examiners record through ZoneAware.violate() (REQ.017)

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

	def data(self, ctxt:Context, situation, values, context=None):
		""" Stores a score into the database
		Arguments
			ctxt -- Simulation context
			situation -- Name of the situation. An associated fact_{situation} table must exist in the database
			values -- A tuple of value for each field in the table
			context -- DataContext for the table's dimension columns (own ship, position)
		"""
		ctxt.sim.data.push(f'fact_{situation}', values, context)
		return

	def __load_scorecard(self, ctxt:Context, file)->Automata:
		""" Loads the scorecard from file
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
		""" Loads the automata from file
		Arguments
			ctxt -- Simulation context
			file -- File path
		""" 
		if file is None:
			return None

		# Resolve the path
		path	= ctxt.sim.config.resolve(file)
		lagata	= Automata(None)

		# Load the compiled legata file
		ctxt.log.info( self.id, f'Loading legata file : {file}' )
		lagata.load( path )
		lagata.dump()

		return lagata


if __name__ == "__main__":
	test = Examiner()


