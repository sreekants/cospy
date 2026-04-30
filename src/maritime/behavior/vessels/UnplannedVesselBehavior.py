#!/usr/bin/python
# Filename: VesselBehavior.py
# Description: Implementation of the VesselBehavior class

from cos.behavior.motion.BrownianMotionBehavior import BrownianMotionBehavior
from cos.behavior.motion.VesselModel import VesselModel
from maritime.navigation.cartography.Map import Map
from math import atan2, cos, sin, degrees, radians

import numpy as np


class UnplannedVesselBehavior(BrownianMotionBehavior):
	def __init__(self, ctxt, config):
		BrownianMotionBehavior.__init__(self, ctxt, config)
		self._map = Map(ctxt)
		self.model	= VesselModel()

		# Load the ship model
		args		= self.get_settings( config )
		if ('ship.model' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load_model( ctxt, ctxt.sim.config.resolve(args['ship.model']) )

		return

	def load_model(self, ctxt, filename):
		""" Loads a simulation model
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""

		self.model.load(self._get_file(ctxt, filename))
		return

	def _get_file(self, ctxt, filename):
		""" Returns the content of a simulation file
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""
		if ctxt is None:
			return open(filename, 'r').read()

		return ctxt.sim.fs.read_file_as_bytes(filename)

if __name__ == "__main__":
	test = UnplannedVesselBehavior(None, None)
