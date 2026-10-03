#!/usr/bin/python
# Filename: Publisher.py
# Description: Bins viewer events per tick and hands the latest of each to the brokers

from cos.core.kernel.Subsystem import Subsystem
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

import threading, time

DEFAULT_INTERVAL	= 0.2		# Wall seconds between pushes to /IPC

class Publisher(Subsystem):
	def __init__(self):
		""" Constructor
		"""
		Subsystem.__init__(self, "Network", "Publisher")
		self.interval	= DEFAULT_INTERVAL
		self.bins		= {}		# Event name -> {key: latest argument}
		self.pushed		= None		# Wall time of the last push
		self.lock		= threading.Lock()
		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		Subsystem.on_init(self, ctxt, module)

		config			= ArgList( module.get("config", "") )
		self.interval	= config.ToFloat( 'interval', DEFAULT_INTERVAL )
		ctxt.sim.ipc.publisher	= self
		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events; pushes the bins once per interval
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		Subsystem.on_timer(self, ctxt, unused)

		now		= time.monotonic()
		if (self.pushed is not None) and (now - self.pushed < self.interval):
			return

		self.push( ctxt.sim.ipc )
		self.pushed	= now
		return

	def post(self, msg:str, key, arg):
		""" Bins an event, replacing the one with the same key since the last push
		Arguments
			msg -- Event name, e.g. vessel.move
			key -- Identity of the sender, e.g. the vessel's guid
			arg -- Event argument
		"""
		with self.lock:
			self.bins.setdefault( msg, {} )[key]	= arg
		return

	def push(self, ipc):
		""" Pushes each bin to /IPC as one event carrying all its arguments
		Arguments
			ipc -- Message queue of the simulation
		"""
		with self.lock:
			bins, self.bins	= self.bins, {}

		for msg, args in bins.items():
			ipc.push( ipc.ipc, msg, None, list(args.values()) )
		return


if __name__ == "__main__":
	test = Publisher()
