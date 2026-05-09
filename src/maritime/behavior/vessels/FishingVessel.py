#!/usr/bin/python
# Filename: FishingVessel.py
# Description: Implementation of the FishingVessel class

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from maritime.behavior.vessels.VesselManeuvers import VesselManeuvers
from maritime.model.vessel.Vessel import Vessel, Operation, Status

from math import atan2, cos, sin, degrees, radians
import numpy as np
import re

# Two operating modes per Specification

class FishingVessel(PlannedVesselBehavior):
    def __init__(self, ctxt, config):
        PlannedVesselBehavior.__init__(self, ctxt, config)
                
        # Sequence of behavior operations
        self.ops = [
            # VesselManeuvers.tss_avoidance,
            VesselManeuvers.overtaking_distance,
            VesselManeuvers.apply_momentum,

            VesselManeuvers.fishing_slowdown
        ]

        self.postops = [
            VesselManeuvers.restore_speed
        ]

        self.reverse    = True
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

    def on_at_waypoint(self, world, t, n, pt):
        if len(pt[3]):
            activity  = pt[3].split('(')

            match activity[0]:
                case 'fishing':
                    args  = re.search(r'\((.*)\)', pt[3])
                    if args is not None:
                        # Push the plan
                        self.push()


                        # Plan a random walk
                        path        = []
                        args        = args[1].split('|')
                        
                        nways       = int(args[0])
                        dist        = float(args[1])
                        sog         = float(args[2])

                        PlannedVesselBehavior.random_walk( path, dist, self.position, nways, sog )
                        self.plan( path )
                        return

            
        PlannedVesselBehavior.on_at_waypoint(self, world, t, n, pt)
        return


if __name__ == "__main__":
    test = FishingVessel(None, None)
