#!/usr/bin/python
# Filename: SeaBuilder.py
# Description: builder class for marine assets

from cos.model.geography.Builder import Builder
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList


class SeaBuilder(Builder):
	def __init__(self, args):
		""" Constructor
		Arguments
			args -- List of arguments
		"""
		Builder.__init__(self, "Builder/Sea", args["Type"], 'Sea', 'isohypses',{
			# Refer: https://mareano.no/en/topics/marine-landscape
			"STRANDFLAT": (100000, "cos.model.geography.Strandflat"),
			"CONTINENTAL_SLOPE": (111000, "cos.model.geography.ContinentalSlope"),
			"MARINE_VALLEY": (113000, "cos.model.geography.MarineValley"),
			"FJORD": (114000, "cos.model.geography.Fjord"),
			"ABYSSAL_PLAIN": (115000, "cos.model.geography.AbyssalPlain"),
			"CONTINENTAL_SHELF_PLAIN": (116000, "cos.model.geography.ContinentalShelfPlain"),
			"MARINE_MOUNTAIN": (117000, "cos.model.geography.MarineMountain")
			} )

		return


	def create(self, ctxt:Context, klass, rec):
		""" Creates a sea artifact from the database
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
						"depth":rec[6],
						"color":rec[7],
						"visible":rec[8]
				} )

		return guid, inst

if __name__ == "__main__":
	test = SeaBuilder()


