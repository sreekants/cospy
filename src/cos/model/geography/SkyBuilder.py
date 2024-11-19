#!/usr/bin/python
# Filename: SkyBuilder.py
# Description: Builder class for aerial assets

from cos.model.geography.Builder import Builder
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList


class SkyBuilder(Builder):
	def __init__(self, args):
		""" Constructor
		Arguments
			args -- List of arguments
		"""
		# Refer: https://mareano.no/en/topics/marine-landscape
		Builder.__init__(self, "Builder/Sky", args["Type"], 'Sky', 'isohypses',
			{
			"FOG": (1100000, "cos.model.geography.Fog"),
			"CLOUD": (1200000, "cos.model.geography.Cloud")
			} )

		return


	def create(self, ctxt:Context, klass, rec):
		""" #TODO: create
		Arguments
			ctxt -- Simulation context
			klass -- Class object
			rec -- Database record of the object
		"""
		guid	= rec[2]
		inst	= klass( ctxt, guid, {
						"id": rec[0],
						"guid":guid,
						"name":rec[1],
						"key":rec[3],
						"type":rec[4],
						"path":self.scale_polygon2D(ctxt, rec[5]),
						"height":rec[6],
						"color":rec[7],
						"visible":rec[8]
				} )

		return guid, inst

if __name__ == "__main__":
	test = SeaBuilder()


