#!/usr/bin/python
# Filename: main.py
# Description: TODO

import os, shutil, getopt, sys
import os.path

from Minsim import Minsim


def get_app_info():
	return {
		"executable": "minsim.py",
		"name"		: "Minimal simulation tool",
		"version"	: "Version: 1.0 [07 Mar 2018]",
		"usage"		:[ 	"[-h][-?] dir"
					],
					
		"help"		:[
			    ["h"	, ["Print help.", usage]],
			    ["?"	, ["Print help.", usage]],
			    ["dir"	, ["Code directory.", None]]
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
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hi:d", ["help"])
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

	theApp = Minsim()
	theApp.run()
	

if __name__ == "__main__":
    main()	
