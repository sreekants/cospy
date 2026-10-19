#!/usr/bin/python
# Filename: Vessel.py
# Description: Types of vessels and their properties, states and characteristics

from cos.core.kernel.Context import Context
from cos.math.geometry import Rectangle
from cos.model.vehicle.Vehicle import Vehicle
from cos.model.vehicle.Signal import Signal
from cos.core.utilities.ArgList import ArgList
from cos.math.geometry.Rectangle import Rectangle

from enum import Enum, Flag
from typing import Any
import math, random, os, yaml
import numpy as np

SIGNALS     = '$(CONFIG)/maritime/signals.yaml'     # Signal vocabulary (REQ.036)
EVALUATOR   = '$(CONFIG)/evaluator.yaml'            # Draught bounds (COS.049)

def afloat(vessels)->list:
    """ The vessels at sea: every vessel but the meta vessels, such as fleet controllers
    Arguments
    	vessels -- Vessels, e.g. every object under /World/Vehicle/Vessel
    """
    return [ v for v in vessels if not getattr(v, 'meta', False) ]

class Type(Flag):
    """Enum for the different types of vessel power drive."""

    POWER_DRIVEN        = 0x00000001   # Power driven vessel propelled by machinery
    SAILING             = 0x00000100   # Sail driven vessel
    SEAPLANE            = 0x00100001   # Sea plane
    WIG                 = 0x00200001   # Wing in ground crafts
    META_VESSEL         = 0x10000000   # Meta vessel (for grouping and other purposes)         
    FLEET               = 0x10001000   # Fleet of vessels

class Operation(Flag):
    """Enum for the different types of vessel by operation."""

    FISHING             = 0x00000001   # Fishing vessel
    TRANSPORT           = 0x00000100   # Transport vessel
    CARGO               = 0x00001000   # Cargo and pcosisions vessel
    SERVICE             = 0x00002000   # Laying, servicing or picking up a navigation mark, submarine cable or pipeline etc.
    TOWING              = 0x00010000   # Towing another vessel astern (Rule 24(a))
    PUSHING             = 0x00020000   # Pushing ahead or towing alongside (Rule 24(c))
    PILOTAGE            = 0x00040000   # Pilot vessel on pilotage duty (Rule 29)
    SAFETY              = 0x00100000   # Safety operation etc.
    MILITARY            = 0x00200000   # Military operation etc.
    FLIGHT              = 0x00400000   # WIG craft taking off, landing or in flight near the surface (Rule 23(c))

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
    MINE_CLEARANCE      = 0x02000000   # Engaged in mine clearance operations etc.
    OTHER               = 0x80000000   # Catch-all for remaining values

