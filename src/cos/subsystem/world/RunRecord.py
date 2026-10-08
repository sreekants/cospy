#!/usr/bin/python
# Filename: RunRecord.py
# Description: Rows of the BI store's configs table that identify a run and its map (REQ-048-02, -03)

from cos.core.kernel.BootLoader import BootLoader
from cos.core.time.Clock import utcnow
from cos.math.geometry.GeoEncoder import GeoEncoder, BITS

import hashlib, os, socket, yaml

MAP_LAYERS		= ('Land', 'Sea', 'Sky')		# [Environment] keys whose YAML names the map databases
GEO_REFERENCE	= ('map.crs', 'map.origin.easting', 'map.origin.northing', 'map.axis.y',
				   'map.unit.metres.x', 'map.unit.metres.y', 'map.bounds')
PROBE			= ('10.255.255.255', 1)			# Non-local address; a UDP connect sends nothing

class RunRecord:
	@staticmethod
	def rows(ctxt, georef)->list:
		""" Builds the run record of the current simulation
		Arguments
			ctxt -- Simulation context
			georef -- The map's GeoReference
		Returns
			List of (name, type, value), values as text
		"""
		config	= ctxt.sim.config
		time	= utcnow().isoformat( timespec='microseconds' )
		host	= RunRecord.host()
		rows	= [
			('run.time',		'run',	time),
			('run.host',		'run',	host),
			('run.signature',	'run',	RunRecord.signature( time, host )),
		]

		scenario	= config.env.get( 'SCENARIO' )
		if scenario:
			rows.append( ('run.scenario', 'run', scenario) )
		rows.append( ('run.case', 'run', str(ctxt.sim.case_id)) )

		country, location	= config.env.get( 'COUNTRY' ), config.env.get( 'LOCATION' )
		if country and location:
			rows.append( ('map.key', 'run.map', f'{country}/{location}') )
		rows	+= [ (name, 'run.map', path) for name, path in RunRecord.databases( ctxt ) ]
		rows	+= RunRecord.georeference( georef, RunRecord.map_configs( ctxt ) )

		rows	+= [
			('position.encoding',	'run.position',	'morton'),
			('position.bits',		'run.position',	str(BITS)),
			('position.order',		'run.position',	'lon-high'),
		]
		return rows

	@staticmethod
	def host()->str:
		""" Hostname and outward IPv4 address, separated by '|'; the address is empty without a network
		"""
		address	= ''
		try:
			with socket.socket( socket.AF_INET, socket.SOCK_DGRAM ) as s:
				s.connect( PROBE )
				address	= s.getsockname()[0]
		except OSError:
			pass
		return f'{socket.gethostname()}|{address}'

	@staticmethod
	def signature(time:str, host:str)->str:
		""" SHA-256 of the run time and host
		Arguments
			time -- run.time
			host -- run.host
		"""
		return 'sha256:' + hashlib.sha256( f'{time}|{host}'.encode('utf-8') ).hexdigest()

	@staticmethod
	def databases(ctxt)->list:
		""" Map databases the run loads, from the database: entries of the [Environment] Land, Sea and Sky YAML
		Arguments
			ctxt -- Simulation context
		Returns
			List of (name, full path) of the databases that exist
		"""
		config	= ctxt.sim.config
		out		= []
		for key in MAP_LAYERS:
			if not config.exists_value( 'Environment', key ):
				continue
			try:
				data	= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes( config.get_file('Environment', key) ) ) or {}
			except Exception:
				continue

			paths	= []
			for module in (data.get('packages') or {}).get('modules') or []:
				if (not BootLoader.is_enabled(module)) or (module.get('database') is None):
					continue
				path	= os.path.abspath( config.resolve( module['database'] ) )
				if (path not in paths) and os.path.isfile( path ):
					paths.append( path )

			for i, path in enumerate( paths ):
				name	= f'map.database.{key.lower()}'
				out.append( (name if i == 0 else f'{name}.{os.path.splitext(os.path.basename(path))[0]}', path) )
		return out

	@staticmethod
	def map_configs(ctxt)->dict:
		""" geo.reference configs of the map's land database
		Arguments
			ctxt -- Simulation context
		"""
		from cos.core.utilities.ActiveRecord import ActiveRecord

		path	= ctxt.sim.config.resolve( '$(MAP)/land.s3db' )
		if not os.path.isfile( path ):
			return {}
		try:
			db	= ActiveRecord.create( 'Config', path, 'configs' )
			return { r[1]: r[3] for r in db.get_all( 'type=\'geo.reference\'' ) }
		except Exception:
			return {}

	@staticmethod
	def georeference(georef, configs:dict)->list:
		""" Map centre and georeference rows; none for a map without a georeference
		Arguments
			georef -- The run's GeoReference
			configs -- geo.reference configs of the map
		"""
		if (georef is None) or (not georef.georeferenced):
			return []

		rows	= []
		bounds	= configs.get( 'map.bounds' )
		if bounds:
			x0, y0, x1, y1	= ( float(v) for v in bounds.split(',') )
			lat, lon		= georef.map_to_gps( (x0 + x1) / 2.0, (y0 + y1) / 2.0 )
			lat, lon		= round( lat, 6 ), round( lon, 6 )		# The code encodes the stored values
			rows	+= [
				('map.centre.lat',	'run.map',	str(lat)),
				('map.centre.lon',	'run.map',	str(lon)),
				('map.centre.gps',	'run.map',	str(GeoEncoder.morton( lat, lon ))),
			]
		rows	+= [ (name, 'geo.reference', str(configs[name])) for name in GEO_REFERENCE if name in configs ]
		return rows


if __name__ == "__main__":
	print( RunRecord.host() )
