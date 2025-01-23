#!/usr/bin/python
# Filename: ZoneAllocation.py
# Description: TODO

from enum import Enum

class ZoneStatus(Enum):
	"""Enum for the zone allocation status."""
	UNAVAILABLE	= 0
	AVAILABLE	= 1
	RESERVED	= 2
	ALLOCATED	= 3

class ZoneAllocation:
	def __init__(self):
		self._status	= ZoneStatus.UNAVAILABLE
		self._occupant	= None
		return

	def reset(self):
		occupant		= self._occupant
		self._status	= ZoneStatus.AVAILABLE
		self._occupant	= None
		return occupant

	def reserve(self, occupant):
		self._status	= ZoneStatus.RESERVED
		self._occupant	= occupant
		return

	def release(self):
		self._status	= ZoneStatus.AVAILABLE
		self._occupant	= None
		return

	def close(self):
		self._status	= ZoneStatus.UNAVAILABLE
		return

	def open(self):
		self._status	= ZoneStatus.AVAILABLE
		return

	@property
	def status(self):
		return self._status

	@property
	def occupant(self):
		return self._occupant

	@property
	def occupied(self):
		return self._occupant is not None

if __name__ == "__main__":
	test = ZoneAllocation()

