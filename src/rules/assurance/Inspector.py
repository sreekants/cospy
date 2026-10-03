#!/usr/bin/python
# Filename: Inspector.py
# Description: Base class for inspectors, the higher-level faculties examiners report to

from cos.model.rule.ScoreCard import ScoreCard
from cos.core.kernel.Faculty import Faculty
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

INSPECTORS	= '/Faculty/Practice/Inspectors'
EXAMINERS	= '/Faculty/Practice/Examiners'


class Inspector(Faculty):
	def __init__(self, type):
		""" Constructor
		Arguments
			type -- Name of the inspector, e.g. 'Test' for /Faculty/Practice/Inspectors/Test
		"""
		Faculty.__init__( self, self.category, type )

		self.scorecard	= ScoreCard()
		return

	@property
	def category(self):
		return 'Practice/Inspectors'

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		config		= ArgList( module.get("config", "") )
		self.setup( ctxt, config )
		Faculty.on_init(self, ctxt, module)
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the inspector, loading its scorecard when one is configured
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		file	= config["scorecard"]
		if file is None:
			self.scorecard.reset()
			return

		self.scorecard.load( ctxt, ctxt.sim.config.resolve_path(file) )
		return

	def begin(self, ctxt:Context, rule_ctxt):
		""" Starts a pass
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		return

	def evaluate(self, ctxt:Context, rule_ctxt):
		""" Runs a pass; messages from examiners arrive on the inspector's IPC topic
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		return

	def end(self, ctxt:Context, rule_ctxt):
		""" Ends a pass
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		return

	@staticmethod
	def examiner(ctxt:Context, id:str):
		""" An examiner loaded in the simulation, e.g. to read its scorecard
		Arguments
			ctxt -- Simulation context
			id -- Examiner id, its class name unless configured otherwise
		Returns
			The examiner, or None when none is loaded under that id
		"""
		return ctxt.sim.objects.find( EXAMINERS, id )


if __name__ == "__main__":
	test = Inspector( 'Inspector' )
