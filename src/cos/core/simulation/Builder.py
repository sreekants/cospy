#!/usr/bin/python
# Filename: Builder.py
# Description: Helper class to build the simulation environment

from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context
from cos.core.kernel.BootLoader import BootLoader
from cos.core.utilities.ActiveRecord import ActiveRecord
from cos.core.utilities.ArgList import ArgList

class Builder(Service):
	def __init__(self, category:str, type:str, model:str, table:str, prototypes, namespace=None):
		""" Constructor
		Arguments
			category -- Category of the object
			type -- Type of the object
			model -- Model name
			table -- Table name
			prototypes -- Prototype definition for types of objects
			namespace -- Namespace of the category
		"""
		Service.__init__(self, category, type )
		self.builder	= type
		self.model		= model
		self.table		= table
		self.namespace	= namespace
		self.prototypes	= prototypes
		return

	def register(self, prototypes):
		""" Registers additional object types
		Arguments
			prototypes -- Prototype definition for types of objects
		"""
		self.prototypes.update( prototypes )
		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		Service.on_init(self, ctxt, module )

		args	= ArgList(module.get("args"))
		if args.IsFalse("Enabled"):
			return

		path	= ctxt.sim.config.resolve( module["database"] )
		self.build( ctxt, args, path, self.builder )
		return

	def build(self, ctxt:Context, args:ArgList, path:str, type:str):
		""" Builds an object
		Arguments
			ctxt -- Simulation context
			args -- List of arguments
			path -- Path of the database with the objects
			type -- Type of the object
		"""
		profile	= self.prototypes[type]
		db		= ActiveRecord.create(self.model, path, self.table)
		records	= db.get_all(f'type={profile[0]}')

		klassname, klass	= BootLoader.load_class( profile[1] )

		category	= Builder.capitalize(self.model)

		if self.namespace is None:
			nspath	= f'/World/{category}/{type}'
		else:
			nspath	= f'/World/{self.namespace}/{category}/{type}'

		for rec in records:
			guid, inst	= self.create( ctxt, klass, rec )

			ctxt.sim.objects.register( nspath, str(guid), inst )

		return


	def scale_polygon2D( self, ctxt:Context, path:str):
		""" Scakes a 2D polygon
		Arguments
			ctxt -- Simulation context
			path -- Polygon path definition
		"""
		if len(path) == 0:
			return ''
		
		points 	= list( tuple( float(num)
							 	for num in item.split(','))
								for item in path.split(' ') )

		mapped	= list( self.map2D_to_str(ctxt, pt) for pt in points )
		return ' '.join(mapped)

	def map2D_to_str( self, ctxt:Context, pt ):
		""" Maps a point to a string
		Arguments
			ctxt -- Simulation context
			pt -- Point to convert
		"""
		pt	= self.map2D(ctxt, pt)
		return f'{int(pt[0])},{int(pt[1])}'

	def map2D( self, ctxt:Context, pt ):
		""" Scales a point
		Arguments
			ctxt -- Simulation context
			pt -- Point to convert
		"""
		return ctxt.sim.world.scales.transpose(pt)

	@staticmethod
	def capitalize( s ):
		""" Capitalizes a text
		Arguments
			s -- Text to encode
		"""

		# Set the last char as a space to capitalize
		# the first character
		last	= ' '
		result	= ''

		for ch in s:
			if last.isupper():
				result	+= ch
				last	= ch
				continue

			if ch.isalpha() & (not last.isalnum()):
				result	+= ch.upper()
			else:
				result	+= ch.lower()

			last	= ch

		return result


if __name__ == "__main__":
	test = Builder()


