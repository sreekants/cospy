#!/usr/bin/python
# Filename: Service.py
# Description: Implementation of the Service class

from cos.lang.rebeca.Actor import Actor
from cos.core.kernel.Service import Service as ServiceBase
from cos.core.kernel.Context import Context
from cos.core.time.Ticker import Ticker
from cos.core.utilities.ArgList import ArgList
from typing import Any
import json

class Service(ServiceBase):
	def __init__(self, args:dict):
		""" Constructor
		Arguments
			args -- List of arguments
		"""
		type		= args.get("Type", "default")
		name		= args.get("Name", "Service")
		ServiceBase.__init__(self, type, name )

		self.listen( f'/Services/{type}/{name}' )

		self.timer			= None
		self.poll_at		= 5
		self.steps			= int( args.get("Steps", 100) )
		self.actor			= None
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		ServiceBase.on_start(self, ctxt, config)
		

		self.init_config(ctxt, config)

		# Pump events to the message services
		self.listen( self.ipc_topic )
		self.poll_ipc( ctxt, [self.ipc_topic] )
		return


	def on_stop(self, ctxt:Context, config):
		""" Callback for simulation shutdown
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		ServiceBase.on_stop(self, ctxt, config)

		# Stop the actor
		if self.actor is not None:
			self.actor.stop()
		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""		
		ServiceBase.on_timer(self, ctxt, unused)


		if (self.timer is None) or (self.timer.signaled() == False):
			return
		
		# Run the actor for a number of steps
		Actor.run_actor( self, self.steps )
		return

	def init_config(self, ctxt, config):
		""" Initializes the configuration
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Parse configurations
		args				= ArgList(config["config"])

		self.poll_at		= args["poll.frequency"]

		# Initialize timer ticks
		if self.poll_at is not None:
			self.timer	= Ticker( int(self.poll_at) )
		else:
			self.timer	= None

		# Initialize actor
		Actor.init_actor( self, ctxt, config )
		return

	def notify(self, ctxt:Context, call:str, unused:str):
		""" Triggers a method
		Arguments
			ctxt -- Simulation context
			call -- Method information
			unused -- Unused variable
		"""
		# Unmarshall the argument
		if call.startswith('{') and call.endswith('}'):
			callinfo	= json.loads( call )
			inst		= callinfo['object']
			method 		= callinfo['method']
			argv		= dict()
			for k, v in callinfo.items():
				if k not in ['object', 'method']:
					argv[k]	= v
		else:
			callinfo	= ArgList(call, '=', ',')
			inst		= callinfo['object']
			method 		= callinfo['method']
			argv		= dict()
			for k, v in callinfo.arglist.items():
				if k not in ['object', 'method']:
					argv[k]	= v

		# Invoke the method on the actor
		self.actor.notify( inst, method, argv )
		return

if __name__ == "__main__":
	test = Service()

