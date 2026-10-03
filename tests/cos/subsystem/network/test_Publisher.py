#!/usr/bin/python
# Filename: test_Publisher.py
# Description: Test cases for the Publisher, which bins viewer events between pushes to /IPC

import types, unittest
from unittest import mock

from cos.subsystem.network.Publisher import Publisher
from cos.core.kernel.MessageQueue import MessageQueue


def drain(ipc):
	""" Returns the (event, args) pairs waiting on /IPC
	"""
	out		= []
	while not ipc.ipcq.queue.empty():
		evt	= ipc.ipcq.queue.get()
		out.append( (evt.msg, evt.arg) )
	return out

def move(guid, x):
	return {"guid": guid, "rect": [x, 0, 4, 2]}


class PublisherTestCase(unittest.TestCase):
	def setUp(self):
		self.ipc		= MessageQueue()
		objects			= types.SimpleNamespace( register=lambda *args: None )
		self.ctxt		= types.SimpleNamespace( sim=types.SimpleNamespace(ipc=self.ipc, objects=objects), ipc=self.ipc )
		self.publisher	= Publisher()
		self.publisher.on_init( self.ctxt, {"config": "interval=0.2"} )

	def tick(self, now):
		with mock.patch( 'cos.subsystem.network.Publisher.time.monotonic', return_value=now ):
			self.publisher.on_timer( self.ctxt, None )

	def test_registers_on_the_message_queue(self):
		self.assertIs( self.ipc.publisher, self.publisher )
		self.assertEqual( self.publisher.interval, 0.2 )

	def test_one_event_per_interval_with_the_latest_of_each_vessel(self):
		self.tick( 0.0 )										# First tick pushes the (empty) bins
		for x in range(5):										# Five ticks inside one interval
			self.ipc.publish( 'vessel.move', 'v1', move('v1', x) )
			self.ipc.publish( 'vessel.move', 'v2', move('v2', 10+x) )
			self.tick( 0.03*(x+1) )
		self.assertEqual( drain(self.ipc), [] )

		self.tick( 0.2 )
		self.assertEqual( drain(self.ipc), [('vessel.move', [move('v1', 4), move('v2', 14)])] )

	def test_bins_are_pushed_per_event_and_emptied(self):
		self.ipc.publish( 'vessel.move', 'v1', move('v1', 1) )
		self.ipc.publish( 'weather.update', 'w1', {"guid": "w1"} )
		self.tick( 0.0 )
		self.assertEqual( drain(self.ipc), [('vessel.move', [move('v1', 1)]), ('weather.update', [{"guid": "w1"}])] )

		self.tick( 0.5 )
		self.assertEqual( drain(self.ipc), [] )

	def test_without_a_publisher_events_go_straight_to_ipc(self):
		ipc		= MessageQueue()
		ipc.publish( 'vessel.move', 'v1', move('v1', 1) )
		ipc.publish( 'vessel.move', 'v1', move('v1', 2) )
		self.assertEqual( drain(ipc), [('vessel.move', [move('v1', 1)]), ('vessel.move', [move('v1', 2)])] )


if __name__ == '__main__':
	unittest.main()
