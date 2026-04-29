#!/usr/bin/python
# Filename: VesselBehavior.py
# Description: Implementation of the VesselBehavior class

from cos.behavior.motion.PathFollowingMotionBehavior import PathFollowingMotionBehavior
from cos.behavior.motion.VesselModel import VesselModel
from maritime.navigation.cartography.Map import Map

from math import atan2, cos, sin, degrees, radians

import numpy as np


class PlannedVesselBehavior(PathFollowingMotionBehavior):
	# Subclasses override these to tune inertia and agility.
	MOMENTUM         = 0.80  # fraction of previous velocity retained each timestep
	MAX_HEADING_RATE = 5.0   # maximum heading change in degrees per timestep

	def __init__(self, ctxt, config):
		PathFollowingMotionBehavior.__init__(self, ctxt, config)
		self._map 	= Map(ctxt)
		self.model	= VesselModel()

		# Load the ship model
		args		= self.get_settings( config )
		if ('ship.model' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load_model( ctxt, ctxt.sim.config.resolve(args['ship.model']) )

		return

	def _apply_momentum(self, target_dx):
		"""Blend current velocity toward target with inertia and a heading-rate clamp."""
		blended    = self.MOMENTUM * self.dx + (1.0 - self.MOMENTUM) * target_dx
		curr_norm  = np.linalg.norm(self.dx)
		blend_norm = np.linalg.norm(blended)

		if curr_norm > 0 and blend_norm > 0:
			curr_angle  = degrees(atan2(self.dx[1],  self.dx[0]))
			blend_angle = degrees(atan2(blended[1],  blended[0]))
			delta       = (blend_angle - curr_angle + 180) % 360 - 180
			if abs(delta) > self.MAX_HEADING_RATE:
				clamped = curr_angle + self.MAX_HEADING_RATE * (1 if delta > 0 else -1)
				blended = np.array((
					blend_norm * cos(radians(clamped)),
					blend_norm * sin(radians(clamped)),
					0.0
				))

		return blended

	def _adjust_velocity(self, world, target_dx):
		"""Hook for subclasses to apply vessel-specific speed and heading rules."""
		return target_dx

	def load_model(self, ctxt, filename):
		""" Loads a simulation model
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""

		self.model.load(self._get_file(ctxt, filename))
		return

	def _get_file(self, ctxt, filename):
		""" Returns the content of a simulation file
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""
		if ctxt is None:
			return open(filename, 'r').read()

		return ctxt.sim.fs.read_file_as_bytes(filename)

	def move(self, world, t, config):
		"""Follow the planned path, applying vessel-specific adjustments and momentum."""
		pos = self.get_pos(t)
		if pos is None:
			self.dx = np.zeros(3)
			return self.rect, self.dx

		target_dx = self._adjust_velocity(world, pos[2])
		self.dx   = self._apply_momentum(target_dx)

		center    = self.rect.center
		newpos    = self.x + self.dx
		self.rect = self.rect.move(newpos[0] - center[0], newpos[1] - center[1])

		if self.can_move(world, self.rect):
			self.last = self.rect
			self.x    = newpos
		else:
			self.rect = self.last

		return self.rect, self.dx



if __name__ == "__main__":
	test = PlannedVesselBehavior(None, None)
