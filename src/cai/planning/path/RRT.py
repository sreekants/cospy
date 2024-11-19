#!/usr/bin/env python
# Filename: RRT.py
# Description: Implementation of the RRT Path Planning Algorithm
# Reference: https://lavalle.pl/RRTCtxtpubs.html

import sys, random
from math import sqrt,cos,sin,atan2
import networkx

class RRTCtxt:
    def __init__(self, goal, range):
        """ Constructor
        Arguments
        	goal -- #TODO
        	range -- #TODO
        """
        self.is_valid_point = self._is_valid_point
        self.is_valid_path  = self._is_valid_path
        self.xrange         = range[0]
        self.yrange         = range[1]
        self.Qgoal          = goal
        return

    @staticmethod
    def _is_valid_point(self, p1):
        """ #TODO: _is_valid_point
        Arguments
        	p1 -- #TODO
        """
        # Check if the point is valid or in an obstacle
        #   if is_in_obstacle(o1): return False

        return True

    @staticmethod
    def _is_valid_path(self, p1, p2):
        """ #TODO: _is_valid_path
        Arguments
        	p1 -- #TODO
        	p2 -- #TODO
        """
        # Check if the point is valid or in an obstacle
        #   if is_intersect_obstacle(p1,p2): return False
        return True

def dist(p1,p2):
    """ #TODO: dist
    Arguments
    	p1 -- #TODO
    	p2 -- #TODO
    """
    return sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

def nearest(ctxt:RRTCtxt, Qrand, G):
    """ #TODO: nearest
    Arguments
    	ctxt -- Simulation context
    	Qrand -- #TODO
    	G -- #TODO
    """
    if Qrand == None:
        return None

    Qnear = G[0]
    for p in G:
        if dist(p,Qrand) < dist(Qnear,Qrand):
            Qnear = p
    return Qnear

def newconf(ctxt:RRTCtxt, p1, p2, dQ):
    """ #TODO: newconf
    Arguments
    	ctxt -- Simulation context
    	p1 -- #TODO
    	p2 -- #TODO
    	dQ -- #TODO
    """
    if p1 == None or p2 == None:
        return None


    if dist(p1,p2) > dQ:
        theta = atan2(p2[1]-p1[1], p2[0]-p1[0])
        p2  = p1[0] + dQ*cos(theta), p1[1] + dQ*sin(theta)

    if ctxt.is_valid_path(ctxt, p1, p2) == False:
        return None

    return p2

def randconf(ctxt:RRTCtxt):
    """ #TODO: randconf
    Arguments
    	ctxt -- Simulation context
    """
    for i in range(1,10):
        x       = ctxt.xrange[0]
        dx      = ctxt.xrange[1]-ctxt.xrange[0]
        y       = ctxt.yrange[0]
        dy      = ctxt.yrange[1]-ctxt.yrange[0]

        Qrand   = (x+random.random()*dx, y+random.random()*dy)
        if ctxt.is_valid_point(ctxt, Qrand) == True:
            return Qrand

    return Qrand

def BuildRRT(ctxt, Qinit, K, dQ):
    """ #TODO: BuildRRT
    Arguments
    	ctxt -- Simulation context
    	Qinit -- #TODO
    	K -- #TODO
    	dQ -- #TODO
    """
    RRT = networkx.Graph()
    G = []

    G.append( Qinit )

    for i in range(0,K):
        Qrand   = randconf(ctxt)
        Qnear   = nearest(ctxt, Qrand, G)
        Qnew    = newconf(ctxt, Qnear, Qrand, dQ)
        if Qnew == None:
            continue

        G.append(Qnew)
        RRT.add_edge( Qnear, Qnew, )

        # Attempt to connect with goal
        if newconf(ctxt, Qnew, ctxt.Qgoal, dQ) != None:
            RRT.add_edge( (Qnear, ctxt.Qgoal) )
            break

    return RRT



# if python says run, then we should run
if __name__ == '__main__':
    import pygame
    from pygame.locals import *

    #constants
    XDIM = 800
    YDIM = 600
    WINSIZE = [XDIM, YDIM]
    EPSILON = 7.0
    NUMNODES = 10000

    white = 255, 240, 200
    black = 20, 20, 40

    #initialize and prepare screen
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('RRTCtxt      S. LaValle    May 2011')
    white = 255, 240, 200
    black = 20, 20, 40
    screen.fill(black)

    ctxt    = RRTCtxt( None, ((0,XDIM),(0,YDIM)) )
    RRT      = BuildRRT( ctxt, (XDIM/2.0,YDIM/2.0), NUMNODES, EPSILON )

    for e in RRT.edges():
        pygame.draw.line(screen,white, e[0], e[1])
        pygame.display.update()


    while True:
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                print( "Leaving because you said so\n" )
                sys.exit()



