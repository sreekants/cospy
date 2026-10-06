#!/usr/bin/python
# Filename: GeoReference.py
# Description: Converts simulation positions to and from GPS (WGS84) using a map's geo.reference configs

from pyproj import CRS, Transformer
import math, os

WGS84			= 'EPSG:4326'
NORTH_STEP		= 1e-4		# Degrees of latitude used to find the direction of true north

class GeoReference:
	def __init__(self, crs=None, easting=0.0, northing=0.0, axis_y='south', metres=(1.0, 1.0)):
		""" Constructor
		Arguments
			crs -- Projected CRS of the map, e.g. 'EPSG:32648'; None for a map with no georeference
			easting -- Easting of map point (0, 0), metres
			northing -- Northing of map point (0, 0), metres
			axis_y -- 'south' when map y grows southward (all generated maps), else 'north'
			metres -- Metres per map unit (x, y)
		"""
		self.crs		= crs
		self.easting	= float(easting)
		self.northing	= float(northing)
		self.south		= str(axis_y).lower() == 'south'
		self.metres		= (float(metres[0]), float(metres[1]))
		self.to_ll		= None
		self.to_grid	= None
		if crs is not None:
			self.to_ll		= Transformer.from_crs( CRS(crs), WGS84, always_xy=True )
			self.to_grid	= Transformer.from_crs( WGS84, CRS(crs), always_xy=True )
		return

	@staticmethod
	def from_configs(configs:dict):
		""" Builds a georeference from a map's configs table
		Arguments
			configs -- Mapping of config name to value, e.g. {'map.crs': 'EPSG:32648', ...}
		Returns
			GeoReference; not georeferenced when map.crs or the origin is missing
		"""
		metres	= ( float(configs.get('map.unit.metres.x', 1.0)), float(configs.get('map.unit.metres.y', 1.0)) )
		crs		= configs.get('map.crs')
		e0		= configs.get('map.origin.easting')
		n0		= configs.get('map.origin.northing')
		if not crs or e0 is None or n0 is None:
			return GeoReference( metres=metres )
		return GeoReference( crs, e0, n0, configs.get('map.axis.y', 'south'), metres )

	@staticmethod
	def load(ctxt, path=None):
		""" Loads the georeference of the current map
		Arguments
			ctxt -- Simulation context
			path -- Map database with the configs table; defaults to $(MAP)/land.s3db
		"""
		from cos.core.utilities.ActiveRecord import ActiveRecord

		if path is None:
			path	= ctxt.sim.config.resolve( '$(MAP)/land.s3db' )

		# Opening a missing database with sqlite would create an empty file
		if (path.startswith('$FS') == False) and (os.path.isfile(path) == False):
			return GeoReference()

		try:
			db		= ActiveRecord.create( 'Config', path, 'configs' )
			configs	= { r[1]: r[3] for r in db.get_all( 'type=\'geo.reference\'' ) }
		except Exception:
			return GeoReference()
		return GeoReference.from_configs( configs )

	@property
	def georeferenced(self):
		""" True when positions can be converted to GPS
		"""
		return self.to_ll is not None

	def grid(self, x, y):
		""" Converts a simulation position to map-CRS easting and northing
		Arguments
			x -- Metres east of map point (0, 0)
			y -- Metres from map point (0, 0) along the map's y axis
		"""
		return self.easting + x, (self.northing - y) if self.south else (self.northing + y)

	def to_gps(self, x, y):
		""" Converts a simulation position in metres to latitude and longitude
		Arguments
			x -- Metres east of map point (0, 0)
			y -- Metres from map point (0, 0) along the map's y axis
		Returns
			(latitude, longitude) in degrees, or (None, None) without a georeference
		"""
		if not self.georeferenced:
			return None, None
		lon, lat	= self.to_ll.transform( *self.grid(x, y) )
		return lat, lon

	def from_gps(self, lat, lon):
		""" Converts latitude and longitude to a simulation position in metres
		Arguments
			lat -- Latitude, degrees
			lon -- Longitude, degrees
		Returns
			(x, y) in metres, or (None, None) without a georeference
		"""
		if not self.georeferenced:
			return None, None
		e, n	= self.to_grid.transform( lon, lat )
		return e - self.easting, (self.northing - n) if self.south else (n - self.northing)

	def map_to_gps(self, u, v):
		""" Converts a position in map units (as stored in the map databases) to latitude and longitude
		Arguments
			u -- Map x, map units
			v -- Map y, map units
		"""
		return self.to_gps( u*self.metres[0], v*self.metres[1] )

	def gps_to_map(self, lat, lon):
		""" Converts latitude and longitude to a position in map units
		Arguments
			lat -- Latitude, degrees
			lon -- Longitude, degrees
		"""
		x, y	= self.from_gps( lat, lon )
		if x is None:
			return None, None
		return x/self.metres[0], y/self.metres[1]

	def north_offset(self, x, y):
		""" Angle from map north to true north at a position (grid convergence)
		Arguments
			x -- Metres east of map point (0, 0)
			y -- Metres from map point (0, 0) along the map's y axis
		Returns
			Radians to add to a map bearing to make it a true bearing; 0 without a georeference
		"""
		if not self.georeferenced:
			return 0.0
		lat, lon	= self.to_gps( x, y )
		x2, y2		= self.from_gps( lat + NORTH_STEP, lon )
		dx, dy		= x2 - x, (y - y2) if self.south else (y2 - y)
		return -math.atan2( dx, dy )		# Map bearing of true north, negated

	def true_bearing(self, bearing, x, y):
		""" Converts a map bearing (clockwise from map north) to a true bearing at a position
		Arguments
			bearing -- Map bearing, radians
			x -- Metres east of map point (0, 0)
			y -- Metres from map point (0, 0) along the map's y axis
		"""
		if bearing is None:
			return None
		return (bearing + self.north_offset(x, y)) % (2*math.pi)

	def describe(self):
		""" One-line description for the run log
		"""
		if not self.georeferenced:
			return 'none (positions cannot be converted to GPS)'
		lat, lon	= self.to_gps( 0.0, 0.0 )
		return f'{self.crs}, map origin E {self.easting:.0f} N {self.northing:.0f} ({lat:.5f}, {lon:.5f}), y axis {"south" if self.south else "north"}'


if __name__ == "__main__":
	test = GeoReference()
