#!/usr/bin/python
# Filename: Builder.py
# Description: Builder class for vessels

from maritime.model.vessel.VesselComposer import VesselComposer
from cos.core.simulation.Builder import Builder as BuilderBaseClass
from cos.core.kernel.Context import Context
from cos.core.kernel.BootLoader import BootLoader
from cos.core.utilities.ArgList import ArgList

import json, datetime

class Builder(BuilderBaseClass):
	def __init__(self, args):
		""" Constructor
		Arguments
			args -- List of arguments
		"""
		BuilderBaseClass.__init__(self, "Builder/Vessel", args["Type"], 'vessel', 'vessels',
			{
			"POWER_DRIVEN": (100000, "maritime.model.vessel.PowerDrivenVessel"),
			"SAILING": (200000, "maritime.model.vessel.SailingVessel"),
			"SEAPLANE": (300000, "maritime.model.vessel.SeaPlane"),
			"WIG": (400000, "maritime.model.vessel.WIG")
			},
			'Vehicle' )

		return


	def create(self, ctxt:Context, klass, rec):
		""" Builds all the vessels in a simulation
		Arguments
			ctxt -- Simulation context
			klass -- Class object
			rec -- Database record of the object
		"""
		guid	= rec[2]
		X		= rec[8].strip()
		R		= rec[9].strip()

		if len(X)>0:
			X	= [float(x) for x in X.split(',')]

		if len(R)>0:
			R	= [float(x) for x in R.split(',')]

		config	= {
						"id": rec[0],
						"guid":guid,
						"name":rec[1],
						"identifier":{
							"imo":rec[4],
							"mmsi":rec[5]
						},
						"length": [float(x) for x in rec[6].split(',')],
						"weight": rec[10],
						"pose":{
							"position": [float(x) for x in rec[7].split(',')],
							"X": X,
							"R": R
						},
						"behavior":rec[11],
						"sprite":rec[12],
						"settings":rec[13]
				}

		inst	= klass( ctxt, guid, config )
		args	= ArgList(rec[13])

		# Delegate to the composer to build the configuration of the vessel
		# including devices and drivers
		composer	= VesselComposer()
		composer.build( ctxt, inst, args )

		inst.init( ctxt, args )
		return guid, inst

	@staticmethod
	def fromjson(pkg:str, profile, args):
		""" Builds a vessel from a configuration
		Arguments
			pkg -- Class name of the vessel type
			profile -- Configuration of the object in JSON
			args -- arguments to pass to the composer
		"""
		klassname, klass	= BootLoader.load_class( pkg )

		config	= json.loads(profile)
		ctxt	= None
		guid	= config["guid"]
		inst	= klass( None, guid, config )
		args	= ArgList(args)

		# Delegate to the composer to build the configuration of the vessel
		# including devices and drivers
		composer	= VesselComposer()
		composer.build( ctxt, inst, args )

		inst.init( ctxt, args )
		inst.sim_init( None, None )
		return inst


if __name__ == "__main__":
	test = Builder()


