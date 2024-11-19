#!/usr/bin/python
# Filename: SeaBuilder.py
# Description: builder class for marine assets

from cos.model.geography.SeaBuilder import SeaBuilder as SeaBuilderBase
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList


class SeaBuilder(SeaBuilderBase):
	def __init__(self, args):
		""" Constructor
		Arguments
			args -- List of arguments
		"""
		SeaBuilderBase.__init__(self, args)

		SeaBuilderBase.register(self, {
			# Maritime zones
			"EXCLUSIVE_ECONOMIC_ZONE": (201000, "maritime.model.geography.ExclusiveEconomicZone"),
			"CONTIGUOUS_ZONE": (202000, "maritime.model.geography.ContiguousZone"),
			"TERRITORIAL_SEA": (203000, "maritime.model.geography.TerritorialSea"),
			"INTERNAL_WATERS": (204000, "maritime.model.geography.InternalWaters"),
			"MARITIME_EXCLUSION_ZONE": (205000, "maritime.model.geography.MaritimeExclusionZone"),

			# Traffic schemes
			"HARBOUR": (301000, "maritime.model.geography.Harbour"),
			"WATERWAY": (302000, "maritime.model.geography.Waterway"),
			"TRAFFIC_SEPARATION_SCHEME": (303000, "maritime.model.geography.TrafficSeparationScheme"),
			"TRAFFIC_LANE": (304000, "maritime.model.geography.TrafficLane"),
			"SEPARATION_ZONE": (305000, "maritime.model.geography.SeparationZone"),
			"ROUNDABOUT": (306000, "maritime.model.geography.Roundabout"),
			"INSHORE_TRAFFIC_ZONE": (307000, "maritime.model.geography.InshoreTrafficZone"),
			"RECOMMENDED_ROUTE": (308000, "maritime.model.geography.RecommendedRoute"),
			"DEEP_WATER_ROUTE": (309000, "maritime.model.geography.DeepwaterRoute"),
			"PRECAUTIONARY_AREA": (310000, "maritime.model.geography.PrecautionaryRoute"),
			"AREA_TO_AVOID": (311000, "maritime.model.geography.AreaToAvoid")
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


