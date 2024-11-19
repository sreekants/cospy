#!/usr/bin/python
# Filename: Overtaking.py
# Description: Implementation of the Overtaking class

from maritime.core.situation.Maneuver import Maneuver
from maritime.core.situation.Types import Encounter as EncounterType
from cos.core.kernel.Context import Context

class Overtaking(Maneuver):
	def __init__(self):
		""" Constructor
		Arguments
			"""
		Maneuver.__init__( self, 'OVERTAKING', 'vessel.overtaking',
					[EncounterType.OTGW, EncounterType.OTSO]
					  )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.setup(ctxt, config)
		return

	def setup(self, ctxt:Context, config):
		""" Sets up the parameters of the situation
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Overridable implementation
		self.range	= 10.0
		return


if __name__ == "__main__":
	test = Overtaking("XXX")


