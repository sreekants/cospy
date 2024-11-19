#!/usr/bin/python
# Filename: TrafficZone.py
# Description: Implementation of the traffic zones class

from cos.model.geography.Sea import Sea, Type
from cos.core.kernel.Context import Context
from cos.math.geometry.Rectangle import Rectangle

class TrafficZone(Sea):
	def __init__( self, ctxt:Context, type, id, config ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
        	type -- Type of the object
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Sea.__init__( self, ctxt, type, id, config )

		self.safe_distance	= self.get_float_property(config, 'safe_distance')
		self.safe_heading	= self.get_float_property(config, 'safe_heading')
		return


	def has_entered(self, points):
		""" Checks if a shape has entered the zone
		Arguments
			points -- Points which describes the shape
		""" 

		for p in points:
			if self.area.encloses(p[0], p[1]):
				return True
			
		return False

	def has_entered_rect(self, rect:Rectangle):
		""" Checks if a rectangle has entered the zone
		Arguments
			rect -- Rectangle from which describes the shape
		""" 

		return self.has_entered( [rect.topleft, rect.topright, rect.bottomleft, rect.bottomright] )

if __name__ == "__main__":
	test = TrafficZone()


