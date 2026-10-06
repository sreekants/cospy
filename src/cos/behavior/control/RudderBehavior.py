#!/usr/bin/python
# Filename: RudderBehavior.py
# Description: Estimates rudder order and angle from a vessel's turn with an inverted Nomoto model

from cos.core.simulation.Behavior import Behavior, ActorBehavior
from cos.core.utilities.ArgList import ArgList

import math

DEFAULT_K			= 2.0		# Non-dimensional Nomoto gain K'
DEFAULT_T			= 0.0		# Nomoto T'; 0 because the motion models turn in steps (about 2 suits smooth motion)
DEFAULT_LENGTH		= 100.0		# Metres, when the vessel has no ship model
DEFAULT_MAX_ANGLE	= 35.0		# Degrees, hard over
DEFAULT_RATE		= 2.5		# Degrees per second the steering gear can move the rudder
DEFAULT_SMOOTHING	= 5.0		# Seconds; time constant of the rate-of-turn filter
MIN_SPEED			= 0.1		# m/s; below this a rudder angle cannot be inferred
MAX_GAP				= 10.0		# Simulated seconds; a longer gap between samples restarts the estimate

class RudderBehavior(Behavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes; settings may override rudder_k, rudder_t,
				rudder_max, rudder_rate, rudder_smoothing and length
		"""
		Behavior.__init__(self, ActorBehavior.CONTROL_DYNAMICS)
		args				= ArgList( config.get('settings', '') if config else '' )
		self.k				= args.ToFloat('rudder_k', DEFAULT_K)
		self.t				= args.ToFloat('rudder_t', DEFAULT_T)
		self.max_angle		= math.radians( args.ToFloat('rudder_max', DEFAULT_MAX_ANGLE) )
		self.rate			= math.radians( args.ToFloat('rudder_rate', DEFAULT_RATE) )
		self.smoothing		= args.ToFloat('rudder_smoothing', DEFAULT_SMOOTHING)
		self.fixed_length	= args.ToFloat('length', 0.0)
		self.vehicle		= None
		self.reset()
		return

	def intialize(self, ctxt, actor, vehicle, config:dict):
		""" Initialize the behavior for the actor
		Arguments
			ctxt -- Simulation context
			actor -- Actor to initialize the behavior for
			vehicle -- Vehicle object to create the actor for
			config -- Configuration attributes
		"""
		Behavior.intialize(self, ctxt, actor, vehicle, config)
		return

	def ioctl(self, op, arg):
		""" Handles operation signals; the estimate takes none
		Arguments
			op -- Operation code
			arg -- arguments for the operation
		"""
		return False

	def reset(self):
		""" Forgets the history, e.g. after a gap in the samples
		"""
		self.rot		= None		# Filtered rate of turn, rad/s
		self.time		= None		# Simulated time of the last sample
		self.angle		= None		# Estimated rudder angle, rad, positive to starboard
		self.order		= None		# Estimated rudder order, rad
		return

	@property
	def length(self):
		""" Length used by the model: settings, then the ship model, then the default (metres)
		"""
		if self.fixed_length > 0:
			return self.fixed_length
		model	= getattr( self.vehicle, 'model', None )
		ship	= getattr( model, 'ship', None )
		length	= getattr( ship, 'length', None )
		if isinstance(length, (int, float)) and length > 0:
			return float(length)
		return DEFAULT_LENGTH

	def observe(self, rot, sog, now):
		""" Updates the estimate from the turn and speed observed at a simulated time
		Arguments
			rot -- Rate of turn, rad/s, positive to starboard; None if unknown
			sog -- Speed over ground, m/s
			now -- Simulated time (datetime)
		Returns
			(angle, order) in radians, or (None, None) while no estimate is possible
		"""
		if rot is None or sog < MIN_SPEED:
			self.reset()
			return None, None

		dt	= (now - self.time).total_seconds() if self.time is not None else 0.0
		if self.time is not None and (dt <= 0 or dt > MAX_GAP):
			self.reset()
			dt	= 0.0

		# Filter the rate of turn, then differentiate the filtered value
		if self.rot is None:
			filtered, rdot	= rot, 0.0
		else:
			alpha		= dt / (self.smoothing + dt)
			filtered	= self.rot + alpha*(rot - self.rot)
			rdot		= (filtered - self.rot) / dt

		# Nomoto: T·r' + r = K·δ, with K = K'·V/L and T = T'·L/V
		length		= self.length
		k			= self.k * sog / length
		t			= self.t * length / sog
		order		= max( -self.max_angle, min(self.max_angle, (t*rdot + filtered) / k) )

		# The steering gear moves the rudder towards the order at a limited rate
		if self.angle is None:
			angle	= order
		else:
			step	= self.rate * dt
			angle	= self.angle + max( -step, min(step, order - self.angle) )

		self.rot, self.time, self.angle, self.order	= filtered, now, angle, order
		return angle, order


if __name__ == "__main__":
	test = RudderBehavior( None, {} )
