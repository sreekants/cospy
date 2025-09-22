#!/usr/bin/python
# Filename: main.py
# Description: Implementation of the main() entry point for RegEval application

import os, shutil, getopt, sys
import os.path

from app import RegEval


def get_app_info():
	return {
		"executable": "regeval.py",
		"name"		: "COLREG Regulation Evaluator",
		"version"	: "Version: 1.0 [17 Feb 2025]",
		"usage"		:[ 	"[-h][-?] dir"
					],
					
		"help"		:[
			    ["h"	, ["Print help.", usage]],
			    ["?"	, ["Print help.", usage]],
			    ["dir"	, ["Code directory.", None]],
			    ["terms"	, ["Dump term catalog.", None]],
			    ["verbose"	, ["Dump processing instructions.", None]],
			    ["match"	, ["Match a wildcard.", None]]
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
		opts, args = getopt.getopt(arglist, "hi:d", ["help","dir"])
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

	theApp = RegEval()
	theApp.run( arglist, get_app_info() )
	

if __name__ == "__main__":
    main()	
