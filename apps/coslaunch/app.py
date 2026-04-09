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

		print("Press CTRL+C to exit...\n")
		try:
			while self.sim.runner.runnable():
				# Wait briefly instead of busy-spinning on the runner state.
				self.sim.runner.thread.join(timeout=0.2)
		except KeyboardInterrupt:
			pass

		self.sim.stop()
		return
		
		

if __name__ == "__main__":
    test = COSLaunch()