class Vessel(Vehicle):
    def __init__(self, ctxt, type, id, config:dict ):
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
        self.vessel_type    = type      # Type enum; self.type is the object scope, e.g. 'Vessel.Type.POWER_DRIVEN'

        self.name           = config["name"]

        identifier          = config["identifier"]
        self.imo            = identifier["imo"]
        self.mmsi           = identifier["mmsi"]
        self.weight         = config['weight']     # Tonnes; None or 0 falls back to the category mass
        settings            = ArgList( config.get('settings', '') or '' )
        self.draft          = settings['draft']             # Metres; None falls back to the ship model
        self.cargo_weight   = settings['cargo_weight']      # Tonnes of cargo aboard; None leaves the weight to the record or model
        self.recid          = int( identifier["imo"] )     # Vessel IMO: the vessel's id in every fact table

        self.operation      = 0
        self.tow_length     = 0.0       # Metres, stern of the towing vessel to the after end of the tow (Rule 24)
        self.status         = Status.UNKNOWN
        self.restriction    = Restriction.NONE
        self.situations     = []        # Active situations; a faculty removes each when it ends

        Vessel.load_signals( ctxt )

        # TODO: Load from the configuration
        self.underkeel_clearance   = .1
        self.motion_allowance      = 0
        self.squat                 = 0
        return

    @property
    def meta(self)->bool:
        """ Whether this is a meta vessel, e.g. a fleet controller, rather than a vessel at sea
        """
        return bool( self.vessel_type & Type.META_VESSEL )

    @property
    def weight(self):
        """ Displacement in tonnes: the vessel record's weight, else the ship model's lightship plus the
        record's cargo_weight, else the ship model's mass, else None
        """
        if self.instance_weight:
            return float( self.instance_weight )

        model   = getattr( self, 'model', None )
        if model is None:
            return None

        cargo   = self.cargo_weight
        return model.lightship + cargo if cargo is not None else model.mass

    @weight.setter
    def weight(self, value):
        self.instance_weight    = value

    @property
    def cargo_weight(self):
        """ Tonnes of cargo aboard from the vessel record's settings (cargo_weight=), or None
        Raises
        	ValueError when the setting is not a number of tonnes, 0 or more
        """
        value   = getattr( self, 'instance_cargo_weight', None )
        if value is None:
            return None

        try:
            tonnes  = float( value )
        except ValueError:
            raise ValueError( f'vessel.s3db settings of {self.name}: cargo_weight={value} is not a number of tonnes' )
        if tonnes < 0.0:
            raise ValueError( f'vessel.s3db settings of {self.name}: cargo_weight={value} is negative' )
        return tonnes

    @cargo_weight.setter
    def cargo_weight(self, value):
        self.instance_cargo_weight  = value

    @property
    def draft(self):
        """ Draught in metres: the vessel record's settings, else the ship model's, else None
        """
        override    = getattr( self, 'instance_draft', None )
        if override:
            return float( override )

        model   = getattr( self, 'model', None )
        return float( model.draft ) if model is not None else None

    @draft.setter
    def draft(self, value):
        self.instance_draft     = value

    @property
    def heading(self):
        """ Returns the object heading
        """
        V	= self.velocity
        return math.degrees(math.atan2( V[1], V[0] ))

    @staticmethod
    def load_signals(ctxt):
        """ Loads the signal vocabulary of the scenario once
        Arguments
        	ctxt -- Simulation context; without a configuration nothing is loaded
        """
        sim     = getattr( ctxt, 'sim', None )
        config  = getattr( sim, 'config', None )
        if config is None:
            return None

        return Signal.configure( config.resolve(SIGNALS), getattr(ctxt, 'log', None) )

    bounds  = {}        # Resolved evaluator.yaml path -> (draught_max, draught_length_ratio_max)

    @staticmethod
    def check_draught(ctxt, vessel, source:str):
        """ Raises when a vessel declares a draught too deep for any ship or for its length
        Arguments
        	ctxt -- Simulation context
        	vessel -- Vessel with its ship model loaded
        	source -- Ship model file the draught came from, unless the vessel record overrides it
        Raises
        	ValueError naming the source, the draught and the bound it exceeds
        """
        draft   = vessel.draft
        model   = getattr( vessel, 'model', None )
        if (draft is None) or (model is None):
            return

        limit, ratio    = Vessel.draught_bounds( ctxt )
        if getattr( vessel, 'instance_draft', None ):
            source  = f'vessel.s3db settings of {vessel.name}'

        length  = float( model.ship.length )
        if (limit is not None) and (draft > limit):
            raise ValueError( f'{source}: draught {draft} m exceeds draught_max {limit} m' )
        if (ratio is not None) and (length > 0.0) and (draft > ratio*length):
            raise ValueError( f'{source}: draught {draft} m exceeds draught_length_ratio_max {ratio} of length {length} m' )
        return

    @staticmethod
    def draught_bounds(ctxt)->tuple:
        """ Draught bounds from evaluator.yaml, read once per file
        Arguments
        	ctxt -- Simulation context
        Returns
        	(draught_max, draught_length_ratio_max), each None when not configured
        """
        path    = ctxt.sim.config.resolve( EVALUATOR )
        if path not in Vessel.bounds:
            config  = {}
            if os.path.exists( path ):
                with open( path, 'rb' ) as f:
                    config  = (yaml.safe_load( f ) or {}).get( 'evaluator', {} ) or {}
            Vessel.bounds[path] = ( config.get('draught_max'), config.get('draught_length_ratio_max') )
        return Vessel.bounds[path]

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

        self.actor.motion.forces[type]   = value
        return


    def init(self, ctxt:Context, args:ArgList ):
        """ Initializes the vessel
        Arguments
        	ctxt -- Simulation context
        	args -- List of arguments
        """
        self.__register_callbacks( ctxt, args )
        return

    def runnable(self, ctxt:Context, config):
        """ Checks if the object is runnable
        Arguments
            ctxt -- Simulation context
            config -- Config information
        """
        if self.actor.runnable(ctxt, (config, self.config)) == False:
            return False
        
        return True

    def data(self):
        """ Returns a description of the vessel
        """
        msgid = random.randrange(1000, 10000)
        return {
                'id': self.vid, 
                'guid': self.id, 
                'data':{
                    'angle':f"{msgid+1000}",
                    'angleAdvices':[],
                    'angleSetpoint':f"{msgid+2000}", 
                    'bottomPropeller':None,
                    'autoAtAngleSetpointDeadband':2,
                    'autoAtThrustSetpointDeadband':1,
                    'disableAutoAtAngleSetpoint':False,
                    'disableAutoAtThrustSetpoint':False,
                    'loading':False,
                    'longitude':0,
                    'latutude':0,
                    'noPadding':False,
                    'singleDirection':False,
                    'starboardPortIndicator':False,
                    'state':True,
                    'topPropeller':None,
                    'touching':False,
                    'thrust':f"{msgid+3000}", 
                    'thrustSetpoint':f"{msgid+4000}",
                    'thrustSetpointAtZeroDeadband':.1,
                    'thrustAdvices':[]
                    }
            }

    def __register_callbacks(self, ctxt:Context, args:ArgList ):
        """ Initializes the vessel
        Arguments
        	ctxt -- Simulation context
        	args -- List of arguments
        """
        self.subscribe( "bridge.control", self.__bridge_control )
        return

    def __bridge_control(self, ctxt:Context, arg:Any):
        """ Handles bridge control commands
        Arguments
        	ctxt -- Simulation context
        	arg -- Message argumnt
        """
        self.actor.notify( ctxt, "bridge.control", arg )
        return
    
    def locate_at(self, position):
        """ Locates the vessel at a new position
        Arguments
        	position -- New position to locate the vessel at
        """
        boundary            = self.actor.rect
        self.actor.rect     = Rectangle(position[0] - boundary.w/2, position[1] - boundary.h/2, boundary.width, boundary.height) 
        self.actor.x        = np.array(position, dtype=float)      # What location and the rule snapshots read
        return

    def heading_towards(self, velocity):
        """ Orients the vessel towards a new direction
        Arguments
        	velocity -- New velocity vector to orient the vessel towards
        """
        self.actor.dx   = velocity
        return

if __name__ == "__main__":
	test = Vessel( Type.POWER_DRIVEN )


