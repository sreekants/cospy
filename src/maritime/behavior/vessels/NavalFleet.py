#!/usr/bin/python
# Filename: NavalFleet.py
# Description: Implementation of the NavalFleet class

from cos.behavior.motion.PreyBehavior import PreyBehavior

class NavalFleet(PreyBehavior):
	def __init__(self, ctxt, config):
		PreyBehavior.__init__(self, ctxt, config)
		return

		

if __name__ == "__main__":
	test = NavalFleet()

