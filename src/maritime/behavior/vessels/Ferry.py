#!/usr/bin/python
# Filename: Ferry.py
# Description: Implementation of the Ferry class

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior


# Specification: medium momentum, fast heading, crosses TSS perpendicularly.
# Ferry does NOT obey TSS lane direction — it arranges its own timing to cross.
class Ferry(PlannedVesselBehavior):
    def __init__(self, ctxt, config):
        PlannedVesselBehavior.__init__(self, ctxt, config)

        self.reverse    = True
        return
    

if __name__ == "__main__":
    test = Ferry(None, None)
