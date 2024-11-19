#!/usr/bin/python
# Filename: LandBuilder.py
# Description: Builder class for land assets

from cos.model.geography.Builder import Builder
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

class LandBuilder(Builder):
	def __init__(self, args):
		""" Constructor
		Arguments
			args -- List of arguments
		"""
		Builder.__init__(self, "Builder/Land", args["Type"], 'Land', 'isohypses',
			{
			"MOUNTAIN": (100000, "cos.model.geography.Mountain"),
			"PLAIN": (200000, "cos.model.geography.Plain"),
			"PLATEAU": (300000, "cos.model.geography.Plateau"),
			"DESERT": (300000, "cos.model.geography.Desert")
			} )

		return


	def create(self, ctxt:Context, klass, rec):
		""" Creates a land artifact from the database
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
						"path": self.scale_polygon2D(ctxt, rec[5]),
						"height":rec[6],
						"color":rec[7],
						"visible":rec[8]
				} )

		return guid, inst


if __name__ == "__main__":
	test = Builder()


