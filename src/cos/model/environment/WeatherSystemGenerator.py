#!/usr/bin/python
# Filename: WeatherSystemGenerator.py
# Description: Implementation of the WeatherSystemGenerator class

import numpy as np
import math, random

EPSILON = 0.0001

class WeatherSystemGenerator:
	def __init__(self, range=2, count=40):
		""" Constructor
		Arguments
			range -- #TODO
			count -- #TODO
		"""
		self.count	= count
		self.data	= []
		self.range	= range
		return

	def generate(self, world):
		""" #TODO: generate
		Arguments
			world -- Reference ot the simulation world
		"""
		i = 1
		while len(self.data) != self.count:
			x = random.randrange( 0, 1200 )
			y = random.randrange( 0, 900 )

			range = self.range
			half = self.range/2

			Xx = float(random.randrange(1,range)-half)/half
			Xy = float(random.randrange(1,range)-half)/half
			Rx = float(random.randrange(1,range)-half)/half

			if Xx == 0 or Xy == 0 or Rx == 0:
				continue

			if world.collider.contains((x,y)) == False:
				rec = f'{i};{x},{y},0;{Xx:0.2},{Xy:0.2},0,0,0,0,0,0,0,0,0,0;{Rx:0.2},0,0,0,0,0,0,0,0,0,0,0\n'
				self.data.append(rec)
				i	= i+1


	def save(self, path):
		""" #TODO: save
		Arguments
			path -- #TODO
		"""
		with open(path,'w') as fp:
			fp.write( 'id;X;Vx;Vr;\n' )
			for rec in self.data:
				fp.write(rec)
		return


if __name__ == "__main__":
	test = WeatherSystemGenerator()


