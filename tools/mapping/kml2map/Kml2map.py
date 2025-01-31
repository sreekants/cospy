#!/usr/bin/python
# Filename: Kml2map.py
# Description: Implementation of the singleton Kml2map application

from Extractor import Extractor
import os

class Kml2map:
	def __init__(self):
		self.xrange		= [0, 10000.0]
		self.yrange		= [0, 10000.0]

		self.xsorig		= 0.0
		self.ysorig		= 0.0

		self.path		= '.'

		self.zonenum	= 35
		self.zonechar	= "N"
		return

	def run(self, args, appinfo):
		if len(args) > 0:
			if self.configure(args, appinfo) == False:
				return -1

		self.extract()
		return 0
	
	def configure(self, args, appinfo):
		next	= 0

		while True:
			if next >= len(args):
				break

			method = args[next]
			if method[0] != '-':
				next = next+1
				continue

			method	= method[1:]

			if hasattr(self, method) and callable(func:=getattr(self, method)):
				try:
					nargs 	= args[next+1:]
					if len(nargs) == 0:
						nargs	= None

					result	= func( nargs )
					if result != None:
						print( result )
						
				except Exception as e:
					print(e)
					return False
				
			next	= next+1
				
		return True

	def dir( self, args ):
		self.path	= args[0]
		return

	@staticmethod
	def get_range(arg, type):
		nchar	= len(arg)
		if (nchar < 2) or (arg[0] != '[') or (arg[-1] != ']'):
			raise ValueError( f"Invalid {type} argument [{arg}]." )
		
		a	= arg[1:nchar-1].split(',')

		return (float(a[0]), float(a[1]))
	
	def scale( self, args ):
		scale		= Kml2map.get_range( args[0], "scale" )
		self.xrange	= [0, scale[0]]
		self.yrange	= [0, scale[1]]
		return

	def offset( self, args ):
		offset		= Kml2map.get_range( args[0], "offset" )
		self.xsorig	= offset[0]
		self.ysorig	= offset[1]
		return

	def zone( self, args ):
		zone			= args[0]
		self.zonenum	= int(zone[:-1])
		self.zonechar	= zone[-1:]
		return

	def extract(self):
		try:
			e = Extractor( {
					"zone":{
						"number":self.zonenum,
						"letter":self.zonechar
					},
					"mapping":{
						"x": ( self.xrange,	[0,1200],   self.xsorig ),
						"y": ( self.yrange, [0,800],   	self.ysorig )
					}
				})
			
			# Extract the map
			e.extract( self.path, "kml", "csv" )

			# Remove all existing data
			e.clear(self.path, "land.s3db")
			e.clear(self.path, "sea.s3db")

			# Output the data.
			e.dump(self.path, "land", "land.s3db")
			e.dump(self.path, "sea", "sea.s3db")
			e.dump(self.path, "tss", "sea.s3db")
		except Exception as e:
			print(e)
			return False
	
		return True
		
		

if __name__ == "__main__":
    test = Kml2map()

