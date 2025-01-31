#!/usr/bin/python
# Filename: main.py
# Description: Implementation of the main() entry point for Kml2map application

import os, shutil, getopt, sys
import os.path

from Kml2map import Kml2map


def get_app_info():
	return {
		"executable": "kml2map.py",
		"name"		: "KML to map converter",
		"version"	: "Version: 1.0 [07 Mar 2018]",
		"usage"		:[ 	"[-h][-?][-dir path][-offset range][-scale range][-zone zone]"
					],
					
		"help"		:[
			    ["h"	, ["Print help.", usage]],
			    ["?"	, ["Print help.", usage]],
			    ["dir"	, ["Database directory.", None]],
			    ["offset"	, ["Offset the output map eg:[-600,20].", None]],
			    ["scale"	, ["Scale output map eg:[5000,5000] - 5km to a pixel on x,y.", None]],
			    ["zone"	, ["UTM zone. eg:35N", None]]
				]		
		}
	


def usage():
	Format	= "name,version,copyright,website"
	AppInfo	= get_app_info()
	
	# Print header
	for attr in Format.split(','):
		if AppInfo.get(attr):
			print( AppInfo[attr] )

	# Print usage			
	print("\nUsage:\n    {}\t{}\n\nOptions:".format(
					AppInfo['executable'], 
					"\n\t\t".join(AppInfo["usage"])) )

	# Pring argument description			
	for help in AppInfo["help"]:
		if len(help[0]) < 3:
			indent	= '\t\t'
		else:
			indent	= '\t'
		
		print( "    -{}{}{}".format(help[0], indent, help[1][0]) )
	
	sys.exit(0)		    
	return

def main():
	arglist	= sys.argv[1:]

	try:
		opts, args = getopt.getopt(arglist, "hi:d", ["help","dir","scale","offset","zone"])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()                     
			sys.exit()                  
		elif opt == '-d':
			global _debug
			_debug = 1 

	theApp = Kml2map()
	theApp.run( arglist, get_app_info() )
	

if __name__ == "__main__":
    main()	
