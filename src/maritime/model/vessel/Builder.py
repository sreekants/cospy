#!/usr/bin/python
# Filename: Builder.py
# Description: Builder class for vessels

from maritime.model.vessel.VesselComposer import VesselComposer
from cos.core.simulation.Builder import Builder as BuilderBaseClass
from cos.core.kernel.Context import Context
from cos.core.kernel.BootLoader import BootLoader
from cos.core.utilities.ArgList import ArgList

import json, datetime, collections, csv, io, types, uuid, zlib, re, random
from cos.core.utilities.ActiveRecord import ActiveRecord
from cos.model.environment.Scales import Scales

ENABLED		= 14		# column index of vessels.enabled (REQ.035)
FLEET		= 800000

SPACING		= 60.0		# Ticks of sailing between a record's copies along its trip (count=)
APART		= 50.0		# Metres between copies placed in a zone (count= with zone=)
BOX			= ( 10.0, 5.0 )	# Half the 20 x 10 m collision box, metres
LOAD		= (0.2, 1.1)	# Load of a copy as a fraction of deadweight, as shipgen fix_models.py

class Builder(BuilderBaseClass):
	# Databases already checked for duplicate identity, so the guard runs once
	# per vessel.s3db rather than once per builder. Five builders share one
	# database, and each reads only the rows of its own type, so the check has
	# to be made over the whole table by one of them.
	audited	= set()
	taken	= {}		# Database path -> guids, IMOs and MMSIs in use, so copies stay unique
	copies	= set()		# guids of copies made by count=

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

		cls.register_disabled( ctxt, path, records )
		cls.taken[path]	= { str(v) for r in records for v in (r[2], r[4], r[5]) }

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

	@classmethod
	def register_disabled(cls, ctxt:Context, path:str, records):
		""" REQ.035: records and logs the vessels switched off with enabled=0
		Arguments
			ctxt -- Simulation context
			path -- Path of the vessel database
			records -- Every row of its vessels table
		"""
		if records and len(records[0]) <= ENABLED:
			ctxt.log.error( 'Builder/Vessel', f'{path} has no enabled column, so no vessel will load (REQ.035). Add it with '
							f'ALTER TABLE vessels ADD COLUMN [enabled] INTEGER NOT NULL DEFAULT 1 CHECK ([enabled] IN (0, 1))' )
			return

		disabled	= getattr( ctxt.sim, 'disabled_vessels', None )
		if disabled is None:
			disabled	= ctxt.sim.disabled_vessels	= {}

		off	= [ r for r in records if r[ENABLED] == 0 ]
		for r in off:
			imo	= str( r[4] )
			disabled[ str(r[2]) ]	= types.SimpleNamespace( id=str(r[2]), name=r[1], type=r[3], imo=r[4], mmsi=r[5],
															 recid=int(imo) if imo.isdigit() else None )
		if off:
			ctxt.log.info( 'Builder/Vessel', f'{path}: {len(off)} vessel(s) disabled: {", ".join(str(r[1]) for r in off)}' )

		# A disabled controller leaves its enabled members built but without motion
		enabled	= { str(r[2]): r[1] for r in records if r[ENABLED] != 0 }
		for r in off:
			if r[3] != FLEET:
				continue
			members	= [ enabled[g] for g in cls.formation( ctxt, r[13] ) if g in enabled ]
			if members:
				ctxt.log.warning( 'Builder/Vessel', f'fleet controller {r[1]} is disabled; its {len(members)} enabled member(s) '
								  f'({", ".join(members)}) will be built but will not move. Disable them too' )
		return

	@staticmethod
	def formation(ctxt:Context, settings):
		""" Member guids of a fleet controller's formation file
		Arguments
			ctxt -- Simulation context
			settings -- The controller's settings
		Returns
			A list of guids, empty when there is no readable formation
		"""
		path	= ArgList( settings )['membership']
		if path is None:
			return []
		try:
			rows	= list( csv.reader(io.StringIO(ctxt.sim.fs.read_file(ctxt.sim.config.resolve(path)))) )
		except Exception:
			return []
		return [ row[1].strip() for row in rows[1:] if len(row) > 1 ]

	def expand(self, ctxt:Context, records, path:str):
		""" Adds the copies a record's count= asks for after the record itself
		Arguments
			ctxt -- Simulation context
			records -- Enabled records of this builder's type
			path -- Path of the vessel database
		"""
		expanded	= []
		for rec in records:
			expanded.append( rec )
			expanded.extend( self.replicate(ctxt, rec, path) )
		return expanded

	def replicate(self, ctxt:Context, rec, path:str):
		""" Copies 2..N of a record with count=N: own identity, spread along the trip or over the zone
		Arguments
			ctxt -- Simulation context
			rec -- Vessel record
			path -- Path of the vessel database
		Returns
			The copies, as records; none without count= or when it cannot apply
		"""
		args	= ArgList( rec[13] )
		if args['count'] is None:
			return []

		name	= rec[1]
		try:
			count	= int( args['count'] )
			spacing	= float( args['spacing'] or SPACING )
		except ValueError:
			ctxt.log.error( 'Builder/Vessel', f'{name}: count={args["count"]} spacing={args["spacing"]} is not a number; no copies' )
			return []

		if count <= 1:
			return []
		if (rec[3] == FLEET) or not (rec[11] or '').strip():
			ctxt.log.warning( 'Builder/Vessel', f'{name}: count= ignored for a fleet controller or member' )
			return []
		if (args['pathfile'] is None) and (args['zone'] is None):
			ctxt.log.warning( 'Builder/Vessel', f'{name}: count= needs a trip (pathfile=) or a zone (zone=); no copies' )
			return []

		start	= float( args['headstart'] or 0.0 )
		placed	= []

		taken	= Builder.taken.setdefault( path, set() )
		copies	= []
		for k in range( 1, count ):
			guid	= str( uuid.uuid5(uuid.NAMESPACE_URL, f'{rec[2]}/copy/{k}') )
			imo		= Builder.unique( taken, lambda salt: Builder.imo(f'{guid}/{salt}') )
			mmsi	= Builder.unique( taken, lambda salt: Builder.mmsi(str(rec[5]), f'{guid}/{salt}') )
			taken.add( guid )

			row		= list( rec )
			row[1], row[2], row[4], row[5]	= f'{name} ({k+1})', guid, imo, mmsi
			row[10]	= None				# Weight from a seeded load once the ship model is known
			if args['pathfile'] is not None:
				row[13]	= Builder.respace( rec[13], start + k*spacing )
			else:
				row[7]	= self.place( ctxt, args["zone"], guid, placed ) or rec[7]
				row[13]	= Builder.respace( rec[13], None )
			copies.append( tuple(row) )
			Builder.copies.add( guid )

		where	= f'{spacing:g} ticks apart along the trip' if args['pathfile'] is not None else f'over zone {args["zone"]}'
		ctxt.log.info( 'Builder/Vessel', f'{name}: {count} instances, {where}' )
		return copies

	@staticmethod
	def respace(settings:str, headstart)->str:
		""" A copy's settings: no count= or spacing=, and its head start along the trip if it has one
		Arguments
			settings -- The record's settings
			headstart -- Ticks of sailing the copy starts ahead (co-located vessels deadlock), or None
		"""
		kept	= [ kv for kv in (settings or '').split() if kv.split('=', 1)[0] not in ('count', 'spacing', 'headstart') ]
		return ' '.join( kept + ([f'headstart={headstart:g}'] if headstart is not None else []) )

	def place(self, ctxt:Context, zone:str, guid:str, placed:list)->str:
		""" A start position for a copy: inside the zone, on water, and apart from the copies placed before it
		Arguments
			ctxt -- Simulation context
			zone -- 'x,y,w,h' in map units
			guid -- The copy's guid, which seeds the draw
			placed -- Positions already given, in metres; the new one is added
		Returns
			'x,y,0' in map units, as the position column holds it
		"""
		x0, y0, w, h	= ( float(v) for v in zone.split(',') )
		sx, sy			= Scales.of( ctxt ).map[:2]
		land			= ctxt.sim.objects.get_all( '/World/Land' ) if getattr( ctxt, 'sim', None ) else []
		rnd				= random.Random( zlib.crc32(guid.encode()) )

		for _ in range( 500 ):
			x, y	= x0 + rnd.random() * w, y0 + rnd.random() * h
			m		= ( x * sx, y * sy )
			corners	= [ (m[0] + dx, m[1] + dy) for dx in (-BOX[0], BOX[0]) for dy in (-BOX[1], BOX[1]) ] + [m]
			if any( body.contains(c) for body in land for c in corners ):
				continue
			if any( (m[0] - p[0])**2 + (m[1] - p[1])**2 < APART**2 for p in placed ):
				continue
			placed.append( m )
			return f'{x:.1f},{y:.1f},0'

		ctxt.log.warning( 'Builder/Vessel', f'zone {zone}: no free water found for a copy; it starts on the record\'s position' )
		return None

	@staticmethod
	def unique(taken:set, make):
		""" The first value make(salt) gives that is not taken, which it then takes
		Arguments
			taken -- Values in use
			make -- Function of a salt returning a candidate
		"""
		salt	= 0
		while (value := make(salt)) in taken:
			salt	+= 1
		taken.add( value )
		return value

	@staticmethod
	def imo(seed:str)->str:
		""" A 7-digit IMO number with a valid check digit
		Arguments
			seed -- Text the number is derived from
		"""
		six		= f'9{zlib.crc32(seed.encode()) % 10**5:05d}'
		return six + str( sum(int(d) * w for d, w in zip(six, range(7, 1, -1))) % 10 )

	@staticmethod
	def mmsi(parent:str, seed:str)->str:
		""" A 9-digit MMSI under the parent's country prefix (MID)
		Arguments
			parent -- The record's MMSI
			seed -- Text the number is derived from
		"""
		mid		= parent[:3] if (len(parent) == 9) and parent.isdigit() else '257'
		return mid + f'{zlib.crc32(seed.encode()) % 10**6:06d}'

	def criteria(self, profile):
		""" SQL filter for the rows this builder loads: only enabled vessels (REQ.035)
		Arguments
			profile -- (type code, class path) of the prototype
		Returns
			A WHERE clause
		"""
		return f'type={profile[0]} AND enabled=1'

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

		# A copy made by count= carries its own load of its class's deadweight
		if (guid in Builder.copies) and (inst.model is not None):
			u			= zlib.crc32( f'load/{guid}'.encode() ) / 0xFFFFFFFF
			inst.weight	= inst.model.lightship + (LOAD[0] + u*(LOAD[1] - LOAD[0])) * inst.model.deadweight
			inst.model.displace( inst.weight )

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


