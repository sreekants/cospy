#!/usr/bin/python
# Filename: Signal.py
# Description: The lights, shapes and sound signals a vehicle is showing, named from one vocabulary (REQ.036)

from cos.model.vehicle.ValueSet import ValueSet

import fnmatch, os, yaml

CLASSES		= ('navigation', 'restricted_visibility', 'encounter')


class Vocabulary:
	""" The signal names a scenario may use, each with the class saying when it may be shown
	"""
	def __init__(self, path:str):
		""" Constructor
		Arguments
			path -- Resolved path to the vocabulary YAML
		Raises
			ValueError when an entry has no known class
		"""
		self.source		= path
		self.names		= {}		# Name -> class

		with open( path, 'rb' ) as f:
			config	= yaml.safe_load( f ) or {}

		for name, entry in (config.get('signals', {}) or {}).items():
			kind	= (entry or {}).get( 'class' )
			if kind not in CLASSES:
				raise ValueError( f'{path}: signal {name!r} has class {kind!r}, expected one of {CLASSES}' )
			self.names[name]	= kind
		return

	def matches(self, pattern:str)->list:
		""" Names a pattern matches, case-sensitively on every platform
		Arguments
			pattern -- Name or wildcard pattern, e.g. 'Sound.Foghorn*'
		"""
		return [ n for n in self.names if fnmatch.fnmatchcase(n, pattern) ]

	def check(self, pattern:str, where:str=None):
		""" Raises unless a pattern names at least one signal
		Arguments
			pattern -- Name or wildcard pattern
			where -- What named it, for the message
		"""
		if not self.matches( pattern ):
			at	= f'{where}: ' if where else ''
			raise ValueError( f'{at}{pattern!r} is not in the signal vocabulary {self.source}' )
		return

	def category(self, name:str):
		""" Class of a signal, or None when the name is not in the vocabulary
		Arguments
			name -- Signal name
		"""
		return self.names.get( name )


class Signal(ValueSet):
	vocabulary	= None		# Shared by every vehicle; None until a scenario loads one
	missing		= None		# Path already reported missing

	def __init__(self):
		ValueSet.__init__(self)
		return

	@classmethod
	def configure(cls, path:str, log=None):
		""" Loads the vocabulary once per process
		Arguments
			path -- Resolved path to the vocabulary YAML
			log -- Logger, for a missing file
		"""
		if (cls.vocabulary is not None) and (cls.vocabulary.source == path):
			return cls.vocabulary

		if (path is None) or (os.path.exists(path) == False):
			if (log is not None) and (cls.missing != path):
				log.warning( 'Signal', f'No signal vocabulary at {path}; signal names are not checked' )
			cls.missing	= path
			return None

		cls.vocabulary	= Vocabulary( path )
		return cls.vocabulary

	@classmethod
	def category(cls, name:str):
		""" Class of a signal, or None without a vocabulary or for an unknown name
		Arguments
			name -- Signal name
		"""
		return cls.vocabulary.category( name ) if cls.vocabulary is not None else None

	def set(self, value):
		""" Shows a signal
		Arguments
			value -- Signal name, e.g. 'Light.Sidelight'
		Raises
			ValueError when a vocabulary is loaded and does not hold the name
		"""
		if (Signal.vocabulary is not None) and (Signal.vocabulary.category(value) is None):
			raise ValueError( f'{value!r} is not in the signal vocabulary {Signal.vocabulary.source}' )
		return ValueSet.set( self, value )

	def find(self, spec):
		""" Whether a shown signal matches a pattern; case-sensitive, unlike StringSet.find on Windows
		Arguments
			spec -- Name or wildcard pattern
		"""
		return any( fnmatch.fnmatchcase(v, spec) for v in self )


if __name__ == "__main__":
	test = Signal()
