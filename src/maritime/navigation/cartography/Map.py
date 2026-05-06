#!/usr/bin/python
# Filename: Map.py
# Description: Fasade for Map related classes

from maritime.model.vessel.Vessel import Vessel, Status
from cos.math.geometry.Rectangle import Rectangle
from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context
from cos.core.time.Ticker import Ticker
from cos.core.utilities.ArgList import ArgList
from cos.math.geometry.Distance import Distance
from cos.model.geography.Sea import Sea, Type

import numpy as np

class Map(Service):
	def __init__(self):
		""" Constructor
		"""
		Service.__init__(self, "Controls/Navigation", "Map")

		self.zones_cache	= {}
		self.cross_dist		= None
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Service.on_start(self, ctxt, config)

		self.init_config(ctxt, config)
		self.init_objects(ctxt, config)
		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		Service.on_timer(self, ctxt, unused)

		self.monitor(ctxt)
		return

	def init_config(self, ctxt, config):
		""" Initializes the configuration
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Parse configurations
		args				= ArgList(config["config"])

		self.poll_at		= args["sample.frequency"]

		# Initialize timer ticks
		if self.poll_at is not None:
			self.timer	= Ticker( int(self.poll_at) )
		else:
			self.timer	= None

		return

	def init_objects(self, ctxt:Context, config):
		""" Initializes the simulation objects
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Load all the actors in the simulation
		objmgr				= ctxt.sim.objects
		self.world			= ctxt.sim.world
		self.vessels		= objmgr.get_all("/World/Vehicle/Vessel")
		self.land			= objmgr.get_all("/World/Land")
		self.sea			= objmgr.get_all("/World/Sea")

		self.reset()
		return


	def monitor(self, ctxt:Context):
		""" Monitors events on the simulation
		Arguments
			ctxt -- Simulation context
		"""

		# Calculate relative distances
		self.__monitor_vehicle_distance(ctxt)
		return
	
	def __monitor_vehicle_distance(self, ctxt:Context):
		processed	= set()

		for lhs in self.vessels:
			for rhs in self.vessels:
				if lhs is rhs:
					continue

				lvid	= lhs.vid
				lloc	= lhs.location

				rvid	= rhs.vid
				rloc	= rhs.location

				# Sort the vessel by identifiers, so we can use a monotinic reference
				if lvid > rvid:
					temp 	= lvid
					lvid	= rvid
					rvid	= temp

				# Check if the two are already mapped.
				crossref	= (lvid, rvid)
				if crossref in processed:
					continue
				
				dist	= Distance.euclidean(lloc, rloc)

				lndx	= self.vmap[lvid][0]
				rndx	= self.vmap[rvid][0]

				# Set the adjacency matrix values
				self.dist_map[lndx][rndx]	= dist
				self.dist_map[rndx][lndx]	= dist

				# Mark as processed
				processed.add( crossref )

		return

	def reset(self):
		self.__reset_vessels()
		self.__reset_zones()
		return
	
	def get_tss_bearing(self, _pt):
		"""Returns the required heading (degrees) for the TSS lane at pt, or None if unknown."""
		return None

	def get_bodies(self, type, bound:Rectangle):
		result		= list()
		return result

	def get_zones(self, type, bound:Rectangle):
		# Search the cache for the file
		if type in self.zones_cache:
			return self.zones_cache[type]
		
		result		= list()
		return result
	
	def get_nearest(self, vessel:Vessel, distance:float):
		result	= []
		vndx	= self.vmap[vessel.vid]

		for n in range(0, len(self.vessels)):
			if vndx[0] == n:
				continue
			
			d	= self.dist_map[vndx[0]][n]
			if d < distance:
				result.append((d, vndx[1]))
		return result

	def in_tss(self, obj):
		return Map.__in_bodies(self.tss, obj)

	def in_noentry(self, obj):
		return Map.__in_bodies(self.noentry, obj)

	def in_traffic(self, obj):
		return Map.__in_bodies(self.traffic, obj)

	def __reset_zones(self):
		self.tss		= []
		self.noentry	= []
		self.traffic	= []

		for o in self.sea:
			if o.type in [Type.TRAFFIC_SEPARATION_SCHEME, Type.SEPARATION_ZONE, Type.ROUNDABOUT, Type.INSHORE_TRAFFIC_ZONE, Type.AREA_TO_AVOID]:
				self.traffic.append(o)

			if o.type in [Type.TRAFFIC_SEPARATION_SCHEME, Type.INSHORE_TRAFFIC_ZONE]:
				self.tss.append(o)

			if o.type in [Type.AREA_TO_AVOID]:
				self.noentry.append(o)
		return

	def __reset_vessels(self):
		nvessel				= len(self.vessels)
		self.vmap			= {}

		# Build a map of vessel identifiers for indexed lookup. Vesse identifiers
		# are not guaranteed to be monotonous. So we build our own lookup map
		n	= 0
		for v in self.vessels:
			self.vmap[v.vid]	= (n, v)
			n					= n+1

		# Build an adjacency matrix
		self.dist_map			= np.zeros([nvessel, nvessel])
		return
	

	@staticmethod
	def __in_bodies(bodies, obj):
		rect	= obj.boundary if isinstance(obj, Vessel) else obj

		for body in bodies:
			if body.intersect(rect):
				return True

		return False


if __name__ == "__main__":
	test = Map()


