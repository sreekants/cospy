#!/usr/bin/python
# Filename: EventId.py
# Description: Hands out a unique, monotonically increasing id for each occurrence in a simulation run

import threading


class EventId:
	""" Process-wide id factory: situations, encounters, episodes, epochs and other occurrences each
	draw one id, so the rows they leave in different tables can be joined on it.
	"""
	_lock	= threading.Lock()
	_next	= 1

	@classmethod
	def next(cls)->int:
		""" A new id, greater than every id handed out before it in this run
		"""
		with cls._lock:
			value		= cls._next
			cls._next	= value + 1
		return value

	@classmethod
	def last(cls)->int:
		""" The id handed out most recently, 0 when none has been
		"""
		with cls._lock:
			return cls._next - 1

	@classmethod
	def reset(cls, start:int=1):
		""" Starts the sequence again, once per run when the kernel starts
		Arguments
			start -- The next id to hand out
		"""
		if int( start ) < 1:
			raise ValueError( f'EventId: ids start at 1, not {start}' )

		with cls._lock:
			cls._next	= int( start )
		return


if __name__ == "__main__":
	print( EventId.next(), EventId.next(), EventId.last() )
