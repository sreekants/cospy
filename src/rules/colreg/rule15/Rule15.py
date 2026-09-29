#!/usr/bin/python
# Filename: Rule15.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from maritime.model.rule.EncounterWatch import EncounterWatch
from maritime.core.situation.Types import Encounter
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

'''
Crossing Situation
When two power-driven vessels are crossing so as to involve risk of collision, the vessel which has the
other on her own starboard side shall keep out of the way and shall, if the circumstances of the case
admit, avoid crossing ahead of the other vessel.
'''

class Rule15(COLREG):
	RANGE	= 4000.0	# Metres within which an onset is recorded (evaluator.yaml r_colregs_2_max)
	DCPA	= 500.0		# Metres of predicted passing distance that is a risk of collision

	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)

		self.watch	= EncounterWatch( Encounter.CRGW, self.DCPA, self.RANGE )
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the rule and its crossing thresholds
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		COLREG.setup( self, ctxt, config )

		self.watch.dcpa		= float( config['encounter.dcpa'] or self.DCPA )
		self.watch.range	= float( config['encounter.range'] or self.RANGE )
		return

	def evaluate(self, ctxt:Context, rule_ctxt):
		""" Queues crossings in which own ship gives way, once past their closest approach, then judges them
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		self.watch.observe( ctxt, rule_ctxt, self )
		COLREG.evaluate( self, ctxt, rule_ctxt )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		COLREG.on_start(self, ctxt, config)

		self.subscribe("vessel.crossing", self.on_crossing)
		return

	def on_crossing(self, ctxt:Context, evt):
		""" Event handler for crossing
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		vessel	= evt[1]
		return


if __name__ == "__main__":
	test = Rule15()


