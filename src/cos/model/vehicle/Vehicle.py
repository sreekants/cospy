#!/usr/bin/python
# Filename: Vehicle.py
# Description: Types of vessels and their properties, states and characteristics

from turtle import position

from cos.model.vehicle.Intent import Intent
from cos.model.vehicle.Signal import Signal
from cos.model.vehicle.Engine import Engine
from cos.model.vehicle.ValueSet import ValueSet
from cos.core.kernel.Object import Object
from cos.core.kernel.Context import Context
from cos.core.simulation.Actor import Actor, ActorBehavior
from cos.core.simulation.Snapshot import Snapshot
from cos.behavior.control.RudderBehavior import RudderBehavior
from cos.math.geometry.Rectangle import Rectangle
from cos.core.utilities.ArgList import ArgList

from enum import Enum, Flag
import numpy as np


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
        self.signal         = Signal()          # Lights, shapes and sound signals shown (REQ.036)
        self.mode           = ValueSet()
        self.model          = None
        self.fleet          = None
        
        self.actor.create( ctxt, self, config )

        # Rudder estimate for bridge displays, unless the vessel configures its own control.dynamics
        if ActorBehavior.CONTROL_DYNAMICS not in self.actor.behaviors:
            steering    = RudderBehavior( ctxt, config )
            self.actor.behaviors[steering.type]  = steering
            steering.intialize( ctxt, self.actor, self, config )

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

        state = Snapshot.state(self.guid)
        if state is not None:
            return state.x

        return self.actor.get_position()

    @property
    def velocity(self):
        """ Returns the object velocity
        """
        if self.actor == None:
            return None

        state = Snapshot.state(self.guid)
        if state is not None:
            return state.dx

        return self.actor.get_velocity()

    @property
    def acceleration(self):
        """ Returns the object acceleration
        """
        if self.actor == None:
            return None

        state = Snapshot.state(self.guid)
        if state is not None:
            return state.d2x

        return self.actor.get_acceleration()

    @property
    def boundary(self):
        """ REturns the bounding rectangle of the object
        """
        if self.actor == None:
            return None

        state = Snapshot.state(self.guid)
        if state is not None:
            return state.rect

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

        world.sim.ipc.publish( 'vessel.move', self.guid, {
            "guid":self.guid,
			"rect": [rect.left, rect.top, rect.right-rect.left, rect.bottom-rect.top],
            "angle": [dx[0],dx[1],dx[2]],
            "intent": self.intent,
            "signal": self.signal,
            "time": world.sim.clock.local.isoformat()     # Scenario local time, for the viewer's clock
            } )

        if world.sim.ipc.has_children( world.sim.ipc.bridge ):
            world.sim.ipc.publish( 'vessel.state', self.guid, self.bridge_state(world, rect, dx) )
        return

    def bridge_state(self, world, rect, dx):
        """ Builds the vessel.state event for bridge displays (SI units; heading and COG clockwise from map north, north_offset makes them true)
        Arguments
        	world -- Reference ot the simulation world
        	rect -- Bounding rectangle in metres
        	dx -- Velocity in metres per simulated second; map y grows southward, as cviz draws it
        """
        now         = world.sim.clock.local
        vx, vy      = float(dx[0]), float(dx[1])
        sog         = float(np.hypot(vx, vy))
        cog         = float(np.arctan2(vx, -vy) % (2*np.pi)) if sog > 1e-6 else None

        # Heading follows course; with no leeway model they are the same. Held while stopped.
        heading     = cog if cog is not None else getattr(self, '_bridge_heading', None)
        rot         = None
        last        = getattr(self, '_bridge_last', None)
        if heading is not None and last is not None and last[0] is not None:
            elapsed = (now - last[1]).total_seconds()
            if elapsed > 0:
                turn    = (heading - last[0] + np.pi) % (2*np.pi) - np.pi
                rot     = float(turn / elapsed)
        self._bridge_last       = (heading, now)
        self._bridge_heading    = heading

        steering    = self.actor.behaviors.get(ActorBehavior.CONTROL_DYNAMICS) if self.actor.behaviors else None
        rudder, order   = steering.observe(rot, sog, now) if hasattr(steering, 'observe') else (None, None)

        x           = rect.left + (rect.right-rect.left)/2.0
        y           = rect.top + (rect.bottom-rect.top)/2.0
        georef      = getattr(world, 'georef', None)
        lat, lon    = georef.to_gps(x, y) if georef is not None else (None, None)
        north       = georef.north_offset(x, y) if lat is not None else None

        return {
            "guid": self.guid,
            "name": self.config.get('name'),
            "imo": (self.config.get('identifier') or {}).get('imo'),
            "time": now.isoformat(),
            "x": x,
            "y": y,
            "lat": lat,
            "lon": lon,
            "north_offset": north,
            "heading": heading,
            "cog": cog,
            "sog": sog,
            "stw": None,
            "rot": rot,
            "rudder": rudder,
            "rudder_order": order,
            "rudder_source": "estimated" if rudder is not None else None,
            "propulsion": None,
            "intent": str(self.intent)
            }

    def sim_init(self, world, rect):
        """ Initialize the simulation
        Arguments
        	world -- Reference ot the simulation world
        	rect -- Location of the object (bounding box)
        """
        if rect is None and self.actor.motion is not None:
            pos     = self.actor.motion.position
        else:
            X	    = self.config['pose']['position']
            pos     = np.array( (X[0], X[1]) )

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

    def raise_signal(self, name:str):
        """ Shows a light, shape or sound signal
        Arguments
        	name -- Signal name from the vocabulary, e.g. 'Sound.Foghorn'
        """
        self.signal.set( name )
        return

    def lower_signal(self, name:str):
        """ Stops showing a signal
        Arguments
        	name -- Signal name
        """
        self.signal.reset( name )
        return

    def is_signaled(self, pattern:str)->bool:
        """ Checks whether a signal matching a pattern is shown
        Arguments
        	pattern -- Signal name or wildcard pattern, e.g. 'Sound.Foghorn*'
        """
        return self.signal.find( pattern )

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


