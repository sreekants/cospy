#!/usr/bin/python
# Filename: Predator.py
# Description: Implementation of the Predator class

from cos.math.geometry.Vector import Vector
from cos.behavior.swarm.Prey import Prey
from cos.behavior.swarm.Boid import Boid

import random, math
from typing import List, Optional, Tuple

class Config:
    def __init__(self):
        self.count = 2
        self.speed = 3.2
        self.killDist = 10.0
        self.maxTurnAngle = math.radians(8.0)
        return

# =========================
# Predator class (js/predator.js)
# =========================
class Predator(Boid):
    def __init__(self, pos: Vector, vel: Vector):
        Boid.__init__(self)
        self.pos = pos
        self.vel = vel
        self.target_index: Optional[int] = None  # for debug line

    @staticmethod
    def create(speed: float, screen: Vector) -> "Predator":
        pos = Vector(random.uniform(0, screen.x), random.uniform(0, screen.y))
        angle = random.uniform(-math.pi, math.pi)
        vel = Vector.from_angle(angle) * speed
        return Predator(pos, vel)

    def move(
        self,
        preyList: List[Prey],
        world,
        cfg
    ):

        self.target_index = None
        if not preyList:
            # wander forward
            self.pos = world.bound(self.pos+self.vel)
            return

        # Find nearest prey
        closest_i = 0
        closest_d = float("inf")
        closest_disp = Vector(0.0, 0.0)

        for i, prey in enumerate(preyList):
            disp = world.shortestBoundedPathTo(self.pos, prey.pos)  # predator -> prey
            d = disp.norm()
            if d < closest_d:
                closest_d = d
                closest_i = i
                closest_disp = disp

        self.target_index = closest_i

        # Kill if close enough
        if closest_d <= cfg.killDist:
            preyList.pop(closest_i)
            self.target_index = None
            # After kill, keep current heading
            self.pos = world.bound(self.pos+self.vel)
            return

        desired_dir = closest_disp.normalize()
        new_heading = Boid.turn(self.vel, desired_dir, cfg.maxTurnAngle)
        self.vel = new_heading * cfg.speed
        self.pos = world.bound(self.pos+self.vel)

		

if __name__ == "__main__":
	test = Predator()

