#!/usr/bin/python
# Filename: Scales.py
# Description: Implementation of the Scales class

from cos.model.environment.Types import DynamicForce

import numpy as np
import os

class Scales:
	def __init__(self):
		""" Constructor
		"""
		unit_vector	= np.ones(3)

		# Scaling vector for maps
		self.map		= unit_vector

		# Scaling vectors for environmental forces
		self.weather	= {
				DynamicForce.WIND_CURRENT: unit_vector,
				DynamicForce.SEA_CURRENT: unit_vector,
				DynamicForce.SEA_WAVE: unit_vector
			}
		return


	# The simulation runs in metres. Map data (shapes, positions, trips, zones) is authored in map
	# units and converted once, when it is loaded, using map.unit.metres from the map's configs
	# table. Everything after loading is unaware of the map scale. Maps without the row use 1.0.

	def load(self, ctxt, path=None):
		""" Loads the metres-per-unit scale of the current map
		Arguments
			ctxt -- Simulation context
			path -- Map database with the configs table; defaults to $(MAP)/land.s3db
		"""
		from cos.core.utilities.ActiveRecord import ActiveRecord

		if path is None:
			path	= ctxt.sim.config.resolve( '$(MAP)/land.s3db' )

		scale	= [1.0, 1.0]
		self.map	= np.array( [1.0, 1.0, 1.0] )

		# Opening a missing database with sqlite would create an empty file
		if (path.startswith('$FS') == False) and (os.path.isfile(path) == False):
			return self.map

		try:
			db		= ActiveRecord.create( 'Config', path, 'configs' )
			for r in db.get_all( 'type=\'geo.reference\'' ):
				if r[1] == 'map.unit.metres.x':
					scale[0]	= float( r[3] )
				if r[1] == 'map.unit.metres.y':
					scale[1]	= float( r[3] )
		except Exception:
			pass		# No map database: one map unit is one metre

		self.map	= np.array( [scale[0], scale[1], 1.0] )
		return self.map

	@staticmethod
	def of(ctxt):
		""" The scales of the simulation world, or one metre per unit where there is no world
		(e.g. behaviours instantiated by the viewer, which receives data already in metres)
		Arguments
			ctxt -- Simulation context, may be None
		"""
		sim		= getattr( ctxt, 'sim', None ) if ctxt is not None else None
		world	= getattr( sim, 'world', None ) if sim is not None else None
		scales	= getattr( world, 'scales', None ) if world is not None else None
		return scales if scales is not None else Scales()

	@property
	def metres(self):
		""" Metres per map unit for lengths and speeds that have no direction
		"""
		return (self.map[0] + self.map[1]) / 2.0

	def transpose(self, x):
		scale	= self.map
		return (x[0]*scale[0], x[1]*scale[1])

	def point(self, v):
		""" Converts a point or vector [x, y, z, ...] from map units to metres (z is unchanged)
		"""
		out		= list(v)
		for n in range( min(2, len(out)) ):
			out[n]	= out[n]*self.map[n]
		return out

	def length(self, value):
		""" Converts a length or speed without direction from map units to metres
		"""
		return value*self.metres

	def rect(self, x, y, width, height):
		""" Converts a map rectangle to metres
		"""
		return ( x*self.map[0], y*self.map[1], width*self.map[0], height*self.map[1] )


if __name__ == "__main__":
	test = Scales()


