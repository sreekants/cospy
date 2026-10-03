#!/usr/bin/python
# Filename: AnchoredVessel.py
# Description: A vessel lying at anchor: it holds its position and reports itself anchored

from cos.behavior.motion.LinearMotionBehavior import LinearMotionBehavior

import numpy as np


class AnchoredVessel(LinearMotionBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		LinearMotionBehavior.__init__(self, ctxt, config)

		self.dx			= np.zeros(3)
		self.d2x		= np.zeros(3)
		self.entropy	= 0
		return

	def move(self, world, t, config):
		""" Holds position; the status is set here because Vessel.__init__ resets it after the behaviours are built
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			config -- Configuration attributes
		"""
		vehicle	= getattr( self, 'vehicle', None )
		if (vehicle is not None) and hasattr( vehicle, 'anchored' ):
			vehicle.anchored()

		self.dx	= np.zeros(3)
		return self.rect, self.dx


if __name__ == "__main__":
	test = AnchoredVessel( None, None )
