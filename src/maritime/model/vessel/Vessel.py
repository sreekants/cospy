#!/usr/bin/python
# Filename: Vessel.py
# Description: Types of vessels and their properties, states and characteristics

from cos.core.kernel.Context import Context
from cos.model.vehicle.Vehicle import Vehicle
from cos.core.utilities.ArgList import ArgList

from enum import Enum, Flag
import math

class Type(Flag):
    """Enum for the different types of vessel power drive."""

    POWER_DRIVEN        = 0x00000001   # Power driven vessel propelled by machinery
    SAILING             = 0x00000100   # Sail driven vessel
    SEAPLANE            = 0x00100001   # Sea plane
    WIG                 = 0x00200001   # Wing in ground crafts

class Operation(Flag):
    """Enum for the different types of vessel by operation."""

    FISHING             = 0x00000001   # Fishing vessel
    TRANSPORT           = 0x00000100   # Transport vessel
    CARGO               = 0x00001000   # Cargo and pcosisions vessel
    SERVICE             = 0x00002000   # Laying, servicing or picking up a navigation mark, submarine cable or pipeline etc.
    SAFETY              = 0x00100000   # Safety operation etc.
    MILITARY            = 0x00200000   # Military operation etc.

class Status(Flag):
    """Status of the vessel (by AIS/COLREG standards)"""
    UNKNOWN             = 0x00000000        # Catch-all for remaining values 9 - 15
    ANCHORED            = 0x00000001        # At anchor
    FASTENED            = 0x00000002
    AGROUND             = 0x00000004        # Aground
    MOORED              = 0x00000008        # Moored
    UNDERWAY            = 0x00000100        # Underway using engine
    NOT_UNDER_COMMAND   = 0x00000200        # Not under command
    RESTRICTED          = 0x00001000


class Restriction(Flag):
    """Enum for the different types of vessel constraints for restricted or constrained vessels."""
    NONE                = 0x00000000   # Unrestricted vessel
    SERVICING           = 0x00000001   # Laying, servicing or picking up a navigation mark, submarine cable or pipeline;
    TRANSPORTING        = 0x00000100   # Replenishment or transferring persons, pcosisions or cargo while underway;
    DREDGING            = 0x00010000   # Dredging vessel
    TOWING              = 0x00020000   # Engaged in a towing operation
    DRAUGHT             = 0x00000100   # Resticted by draught in relation to available depth and width of navigable water
    VISIBILITY          = 0x00000200   # Visibility restricted
    LAUNCHING           = 0x01000000   # Engaged in launching or recovery of aircraft
    PEACE_KEEEPING      = 0x02000000   # Engaged in mine clearance operations etc.
    OTHER               = 0x80000000   # Catch-all for remaining values

class Vessel(Vehicle):
    def __init__(self, ctxt, type, id, config ):
        """ Constructor
        Arguments
        	ctxt -- Simulation context
        	type -- Type of the object
        	id -- Unique identifier
        	config -- Configuration attributes
        """
        category	= 'Vessel'

        if id == None:
            id	= self.__class__.__name__

        Vehicle.__init__( self, ctxt, category, type, id, config )

        self.name           = config["name"]

        identifier          = config["identifier"]
        self.imo            = identifier["imo"]
        self.mmsi           = identifier["mmsi"]
        self.weight         = config['weight']

        self.operation      = 0
        self.status         = Status.UNKNOWN
        self.restriction    = Restriction.NONE

        # TODO: Load from the configuration
        self.underkeel_clearance   = 100
        self.motion_allowance      = 0
        self.squat                 = 0
        return

    @property
    def heading(self):
        """ Returns the object heading
        """
        V	= self.velocity
        return math.degrees(math.atan2( V[1], V[0] ))

    def describe(self):
        """ Returns a description of the vessel
        """
        return self.config

    def restrict(self, restriction:Restriction):
        """ Sets the vessel in a restricted state
        Arguments
        	restriction -- Type of restriction
        """
        self.status         = Status.RESTRICTED
        self.restriction    = restriction

    def state(self, status:Status):
        """ Sets the status of the vessel
        Arguments
        	status -- New status of the vessel
        """
        self.status        = status
        self.restriction   = Restriction.NONE

    def anchored(self):
        """ Sets the vessel state to anchored
        """
        self.state( Status.ANCHORED )

    def under_way(self):
        """ Sets the vessel state to under_way
        """
        self.state( Status.UNDERWAY )

    def moored(self):
        """ Sets the vessel state to moored
        """
        self.state( Status.MOORED )

    def aground(self):
        """ Sets the vessel state to aground
        """
        self.state( Status.AGROUND )


    def force(self, type, value):
        """ Updates he force vector on the vessel
        Arguments
        	type -- Type of the object
        	value -- Force vector
        """
        if self.actor.motion is None:
            return

        self.actor.motion.force[type]   = value
        return


    def init(self, ctxt:Context, args:ArgList ):
        """ Initializes the vessel
        Arguments
        	ctxt -- Simulation context
        	args -- List of arguments
        """
        return

if __name__ == "__main__":
	test = Vessel( Type.POWER_DRIVEN )


