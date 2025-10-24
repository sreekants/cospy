#!/usr/bin/python
# Filename: Actor.py
# Description: Implementation of the Actor class

from compiler.lang.rebeca.VirtualMachine import VirtualMachine

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
		return self.vm.runnable()

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
