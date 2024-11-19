#!/usr/bin/python
# Filename: Context.py
# Description: Runtime Context  of the simulation


class Context:
	def __init__(self, sim, process=None, ipc=None, log=None):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
			process -- Reference to the process in context
			ipc -- Reference to IPC service
			log -- Reference to the logger
		"""
		self.process	= process
		self.ipc		= ipc
		self.sim		= sim

		if log is None:
			self.log		= sim.log
		else:
			self.log		= log
		return


if __name__ == "__main__":
	test = Context()


