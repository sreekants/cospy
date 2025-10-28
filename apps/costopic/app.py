#!/usr/bin/pythonself.api.(args)
# Filename: COSTopic.py
# Description: Runs the application 

from cos.core.api.Topic import Topic
import getopt, time

class COSTopic:
	def __init__(self):
		self.api	= Topic()
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
			
		if len(args) > 0:
			print(f"Unknown command: {args[0]}")

		return -1

	def echo( self, args ):
		count	= 1
		path	= args[-1]

		opts, args = getopt.getopt( args, "n:d", ["help"])
		for opt, arg in opts:
			if opt == '-n':
				count	= int(arg)

		try:
			for n in range(0, count):
				while True:
					msg		= self.api.pop(path)
					if msg != None:
						break

					time.sleep(1)

				print( msg )
				
		except Exception as e:
			print( str(e) )

		return 

	def find( self, args ):
		return '\r\n'.join(self.api.find(args[-1]))

	def info( self, args ):
		return self.api.info(args[-1])

	def list( self, args ):
		path	= ''
		if args!=None and len(args) > 0:
			path	= args[-1]
		return '\r\n'.join(self.api.list(path))

	def type( self, args ):
		return self.api.type(args[-1])
		
	def route( self, args ):
		return self.api.route(args[-2], args[-1])

	def unroute( self, args ):
		return self.api.unroute(args[-1])

	def pub( self, args ):
		return self.api.push(args[0], args[1])

if __name__ == "__main__":
    test = COSTopic()

