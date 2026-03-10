#!/usr/bin/python
# Filename: Predator.py
# Description: Implementation of the Predator class

from cos.math.geometry.Rectangle import Rectangle
from cos.math.geometry.Point import Point
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

class Predator(Boid):
    def __init__(self, pos: Point, vel: Vector, ref=None):
        Boid.__init__(self)
        self.pos = pos
        self.vel = vel
        self.target_index: Optional[int] = None  # for debug line
        self.ref    = ref      # Opaque reference to the actual object 
        return

    @staticmethod
    def create(speed: float, area: Rectangle) -> "Predator":
        pos = Vector(area.x+random.uniform(0, area.width), area.y+random.uniform(0, area.height))
        angle = random.uniform(-math.pi, math.pi)
        vel = Vector.from_angle(angle) * speed
        return Predator(pos, vel)

    def move(
        self,
        preyList,
        world,
        cfg
    ):

        self.target_index = None
        if not preyList:
            # wander forward
            self.pos = world.bound(self,self.pos, self.vel)
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
            self.pos = world.bound(self, self.pos, self.vel)
            return

        desired_dir = closest_disp.normalize()
        new_heading = Boid.turn(self.vel, desired_dir, cfg.maxTurnAngle)
        self.vel = new_heading * cfg.speed
        self.pos = world.bound(self, self.pos, self.vel)

		
    @staticmethod
    def motion(swarm, world, cfg, actors):
        if not actors:
            return

        preyList    = None
        for g in swarm.groups:
            if g[0] == 'prey':
                preyList    = g[2]
                break

        # Move each predator (may remove prey)
        for pred in actors:
            pred.move(preyList, world, cfg)
        return

if __name__ == "__main__":
	test = Predator()

