#!/usr/bin/python
# Filename: PortAuthority.py
# Description: TODO

from maritime.traffic.control.TrafficController import TrafficController, Message
from maritime.traffic.control.ZoneAllocation import ZoneAllocation
from cos.model.geography.MaritimeZone import MaritimeTrafficZone

class PortAuthority:
	def __init__(self):
		self.traffic		= TrafficController(self)
		self.zones			= {}
		self.allocations	= []
		return


	def add_zone(self, zone:MaritimeTrafficZone):
		name				= zone.config["name"]
		self.zones[name]	= (zone, ZoneAllocation())
		return
	
	def get_occupant(self, zonename):
		zoneinfo = self.zones.get(zonename, None)
		if zoneinfo is None:
			return ''
		
		return zoneinfo[1].occupant

	def allowed(self, zonename, name):
		zoneinfo = self.zones.get(name, None)
		if zoneinfo is None:
			return True
		
		return True if (zoneinfo[1].occupant == name) else False

	def zones(self, name):
		occupation	= []
		for k, v in self.zones.items(): 
			if v[1].occupant == name:
				occupation.append(k)
						
		return occupation


	def run(self, ctxt):
		self.traffic.run(ctxt)
		return

	
	def post(self, req:Message):
		self.traffic.requests.put(req)
		return

if __name__ == "__main__":
	from maritime.model.geography.TrafficLane import TrafficLane

	test = PortAuthority()
	test.add_zone( TrafficLane( None, 'bd9d11e4-8f0a-47f3-aafb-4fa4694685f1', {
						"id": 100,
						"guid":'bd9d11e4-8f0a-47f3-aafb-4fa4694685f1',
						"name": 'Zone.10',
						"depth": 1000
						})
					)
