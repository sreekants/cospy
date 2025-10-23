#!/usr/bin/python
# Filename: Sea.py
# Description: Implementation of the sea class

from cos.model.geography.Shape import Shape
from cos.core.kernel.Context import Context

from enum import Enum, Flag

class Type(Flag):
    """Enum for the different types of sea terrain."""
    # Topological classifications
    STRANDFLAT        			= 0x00000001
    CONTINENTAL_SLOPE           = 0x00000010
    MARINE_VALLEY            	= 0x00000100
    FJORD                 		= 0x00001000
    ABYSSAL_PLAIN               = 0x00010000
    CONTINENTAL_SHELF_PLAIN     = 0x00020000
    MARINE_MOUNTAIN          	= 0x00040000

    # Jurisdictional classifications
    EXCLUSIVE_ECONOMIC_ZONE     = 0x20000001
    CONTIGUOUS_ZONE             = 0x20000100
    TERRITORIAL_SEA             = 0x20000200
    INTERNAL_WATERS             = 0x20000400
    MARITIME_EXCLUSION_ZONE     = 0x21000000

    STRAIT                      = 0x20001000
    HARBOUR                     = 0x20002000
    ARCHIPELAGIC_WATERS         = 0x20004000

    # Navigation (&traffic)-related classifications
    WATERWAY                    = 0x40000002
    TRAFFIC_SEPARATION_SCHEME   = 0x40001000
    TRAFFIC_LANE                = 0x40002000
    SEPARATION_ZONE             = 0x40004000
    ROUNDABOUT                  = 0x40010000
    INSHORE_TRAFFIC_ZONE        = 0x40020000
    RECOMMENDED_ROUTE           = 0x40030000
    DEEP_WATER_ROUTE            = 0x40040000
    PRECAUTIONARY_AREA          = 0x40050000
    AREA_TO_AVOID               = 0x40060000

class Sea(Shape):
    def __init__(self, ctxt:Context, type, id, config ):
        """ Constructor
        Arguments
        	ctxt -- Simulation context
        	type -- Type of the object
        	id -- Unique identifier
        	config -- Configuration attributes
        """
        Shape.__init__(self, ctxt, 'Sea', type, id, config )

        self.type   = type
        self.depth	= float(config['depth'])
        self.name	= config['name']
        return

    @property
    def nominal_depth(self):
        """ Nominal depth of the sea
        """
        return self.depth


    def get_float_property(self, config, name):
        val	= config.get(name, None )
        if val is None:
            return None
        
        return float(val)

    def get_int_property(self, config, name):
        if config is None:
            return None
        
        val	= config.get(name, None )
        if val is None:
            return None
        
        return int(val)

    def get_property(self, config, name):
        if config is None:
            return None
        
        return config.get(name, None )

if __name__ == "__main__":
	test = Sea()


