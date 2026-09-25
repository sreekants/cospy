#!/usr/bin/python
# Filename: Rule14.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList
from cos.model.rule.Situation import Situation

import numpy as np

'''
Head-on Situation
(a) When two power-driven vessels are meeting on reciprocal or nearly reciprocal courses so as to
involve risk of collision each shall alter her course to starboard so that each shall pass on the port
side of the other.
(b) Such a situation shall be deemed to exist when a vessel sees the other ahead or nearly ahead and
by night she could see the masthead lights of the other in a line or nearly in a line and/or both
sidelights and by day she observes the corresponding aspect of the other vessel.
(c) When a vessel is in any doubt as to whether such a situation exists she shall assume that it does
exist and act accordingly.
'''

class Rule14(COLREG):
	ANGLE	= 13.0		# Degrees: nearly reciprocal, nearly ahead (evaluator.yaml theta_critical_ho)
	RANGE	= 4000.0	# Metres within which an onset is recorded (evaluator.yaml r_colregs_2_max)
	DCPA	= 500.0		# Metres of predicted passing distance that is a risk of collision

	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)

		self.angle		= self.ANGLE
		self.range		= self.RANGE
		self.dcpa		= self.DCPA
		self.onsets		= {}		# (own id, target id) -> [onset time, last distance]
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the rule and its head-on thresholds
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		COLREG.setup( self, ctxt, config )

		self.angle	= float( config['headon.angle'] or self.ANGLE )
		self.range	= float( config['headon.range'] or self.RANGE )
		self.dcpa	= float( config['headon.dcpa'] or self.DCPA )
		return

	def evaluate(self, ctxt:Context, rule_ctxt):
		""" Queues head-on encounters that have passed their closest approach, then judges them
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		self.observe( ctxt, rule_ctxt )
		COLREG.evaluate( self, ctxt, rule_ctxt )
		return

	def observe(self, ctxt:Context, rule_ctxt):
		""" Records head-on onsets and queues each at its closest approach
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		vessels		= rule_ctxt.vessels or []
		subjects	= getattr( rule_ctxt, 'subjects', None ) or vessels
		now			= ctxt.sim.now()

		for own in subjects:
			for target in vessels:
				if own is target:
					continue

				key			= ( own.id, target.id )
				distance	= float( np.linalg.norm(Rule14.offset(own, target)) )
				onset		= self.onsets.get( key )

				if onset is None:
					if Rule14.head_on( own, target, self.angle, self.dcpa, self.range ):
						self.onsets[key]	= [now, distance]
					continue

				if distance > onset[1]:
					del self.onsets[key]
					if distance <= self.range:
						situation	= Situation( own, target )
						situation.maneuvers['HeadOn']	= onset[0]
						self.add_situation( situation )
					continue

				onset[1]	= distance
		return

	@staticmethod
	def offset(own, target):
		""" Target position relative to own ship
		Arguments
			own -- Own ship
			target -- Target ship
		"""
		return (np.asarray( target.location, dtype=float ) - np.asarray( own.location, dtype=float ))[:2]

	@staticmethod
	def head_on(own, target, angle:float, dcpa:float, range:float)->bool:
		""" Rule 14(b): reciprocal courses, target ahead, closing with risk of collision
		Arguments
			own -- Own ship
			target -- Target ship
			angle -- Tolerance in degrees for 'nearly' reciprocal and 'nearly' ahead
			dcpa -- Predicted passing distance below which there is risk of collision
			range -- Distance beyond which no onset is recorded
		"""
		vo		= np.asarray( own.velocity, dtype=float )[:2]
		vt		= np.asarray( target.velocity, dtype=float )[:2]
		d		= Rule14.offset( own, target )

		if (not np.any(vo)) or (not np.any(vt)) or (not np.any(d)) or (np.linalg.norm(d) > range):
			return False

		if Rule14.between( vo, -vt ) > angle or Rule14.between( vo, d ) > angle:
			return False

		v		= vt - vo
		speed	= float( v @ v )
		tcpa	= -float( d @ v ) / speed if speed > 0.0 else 0.0
		if tcpa <= 0.0:
			return False

		return float( np.linalg.norm(d + v*tcpa) ) <= dcpa

	@staticmethod
	def between(a, b)->float:
		""" Angle between two vectors, degrees
		Arguments
			a -- Vector
			b -- Vector
		"""
		norm	= float( np.linalg.norm(a) ) * float( np.linalg.norm(b) )
		if norm == 0.0:
			return 180.0

		c	= float( a @ b ) / norm
		return float( np.degrees(np.arccos(max(-1.0, min(1.0, c)))) )


if __name__ == "__main__":
	test = Rule14()
