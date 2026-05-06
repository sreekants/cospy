#!/usr/bin/python
# Filename: ContainerShip.py
# Description: Implementation of the ContainerShip class

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from maritime.behavior.vessels.VesselManeuvers import VesselManeuvers


# Specification: high momentum, slow heading, strict TSS lane compliance
class ContainerShip(PlannedVesselBehavior):
    def __init__(self, ctxt, config):
        PlannedVesselBehavior.__init__(self, ctxt, config)

        # Sequence of behavior operations
        self.ops = [
    		# Container ships always obey TSS direction — hard correction, never violated.
            VesselManeuvers.tss_compliance,
            VesselManeuvers.overtaking_separation,
            VesselManeuvers.apply_momentum
        ]

        self.reverserun     = False
        return



if __name__ == "__main__":
    test = ContainerShip(None, None)
