#!/usr/bin/python
# Filename: Actor.py
# Description: Implementation of the Actor class

from compiler.lang.rebeca.VirtualMachine import VirtualMachine
from cos.lang.rebeca.IPCPort import IPCPort

class Actor:
	def __init__(self, interfaces:dict= None):
		self.vm = VirtualMachine(interfaces)            
		return

	def load(self, path:str):
		self.vm.load(path)
		return
	
	def start(self, argv:dict=None):
		self.vm.start(argv)
		return
	
	def stop(self):
		self.vm.stop()
		return
	
	def run(self, steps=-1):
		return self.vm.step(steps)
		
	def runnable(self):
		return self.vm.pending()

	def notify( self, var:str, method:str, args:dict=None):
		""" Invokes a method on the actor
		Arguments
			var -- Variable name
			method -- Method name
			ctxt -- Simulation context
			args -- Method argument
		"""
		return self.vm.invoke(var, method, args)
	
	@staticmethod
	def init_actor(service, ctxt, config):
		""" Initializes the actor
		Arguments
			service -- A service service
			ctxt -- Simulation context
			config -- Configuration attributes
		"""

		path 		= ctxt.sim.config.resolve( config["program"] )

		# Create the actor bound to the ports
		service.actor	= Actor({
				'port': IPCPort(ctxt)
			})
		
		service.actor.load( path )

		# Build a dictionary of command line parameters
		vars		= config.get("argv", "")
		argv		= dict((k.strip(), v.strip()) for k,v in 
              			(item.split('=') for item in vars.split(' ')))
		
		service.actor.start( argv )
		return
	
	@staticmethod
	def run_actor(service, steps=-1):
		""" Runs the actor for a number of steps
		Arguments
			service -- A service service
			steps -- Number of steps to run
		"""
		# Run the actor for a number of steps
		service.actor.run(steps)
		return

if __name__ == "__main__":
	test = Actor()

    # Load a Rebeca program that uses the port
	test.load('map.rebeca')

    # Start the simulation and run for a number of steps
	test.start({
        'id': 'VehicleSimulation1',
        'lane': 2111
        })
    
	test.run(100)
	test.stop()
