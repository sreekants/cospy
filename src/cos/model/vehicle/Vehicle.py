#!/usr/bin/python
# Filename: Vehicle.py
# Description: Types of vessels and their properties, states and characteristics

from cos.model.vehicle.Intent import Intent
from cos.model.vehicle.Engine import Engine
from cos.model.vehicle.ValueSet import ValueSet
from cos.core.kernel.Object import Object
from cos.core.kernel.Context import Context
from cos.core.simulation.Actor import Actor, ActorBehavior
from cos.math.geometry.Rectangle import Rectangle
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

VID = 0

class Vehicle(Object):
    def __init__(self, ctxt:Context, category, type, id, config ):
        """ Constructor
        Arguments
        	ctxt -- Simulation context
        	category -- Category of the object
        	type -- Type of the object
        	id -- Unique identifier
        	config -- Configuration attributes
        """
        if id == None:
            id	= self.__class__.__name__

        scope	= f'{category}/{type}'

        Object.__init__( self, scope, id, id )
        self.config         = config
        self.actor		    = Actor(ctxt, config)
        self.devices        = {}
        self.engine         = Engine()

        # Property sets
        self.intent         = Intent()
        self.mode           = ValueSet()
        
        # Builds the values.
        self.build_values()

        global VID

        VID                 = VID+1
        self.vid            = VID
        return

    def build_values(self):
        """ Buids the values
        """
        # Builds the operation manifest
        self.operation      = ValueSet()

        # Builds the cargo manifest
        self.cargo  = ValueSet()
        args    = ArgList( self.config.get('settings', '') )
        cargo   = args['cargo']
        if cargo is not None:
            for c in cargo.split(','):
                self.cargo.add(c)
        return

    def describe(self):
        """ Describes the object confituration
        """
        return self.config

    @property
    def location(self):
        """ Returns the object location
        """
        if self.actor == None:
            return None

        return self.actor.get_position()

    @property
    def velocity(self):
        """ Returns the object velocity
        """
        if self.actor == None:
            return None

        return self.actor.get_velocity()

    @property
    def acceleration(self):
        """ Returns the object acceleration
        """
        if self.actor == None:
            return None

        return self.actor.get_acceleration()

    @property
    def boundary(self):
        """ REturns the bounding rectangle of the object
        """
        if self.actor == None:
            return None
        return self.actor.rect

    # Simulation functions
    def sim_update(self, world):
        """ Updates the simulation
        Arguments
        	world -- Reference ot the simulation world
        """
        rect, dx, result    = self.actor.update(world, self.config)
        if rect == None:
            return

        world.sim.ipc.push( '/IPC', 'vessel.move', None, [{
            "guid":self.guid,
			"rect": [rect.left, rect.top, rect.right-rect.left, rect.bottom-rect.top],
            "angle": [dx[0],dx[1],dx[2]]
            }] )
        return

    def sim_init(self, world, rect):
        """ Initialize the simulation
        Arguments
        	world -- Reference ot the simulation world
        	rect -- Location of the object (bounding box)
        """
        if rect is None:
            pos     = self.actor.motion.position
            rect    = (pos[0],pos[1], 20, 10)

        self.actor.init( Rectangle( rect[0], rect[1], rect[2], rect[3]) )

        self.motion	    = self.actor.behaviors.get(ActorBehavior.MOTION)
        return

    def force(self, type, value):
        """ Sets a force vector on the vehicle
        Arguments
        	type -- Type of the object
        	value -- Force vector
        """
        if self.motion is not None:
            self.motion.force(type, value)
        return

    def device(self, name:str):
        """ Returns a device onboard the vehicle
        Arguments
        	name -- Name of the object
        """
        return self.devices.get(name)

    def ioctl( self, op, arg ):
        """ Sends a signal to the actors
        Arguments
        	op -- Operation code
            arg -- arguments for the operation
        """

        for behavior in self.actor.behaviors.values():
            behavior.ioctl( op, arg )

        return

if __name__ == "__main__":
	test = Vehicle( Type.POWER_DRIVEN )


