#!/usr/bin/python
# Filename: Actor.py
# Description: TODO

import queue, fnmatch

class Actor:
	def __init__(self):
		self.requests	= queue.Queue()
		return

	def pump(self, ctxt, fn):
		while self.requests.empty() == False:
			req = self.requests.get()
			fn(ctxt, req)

	def run(self, ctxt, fn):
		self.pump(ctxt, fn)
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
	test = Actor()

