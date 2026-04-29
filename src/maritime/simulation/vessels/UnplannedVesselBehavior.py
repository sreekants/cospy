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
		return


if __name__ == "__main__":
	test = UnplannedVesselBehavior(None, None)
