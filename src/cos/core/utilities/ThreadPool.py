#!/usr/bin/python
# Filename: ThreadPool.py
# Description: Helper thread pool class

from threading import Thread, RLock, Event
import heapq, time, os

class PoolTask:
	# enum PRIORITY
	HIGHEST	= 0x10,
	HIGH	= 0x20,
	NORMAL	= 0x40,
	LOW		= 0x60,
	LOWEST	= 0x80

	#enum STATUS
	FLAG_RUNNABLE	= 0x10,
	FLAG_ERROR		= 0x20,

	NOT_FOUND		= 0x01,
	CREATED			= 0x12,	# Initialized and ready to run
	ABORTED			= 0x03,	# Aborted by the OS
	RUNNING			= 0x14,	# Currently running
	READY			= 0x15,	# Resumed by the OS
	SUSPENDED		= 0x16,	# Suspended by the OS
	BLOCKED			= 0x17, # Blocked on an event.
	COMPLETED		= 0x08,	# Completed normally
	ABNORMAL_EXIT	= 0x29,	# Aborted with an unhandled exception
	RUNTIME_ERROR	= 0x2A,	# Aborted with a runtime error.

	# Following status is a mask to filter tasks with any status
	STATUS_UNKNOWN	= 0xFF

	def __init__(self, priority, data ):
		""" Constructor.
		"""
		self.priority	= priority
		self.data		= data
		self.status		= PoolTask.CREATED
		self.active		= True
		self.threadid		= -1
		return

	# Overridables
	def execute( self, pool ):
		""" Executes the task
		Arguments
			self -- reference to this instance
			pool -- Reference to the containing thread pool
		"""
		return

	@property
	def type(self):
		""" Returns the type of the task
		"""
		return 'Pool.Task'

	def	on_event( self, event ):
		""" Event handler for event
		Arguments
			event -- Event sent to the thread
		"""
		return

	def	on_begin( self, pool ):
		""" Event handler for begin
		Arguments
			pool -- Reference to the containing thread pool
		"""
		return

	def	on_end( self, pool ):
		""" Event handler for end
		Arguments
			pool -- Reference to the containing thread pool
		"""
		return

	def	on_error( self, pool, ex ):
		""" Event handler for error
		Arguments
			pool -- Reference to the containing thread pool
			ex -- Exception for the error
		"""
		return

	def	on_delete( self, pool ):
		""" Event handler for delete
		Arguments
			pool -- Reference to the containing thread pool
		"""
		return

	def can_exit(self):
		""" Indicates that the thread pool can delete this task on exit.
		"""
		return True

	@property
	def complete(self):
		""" Checks if the thread has completed
		Arguments
			self -- reference to this instance
		"""
		return (self.status[0]&0x0F) >= PoolTask.COMPLETED[0]


class CallbackPoolTask(PoolTask):
	def __init__(self, fn, data, priority:int ):
		""" Constructor.
		Arguments
			self -- reference to this instance
		"""
		PoolTask.__init__(self, priority, data)
		self.fn		= fn
		return

	# Overridables
	def execute( self, pool ):
		""" Executes the task
		Arguments
			self -- reference to this instance
			ThreadPool -- Reference to the containing thread pool
		"""
		self.fn( pool, self.data )
		return


class PoolThread(Thread):
	def __init__(self, pool):
		""" Constructor.
		Arguments
			self -- reference to this instance
			pool -- reference to the pool
		"""
		Thread.__init__(self)
		self.ThreadPool	= pool
		self.can_exit	= False
		self.task		= None
		return

	def run(self):
		""" Thread run method. Process all pending tasks.
		Arguments
			self -- reference to this instance
		"""

		while self.can_exit == False:
			self.ThreadPool.wait(.5)

			# Check again (double-locking) if the signal is one for an exit
			if self.can_exit:
				break

			if self.next() == False:
				continue

			if self.task.active == False:
				self.requeue()
				continue

			try:
				# Signal the beginning of the task
				self.task.on_begin( self.ThreadPool )
				self.ThreadPool.on_begin( self.task )

				# Execute the task
				self.execute_task( self.task )

				# Invoke override to signal the end of the task
				self.ThreadPool.on_end( self.task )
				self.task.on_end( self.ThreadPool )

				if self.task.can_exit()==False:
					self.requeue()
					continue

				self.task.status = PoolTask.COMPLETED

				self.clear()

			except Exception as e:
				self.task.status = PoolTask.ABNORMAL_EXIT
				self.ThreadPool.on_error( self.task, e )
				self.clear()

		return

	def execute_task(self, task):
		""" Executes the current task
		Arguments
			self -- reference to this instance
			task -- task to run
		"""
		try:
			task.status	= PoolTask.RUNNING
			task.execute( self.ThreadPool )
			if task.can_exit == True:
				task.status 	= PoolTask.COMPLETED
			else:
				task.status 	= PoolTask.READY

		except Exception as e:
			self.task.status 	= PoolTask.RUNTIME_ERROR
			self.task.on_error( self.ThreadPool, e )
			self.ThreadPool.on_error( self.task, e )

		return

	def requeue(self):
		""" Requeue the current tast
		"""
		with self.ThreadPool.lock:
			self.ThreadPool.queue(self.task)
			self.task == None
		return

	def clear(self):
		""" Clear the current task
		"""
		with self.ThreadPool.lock:
			self.task == None
		return

	def next(self):
		""" Switches to the next task in the queue
		"""
		with self.ThreadPool.lock:
			tasks	= []
			result	= self.ThreadPool.pop( tasks, 1 )

			if result == True:
				self.task	= tasks[0]

		return result

	def stop(self):
		""" Stops the thread
		Arguments
			self -- reference to this instance
		"""
		self.can_exit	= True
		return

