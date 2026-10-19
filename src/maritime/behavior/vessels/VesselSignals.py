#!/usr/bin/python
# Filename: VesselSignals.py
# Description: Lights, day shapes and fog signals a vessel shows for its state (COLREG Rules 23, 25, 26, 27, 30, 35)

from maritime.model.vessel.Vessel import Type, Status, Operation
from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.resolver.VesselDeclarationsResolver import VesselDeclarationsResolver
from cos.model.vehicle.Signal import Signal

import types, yaml
import numpy as np

LEGATA		= '$(CONFIG)/legata.yaml'		# Same visibility, night window and constants as the rules

# State -> signals, each with the condition (a key of WHEN) under which it is shown
TABLE	= {
	'power_driven': {												# Rule 23 (a), (d)(i); Rule 35 (a), (b)
		'lights': [ ('Light.Masthead.Forward.1x', 'length >= 12'), ('Light.Masthead.Abaft', 'length >= 50'),
					('Light.Sidelight', None), ('Light.Sternlight', 'length >= 12'), ('Light.Allround.White', 'length < 12') ],
		'shapes': [],
		'sounds': [ ('Sound.Foghorn.Prolonged.1x', 'making way'), ('Sound.Foghorn.Prolonged.2x', 'not making way') ],
	},
	'sailing': {													# Rule 25 (a); Rule 35 (c)
		'lights': [ ('Light.Sidelight', None), ('Light.Sternlight', None) ],
		'shapes': [],
		'sounds': [ ('Sound.Foghorn.Prolonged.Short.2x', None) ],
	},
	'not_under_command': {											# Rule 27 (a); Rule 35 (c)
		'lights': [ ('Light.Allround.Red.2x', None), ('Light.Sidelight', 'making way'), ('Light.Sternlight', 'making way') ],
		'shapes': [ ('Shape.Ball.2x', None) ],
		'sounds': [ ('Sound.Foghorn.Prolonged.Short.2x', None) ],
	},
	'restricted': {													# Rule 27 (b)(i)-(iii); Rule 35 (c)
		'lights': [ ('Light.Allround.RedWhiteRed', None), ('Light.Masthead.Forward.1x', 'making way'),
					('Light.Masthead.Abaft', 'making way, length >= 50'),
					('Light.Sidelight', 'making way'), ('Light.Sternlight', 'making way') ],
		'shapes': [ ('Shape.BallDiamondBall', None) ],
		'sounds': [ ('Sound.Foghorn.Prolonged.Short.2x', None) ],
	},
	'trawling': {													# Rule 26 (b); Rule 35 (c), (d)
		'lights': [ ('Light.Allround.GreenWhite', None), ('Light.Masthead.Abaft', 'length >= 50'),
					('Light.Sidelight', 'making way'), ('Light.Sternlight', 'making way') ],
		'shapes': [ ('Shape.Cones.ApexTogether', None) ],
		'sounds': [ ('Sound.Foghorn.Prolonged.Short.2x', None) ],
	},
	'fishing': {													# Rule 26 (c), other than trawling; Rule 35 (c), (d)
		'lights': [ ('Light.Allround.RedWhite', None), ('Light.Sidelight', 'making way'), ('Light.Sternlight', 'making way') ],
		'shapes': [ ('Shape.Cones.ApexTogether', None) ],
		'sounds': [ ('Sound.Foghorn.Prolonged.Short.2x', None) ],
	},
	'anchored': {													# Rule 30 (a), (c); Rule 35 (g); the bell also under 20 m ((i), (j))
		'lights': [ ('Light.Anchor.Forward', None), ('Light.Anchor.Aft', None), ('Light.Deck', 'length >= 100') ],
		'shapes': [ ('Shape.Ball.1x', None) ],
		'sounds': [ ('Sound.Bell', None), ('Sound.Gong', 'length >= 100') ],
	},
	'aground': {													# Rule 30 (d); Rule 35 (h); the bell also under 20 m ((i), (j))
		'lights': [ ('Light.Anchor.Forward', None), ('Light.Anchor.Aft', None), ('Light.Allround.Red.2x', None) ],
		'shapes': [ ('Shape.Ball.3x', None) ],
		'sounds': [ ('Sound.Bell', None), ('Sound.Bell.Strokes.3x', None), ('Sound.Gong', 'length >= 100') ],
	},
	'moored': { 'lights': [], 'shapes': [], 'sounds': [] },
}

WHEN	= {
	None						: lambda s: True,
	'length < 12'				: lambda s: s.length < 12,
	'length >= 12'				: lambda s: s.length >= 12,
	'length >= 50'				: lambda s: s.length >= 50,
	'length >= 100'				: lambda s: s.length >= 100,
	'making way'				: lambda s: s.making_way,
	'not making way'			: lambda s: not s.making_way,
	'making way, length >= 50'	: lambda s: s.making_way and (s.length >= 50),
}

PREFIX	= { 'lights': 'Light.', 'shapes': 'Shape.', 'sounds': 'Sound.' }


