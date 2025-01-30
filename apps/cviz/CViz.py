#!/usr/bin/python
# Filename: CViz.py
# Description: Implementation of CViz application

from cos.tools.cviz.RPCAgent import RPCAgent
from cos.tools.cviz.VirtualWorld import VirtualWorld
from cos.core.network.ZMQTransport import ZMQTransport

from os import environ

          
class CViz:
	def __init__(self):
		self.world	= VirtualWorld()
		self.agent	= RPCAgent()	
		return

	def run(self, args, appinfo):
		# Hide pygame preamble
		environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
		
		self.configure(args, appinfo)
		self.simulate()
		return -1

	def simulate(self):		
		self.world.run()
		return
		
	def configure(self, args, appinfo):
		if len(args) == 0:
			return
		print("args: ", args)
		
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

