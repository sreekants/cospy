#!/usr/bin/python
# Filename: Ferry.py
# Description: Implementation of the Ferry class

from maritime.simulation.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from cos.math.geometry.Distance import Distance

import numpy as np


class Ferry(PlannedVesselBehavior):
    # Specification: medium momentum, fast heading, crosses TSS perpendicularly.
    # Ferry does NOT obey TSS lane direction — it arranges its own timing to cross.
    MOMENTUM         = 0.75   # medium inertia
    MAX_HEADING_RATE = 8.0    # degrees per timestep; agile enough to time crossing

    # Distance thresholds when crossing TSS traffic (spec §Distance Keeping)
    CROSSING_AFT_MIN  = 50.0   # metres; minimum when crossing at aft of a TSS vessel
    CROSSING_FORE_MIN = 250.0  # metres; minimum when crossing in front of approaching traffic

    def _adjust_velocity(self, world, target_dx):
        return self._crossing_separation(world, target_dx)

    def _crossing_separation(self, world, target_dx):
        """Slow the ferry when it would pass too close to TSS traffic.

        Crossing at aft of a TSS vessel: 50 m minimum.
        Crossing in front of an approaching TSS vessel: 200–300 m (250 m used).
        """
        try:
            vessels = world.get_objects("vessel")
        except Exception:
            return target_dx

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
                min_dist = dist
                # Fore crossing: the other vessel is ahead in the ferry's crossing
                # direction, meaning the ferry will pass in front of it.
                fore_crossing = np.dot(target_dx, other - self.x) > 0

        if min_dist == float('inf'):
            return target_dx

        min_sep = self.CROSSING_FORE_MIN if fore_crossing else self.CROSSING_AFT_MIN
        if min_dist < min_sep:
            return target_dx * max(min_dist / min_sep, 0.0)

        return target_dx


if __name__ == "__main__":
    test = Ferry(None, None)
