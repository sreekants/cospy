#!/usr/bin/python
# Filename: Captain.py
# Description: TODO

from maritime.traffic.actor.Actor import Actor
from maritime.traffic.control.TrafficController import Message

class Captain(Actor):
	def __init__(self):
		Actor.__init__(self)
		return

	def send(self, ctxt, target, msg):
		if isinstance(target, str):
			target = ctxt.vts.get_actor(target)

		if target is None:
			# TODO: Trace an error
			return
		
		target.post( msg )
		return

		

if __name__ == "__main__":
	test = Captain()
	test.send( None, 'PortAuthority', Message('me', 'RELEASE', 'Zone.10'))

