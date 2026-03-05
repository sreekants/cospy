#!/usr/bin/python
# Filename: Swarm.py
# Description: Implementation of the Swarm class

from cos.behavior.swarm.Prey import Prey
from cos.behavior.swarm.Predator import Predator
from typing import List
from cos.math.geometry.Vector import Vector

class Swarm:
    def __init__(self, prey_cfg, pred_cfg, area=None):
        self.prey_cfg = prey_cfg
        self.pred_cfg = pred_cfg

        self.preyList       = [Prey.create(prey_cfg.speed, area) for _ in range(prey_cfg.count)]
        self.predatorList   = [Predator.create(pred_cfg.speed, area) for _ in range(pred_cfg.count)]
        return

    def movePredators(self, world):
        if not self.predatorList:
            return
        
        # Move each predator (may remove prey)
        for pred in self.predatorList:
            pred.move(self.preyList, world, self.pred_cfg)
        return

    def movePrey(self, world):
        if not self.preyList:
            return

        # Precompute neighbor info
        tooClose, tooFar, avgDist = self.calcNeighbourDists(self.prey_cfg.minSeparation, world)
        meanHeading = self.calcMeanHeading()

        for i in range(0, len(self.preyList)):
            self.preyList[i].move(
                tooClose=tooClose[i],
                tooFar=tooFar[i],
                avgDist=avgDist[i],
                meanHeading=meanHeading,
                predatorList=self.predatorList,
                world=world,
                cfg=self.prey_cfg
            )

        return

    def calcNeighbourDists(
        self,
        minSeparation: float,
        world
        ):
        """
        For each prey i:
            - tooClose[i] : list of vectors pointing away from neighbors closer than minSeparation
            - tooFar[i]   : list of unit vectors pointing toward neighbors farther than minSeparation
            - avgDist[i]  : average distance to all other prey
        """
        n = len(self.preyList)
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
                disp = world.shortestBoundedPathTo(self.preyList[i].pos, self.preyList[j].pos)  # i->j
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


    def calcMeanHeading(self):
        """Average (normalized) heading of all prey."""
        if not self.preyList:
            return Vector(0.0, 0.0)
        s = Vector(0.0, 0.0)
        for p in self.preyList:
            s = s + p.vel.normalize()
        return s.normalize()







if __name__ == "__main__":
	test = Swarm()

