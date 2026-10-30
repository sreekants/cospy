#!/usr/bin/python
# Filename: CViz.py
# Description: Implementation of CViz application

from cos.tools.cviz.RPCAgent import RPCAgent
from cos.core.network.ZMQTransport import ZMQTransport

from os import environ
import importlib

# View name -> (module, class) of its world; imported on demand, so each view needs only its own renderer
VIEWS	= {
	"2d":	("cos.tools.cviz.VirtualWorld", "VirtualWorld"),
	"3d":	("cos.ui.3d.VirtualWorld3D", "VirtualWorld3D"),
}

class CViz:
	def __init__(self, view="2d"):
		""" Constructor
		Arguments
			view -- Name of the view in VIEWS
		"""
		# Hide pygame preamble; it prints on import
		environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

		module, name	= VIEWS[view]
		self.world	= getattr( importlib.import_module(module), name )()
		self.agent	= RPCAgent()
		return

	def run(self, args, appinfo):
		self.configure(args, appinfo)
		self.simulate()
		return -1

	def simulate(self):		
		self.world.run()
		return
		
	def configure(self, args, appinfo):
		if len(args) == 0:
			return
		
		for help in appinfo["help"]:
			if help[0] != args[0]:
				continue

			method = args[0]
			if hasattr(self, method) and callable(func:=getattr(self, method)):
				try:
					args 	= args[1:]
					if len(args) == 0:
						args	= None

					result	= func( args )				
				except Exception as e:
					print(e)
					return -1
				
		return 0

	def host( self, args ):
		ZMQTransport.set_host(args[0])
		return 

if __name__ == "__main__":
    test = CViz()

