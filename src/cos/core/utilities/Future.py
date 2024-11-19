#!/usr/bin/python
# Filename: Future.py
# Description: Implementation of a futures class.

from cos.core.utilities.ThreadPool import ThreadPool, PoolTask, CallbackPoolTask

import time

class Future(CallbackPoolTask):
	def __init__(self, pool:ThreadPool, fn:function, ctxt=None, priority=PoolTask.NORMAL):
		""" Constructor
		Arguments
			pool -- Thread pool to use
			fn -- Function to call
			ctxt -- Simulation context
			priority -- Priority of the call
		"""
		CallbackPoolTask.__init__(self, fn, ctxt, priority)

		self.pool		= pool
		self.result		= None
		self.exception	= None

		# Pool the task
		self.pool.queue( self )
		return

	def __lt__(self, other):
		""" Less than operator
		Arguments
			other -- object to compare to
		"""
		return (self.priority < other.priority)

	def execute( self, pool:ThreadPool ):
		""" Executes the task
		Arguments
				pool -- Reference to the containing thread pool
		"""
		self.pool		= pool
		self.result		= self.fn( pool, self.data )
		return

	def	on_error( self, pool:ThreadPool, ex:Exception ):
		""" on_error
		Arguments
			pool -- Reference to the pool
			ex -- Exception raised
		"""
		self.exception	= ex
		return

	def get(self):
		""" Returns the result on completion
		Arguments
			"""
		while self.complete == False:
			self.pool.wait(.05)

		return self.result

	def	cancel(self):
		""" Cancels the task
		"""
		self.pool.remove( self.taskid )
		return

	def wait(self, timeout=None):
		""" Waits for the task to complete
		Arguments
			timeout=None -- Timeout for the wait
		"""
		if self.complete == True:
			return

		# Handle infinite timeout
		if timeout == None:
			while self.complete == False:
				self.pool.WaitForEvent(0.5)
			return

		while self.complete == False:
			start	= time.clock()

			# Wait for an event
			if self.pool.WaitForEvent(timeout)==False:
				break

			# Subtract the elapsed time from the timeout
			timeout	-= time.clock() - start

		return

	def valid(self):
		""" Checks if the task has completed
		Arguments
			"""
		return self.GetStatus() == PoolTask.COMPLETED

	def error(self):
		""" Returns the error
		Arguments
			"""
		return self.exception

if __name__ == "__main__":
    test = Future()


