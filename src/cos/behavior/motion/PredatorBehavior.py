#!/usr/bin/python
# Filename: PredatorBehavior.py
# Description: Implementation of the PredatorBehavior class

from cos.behavior.motion.FleetBehavior import FleetBehavior
from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.core.kernel.Configuration import Configuration
from cos.math.geometry.Distance import Distance
from io import StringIO
from math import cos,sin,atan2
import numpy as np
import csv

class PredatorBehavior(FleetBehavior):
	def __init__(self):
		print( "Hello" )
		return

		

if __name__ == "__main__":
	test = PredatorBehavior()

