#!/usr/bin/python
# Filename: FishingVessel.py
# Description: Implementation of the FishingVessel class

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from maritime.behavior.vessels.VesselManeuvers import VesselManeuvers
from maritime.model.vessel.Vessel import Vessel, Operation, Status

from math import atan2, cos, sin, degrees, radians
import numpy as np

# Two operating modes per Specification

class FishingVessel(PlannedVesselBehavior):
    def __init__(self, ctxt, config):
        PlannedVesselBehavior.__init__(self, ctxt, config)
                
        # Sequence of behavior operations
        self.ops = [
            VesselManeuvers.tss_avoidance,
            VesselManeuvers.overtaking_separation,
            VesselManeuvers.apply_momentum,

            VesselManeuvers.fishing_slowdown
        ]

        self.postops = [
            VesselManeuvers.restore_speed
        ]

        self.reverserun     = True
        return

    def ioctl(self, op, arg):
        """Switch between TRANSPORT and FISHING modes at runtime."""

        if op == 'operation.fishing':
            self.mode   = Operation.FISHING
            return True
        elif op == 'operation.transport':
            self.mode   = Operation.TRANSPORT
            return True

        return PlannedVesselBehavior.ioctl(self, op, arg)

    def on_waypoint(self, world, t, n, pt):
        # Push the plan
        self.push()


        # Plan a random walk
        path        = []
        nways       = 5 
        dist        = 5
        
        self.plan( PlannedVesselBehavior.random_walk(path, dist, self.position, nways) )
        
        return


if __name__ == "__main__":
    test = FishingVessel(None, None)
