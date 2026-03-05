#!/usr/bin/python
# Filename: Prey.py
# Description: Implementation of the Prey class

from cos.math.geometry.Vector import Vector
from cos.behavior.swarm.Boid import Boid

import math, random

class Config:
    def __init__(self):
        self.count = 25
        self.speed = 2.6
        self.minSeparation = 18.0
        self.minFlockDist = 55.0
        self.predatorSightDist = 100.0
        self.maxTurnAngle = math.radians(9.0)
        self.cohesion = 0.7
        self.alignment = 0.9
        self.separation = 1.3
        self.flee = 2.5
        self.predatorAvoidance = 2.0 
        return

class Prey(Boid):
    def __init__(self, pos: Vector, vel: Vector):
        Boid.__init__(self)
        self.pos = pos
        self.vel = vel
        return

    @staticmethod
    def create(speed: float, area: Vector):
        pos = Vector(random.uniform(0, area.x), random.uniform(0, area.y))
        angle = random.uniform(-math.pi, math.pi)
        vel = Vector.from_angle(angle) * speed
        return Prey(pos, vel)

    def move(
        self,
        tooClose,
        tooFar,
        avgDist: float,
        meanHeading: Vector,
        predatorList,
        world,
        cfg: dict):

        change = Vector(0.0, 0.0)

        # Cohesion: if we're far from flock, move toward others (sum tooFar)
        if avgDist > cfg.minFlockDist and tooFar:
            cohesion_vec = Vector(0.0, 0.0)
            for v in tooFar:
                cohesion_vec = cohesion_vec+v
            cohesion_vec = cohesion_vec.normalize()
            change = change+(cohesion_vec * cfg.cohesion)

        # Alignment: head toward mean heading
        if meanHeading.mag2() > 0:
            change = change+(meanHeading.normalize() * cfg.alignment)

        # Separation: move away from too-close neighbors
        if tooClose:
            sep_vec = Vector(0.0, 0.0)
            for v in tooClose:
                sep_vec = sep_vec+v  # these should already point away
            sep_vec = sep_vec.normalize()
            change = change+(sep_vec * cfg.separation)

        # Flee predator: strongest when closest predator is near
        closest_pred_disp = None  # displacement from prey -> predator (shortest bounded)
        closest_pred_dist = float("inf")
        for pred in predatorList:
            disp = world.shortestBoundedPathTo(self.pos, pred.pos)
            d = disp.norm()
            if d < closest_pred_dist:
                closest_pred_dist = d
                closest_pred_disp = disp

        if closest_pred_disp is not None and closest_pred_dist < cfg.predatorSightDist:
            # Flee direction is opposite of predator displacement
            flee_dir = (closest_pred_disp * -1.0).normalize()
            # Scale linearly by proximity (1 at d=0, 0 at sightDist)
            scale = max(0.0, (cfg.predatorSightDist - closest_pred_dist) / cfg.predatorSightDist)
            change = change+(flee_dir * (cfg.flee * scale))

        # If there's no change vector, keep going
        if change.mag2() == 0:
            desired_dir = self.vel.normalize()
        else:
            desired_dir = change.normalize()

        new_heading = Boid.turn(self.vel, desired_dir, cfg.maxTurnAngle)
        self.vel = new_heading * cfg.speed
        self.pos = world.bound(self.pos+self.vel)

		
    @staticmethod
    def motion(swarm, world, cfg, actors):
        if not actors:
            return

        # Precompute neighbor info
        tooClose, tooFar, avgDist = Prey.calcNeighbourDists(cfg.minSeparation, world, actors)
        meanHeading = Prey.calcMeanHeading(actors)

        for i in range(0, len(actors)):
            actors[i].move(
                tooClose=tooClose[i],
                tooFar=tooFar[i],
                avgDist=avgDist[i],
                meanHeading=meanHeading,
                predatorList=actors,
                world=world,
                cfg=cfg
            )

        return


    @staticmethod
    def calcNeighbourDists(
        minSeparation: float,
        world,
        actors
        ):
        """
        For each prey i:
            - tooClose[i] : list of vectors pointing away from neighbors closer than minSeparation
            - tooFar[i]   : list of unit vectors pointing toward neighbors farther than minSeparation
            - avgDist[i]  : average distance to all other prey
        """
        n = len(actors)
        tooClose: List[List[Vector]] = [[] for _ in range(n)]
        tooFar: List[List[Vector]] = [[] for _ in range(n)]
        avgDist: List[float] = [0.0 for _ in range(n)]

        if n <= 1:
            return tooClose, tooFar, avgDist

        for i in range(n):
            dist_sum = 0.0
            for j in range(n):
                if i == j:
                    continue
                disp = world.shortestBoundedPathTo(actors[i].pos, actors[j].pos)  # i->j
                d = disp.norm()
                dist_sum += d

                if d < 1e-9:
                    continue

                if d < minSeparation:
                    # vector pointing away from neighbor: -(i->j)
                    tooClose[i].append((disp * -1.0).normalize())
                else:
                    # vector pointing toward neighbor
                    tooFar[i].append(disp.normalize())

            avgDist[i] = dist_sum / (n - 1)
            
        return tooClose, tooFar, avgDist


    @staticmethod
    def calcMeanHeading(actors):
        """Average (normalized) heading of all prey."""
        if not actors:
            return Vector(0.0, 0.0)
        s = Vector(0.0, 0.0)
        for p in actors:
            s = s + p.vel.normalize()
        return s.normalize()


if __name__ == "__main__":
	test = Prey()

