#!/usr/bin/python
# Filename: Land.py
# Description: Implementation of the land class

from cos.model.geography.Shape import Shape
from cos.core.kernel.Context import Context

from enum import Enum, Flag

class Type(Flag):
    """Enum for the different types of land terrain."""

    MOUNTAIN        	= 0x00000001
    PLAIN           	= 0x00000010
    PLATEAU            	= 0x00000100
    DESERT              = 0x00001000

class Land(Shape):
    def __init__( self, ctxt:Context, type, id, config ):
        """ Constructor
        Arguments
        	ctxt -- Simulation context
        	type -- Type of the object
        	id -- Unique identifier
        	config -- Configuration attributes
        """
        Shape.__init__(self, ctxt, 'Land', type, id, config )

        self.type   = type
        self.height	= float(config['height'])
        return


if __name__ == "__main__":
	test = Land()


