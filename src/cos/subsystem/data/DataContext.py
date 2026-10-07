#!/usr/bin/python
# Filename: DataContext.py
# Description: Snapshot of the dimension values (own ship, position) that accompany a fact row

from cos.math.geometry.GeoEncoder import GeoEncoder


class DataContext:
	""" Values for a fact row's dimension columns, taken when the event happens. Each attribute is
	named after a dimension leaf in the schema (Fleet.vessel -> vessel, Location.gps -> gps).
	"""
	def __init__(self, vessel=None, gps=None):
		""" Constructor
		Arguments
			vessel -- Own ship IMO, as the row's own-ship measure records it; None when there is none
			gps -- Morton code of the own ship's position; None when not known
		"""
		self.vessel	= vessel
		self.gps	= gps
		return

	@staticmethod
	def of(ctxt, vessel, vessel_id):
		""" Snapshot of an own ship now
		Arguments
			ctxt -- Simulation context
			vessel -- Own ship
			vessel_id -- The id the row records for it (its IMO)
		Returns
			DataContext; gps is None when the map has no georeference
		"""
		return DataContext( vessel_id, DataContext.position( ctxt, vessel ) )

	@staticmethod
	def position(ctxt, vessel):
		""" Morton code of a vessel's centre, or None without a georeference or a position
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel
		"""
		try:
			rect		= vessel.boundary
			rect		= rect() if callable( rect ) else rect		# a property on Vehicle
			georef		= ctxt.sim.world.georef
			lat, lon	= georef.to_gps( (rect.left + rect.right) / 2.0, (rect.top + rect.bottom) / 2.0 )
		except AttributeError:
			return None

		if lat is None:
			return None
		return GeoEncoder.morton( lat, lon )

	def value(self, leaf:str):
		""" Value for a dimension leaf; None when this context does not carry it
		Arguments
			leaf -- Dimension leaf name, e.g. 'vessel' or 'gps'
		"""
		return self.__dict__.get( leaf.lower() )

	def __repr__(self):
		return f'DataContext(vessel={self.vessel!r}, gps={self.gps!r})'


if __name__ == "__main__":
	test = DataContext( 9074729, 0 )
