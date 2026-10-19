#!/usr/bin/python
# Filename: Yacht.py
# Description: Implementation of the Yacht class

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from cos.behavior.motion.PathFollowingMotionBehavior import PathFollowingMotionBehavior

import numpy as np
import random


# Specification: no path following, high momentum (preserves speed),
# fast heading (large direction changes allowed), stays outside TSS.
# When crossing to the other side, uses the same clearances as Ferry.
class Yacht(PlannedVesselBehavior):
    def __init__(self, ctxt, config):
        PlannedVesselBehavior.__init__(self, ctxt, config)

        return


    def on_watch_course(self, ctxt):
        PlannedVesselBehavior.on_watch_course(self, ctxt)
        return

        
if __name__ == "__main__":
    test = Yacht(None, None)