class VesselSignals:
	conditions	= None		# Shared by every vessel; read once from legata.yaml

	def __init__(self):
		return

	@classmethod
	def configure(cls, ctxt, path:str=LEGATA):
		""" Reads the visibility, night window and constants the rules use, once per process
		Arguments
			ctxt -- Simulation context
			path -- legata.yaml
		"""
		if cls.conditions is not None:
			return cls.conditions

		file		= ctxt.sim.config.resolve( path )
		config		= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(file) )
		entries		= { r['scope']: r for r in config['language']['resolvers'] }

		target		= TargetResolver()
		target.init( ctxt, entries['target'] )
		decls		= VesselDeclarationsResolver()
		decls.init( ctxt, entries['vessel'] )

		cls.conditions	= types.SimpleNamespace(
			target		= target,
			visibility	= target.visibility,
			range		= float( decls.decls['RestrictedVisibility.Range'] ),
			making_way	= float( decls.decls['MakingWay.Speed'] ) )
		return cls.conditions

	@staticmethod
	def state(vessel)->str:
		""" Row of TABLE for a vessel's status, operation and type
		Arguments
			vessel -- Vessel
		"""
		status	= vessel.status
		if status == Status.AGROUND:
			return 'aground'
		if status == Status.NOT_UNDER_COMMAND:
			return 'not_under_command'
		if status == Status.RESTRICTED:
			return 'restricted'

		# Fishing at anchor shows the fishing signals (Rule 35(d))
		operation	= getattr( vessel, 'operation', 0 ) or 0
		if Operation.FISHING.value & (operation.value if isinstance(operation, Operation) else int(operation)):
			gear	= getattr( getattr(vessel, 'model', None), 'fishing_gear', 'other' )
			return 'trawling' if gear == 'trawl' else 'fishing'

		if status == Status.ANCHORED:
			return 'anchored'
		if status in (Status.MOORED, Status.FASTENED):
			return 'moored'

		kind	= getattr( vessel, 'vessel_type', vessel.type )
		if isinstance( kind, Type ) and (Type.SAILING in kind):
			return 'sailing'

		return 'power_driven'

	@staticmethod
	def required(vessel, kind:str, speed:float, making_way:float)->list:
		""" Signals of one kind a vessel's state requires
		Arguments
			vessel -- Vessel
			kind -- 'lights', 'shapes' or 'sounds'
			speed -- Speed over ground, metres per second
			making_way -- Speed above which a vessel is making way
		"""
		model	= getattr( vessel, 'model', None )
		facts	= types.SimpleNamespace(
			length		= float( model.ship.length ) if model is not None else 0.0,
			making_way	= speed > making_way )

		return [ name for name, when in TABLE[VesselSignals.state(vessel)][kind] if WHEN[when](facts) ]

	@staticmethod
	def show(vessel, kind:str, names:list):
		""" Replaces the signals of one kind a vessel shows; encounter signals (Rule 34) are left alone
		Arguments
			vessel -- Vessel
			kind -- 'lights', 'shapes' or 'sounds'
			names -- Signals to show
		"""
		prefix	= PREFIX[kind]
		for name in [ n for n in vessel.signal if n.startswith(prefix) and (n not in names) ]:
			if Signal.category( name ) != 'encounter':
				vessel.lower_signal( name )

		for name in names:
			vessel.raise_signal( name )
		return

	@staticmethod
	def update(b, kind:str, shown, dx):
		""" Shows the signals of one kind when shown(night, restricted) holds, and none otherwise
		Arguments
			b -- Vessel behaviour
			kind -- 'lights', 'shapes' or 'sounds'
			shown -- Function of (night, restricted visibility)
			dx -- Velocity the behaviour has set
		"""
		c			= VesselSignals.conditions
		vessel		= b.vehicle
		if (c is None) or (vessel is None):
			return dx

		night		= c.target.is_night( getattr(b.clock, 'local', None) )
		restricted	= c.visibility < c.range
		speed		= float( np.linalg.norm(dx[:2]) ) if dx is not None else 0.0

		names		= VesselSignals.required( vessel, kind, speed, c.making_way ) if shown(night, restricted) else []
		VesselSignals.show( vessel, kind, names )
		return dx

	@staticmethod
	def navigation_lights(b, world, t, dx):
		""" Lights at night or in restricted visibility (Rule 20(b), (c)); none by day in clear visibility
		Arguments
			b -- Vessel behaviour
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			dx -- Velocity the behaviour has set
		"""
		return VesselSignals.update( b, 'lights', lambda night, restricted: night or restricted, dx )

	@staticmethod
	def day_shapes(b, world, t, dx):
		""" Day shapes, by day only (Rule 20(d))
		Arguments
			b -- Vessel behaviour
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			dx -- Velocity the behaviour has set
		"""
		return VesselSignals.update( b, 'shapes', lambda night, restricted: not night, dx )

	@staticmethod
	def fog_signals(b, world, t, dx):
		""" Fog signals, held while visibility is restricted (Rule 35)
		Arguments
			b -- Vessel behaviour
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			dx -- Velocity the behaviour has set
		"""
		return VesselSignals.update( b, 'sounds', lambda night, restricted: restricted, dx )


if __name__ == "__main__":
	test = VesselSignals()
