#!/usr/bin/python
# Filename: FishingVessel.py
# Description: Implementation of the FishingVessel class

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from maritime.model.vessel.Vessel import Vessel, Operation, Status

from math import atan2, cos, sin, degrees, radians
import numpy as np
import re

# Two operating modes per Specification

class FishingVessel(PlannedVesselBehavior):
    def __init__(self, ctxt, config):
        PlannedVesselBehavior.__init__(self, ctxt, config)

        self.fishing_trip   = False     # A fishing(...) trip action is running
        self.fishing_ioctl  = False     # ioctl('operation.fishing') is in effect

        self.reverse    = True
        return

    def update_mode(self):
        """ Fishing while a fishing trip action runs or the fishing ioctl is in effect, else transport
        """
        self.mode   = Operation.FISHING if (self.fishing_trip or self.fishing_ioctl) else Operation.TRANSPORT
        return

    @staticmethod
    def declare_operation(b, world, t, dx):
        """ Sets the vessel's operation from the behaviour's mode, so the rules and signals read it
        Arguments
            b -- Vessel behaviour
            world -- Reference ot the simulation world
            t -- Time on the simulation clock
            dx -- Velocity the behaviour has set
        """
        b.vehicle.operation = b.mode
        return dx

    def ioctl(self, op, arg):
        """Switch between TRANSPORT and FISHING modes at runtime."""

        if op == 'operation.fishing':
            self.fishing_ioctl  = True
            self.update_mode()
            return True
        elif op == 'operation.transport':
            self.fishing_ioctl  = False
            self.update_mode()
            return True

        return PlannedVesselBehavior.ioctl(self, op, arg)

    def on_end_path(self, world, t, n, pt):
        """ Ends a fishing trip action when its random walk is done and the trip resumes
        Arguments
            world -- Reference ot the simulation world
            t -- Time on the simulation clock
            n -- Waypoint index
            pt -- Waypoint
        """
        resumed = PlannedVesselBehavior.on_end_path(self, world, t, n, pt)
        if resumed and self.fishing_trip:
            self.fishing_trip   = False
            self.update_mode()
        return resumed

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
                        # Trip actions are authored in map units; the simulation runs in metres
                        dist        = world.scales.length( float(args[1]) )
                        sog         = world.scales.length( float(args[2]) )

                        PlannedVesselBehavior.random_walk( path, dist, self.position, nways, sog )
                        self.plan( path )
                        self.fishing_trip   = True
                        self.update_mode()
                        return

            
        PlannedVesselBehavior.on_at_waypoint(self, world, t, n, pt)
        return


if __name__ == "__main__":
    test = FishingVessel(None, None)
