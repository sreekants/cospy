#!/usr/bin/python
# Filename: NetworkManager.py
# Description: Network manager kernel subsystem

from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.kernel.Subsystem import Subsystem
from cos.core.kernel.Context import Context
from cos.core.kernel.IPCMessage import IPCMessage, IPCFlags

class NetworkManager(Subsystem):
	def __init__(self):
		""" Constructor
		"""
		Subsystem.__init__(self, "Kernel", "NetworkManager")
		return



if __name__ == "__main__":
	test = NetworkManager()


