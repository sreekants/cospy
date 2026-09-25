#!/usr/bin/python
# Filename: Classification.py
# Description: Classifies an encounter from bearings and courses (COS.025)

from maritime.core.situation.Types import Encounter as Type

import math, yaml
import numpy as np

# Resolver names for each encounter type
NAMES	= {
	Type.HO		: 'HeadOn',
	Type.OTSO	: 'Overtaken',
	Type.OTGW	: 'Overtaking',
	Type.CRSO	: 'StandOn',
	Type.CRGW	: 'GiveWay',
	Type.NAR	: '',
}


class Thresholds:
	def __init__(self, config=None):
		""" Classification angles in degrees and range in metres, as named in config/evaluator.yaml
		Arguments
			config -- The evaluator: section, or None for its defaults
		"""
		config			= config or {}
		self.head_on	= float( config.get('theta_critical_ho', 13.0) )
		self.overtake	= float( config.get('theta_critical_ot', 45.0) )
		self.crossing	= float( config.get('theta_critical_cr', -10.0) )
		self.abaft_min	= float( config.get('theta_ot_min', 112.5) )
		self.abaft_max	= float( config.get('theta_ot_max', 247.5) )
		self.range		= float( config.get('r_colregs_2_max', 4000.0) )	# Metres within which pairs are classified
		self.release	= float( config.get('encounter_release', 10.0) )	# Seconds unclassified before an encounter ends
		return

	@staticmethod
	def load(path:str):
		""" Reads the thresholds from an evaluator file
		Arguments
			path -- Path to evaluator.yaml
		"""
		with open( path, 'rb' ) as f:
			config	= yaml.safe_load( f ) or {}

		return Thresholds( config.get('evaluator', {}) )


THRESHOLDS	= Thresholds()


def configure(thresholds:Thresholds):
	""" Sets the thresholds every classification uses
	Arguments
		thresholds -- Thresholds
	"""
	global THRESHOLDS
	THRESHOLDS	= thresholds
	return


def wrap(angle:float)->float:
	""" An angle in degrees, in (-180, 180]
	Arguments
		angle -- Angle in degrees
	"""
	angle	= math.fmod( angle, 360.0 )
	if angle > 180.0:
		angle	-= 360.0
	elif angle <= -180.0:
		angle	+= 360.0
	return angle


def course(v)->float:
	""" Course of a velocity in map degrees; clockwise, since map y grows south
	Arguments
		v -- Velocity
	"""
	return math.degrees( math.atan2(v[1], v[0]) )


def bearing(own, target)->float:
	""" Relative bearing of target from own ship's course; positive is starboard
	Arguments
		own -- Own ship
		target -- Target ship
	"""
	d	= (np.asarray( target.location, dtype=float ) - np.asarray( own.location, dtype=float ))[:2]
	return wrap( math.degrees(math.atan2(d[1], d[0])) - course(np.asarray(own.velocity, dtype=float)) )


def classify(own, target, t:Thresholds=None):
	""" Names the encounter between two vessels, from own ship's point of view
	Arguments
		own -- Own ship
		target -- Target ship
		t -- Thresholds, THRESHOLDS when None
	Returns
		(α, β, type): the bearing of the target from own ship, of own ship from the target, and
		the encounter type; NAR unless both are under way and closing
	"""
	t		= t or THRESHOLDS
	vo		= np.asarray( own.velocity, dtype=float )[:2]
	vt		= np.asarray( target.velocity, dtype=float )[:2]
	d		= (np.asarray( target.location, dtype=float ) - np.asarray( own.location, dtype=float ))[:2]

	if (not np.any(vo)) or (not np.any(vt)) or (not np.any(d)):
		return 0.0, 0.0, Type.NAR

	α		= bearing( own, target )
	β		= bearing( target, own )

	if float( d @ (vt - vo) ) >= 0.0:
		return α, β, Type.NAR			# Not closing

	so		= float( np.linalg.norm(vo) )
	st		= float( np.linalg.norm(vt) )
	crossed	= abs( wrap(course(vt) - course(vo)) ) > t.head_on

	if (abs(α) < t.head_on) and (abs(β) < t.head_on):
		return α, β, Type.HO

	# Rule 13(b): coming up from more than 22.5° abaft the other's beam
	if (t.abaft_min < β % 360.0 < t.abaft_max) and (abs(α) < t.overtake) and (so > st):
		return α, β, Type.OTGW

	if (t.abaft_min < α % 360.0 < t.abaft_max) and (abs(β) < t.overtake) and (st > so):
		return α, β, Type.OTSO

	# Rule 15: the vessel with the other on her starboard side keeps out of the way
	if crossed and (t.crossing < α < t.abaft_min) and (-t.abaft_min < β < -t.crossing):
		return α, β, Type.CRGW

	if crossed and (t.crossing < β < t.abaft_min) and (-t.abaft_min < α < -t.crossing):
		return α, β, Type.CRSO

	return α, β, Type.NAR


if __name__ == "__main__":
	test = Thresholds()
