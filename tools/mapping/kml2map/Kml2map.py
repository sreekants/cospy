#!/usr/bin/python
# Filename: Kml2map.py
# Description: Implementation of the singleton Kml2map application

from Extractor import Extractor
import os

class Kml2map:
	def __init__(self):
		self.xrange	= [0, 7000]
		self.yrange	= [0, 5000]

		self.xsorig	= -600
		self.ysorig	= 50

		# REMOVE
		self.xorig	= 0
		self.yorig	= 0 


		self.path	= '.'
		return

	def run(self, args, appinfo):
		if len(args) > 0:
			self.configure(args, appinfo)

		self.extract()
		return 0
	
	def configure(self, args, appinfo):
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

	def dir( self, args ):
		self.path	= args[0]
		return

	def extract(self):
		e = Extractor( {
				"zone":{
					"number":35,
					"letter":"N"
				},
				"mapping":{
					"x": ( self.xrange,	[0,1200],   self.xsorig ),
					"y": ( self.yrange, [0,800],   	self.ysorig )
				}
			})
		

		e.extract( self.path, "kml", "csv" )

		e.clear(self.path, "land.s3db")
		e.clear(self.path, "sea.s3db")

		# Output the data.
		e.dump(self.path, "land", "land.s3db")
		e.dump(self.path, "sea", "sea.s3db")
		e.dump(self.path, "tss", "sea.s3db")
		return
		
		

if __name__ == "__main__":
    test = Kml2map()

