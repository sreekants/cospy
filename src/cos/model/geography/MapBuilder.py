#!/usr/bin/python
# Filename: MapBuilder.py
# Description: Implementation of the MapBuilder class

from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context
from cos.core.kernel.BootLoader import BootLoader
from cos.core.utilities.ActiveRecord import ActiveRecord
from cos.core.utilities.ArgList import ArgList

from pathlib import Path

class MapBuilder(Service):
	def __init__(self):

		Service.__init__(self, "Builder/Land", "Map" )

		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		Service.on_init(self, ctxt, module )

		self.args	= ArgList(self.resolve_args(ctxt, module))
		if self.args.IsFalse("Enabled"):
			return

		path	= ctxt.sim.config.resolve( module["database"] )
		self.build( ctxt, self.args, path )
		return

	def resolve_args(self, ctxt:Context, module):
		args 	= module.get("args")
		return ctxt.sim.config.resolve_argv(args) if args else None

	def build(self, ctxt:Context, args:ArgList, path:str):
		""" Builds an object
		Arguments
			ctxt -- Simulation context
			path -- Path of the database with the configurations
		"""

		background	= {
			'data'		: None,
			'format'	: None,
			'size'		: None,
			'scale'		: None,
			'data'		: None
			}

		db		= ActiveRecord.create('Config', path, 'configs')
		records	= db.get_all(f'type=\'display.configuration\'')


		# Initialize the configurations
		scale		= [1.0, 1.0]
		file		= None
		filepath	= None

		for r in records:
			match r[1]:
				case 'map.background.scale.x':
					scale[0]	= float(r[3])

				case 'map.background.scale.y':
					scale[1]	= float(r[3])
		
				case 'map.background.image':
					filepath	= r[3]
					file		= ctxt.sim.config.resolve(filepath)


		
		background['format']	= None
		background['size']		= None
		background['scale']		= (scale[0], scale[1])
		background['file']		= filepath

		if filepath:
			background['data']		= ctxt.sim.fs.read_file_as_bytes(file)
			background['format']	= Path(filepath).suffix.lower()

		world		= ctxt.sim.objects.get('/Services/Kernel/World')
		world.environ.set_background(background)

		return background

	def generate_map(self):
		return background


if __name__ == "__main__":
	test = MapBuilder()

