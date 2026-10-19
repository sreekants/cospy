#!/usr/bin/python
# Filename: ContainerShip.py
# Description: Implementation of the ContainerShip class

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior


# Specification: high momentum, slow heading, strict TSS lane compliance
class ContainerShip(PlannedVesselBehavior):
    def __init__(self, ctxt, config):
        PlannedVesselBehavior.__init__(self, ctxt, config)

        self.reverse    = False
        return



if __name__ == "__main__":
    test = ContainerShip(None, None)
