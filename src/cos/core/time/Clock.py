#!/usr/bin/python
# Filename: Clock.py
# Description: Implementation of the Clock class, the simulated clock of the kernel

import datetime, threading

DEFAULT_STEP	= 1.0		# Simulated seconds per tick
DEFAULT_EPOCH	= datetime.datetime( 2026, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc )

class Clock:
	def __init__(self, step=DEFAULT_STEP, epoch=DEFAULT_EPOCH):
		""" Constructor
		Arguments
			step -- Simulated seconds per tick
			epoch -- Simulated time at tick 0, a timezone-aware datetime
		"""
		self.ticks		= 0
		self.local_view	= threading.local()
		self.configure( step, epoch )
		return

	def configure(self, step=DEFAULT_STEP, epoch=DEFAULT_EPOCH):
		""" Sets the tick length and the epoch
		Arguments
			step -- Simulated seconds per tick
			epoch -- Simulated time at tick 0, a timezone-aware datetime or ISO 8601 text
		"""
		if isinstance( epoch, str ):
			epoch	= datetime.datetime.fromisoformat( epoch.strip() )
		if epoch.tzinfo is None:
			raise ValueError( f'Clock: epoch {epoch.isoformat()} has no timezone' )
		if float(step) <= 0:
			raise ValueError( f'Clock: tick length must be positive, not {step}' )

		self.step	= float(step)
		self.epoch	= epoch
		return

	def advance(self):
		""" Advances the clock by one tick. Only the thread that owns the clock calls this
		"""
		self.ticks	= self.ticks+1
		return self.ticks

	def reset(self):
		""" Resets the clock to tick 0
		"""
		self.ticks	= 0
		return

	def pin(self, tick):
		""" Freezes the clock at a tick for the calling thread
		Arguments
			tick -- Tick the calling thread reads until unpin()
		"""
		self.local_view.tick	= tick
		return

	def unpin(self):
		""" Returns the calling thread to the live tick
		"""
		self.local_view.tick	= None
		return

	@property
	def live(self):
		""" Returns the latest tick, whatever the calling thread has pinned
		"""
		return self.ticks

	@property
	def tick(self):
		""" Returns the tick seen by the calling thread
		"""
		pinned	= getattr( self.local_view, 'tick', None )
		return self.ticks if pinned is None else pinned

	@property
	def seconds(self):
		""" Returns the simulated seconds since the epoch
		"""
		return self.tick * self.step

	@property
	def utc(self):
		""" Returns the simulated time in UTC
		"""
		return self.local.astimezone( datetime.timezone.utc )

	@property
	def local(self):
		""" Returns the simulated time in the epoch's timezone, the scenario's local time
		"""
		return self.epoch + datetime.timedelta( seconds=self.seconds )

	@property
	def tickcount(self):
		""" Returns the tick seen by the calling thread
		"""
		return self.tick

def hour_of(now):
	""" Local hour of a clock reading
	Arguments
		now -- A datetime, or simulated seconds since midnight of the first day
	"""
	if now is None:
		return None

	if isinstance( now, datetime.datetime ):
		return now.hour

	try:
		return int( (float(now) // 3600) % 24 )
	except (TypeError, ValueError):
		return None

def within_hours(hour, start, end)->bool:
	""" Whether an hour falls in a daily window, which wraps midnight when start > end
	Arguments
		hour -- Hour of the day, None when unknown
		start -- First hour in the window
		end -- First hour after the window
	"""
	if (hour is None) or (start == end):
		return False

	if start > end:
		return (hour >= start) or (hour < end)

	return start <= hour < end

def utcnow():
	""" Returns the host time in UTC, for timestamps of real-time events
	"""
	return datetime.datetime.now( datetime.timezone.utc )


if __name__ == "__main__":
	test = Clock()


