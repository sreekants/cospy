#!/usr/bin/python
# Filename: TrafficController.py
# Description: TODO

from maritime.traffic.actor.TrafficActor import TrafficActor
from maritime.traffic.control.ZoneAllocation import ZoneAllocation

class Message:
	def __init__(self, sender, action:str=None, target:str=None):
		self.source		= sender
		self.action		= action
		self.target		= target
		return

class TrafficController(TrafficActor):
	def __init__(self, authority):
		TrafficActor.__init__(self)
		self.authority	= authority
		self.vts		= None
		return

	def run(self, ctxt):
		# Process all messages
		TrafficActor.run(self, ctxt, self.process)
		return

	def process(self, ctxt, req:Message):
		zoneinfo = self.authority.zones.get(req.target, None)

		if req.action == 'RESERVE':
			if zoneinfo is None:
				#TODO: Trace error
				return
			
			zone:ZoneAllocation	= zoneinfo[1]
			if zone.occupied:
				self.send(ctxt, req.target, Message(self.name, 'RESERVE.DENIED', req.target))
				return
			
			zone.reserve(req.source)
			return
		
		if req.action == 'RELEASE':
			if zoneinfo is None:
				#TODO: Trace error
				return
			
			zone:ZoneAllocation	= zoneinfo[1]
			if zone.occupant != req.source:
				return
			
			zone.release()
			return
		
		return


if __name__ == "__main__":
	test = TrafficController()

