#!/usr/bin/python
# Filename: VesselManeuvers.py
# Description: Implementation of the VesselManeuvers class

from maritime.model.vessel.Vessel import Vessel, Operation, Status

from math import atan2, cos, sin, degrees, radians

import random
import numpy as np

class VesselManeuvers:
	def __init__(self):
		return

	@staticmethod
	def tss_compliance(b, world, t, target_dx):
		# Container ships always obey TSS direction — hard correction, never violated.
		if not b.map.in_tss(b.vehicle.boundary):
			return target_dx

		tss_bearing = b.map.get_tss_bearing(b.x)
		if tss_bearing is None or np.linalg.norm(target_dx) == 0:
			return target_dx

		current_bearing = degrees(atan2(target_dx[1], target_dx[0]))
		delta 	= (tss_bearing - current_bearing + 180) % 360 - 180
		model 	= b.vehicle.model

		if abs(delta) <= model.tss_angle_tol:
			return target_dx

		step      = min(abs(delta), model.max_yaw_rate * 3) * (1 if delta > 0 else -1)
		new_angle = current_bearing + step
		speed     = np.linalg.norm(target_dx)
		return np.array((
			speed * cos(radians(new_angle)),
			speed * sin(radians(new_angle)),
			0.0
		))

		
	@staticmethod
	def apply_momentum(b, world, t, target_dx):
		"""Blend current velocity toward target with inertia and a heading-rate clamp."""
		model 		= b.vehicle.model
		blended    	= model.momentum * b.dx + (1.0 - model.momentum) * target_dx
		curr_norm  	= np.linalg.norm(b.dx)
		blend_norm 	= np.linalg.norm(blended)


		if curr_norm > 0 and blend_norm > 0:
			curr_angle  = degrees(atan2(b.dx[1],  b.dx[0]))
			blend_angle = degrees(atan2(blended[1],  blended[0]))
			delta       = (blend_angle - curr_angle + 180) % 360 - 180
			if abs(delta) > model.max_yaw_rate:
				clamped = curr_angle + model.max_yaw_rate * (1 if delta > 0 else -1)
				blended = np.array((
					blend_norm * cos(radians(clamped)),
					blend_norm * sin(radians(clamped)),
					0.0
				))

		return blended


	@staticmethod
	def overtaking_separation(b):
		model 		= b.vehicle.model

		# Get all the vessels in the visible range
		if not b.nearest:
			return 1.0
		
		# Find the nearest vehicle and check if the ego vessel is overtaking it
		min_dist      = float('inf')
		is_overtaking = False

		for v in b.nearest:
			dist  = v[0]

			if dist < min_dist:
				min_dist      = dist
				is_overtaking = np.dot(b.dx, v[1].location - b.x) > 0

		# Apply rules here
		# Maintain the safe distance defaulting to the TSS distance rules 
		# otherwise, observe the overtaking distance rule.
		min_sep = model.overtake_lat_min if is_overtaking else model.tss_min_dist

		if min_dist < min_sep:
			return max(min_dist / min_sep, 0.0)

		return 1.0

	@staticmethod
	def overtaking_distance(b, world, t, target_dx):
		return target_dx*VesselManeuvers.overtaking_separation(b)

	@staticmethod
	def crossing_separation(b, world):
		model 		= b.vehicle.model

		"""Returns a speed scale factor [0.0, 1.0] based on proximity to TSS traffic."""
		# Get all the vessels in the visible range
		if not b.nearest:
			return 1.0

		# Find the nearest vehicle and check if the ego vessel is overtaking it
		min_dist      = float('inf')
		fore_crossing = False

		for v in b.nearest:
			dist  = v[0]

			if dist < min_dist:
				min_dist        = dist
				fore_crossing   = np.dot(b.dx, v[0] - b.x) > 0

		min_sep = model.crossing_fore_min if fore_crossing else model.crossing_aft_min
		if min_dist < min_sep:
			return max(min_dist / min_sep, 0.0)

		return 1.0

	@staticmethod
	def crossing_slowdown(b, world, t, target_dx):
		b.saved_x    = b.x.copy()
		b.saved_rect = b.rect
		b.saved_dx   = b.dx.copy()

		# Pre-scale velocity for vessel separation before the Brownian step
		b.xscale    = VesselManeuvers.crossing_separation(b, world)

		return target_dx * b.xscale

	@staticmethod        
	def restore_speed(b, world, t, target_dx):
		model 		= b.vehicle.model

		# Momentum: restore speed gradually after a separation slowdown
		if b.xscale < 1.0:
			b.dx = model.momentum * b.dx + (1.0 - model.momentum) * b.saved_dx

		return b.dx


	@staticmethod
	def fishing_slowdown(b, world, t, target_dx):
		if b.mode != Operation.FISHING:
			return target_dx
		
		b.saved_x    = b.x.copy()
		b.saved_rect = b.rect
		b.saved_dx   = b.dx.copy()

		# Pre-scale velocity for vessel separation before the Brownian step
		b.xscale    = VesselManeuvers.fishing_separation(b, world, t, target_dx)

		return target_dx * b.xscale


	@staticmethod
	def fishing_separation(b, world, t, target_dx):
		"""Returns a speed scale factor based on proximity to any other vessel's aft.

		Fishing vessels must keep at least 1000 m from the aft of any other vessel.
		Without velocity data from the world query, a 1000 m omnidirectional buffer
		is used as a conservative approximation.
		"""
		model 		= b.vehicle.model

		# Get all the vessels in the visible range
		if not b.nearest:
			return 1.0
		
		# Find the nearest vehicle and check if the ego vessel is overtaking it
		min_dist      = float('inf')

		for v in b.nearest:
			dist  = v[0]

			if dist < min_dist:
				min_dist = dist

		if min_dist < model.fishing_aft_dist:
			return max(min_dist / model.fishing_aft_dist, 0.0)

		return 1.0

	@staticmethod
	def tss_avoidance(b, world, t, target_dx):
		# TSS avoidance: revert and randomize heading if we've drifted into TSS
		if b.map.in_tss(b.vehicle.boundary):
			b.x      = b.saved_x
			b.rect   = b.saved_rect
			b.last   = b.saved_rect
			b.randomize_direction()
		return target_dx


	@staticmethod
	def raise_anchor(b, world, t, target_dx):
		if (b.anchor_watch is not None) and (b.anchor_watch.signaled() == True):
			b.movable        = True
			b.anchor_watch   = None
			b.vehicle.underway()

		return target_dx

	@staticmethod
	def stop_for_safety(b, world, t, target_dx):
		model 		= b.vehicle.model

		if model.stop_on_traffic == False:
			return target_dx
		
		intent	= 'Speed.SlowdownForTraffic'

		# Half if any targetship is in the ample_time range of the ownship
		for v in b.nearest:
			dist  = v[0]

			if dist < model.range_ample_time:
				b.vehicle.intent.set(intent)
				return target_dx * .05
			
		b.vehicle.intent.reset(intent)
		return target_dx
    
if __name__ == "__main__":
	test = VesselManeuvers()

