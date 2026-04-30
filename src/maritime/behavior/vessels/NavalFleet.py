#!/usr/bin/python
# Filename: NavalFleet.py
# Description: Implementation of the NavalFleet class

from cos.behavior.motion.FleetBehavior import FleetBehavior

class NavalFleet(FleetBehavior):
	def __init__(self, ctxt, config):
		FleetBehavior.__init__(self, ctxt, config)
		return

		

if __name__ == "__main__":
	test = NavalFleet()

