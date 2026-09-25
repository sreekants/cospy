#!/usr/bin/python
# Filename: VesselFilter.py
# Description: The vessels under test (REQ.024), loaded from YAML; filters situations and telemetry

import os, yaml

KEYS	= ('guid', 'recid', 'imo', 'mmsi', 'name')


class VesselFilter:
	""" Which vessels are under test.
	"""

	def __init__(self):
		""" Constructor
		"""
		self.source		= None		# File the list was loaded from
		self.entries	= []		# Entries as written, e.g. {'guid': '...'}
		self.telemetry	= {}		# Fact table -> columns naming vessels
		self.vessels	= []		# Resolved vessels under test
		self.ids		= set()		# Object ids of the vessels under test
		self.values		= set()		# Every identifier they carry, as strings
		self.named		= {}		# Object id -> entry that named it, as key=value
		return

	@property
	def active(self)->bool:
		""" Whether anything is filtered
		"""
		return len( self.entries ) > 0

	def load(self, path:str):
		""" Loads the list
		Arguments
			path -- Resolved path to the YAML file; None or absent means no filter
		Returns
			A list of problems, empty when the file is sound
		"""
		self.source		= path
		self.entries	= []
		self.telemetry	= {}

		if (path is None) or (os.path.exists(path) == False):
			return []

		with open( path, 'rb' ) as f:
			config	= yaml.safe_load( f ) or {}

		problems	= []
		for n, entry in enumerate( config.get('under_test', []) or [] ):
			if not isinstance( entry, dict ) or (len(entry) != 1) or (next(iter(entry)) not in KEYS):
				problems.append( f'{path}: under_test[{n}] must be one of {KEYS} with a value, not {entry!r}' )
				continue
			self.entries.append( entry )

		for table, columns in (config.get('telemetry', {}) or {}).items():
			if isinstance( columns, str ):
				columns	= [ columns ]
			self.telemetry[table]	= list( columns or [] )

		return problems

	def resolve(self, vessels):
		""" Matches the entries against the scenario's vessels
		Arguments
			vessels -- Every vessel in the simulation
		Returns
			A list of problems, empty when every entry names exactly one vessel
		"""
		self.vessels	= []
		self.ids		= set()
		self.values		= set()
		self.named		= {}

		problems	= []
		for n, entry in enumerate( self.entries ):
			key, value	= next( iter(entry.items()) )
			found		= [ v for v in vessels if str(self.identifier(v, key)) == str(value) ]

			if len( found ) != 1:
				problems.append( f'{self.source}: under_test[{n}] {key}={value} matches '
								 f'{len(found)} vessels; it must match exactly one' )
				continue

			vessel	= found[0]
			if vessel.id not in self.ids:
				self.vessels.append( vessel )
				self.ids.add( vessel.id )
				self.named[vessel.id]	= f'{key}={value}'
				self.values.update( str(self.identifier(vessel, k)) for k in KEYS
									if self.identifier(vessel, k) not in (None, '', 0, '0') )

		return problems

	def ambiguous(self, vessels):
		""" Identifiers of vessels under test that other vessels share
		Arguments
			vessels -- Every vessel in the simulation
		Returns
			A list of (key, value) pairs a telemetry row could match wrongly
		"""
		shared	= []
		for mine in self.vessels:
			for key in KEYS:
				value	= self.identifier( mine, key )
				if value in (None, '', 0, '0'):
					continue
				if any( (v.id not in self.ids) and (str(self.identifier(v, key)) == str(value))
						for v in vessels ):
					shared.append( (key, value) )
		return shared

	def select(self, vessels):
		""" The vessels under test among a list
		Arguments
			vessels -- Candidate vessels
		Returns
			The list unchanged when nothing is filtered
		"""
		if not self.active:
			return vessels

		return [ v for v in (vessels or []) if v.id in self.ids ]

	def under_test(self, vessel)->bool:
		""" Whether a vessel is under test
		Arguments
			vessel -- Vessel
		"""
		return (not self.active) or (getattr(vessel, 'id', None) in self.ids)

	def keeps(self, topic:str, fields, row)->bool:
		""" Whether a telemetry row should be written
		Arguments
			topic -- Fact table
			fields -- Payload field names, in order
			row -- Payload values
		Returns
			True unless the table is filtered and no vessel column names a
			vessel under test
		"""
		columns	= self.telemetry.get( topic )
		if (not self.active) or (not columns):
			return True

		for column in columns:
			try:
				value	= row[ fields.index(column) ]
			except (ValueError, IndexError):
				continue
			if str( value ) in self.values:
				return True

		return False

	def records(self):
		""" Rows for fact_under_test, recording the list with the data (REQ-024-06)
		Returns
			One row per vessel under test, or one row with filtered=0 when nothing is filtered
		"""
		source	= self.source or ''
		tables	= ','.join( sorted(self.telemetry) )
		if not self.active:
			return [ (0, 0, '', '', '', source, '') ]

		return [ (1, self.identifier(v, 'imo') or 0, v.id, getattr(v, 'name', '') or '',
				  self.named.get(v.id, ''), source, tables) for v in self.vessels ]

	def describe(self)->str:
		""" One line for the log
		"""
		if not self.active:
			return f'every vessel is under test (no list at {self.source})'

		names	= ', '.join( f'{getattr(v, "name", v.id)} [{v.id}]' for v in self.vessels )
		tables	= ', '.join( sorted(self.telemetry) ) or 'none'
		return f'{len(self.vessels)} vessel(s) under test from {self.source}: {names}; telemetry filtered: {tables}'

	@staticmethod
	def identifier(vessel, key:str):
		""" A vessel's identifier of one kind
		Arguments
			vessel -- Vessel
			key -- One of KEYS
		"""
		if key == 'guid':
			return getattr( vessel, 'id', None )

		return getattr( vessel, key, None )


if __name__ == "__main__":
	test = VesselFilter()