class ThreadPool:
	def __init__(self):
		""" Constructor
		Arguments
			self -- reference to this instance
		"""
		self.threads		= []
		self.taskq			= []
		self.lock			= RLock()
		self.queue_signal	= Event()
		self.empty_signal	= Event()
		self.curr_tid		= 0
		return

	def close(self):
		""" Closes the threadpool releasing resources
		Arguments
			self -- reference to this instance
		"""
		if self.taskq == None:
			return

		# Signal all threads to stop
		for t in self.threads:
			t.stop()

		# Clear any pending tasks
		self.clear()

		# Wait for all threads to end
		for t in self.threads:
			t.join()

		self.threads	= []
		return

	@property
	def size(self):
		""" Returns the number of threads in the pool
		"""
		return len(self.threads)

	@property
	def pending(self):
		""" Returns the number of pending tasks in the pool
		"""
		with self.lock:
			result	= len( self.taskq )

		return result

	def create( self, maxthreads ):
		""" Creates the pool
		Arguments
			maxthreads -- Maximum threads
		"""
		# The optimal number of threads running on the server
		# is two times the number of processors.
		# (Refer: Advanced Windows - Jeffery Richter)
		if maxthreads == 0:
			maxthreads	= os.cpu_count()

		for n in range(0,maxthreads):
			self.threads.append( self.create_thread() )

		return len(self.threads)

	def create_thread(self):
		""" Overridable to create the pool thread instance
		"""
		thread	= PoolThread(self)
		thread.start()
		return thread

	# Task functions
	def wait(self):
		""" Waits for all tasks to complete
		"""
		while self.pending != 0:
			time.sleep(1)

		return

	def clear(self):
		""" Clears all pending tasks
		"""
		return


	def	queue( self, task:PoolTask ):
		""" Queues a task on the thread pool
		Arguments
			fnTaskProc -- Callback function to invoke to process the task
			data -- Context data to pass to the callback
			TaskPriority=PoolTask.NORMAL -- Priority of the task
		"""
		with self.lock:
			self.curr_tid	+= 1
			task.taskid		= self.curr_tid
			heapq.heappush( self.taskq, [task.priority, task] )

			# Set the event
			self.queue_signal.set()

		return self.curr_tid

	def queue_callback( self, fn, data=None, priority=PoolTask.NORMAL ):
		""" Queues a function callback as a task on the thread pool
		Arguments
			fn -- Callback function to invoke to process the task
			data -- Context data to pass to the callback
			priority=PoolTask.NORMAL -- Priority of the task
		"""
		return self.queue( CallbackPoolTask(fn, data, priority) )


	def	pop( self, result:list, numtask:int ):
		""" Pops the next task in the queue
		Arguments
			result -- List to populate with tasks
			numtask -- Maximum number of tasks to retrieve
		"""
		with self.lock:
			for n in range(0,numtask):
				if len(self.taskq)==0:
					break

				priority, task	= heapq.heappop( self.taskq )

				result.append( task )

			# Reset the event
			if len(self.taskq) == 0:
				self.queue_signal.clear()


		if len(result) == 0:
			return False

		return True

	def remove( self, tid ):
		""" Removes a task with a identifier from the queue
		Arguments
			tid -- Task identifier
		"""
		with self.lock:
			for task in self.taskq:
				if task.taskid == tid:
					self.taskq.remove( task )
					return True

		return False


	def for_each( self, fn ):
		""" Invokes a callback for each task
		Arguments
			fn -- Callback (derived from CallbackPoolTask): to invoke
		"""
		with self.lock:
			for task in self.taskq:
				fn( self, task )
		return

	def	post( self, tid, event ):
		""" Sends an event to a task
		Arguments
			tid -- Task ID to match
			event -- event to pass to the task
		"""
		with self.lock:
			for task in self.taskq:
				if task.taskid == tid:
					task.on_event( task, event )
		return

	def get_task_status( self, tid ):
		""" Returns the status of a task
		Arguments
			tid -- Task ID
		"""
		with self.lock:
			for task in self.taskq:
				if task.taskid == tid:
					return task.status

		return PoolTask.STATUS_UNKNOWN


	def wait(self, timeout=None):
		""" Wait for the queue to be signaled
		Arguments
			timeout=None -- Timeout to wait for
		"""
		return self.queue_signal.wait(timeout)

	def	on_error( self, task, ex ):
		""" Event handler for error
		Arguments
			task -- Task reference
			ex -- Exception for the error
		"""
		return

	def	on_begin( self, task ):
		""" Event handler for begin
		Arguments
			task -- Task reference
		"""
		return

	def	on_end( self, task ):
		""" Event handler for end
		Arguments
			task -- Task reference
		"""
		return

if __name__ == '__main__':
    test = ThreadPool()


