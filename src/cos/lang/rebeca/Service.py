#!/usr/bin/python
# Filename: Service.py
# Description: Implementation of the Service class

from cos.lang.rebeca.Actor import Actor
from cos.lang.rebeca.IPCPort import IPCPort
from cos.core.kernel.Service import Service as ServiceBase
from cos.core.kernel.Context import Context
from cos.core.time.Ticker import Ticker
from cos.core.utilities.ArgList import ArgList

class Service(ServiceBase):
	def __init__(self, args:dict):
		""" Constructor
		Arguments
			args -- List of arguments
		"""
		ServiceBase.__init__(self, args["Type"], args["Name"] )

		self.timer			= None
		self.poll_at		= 1
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
		if self.actor is None:
			return
		
		ServiceBase.on_timer(self, ctxt, unused)

		if (self.timer is None) or (self.timer.signaled() == False):
			return

		# Run the actor for a number of steps
		self.actor.run(self.steps)

		# Check if the actor is still runnable
		if self.actor.runnable() == False:
			self.actor.stop()
			self.actor	= None

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
		self.init_actor( ctxt, config )
		return
		
	def init_actor(self, ctxt, config):
		""" Initializes the actor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""

		path 		= ctxt.sim.config.resolve( config["program"] )

		# Create the actor bound to the ports
		self.actor	= Actor({
				'port': IPCPort(ctxt)
			})
		
		self.actor.load( path )

		# Build a dictionary of command line parameters
		vars		= config.get("argv", "")
		argv		= dict((k.strip(), v.strip()) for k,v in 
              			(item.split('=') for item in vars.split(' ')))
		
		self.actor.start( argv )
		return

if __name__ == "__main__":
	test = Service()

