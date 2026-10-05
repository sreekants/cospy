#!/usr/bin/python
# Filename: Topic.py
# Description: A message topic on the message queue

import queue, fnmatch

class DroppingQueue(queue.Queue):
	def __init__(self, maxsize):
		""" Constructor
		Arguments
			maxsize -- Maximum number of queued items; the oldest is dropped to make room
		"""
		queue.Queue.__init__(self, maxsize)
		self.dropped	= 0		# Items dropped since the last take_dropped()
		return

	def put(self, item, block=True, timeout=None):
		""" Queues an item, dropping the oldest when full; never blocks
		Arguments
			item -- Item to queue
			block -- Ignored
			timeout -- Ignored
		"""
		with self.mutex:
			if len(self.queue) >= self.maxsize:
				self.queue.popleft()
				self.dropped	+= 1
			self.queue.append(item)
			self.unfinished_tasks	+= 1
			self.not_empty.notify()
		return

	def take_dropped(self):
		""" Returns and resets the number of items dropped
		"""
		with self.mutex:
			dropped, self.dropped	= self.dropped, 0
		return dropped

class Topic:
	def __init__(self, maxsize=0):
		""" Constructor
		Arguments
			maxsize -- Bound on queued messages, dropping the oldest when full; 0 is unbounded
		"""
		self.queue			= DroppingQueue(maxsize) if maxsize > 0 else queue.Queue()
		self.subscribers	= []
		self.throttle_rate	= 100000
		return


if __name__ == "__main__":
	test = Topic()


