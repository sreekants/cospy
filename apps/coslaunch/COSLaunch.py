#!/usr/bin/python
# Filename: COSLaunch.py
# Description: Implementation of COSLaunch application

from cos.core.simulation.Simulation import Simulation
from os import environ

class COSLaunch:
	def __init__(self):
		self.sim = Simulation.instance()
		return

	def run(self, args, appinfo, settings):
		# Hide pygame preamble
		environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

		self.sim.start( settings )
		input("Press Enter to exit...\n")
		self.sim.stop()
		return
		
		

if __name__ == "__main__":
    test = COSLaunch()

