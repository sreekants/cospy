#!/usr/bin/python
# Filename: main.py
# Description: Main entry for COSLaunch application

import os, shutil, getopt, sys
import os.path

from COSLaunch import COSLaunch

IMAGE=None

def get_app_info():
	return {
		"executable": "cossim.py",
		"name"		: "COS Simulation Operating system",
		"version"	: "Version: 1.0 [07 Mar 2018]",
		"usage"		:[ 	"[-h][-?][-i image]"
					],
					
		"help"		:[
			    ["h"		, ["Print help.", usage]],
			    ["?"		, ["Print help.", usage]],
			    ["i"		, ["Set the image.", set_image]],
			    ["image"	, ["Code directory.", None]]
				]		
		}
	

def preamble():
	Format	= "name,version,copyright"
	AppInfo	= get_app_info()
	
	# Print header
	for attr in Format.split(','):
		if AppInfo.get(attr):
			print( AppInfo[attr] )

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
		if len(help[0]) <= 3:
			indent	= '\t\t'
		else:
			indent	= '\t'
		
		print( "    {}{}{}".format(help[0], indent, help[1][0]) )
	
	sys.exit(0)		    
	return

def set_image():
	global IMAGE
	IMAGE	= sys.argv[-1]
	if os.path.isfile(IMAGE) == False:
		print( f'[{IMAGE}] is not an image file.')
		sys.exit(-1)
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
		elif opt in ("-i"):
			set_image()
		elif opt == '-d':
			global _debug               
			_debug = 1                  

	preamble()
	theApp = COSLaunch()
	theApp.run( args, get_app_info(), {
			'image' : IMAGE
			})
	

if __name__ == "__main__": 
    main()	
