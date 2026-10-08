#!/usr/bin/python
# Filename: Examination.py
# Description: Implementation of the Examination class, the event every examiner receives

from enum import Enum

EXAMINATION	= 'examination'		# Message name an examination is posted under


class ExaminationType(Enum):
	""" What an examination's body is
	"""
	VOYAGE_EPISODE			= 1
	ENCOUNTER_EPISODE		= 2
	GROUNDING_EPISODE		= 3
	COMM_FAILURE_EPISODE	= 4
	VIOLATION_EPISODE		= 5
	EPOCH_EPISODE			= 6

	# One per continuous check; the body is a rule Situation
	ENCOUNTER				= 101
	GROUNDING				= 102
	BERTHING				= 103
	SPEED					= 104
	NIGHT_TIME				= 105
	SIGNAL					= 106
	NUISANCE				= 107
	CARGO					= 108
	EXTREME_WEATHER			= 109
	RISK					= 110


class Examination:
	def __init__(self, type:ExaminationType, body):
		""" Constructor
		Arguments
			type -- Kind of examination, telling the examiner what the body is
			body -- Payload to examine
		"""
		if isinstance( type, ExaminationType ) == False:
			raise TypeError( f'Examination: type must be an ExaminationType, not {type!r}' )

		self.type	= type
		self.body	= body
		return

	def __repr__(self):
		return f'Examination({self.type.name}, {type(self.body).__name__})'



if __name__ == "__main__":
	test = Examination( ExaminationType.VOYAGE_EPISODE, None )
