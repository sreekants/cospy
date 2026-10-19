#!/usr/bin/python
# Filename: Motorboat.py
# Description: Implementation of the Motorboat class

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior

import numpy as np


# Specification: Recreational — no path following, high momentum (preserves speed),
class Motorboat(PlannedVesselBehavior):
    def __init__(self, ctxt, config):
        PlannedVesselBehavior.__init__(self, ctxt, config)

        self.reverse    = True
        return



if __name__ == "__main__":
    test = Motorboat(None, None)
