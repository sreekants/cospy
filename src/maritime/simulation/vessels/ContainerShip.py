#!/usr/bin/python
# Filename: ContainerShip.py
# Description: Implementation of the ContainerShip class

from maritime.simulation.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from cos.math.geometry.Distance import Distance
from math import atan2, cos, sin, degrees, radians

import numpy as np


class ContainerShip(PlannedVesselBehavior):
    # Specification: high momentum, slow heading, strict TSS lane compliance
    MOMENTUM         = 0.92   # high inertia
    MAX_HEADING_RATE = 2.0    # degrees per timestep

    TSS_MIN_DIST     = 800.0  # metres; normal separation inside TSS
    OVERTAKE_LAT_MIN = 55.0   # metres; lateral separation while overtaking
    TSS_ANGLE_TOL    = 30.0   # degrees; tolerance before lane correction kicks in

    def _adjust_velocity(self, world, target_dx):
        target_dx = self._tss_compliance(target_dx)
        target_dx = self._separation_adjust(world, target_dx)
        return target_dx

    def _tss_compliance(self, target_dx):
        # Container ships always obey TSS direction — hard correction, never violated.
        if not self._map.in_tss(self.x):
            return target_dx

        tss_bearing = self._map.get_tss_bearing(self.x)
        if tss_bearing is None or np.linalg.norm(target_dx) == 0:
            return target_dx

        current_bearing = degrees(atan2(target_dx[1], target_dx[0]))
        delta = (tss_bearing - current_bearing + 180) % 360 - 180

        if abs(delta) <= self.TSS_ANGLE_TOL:
            return target_dx

        step      = min(abs(delta), self.MAX_HEADING_RATE * 3) * (1 if delta > 0 else -1)
        new_angle = current_bearing + step
        speed     = np.linalg.norm(target_dx)
        return np.array((
            speed * cos(radians(new_angle)),
            speed * sin(radians(new_angle)),
            0.0
        ))

    def _separation_adjust(self, world, target_dx):
        try:
            vessels = world.get_objects("vessel")
        except Exception:
            return target_dx

        min_dist      = float('inf')
        is_overtaking = False

        for v in vessels:
            pos = v.get('position') if isinstance(v, dict) else None
            if pos is None:
                continue
            other = np.array((float(pos[0]), float(pos[1]), 0.0))
            dist  = Distance.euclidean(self.x, other)
            if dist < 1.0:   # skip self
                continue
            if dist < min_dist:
                min_dist      = dist
                is_overtaking = np.dot(self.dx, other - self.x) > 0

        min_sep = self.OVERTAKE_LAT_MIN if is_overtaking else self.TSS_MIN_DIST
        if min_dist < min_sep:
            return target_dx * max(min_dist / min_sep, 0.0)

        return target_dx


if __name__ == "__main__":
    test = ContainerShip(None, None)
