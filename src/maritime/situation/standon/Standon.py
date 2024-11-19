#!/usr/bin/python
# Filename: Standon.py
# Description: Implementation of the Standon class

from maritime.core.situation.Maneuver import Maneuver
from maritime.core.situation.Types import Encounter as EncounterType
from cos.core.kernel.Context import Context

class Standon(Maneuver):
	def __init__(self):
		""" Constructor
		Arguments
			self -- reference to this instance
		"""
		Maneuver.__init__( self, 'STANDON', 'vessel.standon',
					[EncounterType.CRSO, EncounterType.OTSO]
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
	test = Standon("XXX")


