#!/usr/bin/python
# Filename: Minsim.py
# Description: A minimal simulator client

from cos.tools.cviz.RPCAgent import RPCAgent
from cos.tools.cviz.Dispatcher import Dispatcher

from cos.core.api.Vessel import Vessel

import time, random

class Minsim:
	def __init__(self):
		self.dispatch   = Dispatcher(self)
		self.vessel_id	= 'bedc897f-512b-45a2-aea4-bcfc248d2a8d'
		self.proxy		= Vessel()
		return

	def run(self):
		self.init()
		self.loop()
		return

	def init(self):
		# Register events you want to listen to.  (topics)

		self.dispatch.subscribe("vessel.move", self.on_vessel_move)
		# self.dispatch.subscribe("weather.update", self.on_weather_update)

		self.ipc	= RPCAgent()
		self.ipc.connect()

		info		= self.proxy.describe( self.vessel_id )
		print( f'{info["name"]} at {info["pose"]["position"]}' )

		self.loopcount	= 0
		self.start		= time.time()
		return
	
	def loop(self):
		while True:
			# Listen and handle events
			if self.listen() == False:
				break

			# Every 10 seconds steer the vessel
			duration	= int(time.time() - self.start)
			if (duration%10) == 0:
				self.start	=  time.time()
				self.steer_vessel()

			time.sleep(1)
		return
	
	def listen(self):
		""" Polls for events in the simulation
		"""
		# Pump simulation events
		self.ipc.pump( self.dispatch )

		# Process events in the queue
		if self.handle_events() == False:
			return False

		return True

	def on_vessel_move(self, args):
		# print(args)
		return

	def on_weather_update(self, args):
		# print(args)
		return
	
	def handle_events(self):
		# Handle your UI events here.
		return True

	def steer_vessel(self):
		# We will just randomly place the vessel and steer it in a different direction
		# Try playing with various vector attributes, this is only a simple demonstration

		x	= [random.randrange(100, 400), random.randrange(100, 200)]
		v	= [float(random.randrange(1, 200))/100.0-1.0, float(random.randrange(1, 200))/100.0-1.0]
		ω	= [0, 0]

		self.move( x, v, ω )
		return
	
	def move( self, x, v, ω ):
		self.proxy.update( self.vessel_id, {
			
			"pose": {
				# All attributes are optional. You may either set position, X or R.
				# if no property is specified the current state of the property on
				# the server is not modified.
				"position": [x[0], x[1], 0.0],		
				"X": [v[0], v[1], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
				"R": [ω[0], ω[1], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
			}
		})
		return

if __name__ == "__main__":
    test = Minsim()

