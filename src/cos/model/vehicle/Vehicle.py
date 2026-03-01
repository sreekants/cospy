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


VID = 0

class Vehicle(Object):
    def __init__(self, ctxt:Context, category:str, type, id:str, config:dict ):
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
        
        self.actor.create( ctxt, self, config )

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


