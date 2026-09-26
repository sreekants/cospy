#!/usr/bin/python
# Filename: Location.py
# Description: Settings of the simulated location, loaded once from $(SIMULATION)/location.yaml

from cos.core.kernel.Context import Context

import yaml

DEFAULT		= '$(SIMULATION)/location.yaml'


class Location:
	""" Location settings shared by every faculty, and the depth fallback count (REQ.022)
	"""
	_shared		= {}

	@classmethod
	def shared(cls, ctxt:Context, path=None):
		""" The settings at path, loaded on first use
		Arguments
			ctxt -- Simulation context
			path -- Settings file; defaults to $(SIMULATION)/location.yaml
		Raises
			ValueError when the file is missing or declares no nominal depth
		"""
		resolved	= ctxt.sim.config.resolve( path or DEFAULT )
		if resolved not in cls._shared:
			location	= cls()
			location.load( ctxt, resolved )
			cls._shared[resolved]	= location

		return cls._shared[resolved]

	def __init__(self, nominal_depth=None):
		""" Constructor
		Arguments
			nominal_depth -- Seabed depth in metres where the map reports none
		"""
		self.path			= None
		self.nominal_depth	= nominal_depth
		self.queries		= 0
		self.fallbacks		= 0
		return

	def load(self, ctxt:Context, path:str):
		""" Reads location.depth.nominal from path
		Arguments
			ctxt -- Simulation context
			path -- Resolved path of location.yaml
		"""
		try:
			config	= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(path) ) or {}
		except Exception as e:
			raise ValueError( f'No location settings in {path}: {e}' )

		depth	= ((config.get('location', {}) or {}).get('depth', {}) or {})
		nominal	= depth.get( 'nominal' )
		if isinstance(nominal, bool) or not isinstance(nominal, (int, float)) or nominal <= 0:
			raise ValueError( f'{path}: location.depth.nominal must be a positive depth in metres, not {nominal!r}' )

		self.path			= path
		self.nominal_depth	= float( nominal )
		return

	def seabed_depth(self, measured):
		""" The measured depth, or the nominal depth when the map reports none
		Arguments
			measured -- Depth off the map shapes, or None
		"""
		self.queries	+= 1
		if measured is not None:
			return measured

		self.fallbacks	+= 1
		return self.nominal_depth

	def describe(self)->str:
		""" One line for the run log
		"""
		return f'{self.fallbacks} of {self.queries} depth queries used the nominal depth ' \
			   f'{self.nominal_depth:.0f} m from {self.path}'


if __name__ == "__main__":
	test = Location( 4000.0 )
