#!/usr/bin/python
# Filename: Cpa.py
# Description: Implementation of the Cpa class

from cos.math.geometry.Vector import Vector
from cos.math.geometry.Position import Position

import math
from dataclasses import dataclass


class CPA:
    def __init__(self, p1, v1, p2, v2):
        """
        Compute CPA between two moving points with constant velocities.
        p1, v1: position and velocity of object 1
        p2, v2: position and velocity of object 2

        """

        """
        Derivation:
            Let r(t) = (p2 - p1) + (v2 - v1) * t = dx + dv * t
            Minimize |r(t)|^2 => derivative 2 * r(t)·vr = 0
            => t* = - (r0·vr) / |dv|^2  (if |dv|>0), else relative speed is zero.
        """

        dx      = p2 - p1          # initial relative position
        dv      = v2 - v1          # relative velocity
        dist    = dv.dot(dv)       

        if dist == 0.0:
            # No relative motion: distance is constant; CPA is now.
            t_star = 0.0
        else:
            t_star = - dx.dot(dv) / dist


        # Unclamped CPA (can be in the past)
        self.tcpa               = t_star
        self.p1_at_cpa          = p1.at(v1, t_star)
        self.p2_at_cpa          = p2.at(v2, t_star)
        self.dcpa               = (self.p2_at_cpa-self.p1_at_cpa).norm()

        # CPA going forward in time only (optional, often useful in operations)
        self.t_cpa_future       = max(0.0, t_star)
        self.future_p1_at_cpa   = p1.at(v1, self.t_cpa_future)
        self.future_p2_at_cpa   = p2.at(v2, self.t_cpa_future)
        self.future_dcpa        = (self.future_p2_at_cpa-self.future_p1_at_cpa).norm()

        return
	

if __name__ == "__main__":
    # Object 1 at (0,0) heading east 3 m/s
    p1 = Position(0.0, 0.0)
    v1 = Vector(3.0, 0.0)

    # Object 2 at (10, 10) heading south-west 2 m/s in x, -1 m/s in y
    p2 = Position(10.0, 10.0)
    v2 = Vector(-2.0, -1.0)

    res = CPA(p1, v1, p2, v2)

    print(f"tcpa = {res.tcpa:.3f} s (unclamped), distance = {res.dcpa:.3f} m")
    print(f"t_cpa_future = {res.t_cpa_future:.3f} s, distance = {res.future_dcpa:.3f} m")
    print(f"p1_at_cpa = {res.p1_at_cpa}, p2_at_cpa = {res.p2_at_cpa}")
