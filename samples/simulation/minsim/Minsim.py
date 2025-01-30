#!/usr/bin/python
# Filename: Minsim.py
# Description: A minimal simulator client

from cos.tools.cviz.RPCAgent import RPCAgent
from cos.tools.cviz.Dispatcher import Dispatcher

from cos.core.api.Vessel import Vessel

import time

class Minsim:
	def __init__(self):
		self.dispatch   = Dispatcher(self)
		self.vessel_id	= 'bedc897f-512b-45a2-aea4-bcfc248d2a8d'
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

		return
	
	def loop(self):
		while True:
			# Listen and handle events
			if self.listen() == False:
				break

			# TODO: Do your stuff on the simulation here....

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
		print(args)
		return

	def on_weather_update(self, args):
		print(args)
		return
	
	def handle_events(self):
		# Handle your UI events here.
		return True

	def move(self, X, Y):
		v	= Vessel()
		v.update( self.vessel_id, {
			"X": X,
			"Y": Y
		})
		return

if __name__ == "__main__":
    test = Minsim()

