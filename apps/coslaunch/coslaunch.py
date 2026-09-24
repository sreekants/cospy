#!/usr/bin/python
# Filename: main.py
# Description: Main entry for COSLaunch application

import os, shutil, getopt, sys
import os.path

from app import COSLaunch

IMAGE=None
CONFIG=None

def get_app_info():
	return {
		"executable": "coslaunch.py",
		"name"		: "COS Simulation Operating system",
		"version"	: "Version: 1.0 [07 Mar 2018]",
		"usage"		:[ 	"[-h][-?][-i image][-c|-config path/to/cos.ini]"
					],
					
		"help"		:[
			    ["h"		, ["Print help.", usage]],
			    ["?"		, ["Print help.", usage]],
			    ["i"		, ["Set the image.", set_image]],
			    ["c"		, ["Path to cos.ini (optional).", set_config]],
			    ["config"	, ["Same as -c.", set_config]],
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

def set_image(path):
	global IMAGE
	IMAGE	= path
	if os.path.isfile(IMAGE) == False:
		print( f'[{IMAGE}] is not an image file.')
		sys.exit(-1)
	return

def set_config(path):
	global CONFIG
	if os.path.isfile(path) == False:
		print( f'[{path}] is not a configuration file.')
		sys.exit(-1)
	CONFIG	= os.path.abspath(path)
	return

def normalize_argv(argv):
	""" getopt does not support single-dash long options, so map
	-config/-image/-help to their --long equivalents.
	"""
	longopts	= ['config', 'image', 'help']
	return [ '-' + a if a.split('=')[0][1:] in longopts else a for a in argv ]

def main():
	try:
		opts, args = getopt.getopt(normalize_argv(sys.argv[1:]), "h?i:c:d", ["help", "image=", "config="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "-?", "--help"):
			usage()                     
			sys.exit()                  
		elif opt in ("-i", "--image"):
			set_image(arg)
		elif opt in ("-c", "--config"):
			set_config(arg)
		elif opt == '-d':
			global _debug               
			_debug = 1                  

	preamble()
	theApp = COSLaunch()
	theApp.run( args, get_app_info(), {
			'image' : IMAGE,
			'config': CONFIG
			})
	

if __name__ == "__main__": 
    main()	
