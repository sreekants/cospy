#!/usr/bin/python
# Filename: Builder.py
# Description: Builder class for vessels

from maritime.model.vessel.VesselComposer import VesselComposer
from cos.core.simulation.Builder import Builder as BuilderBaseClass
from cos.core.kernel.Context import Context
from cos.core.kernel.BootLoader import BootLoader
from cos.core.utilities.ArgList import ArgList

import json, datetime, collections
from cos.core.utilities.ActiveRecord import ActiveRecord
from cos.model.environment.Scales import Scales

class Builder(BuilderBaseClass):
	# Databases already checked for duplicate identity, so the guard runs once
	# per vessel.s3db rather than once per builder. Five builders share one
	# database, and each reads only the rows of its own type, so the check has
	# to be made over the whole table by one of them.
	audited	= set()

	@classmethod
	def audit(cls, ctxt:Context, path:str):
		""" COS-029-03: refuses a vessel database that cannot be attributed
		Arguments
			ctxt -- Simulation context
			path -- Path of the vessel database
		Returns
			The number of duplicated values found

		A duplicated guid, IMO or MMSI means two vessels' findings merge into
		one bucket for the whole run, and nothing downstream can separate them
		again. The run is allowed to continue - stopping a sweep on a data
		defect is its own kind of damage - but it is logged as an error, once,
		with the offending values named.
		"""
		if path in cls.audited:
			return 0

		cls.audited.add( path )

		try:
			db		= ActiveRecord.create( 'vessel', path, 'vessels' )
			records	= db.get_all()
		except Exception as e:
			ctxt.log.warning( 'Builder/Vessel', f'Identity audit skipped for {path}: {e}' )
			return 0

		# (column index, what it is called in the log)
		fields	= ( (2, 'guid'), (4, 'imo'), (5, 'mmsi') )
		total	= 0

		for index, label in fields:
			counts	= collections.Counter( str(r[index]) for r in records )
			repeats	= { v: n for v, n in counts.items() if n > 1 }
			for value, n in sorted( repeats.items(), key=lambda kv: -kv[1] ):
				names	= [ str(r[1]) for r in records if str(r[index]) == value ]
				ctxt.log.error( 'Builder/Vessel',
								f'{label} {value!r} is shared by {n} vessels '
								f'({", ".join(names[:6])}{" ..." if n > 6 else ""}); '
								f'their findings cannot be told apart (COS.029)' )
			total	+= len( repeats )

		if total:
			ctxt.log.error( 'Builder/Vessel',
							f'{path}: {total} duplicated identity value(s). '
							f'Run tools/mapping/fix_identity.py --apply' )

		return total

	def __init__(self, args:dict):
		""" Constructor
		Arguments
			args -- List of arguments
		"""
		BuilderBaseClass.__init__(self, "Builder/Vessel", args["Type"], 'vessel', 'vessels',
			{
			"POWER_DRIVEN": (100000, "maritime.model.vessel.PowerDrivenVessel"),
			"SAILING": (200000, "maritime.model.vessel.SailingVessel"),
			"SEAPLANE": (300000, "maritime.model.vessel.SeaPlane"),
			"WIG": (400000, "maritime.model.vessel.WIG"),

			"FLEET": (800000, "maritime.model.vessel.Fleet")
			},
			'Vehicle' )

		return



	def build(self, ctxt:Context, args, path:str, type:str):
		""" Builds the vessels of one type, auditing the database first
		Arguments
			ctxt -- Simulation context
			args -- Builder arguments
			path -- Path of the vessel database
			type -- Prototype name
		"""
		# COS-029-03. Five builders share one vessel.s3db and each sees only
		# its own type's rows, so the duplicate check runs here, over the whole
		# table, and only for the first builder to reach it.
		Builder.audit( ctxt, path )

		return BuilderBaseClass.build( self, ctxt, args, path, type )

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

		# vessel.s3db is authored in map units; the simulation runs in metres
		scales	= Scales.of( ctxt )

		if len(X)>0:
			X	= [float(x) for x in X.split(',')]
			X[0:3]	= scales.point( X[0:3] )		# Velocity
			X[3:6]	= scales.point( X[3:6] )		# Acceleration

		if len(R)>0:
			R	= [float(x) for x in R.split(',')]

		config	= {
						"id": rec[0],
						"guid":guid,
						"name":rec[1],
						"type":rec[3],
						"identifier":{
							"imo":rec[4],
							"mmsi":rec[5]
						},
						"length": [float(x) for x in rec[6].split(',')],
						"weight": rec[10],
						"pose":{
							"position": scales.point( [float(x) for x in rec[7].split(',')] ),
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
		composer.build( ctxt, inst, args, config )

		inst.init( ctxt, args )

		if inst.runnable(ctxt, self.args) == False:
			return guid, None
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


