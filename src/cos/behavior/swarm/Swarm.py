#!/usr/bin/python
# Filename: Swarm.py
# Description: Implementation of the Swarm class

from cos.behavior.swarm.Prey import Prey
from cos.behavior.swarm.Predator import Predator

class Swarm:
    def __init__(self):
        self.groups    = []
        return
    
    def setPreys(self, prey_cfg, preyList, fnMove=None):
        fnMove      = Prey.motion if fnMove is None else fnMove
        self.groups.append( ('prey', prey_cfg, preyList, fnMove) )
        return preyList

    def setPredators(self, pred_cfg, predatorList, fnMove=None):
        fnMove      = Predator.motion if fnMove is None else fnMove
        self.groups.append( ('predator', pred_cfg, predatorList, fnMove) )
        return predatorList

    def move(self, world):
        for _, cfg, actors, fn in self.groups:
            fn(self, world, cfg, actors)
        return
    







if __name__ == "__main__":
	test = Swarm()

