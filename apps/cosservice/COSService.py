#!/usr/bin/python
# Filename: COSService.py
# Description: Runs the application 

from cos.core.api.Service import Service

class COSService:
	def __init__(self):
		self.api	= Service()
		return

	def run(self, args, appinfo):	
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
					if result != None:
						print( result )
						
				except Exception as e:
					print(e)
					return -1
				
				return 0

		return -1
		
	def list( self, args ):
		return '\r\n'.join(self.api.list(args))
		
	def info( self, args ):
		return self.api.info(args[0])

if __name__ == "__main__":
	test = COSService()
	test.list( [] )

