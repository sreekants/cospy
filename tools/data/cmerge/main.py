#!/usr/bin/python
# Filename: main.py
# Description: Implementation of the main() entry point for Cmerge application

import os, getopt, sys
import os.path

sys.path.insert( 0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'src') )

from app import CMergeApp


def get_app_info():
	return {
		"executable": "cmerge.py",
		"name"		: "COS sweep database consolidator",
		"version"	: "Version: 1.0 [25 Sep 2026]",
		"usage"		:[ 	"[-h][-?][-t template][-o output][-f] listfile"
					],

		"help"		:[
			    ["h"	, ["Print help.", usage]],
			    ["?"	, ["Print help.", usage]],
			    ["t"	, ["Template database (default config/data/maritime.s3db).", None]],
			    ["o"	, ["Consolidated database to create (default maritime.consolidated.s3db).", None]],
			    ["f"	, ["Replace the output if it exists.", None]],
			    ["listfile"	, ["Text file, one maritime.workingset.s3db path per line.", None]]
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
		opts, args = getopt.getopt(sys.argv[1:], "h?t:o:f", ["help"])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	theApp = CMergeApp()
	for opt, arg in opts:
		if opt in ("-h", "-?", "--help"):
			usage()
		elif opt == '-t':
			theApp.template	= arg
		elif opt == '-o':
			theApp.output	= arg
		elif opt == '-f':
			theApp.force	= True

	if len(args) != 1:
		usage()

	sys.exit( theApp.run(args[0]) )


if __name__ == "__main__":
    main()
