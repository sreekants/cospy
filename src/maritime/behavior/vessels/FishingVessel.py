#!/usr/bin/python
# Filename: FishingVessel.py
# Description: Implementation of the FishingVessel class

from maritime.behavior.vessels.UnplannedVesselBehavior import UnplannedVesselBehavior
from maritime.navigation.cartography.Map import Map
from cos.math.geometry.Distance import Distance
from io import StringIO
from math import atan2, cos, sin, degrees, radians

import numpy as np
import csv


class FishingVessel(UnplannedVesselBehavior):
    # Two operating modes per Specification
    NAVIGATING = 'navigating'
    FISHING    = 'fishing'

    def __init__(self, ctxt, config):
        UnplannedVesselBehavior.__init__(self, ctxt, config)

        self.mode = self.NAVIGATING

        # Navigation path state (used in NAVIGATING mode)
        self._nav_path    = []
        self._nav_current = None
        self._nav_next    = None
        self._nav_at      = 0
        self._nav_loop    = False

        args = self.get_settings(config)
        if ('pathfile' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
            self._load_nav_path(ctxt, ctxt.sim.config.resolve(args['pathfile']))
            self._nav_loop = args.IsTrue('loop')
            if self._nav_path:
                self.mode = self.NAVIGATING
                
        return

    def ioctl(self, op, arg):
        """Switch between NAVIGATING and FISHING modes at runtime."""
        if op == 'fishing.mode':
            self.mode = self.FISHING if arg else self.NAVIGATING
            return True
        return UnplannedVesselBehavior.ioctl(self, op, arg)

    # ------------------------------------------------------------------
    # Navigation path management (NAVIGATING mode only)
    # ------------------------------------------------------------------

    def _load_nav_path(self, ctxt, filename):
        data   = ctxt.sim.fs.read_file(filename)
        reader = csv.reader(StringIO(data), delimiter=',')
        rownum = 0
        for waypoint in reader:
            if rownum == 0:
                rownum += 1
                continue
            t   = float(waypoint[1])
            x   = float(waypoint[2])
            y   = float(waypoint[3])
            z   = float(waypoint[4])
            sog = float(waypoint[5])
            cog = float(waypoint[6])
            self._nav_path.append((t, np.array((x, y, z)), np.array((sog, cog, 0.0))))
            if rownum == 1:
                self._nav_current = self._nav_path[0]
                self._nav_at      = 0
                self.x            = self._nav_current[1]
            if rownum == 2:
                self._nav_next = self._nav_path[1]
            rownum += 1

    def _nav_restart(self):
        if len(self._nav_path) < 2:
            return
        self._nav_current = self._nav_path[0]
        self._nav_at      = 0
        self.x            = self._nav_current[1]
        self._nav_next    = self._nav_path[1]

    def _nav_heading(self):
        """Advance to next waypoint if close enough and return target velocity vector."""
        if (self._nav_next is None) or (self._nav_current is None):
            return None

        sog = self._nav_current[2][0]
        if Distance.euclidean(self.x, self._nav_next[1]) <= sog:
            self._nav_at += 1
            if self._nav_at >= len(self._nav_path):
                self._nav_current = None
                self._nav_next    = None
                if self._nav_loop:
                    self._nav_restart()
                return None
            self._nav_current = self._nav_next
            self._nav_next    = self._nav_path[self._nav_at]

        theta = atan2(self._nav_next[1][1] - self.x[1], self._nav_next[1][0] - self.x[0])
        return np.array((sog * cos(theta), sog * sin(theta), 0.0))

    # ------------------------------------------------------------------
    # Shared behavioral helpers
    # ------------------------------------------------------------------

    def _apply_momentum(self, target_dx):
        """Low momentum: blends quickly toward target with a loose heading-rate clamp."""
        blended    = self.model.momentum * self.dx + (1.0 - self.model.momentum) * target_dx
        curr_norm  = np.linalg.norm(self.dx)
        blend_norm = np.linalg.norm(blended)

        if curr_norm > 0 and blend_norm > 0:
            curr_angle  = degrees(atan2(self.dx[1],  self.dx[0]))
            blend_angle = degrees(atan2(blended[1],  blended[0]))
            delta       = (blend_angle - curr_angle + 180) % 360 - 180
            if abs(delta) > self.model.max_heading_rate:
                clamped = curr_angle + self.model.max_heading_rate * (1 if delta > 0 else -1)
                blended = np.array((
                    blend_norm * cos(radians(clamped)),
                    blend_norm * sin(radians(clamped)),
                    0.0
                ))

        return blended

    def _tss_compliance(self, target_dx):
        """Nudge heading toward TSS lane direction when navigating within TSS.

        Fishing vessels generally obey TSS direction while navigating; violations
        (entering from edges) are controlled externally via ioctl/mode.
        """
        if not self._map.in_tss(self.x):
            return target_dx

        tss_bearing = self._map.get_tss_bearing(self.x)
        if tss_bearing is None or np.linalg.norm(target_dx) == 0:
            return target_dx

        current_bearing = degrees(atan2(target_dx[1], target_dx[0]))
        delta = (tss_bearing - current_bearing + 180) % 360 - 180

        if abs(delta) <= self.model.tss_angle_tol:
            return target_dx

        step      = min(abs(delta), self.model.max_heading_rate * 2) * (1 if delta > 0 else -1)
        new_angle = current_bearing + step
        speed     = np.linalg.norm(target_dx)
        return np.array((
            speed * cos(radians(new_angle)),
            speed * sin(radians(new_angle)),
            0.0
        ))

    def _tss_separation(self, world, target_dx):
        """800 m separation from other vessels when navigating inside TSS."""
        try:
            vessels = world.get_objects("vessel")
        except Exception:
            return target_dx

        min_dist = float('inf')
        for v in vessels:
            pos = v.get('position') if isinstance(v, dict) else None
            if pos is None:
                continue
            other = np.array((float(pos[0]), float(pos[1]), 0.0))
            dist  = Distance.euclidean(self.x, other)
            if dist < 1.0:
                continue
            if dist < min_dist:
                min_dist = dist

        if min_dist < self.model.tss_min_dist:
            return target_dx * max(min_dist / self.model.tss_min_dist, 0.0)

        return target_dx

    def _fishing_separation(self, world):
        """Returns a speed scale factor based on proximity to any other vessel's aft.

        Fishing vessels must keep at least 1000 m from the aft of any other vessel.
        Without velocity data from the world query, a 1000 m omnidirectional buffer
        is used as a conservative approximation.
        """
        try:
            vessels = world.get_objects("vessel")
        except Exception:
            return 1.0

        min_dist = float('inf')
        for v in vessels:
            pos = v.get('position') if isinstance(v, dict) else None
            if pos is None:
                continue
            other = np.array((float(pos[0]), float(pos[1]), 0.0))
            dist  = Distance.euclidean(self.x, other)
            if dist < 1.0:
                continue
            if dist < min_dist:
                min_dist = dist

        if min_dist < self.model.fishing_aft_dist:
            return max(min_dist / self.model.fishing_aft_dist, 0.0)

        return 1.0

    # ------------------------------------------------------------------
    # Mode-dispatched movement
    # ------------------------------------------------------------------

    def move(self, world, t, config):
        if self.mode == self.NAVIGATING:
            return self._move_navigating(world)
        return self._move_fishing(world, t, config)

    def _move_navigating(self, world):
        target_dx = self._nav_heading()
        if target_dx is None:
            # End of path reached — transition to fishing mode
            self.mode = self.FISHING
            self.dx   = np.zeros(3)
            return self.rect, self.dx

        target_dx = self._tss_compliance(target_dx)
        target_dx = self._tss_separation(world, target_dx)
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

    def _move_fishing(self, world, t, config):
        saved_x    = self.x.copy()
        saved_rect = self.rect
        saved_dx   = self.dx.copy()

        scale   = self._fishing_separation(world)
        self.dx = self.dx * scale

        rect, dx = UnplannedVesselBehavior.move(self, world, t, config)

        # Restore speed; low momentum means quick recovery
        if scale < 1.0:
            self.dx = self.model.momentum * self.dx + (1.0 - self.model.momentum) * saved_dx

        # Fishing only outside TSS: revert and randomize if we've drifted in
        if self._map.in_tss(self.x):
            self.x    = saved_x
            self.rect = saved_rect
            self.last = saved_rect
            self.randomize_direction()
            rect = self.rect
            dx   = self.dx

        return rect, dx


if __name__ == "__main__":
    test = FishingVessel(None, None)
