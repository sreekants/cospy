#!/usr/bin/python
# Filename: Motorboat.py
# Description: Implementation of the Motorboat class

from maritime.behavior.vessels.UnplannedVesselBehavior import UnplannedVesselBehavior
from maritime.navigation.cartography.Map import Map
from cos.math.geometry.Distance import Distance

import numpy as np


# Specification: Recreational — no path following, high momentum (preserves speed),
class Motorboat(UnplannedVesselBehavior):
    def __init__(self, ctxt, config):
        UnplannedVesselBehavior.__init__(self, ctxt, config)
        return

    def randomize_direction(self):
        """Fast heading: large turns allowed. High momentum: speed magnitude preserved."""
        speed = np.linalg.norm(self.dx)
        super().randomize_direction()
        new_speed = np.linalg.norm(self.dx)
        if speed > 0 and new_speed > 0:
            self.dx = self.dx * (speed / new_speed)

    def _crossing_separation(self, world):
        """Returns a speed scale factor [0.0, 1.0] based on proximity to TSS traffic."""
        try:
            vessels = world.get_objects("vessel")
        except Exception:
            return 1.0

        min_dist      = float('inf')
        fore_crossing = False

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
                fore_crossing = np.dot(self.dx, other - self.x) > 0

        if min_dist == float('inf'):
            return 1.0

        min_sep = self.CROSSING_FORE_MIN if fore_crossing else self.CROSSING_AFT_MIN
        if min_dist < min_sep:
            return max(min_dist / min_sep, 0.0)

        return 1.0

    def move(self, world, t, config):
        saved_x    = self.x.copy()
        saved_rect = self.rect
        saved_dx   = self.dx.copy()

        # Pre-scale velocity for vessel separation before the Brownian step
        scale   = self._crossing_separation(world)
        self.dx = self.dx * scale

        rect, dx = UnplannedVesselBehavior.move(self, world, t, config)

        # Momentum: restore speed gradually after a separation slowdown
        if scale < 1.0:
            self.dx = self.MOMENTUM * self.dx + (1.0 - self.MOMENTUM) * saved_dx

        # TSS avoidance: revert and randomize heading if we've drifted into TSS
        if self._map.in_tss(self.x):
            self.x    = saved_x
            self.rect = saved_rect
            self.last = saved_rect
            self.randomize_direction()
            rect = self.rect
            dx   = self.dx

        return rect, dx


if __name__ == "__main__":
    test = Motorboat(None, None)
