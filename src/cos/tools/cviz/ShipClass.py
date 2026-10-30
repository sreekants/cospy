#!/usr/bin/python
# Filename: ShipClass.py
# Description: Principal dimensions of a vessel, read from its ship model file

from cos.core.utilities.ArgList import ArgList
from pathlib import Path
import os, re, yaml

# Used when a vessel names no ship model, or its file cannot be read
DEFAULT_DIMENSIONS	= (20.0, 5.0, 1.5)

class ShipClass:
	cache	= {}		# Ship model path -> ShipClass

	def __init__(self, name:str, length:float, width:float, draft:float, kind:str):
		""" Constructor
		Arguments
			name -- Ship model name, e.g. container
			length -- Length overall in metres
			width -- Greatest breadth in metres
			draft -- Draft in metres
			kind -- Activity type of the model, e.g. tanker
		"""
		self.name	= name
		self.length	= length
		self.width	= width
		self.draft	= draft
		self.kind	= kind
		return

	@classmethod
	def of(cls, config:dict):
		""" Returns the ship class of a vessel from its world description
		Arguments
			config -- Vessel configuration from describe("world")
		Returns
			A ShipClass, with default dimensions when the model is unknown
		"""
		settings	= ArgList( config.get("settings", None) )
		modelfile	= settings['ship.model']
		if not modelfile:
			return cls( 'unknown', *DEFAULT_DIMENSIONS, 'unknown' )

		if modelfile not in cls.cache:
			cls.cache[modelfile]	= cls.load( modelfile )
		return cls.cache[modelfile]

	@classmethod
	def load(cls, modelfile:str):
		""" Loads a ship model file
		Arguments
			modelfile -- Path as the vessel database names it, e.g. $(CONFIG)/vehicle/ship/ferry.yaml
		"""
		name	= Path( modelfile ).stem
		path	= cls.resolve( modelfile )
		try:
			with open( path, 'rb' ) as f:
				model	= yaml.safe_load( f ) or {}
		except OSError:
			print( f'Ship model {modelfile} not found at {path}; using default dimensions' )
			return cls( name, *DEFAULT_DIMENSIONS, name )

		physics	= model.get( 'physics', {} ) or {}
		kind	= (model.get( 'activity', {} ) or {}).get( 'type', name )
		return cls( name,
					float( physics.get('length', DEFAULT_DIMENSIONS[0]) ),
					float( physics.get('width', DEFAULT_DIMENSIONS[1]) ),
					float( physics.get('draft', DEFAULT_DIMENSIONS[2]) ),
					str( kind ) )

	@staticmethod
	def resolve(modelfile:str):
		""" Expands $(CONFIG) and $(ROOT) in a ship model path on this machine
		Arguments
			modelfile -- Path with configuration macros
		"""
		root	= os.environ.get( 'COS_ROOT', str(Path(__file__).resolve().parents[4]) )
		config	= os.environ.get( 'COS_CONFIG', os.path.join(root, 'config') )
		macros	= { 'CONFIG': config, 'ROOT': root, 'DB': config }
		return re.sub( r'\$\((\w+)\)', lambda m: macros.get(m.group(1), m.group(0)), modelfile )


if __name__ == "__main__":
	test = ShipClass.of( {"settings": "ship.model=$(CONFIG)/vehicle/ship/ferry.yaml"} )
	print( vars(test) )
