#!/usr/bin/python
# Filename: Motorboat.py
# Description: Implementation of the Motorboat class

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from maritime.behavior.vessels.VesselManeuvers import VesselManeuvers

import numpy as np


# Specification: Recreational — no path following, high momentum (preserves speed),
class Motorboat(PlannedVesselBehavior):
    def __init__(self, ctxt, config):
        PlannedVesselBehavior.__init__(self, ctxt, config)

        # Sequence of behavior operations
        self.ops = [
            VesselManeuvers.tss_compliance,
            VesselManeuvers.overtaking_separation,
            VesselManeuvers.apply_momentum,
            
            VesselManeuvers.crossing_slowdown
        ]

        self.postops = [
            VesselManeuvers.restore_speed
        ]

        self.reverserun     = True
        return



if __name__ == "__main__":
    test = Motorboat(None, None)
