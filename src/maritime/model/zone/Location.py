#!/usr/bin/python
# Filename: Location.py
# Description: Settings of the simulated location, loaded once from $(SIMULATION)/location.yaml

from cos.core.kernel.Context import Context

import yaml

DEFAULT		= '$(SIMULATION)/location.yaml'
MEASURED	= 'measured'		# Depth off a map shape
NOMINAL		= 'nominal'			# Depth from the fallback


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
		self.tss			= {}		# Traffic separation scheme defaults: safe_distance, separation_distance
		self.lanes			= {}		# Lane shape name or dotted prefix -> its settings, e.g. safe_heading
		self.queries		= 0
		self.fallbacks		= 0
		return

	def load(self, ctxt:Context, path:str):
		""" Reads location.sea.depth.nominal and the optional location.sea.tss from path
		Arguments
			ctxt -- Simulation context
			path -- Resolved path of location.yaml
		"""
		try:
			config	= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(path) ) or {}
		except Exception as e:
			raise ValueError( f'No location settings in {path}: {e}' )

		location	= config.get( 'location', {} ) or {}
		if 'depth' in location:
			raise ValueError( f'{path}: location.depth has moved to location.sea.depth' )

		sea		= location.get( 'sea', {} ) or {}
		nominal	= (sea.get( 'depth', {} ) or {}).get( 'nominal' )
		if not Location.positive( nominal ):
			raise ValueError( f'{path}: location.sea.depth.nominal must be a positive depth in metres, not {nominal!r}' )

		tss		= sea.get( 'tss', {} ) or {}
		self.tss	= Location.lane_settings( path, 'location.sea.tss', {k: v for k, v in tss.items() if k != 'lanes'} )
		self.lanes	= { str(name): Location.lane_settings(path, f'location.sea.tss.lanes.{name}', settings or {})
						for name, settings in (tss.get( 'lanes', {} ) or {}).items() }

		self.path			= path
		self.nominal_depth	= float( nominal )
		return

	@staticmethod
	def lane_settings(path:str, where:str, settings:dict)->dict:
		""" Checks TSS settings: distances positive, a heading in degrees
		Arguments
			path -- Location file, for the error
			where -- Key the settings were read from, for the error
			settings -- The settings
		Raises
			ValueError on an unknown key or a bad value
		"""
		checked	= {}
		for key, value in settings.items():
			if key in ('safe_distance', 'separation_distance'):
				if not Location.positive( value ):
					raise ValueError( f'{path}: {where}.{key} must be a positive distance in metres, not {value!r}' )
			elif key == 'safe_heading':
				if isinstance(value, bool) or not isinstance(value, (int, float)) or not (0 <= value < 360):
					raise ValueError( f'{path}: {where}.safe_heading must be degrees in [0, 360), not {value!r}' )
			else:
				raise ValueError( f'{path}: {where}.{key} is not a TSS setting' )
			checked[key]	= float( value )
		return checked

	@staticmethod
	def positive(value)->bool:
		""" Whether a setting is a positive number, not a boolean
		Arguments
			value -- Setting read from the file
		"""
		return (not isinstance(value, bool)) and isinstance(value, (int, float)) and (value > 0)

	def lane(self, name:str, key:str):
		""" A TSS setting for a lane: the longest lane entry naming it, else the scheme default
		Arguments
			name -- Shape name of the lane, e.g. Copenhagen.TSS.Northbound.4.1
			key -- safe_distance, safe_heading or separation_distance
		Returns
			The value, or None when the location sets none
		"""
		name	= name or ''
		matches	= [ entry for entry, settings in self.lanes.items()
					if (key in settings) and ((name == entry) or name.startswith(entry + '.')) ]
		if matches:
			return self.lanes[max( matches, key=len )][key]

		return self.tss.get( key )

	def seabed_depth(self, measured, nominal=None):
		""" The measured depth, or the nominal depth when the map reports none
		Arguments
			measured -- Depth off the map shapes, or None
			nominal -- The zones' nominal depth where they set one, else None for the location's
		"""
		self.queries	+= 1
		if measured is not None:
			return measured

		self.fallbacks	+= 1
		return self.nominal_depth if nominal is None else nominal

	@staticmethod
	def provenance(measured)->str:
		""" Where a depth came from, for the recorded data (REQ-022-04)
		Arguments
			measured -- Depth off the map shapes, or None
		"""
		return MEASURED if measured is not None else NOMINAL

	def describe(self)->str:
		""" One line for the run log
		"""
		return f'{self.fallbacks} of {self.queries} depth queries used the nominal depth ' \
			   f'{self.nominal_depth:.0f} m from {self.path}'


if __name__ == "__main__":
	test = Location( 4000.0 )
