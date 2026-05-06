#!/usr/bin/python
# Filename: Yacht.py
# Description: Implementation of the Yacht class

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from maritime.behavior.vessels.VesselManeuvers import VesselManeuvers

import numpy as np


# Specification: no path following, high momentum (preserves speed),
# fast heading (large direction changes allowed), stays outside TSS.
# When crossing to the other side, uses the same clearances as Ferry.
class Yacht(PlannedVesselBehavior):
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
            VesselManeuvers.restore_speed,      # Restore speed after slowdown
            #VesselManeuvers.raise_anchor        # Raise anchor on timeout
        ]

        self.reverserun     = True
        self.anchor_time    = 0.5
        return


    def on_waypoint(self, world, t, n, pt):
        self.anchor( self.anchor_time )
        return

    def randomize_direction(self):
        """Fast heading: large turns allowed. High momentum: speed magnitude preserved."""
        speed = np.linalg.norm(self.dx)
        super().randomize_direction()
        new_speed = np.linalg.norm(self.dx)
        if speed > 0 and new_speed > 0:
            self.dx = self.dx * (speed / new_speed)

        return


if __name__ == "__main__":
    test = Yacht(None, None)
