#!/usr/bin/python
# Filename: Rule12.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from maritime.model.rule.EncounterWatch import EncounterWatch
from maritime.core.situation.Types import Encounter
from cos.model.environment.Types import DynamicForce
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

import numpy as np

'''
Sailing Vessels
(a) When two sailing vessels are approaching one another, so as to involve risk of collision, one of
them shall keep out of the way of the other as follows;
(i) when each has the wind on a different side, the vessel which has the wind on the port
side shall keep out of the way of the other;
(ii) when both have the wind on the same side, the vessel which is to windward shall keep
out of the way of the vessel which is to leeward;
(iii) if a vessel with the wind on the port side sees a vessel to windward and cannot
determine with certainty whether the other vessel has the wind on the port or on the
starboard side, she shall keep out of the way of the other.
(b) For the purposes of this Rule the windward side shall be deemed to be the side opposite to that
on which the mainsail is carried or, in the case of a square-rigged vessel, the side opposite to that on
which the largest fore-and-aft sail is carried.
'''

class Rule12(COLREG):
	RANGE	= 4000.0	# Metres within which an onset is recorded (evaluator.yaml r_colregs_2_max)
	DCPA	= 500.0		# Metres of predicted passing distance that is a risk of collision

	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)

		# Every encounter at risk but overtaking (Rule 13), with each vessel's tack at onset
		self.watch	= EncounterWatch( None, self.DCPA, self.RANGE, excluded=(Encounter.OTGW, Encounter.OTSO),
									  snapshot=Rule12.snapshot )
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the rule and its encounter thresholds
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		COLREG.setup( self, ctxt, config )

		self.watch.dcpa		= float( config['encounter.dcpa'] or self.DCPA )
		self.watch.range	= float( config['encounter.range'] or self.RANGE )
		return

	def feed(self, ctxt:Context, rule_ctxt):
		""" Queues encounters at risk, once past their closest approach
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		self.watch.observe( ctxt, rule_ctxt, self )
		return

	@staticmethod
	def snapshot(own, target)->dict:
		""" Each vessel's tack, and whether own ship is to windward, at the onset of an encounter
		Arguments
			own -- Own ship
			target -- Target ship
		"""
		return { 'tack':		tack( own, wind(own) ),
				 'target_tack':	tack( target, wind(target) ),
				 'windward':	windward( own, target, wind(own) ) }


def wind(vessel):
	""" Wind vector acting on a vessel, the direction the wind blows towards; None if unknown
	Arguments
		vessel -- Vessel
	"""
	motion	= getattr( getattr(vessel, 'actor', None), 'motion', None )
	forces	= getattr( motion, 'forces', None ) or {}
	w		= forces.get( DynamicForce.WIND_CURRENT )
	return np.asarray( w, dtype=float )[:2] if w is not None else None


def tack(vessel, w)->str:
	""" Side the wind comes over, 'Port' or 'Starboard'; 'Unknown' when stopped, calm, or dead ahead or astern
	Arguments
		vessel -- Vessel
		w -- Wind vector acting on the vessel
	"""
	h	= np.asarray( vessel.velocity, dtype=float )[:2]
	if (w is None) or (not np.any(h)) or (not np.any(w)):
		return 'Unknown'

	# Map y grows south, so a positive cross product is starboard (as passing_side)
	cross	= -(h[0]*w[1] - h[1]*w[0])
	if cross == 0.0:
		return 'Unknown'

	return 'Starboard' if cross > 0.0 else 'Port'


def windward(own, target, w):
	""" Whether own ship is upwind of the target; None in a calm
	Arguments
		own -- Own ship
		target -- Target ship
		w -- Wind vector acting on own ship
	"""
	if (w is None) or (not np.any(w)):
		return None

	d	= (np.asarray( target.location, dtype=float ) - np.asarray( own.location, dtype=float ))[:2]
	return bool( d @ w > 0.0 )		# The target lies downwind



if __name__ == "__main__":
	test = Rule12()


