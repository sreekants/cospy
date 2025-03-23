#!/usr/bin/python
# Filename: Sea.py
# Description: Implementation of the sea class

from cos.core.kernel.Context import Context
from cos.model.geography.Shape import Shape
from enum import Enum, Flag

class Type(Flag):
    """Enum for the different types of air behaviors."""
    FOG             			= 0x00000001
    CLOUD                       = 0x00000010

class Sky(Shape):
    def __init__(self, ctxt:Context, type, id, config ):
        """ Constructor
        Arguments
        	ctxt -- Simulation context
        	type -- Type of the object
        	id -- Unique identifier
        	config -- Configuration attributes
        """
        Shape.__init__(self, ctxt, 'Sky', type, id, config )

        self.type   = type
        self.height	= float(config['height'])
        return

    @property
    def nominal_height(self):
        """ Returns the nominal height of the sky
        """
        return self.height


if __name__ == "__main__":
	test = Sea()


