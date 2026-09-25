#!/usr/bin/python
# Filename: ZoneRules.py
# Description: Config-driven zone rules and seabed lookup shared by the examiners

# Zone-local regulation - a speed limit in a strait, an overtaking ban in a
# narrow reach, a cargo class barred from internal waters - is data, not code.
# It lives in config/examiner/zones.yaml so a scenario designer can retune a
# jurisdiction without touching an examiner, exactly as score.json retunes a
# Legata rule's penalties.
#
# Rules resolve in three layers, most specific winning:
#   1. the 'settings' of the map shape the vessel is inside, so a single zone
#      in a scenario's map can override everything below it;
#   2. the named zone entry in zones.yaml;
#   3. the zone's Sea.Type entry, then 'default'.

import yaml

from cos.model.geography.Sea import Type as SeaType
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList


class ZoneRules:
	""" Zone-local rules, the seabed under a vessel, and the penalty scorecard.
	"""

	def __init__(self):
		""" Constructor
		"""
		self.zones		= {}		# Zone name -> rules
		self.types		= {}		# Sea.Type name -> rules
		self.defaults	= {}
		self.penalties	= {}		# Event -> penalty score
		self.concerns	= {}		# Event -> cross-cutting concern
		self.vocabulary	= []		# Concerns an event may map to - the j axis
		self.sections	= {}		# Examiner-specific blocks, e.g. 'collision'
		return

	def load(self, ctxt:Context, path:str):
		""" Loads the zone rules
		Arguments
			ctxt -- Simulation context
			path -- Path to the zone rules file
		"""
		if path is None:
			return

		resolved	= ctxt.sim.config.resolve( path )
		config		= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(resolved) )
		rules		= config.get( 'zones', {} ) if config else {}

		self.defaults	= rules.get( 'default', {} ) or {}
		self.types		= rules.get( 'types', {} ) or {}
		self.zones		= rules.get( 'named', {} ) or {}
		self.penalties	= (config.get('penalties', {}) if config else {}) or {}

		concerns		= (config.get('concerns', {}) if config else {}) or {}
		self.vocabulary	= list( concerns.get('vocabulary', []) or [] )
		self.concerns	= concerns.get( 'events', {} ) or {}

		# Everything else in the file is an examiner-specific block, reached
		# through section(). Keeping them here means one file and one load.
		self.sections	= { k: v for k, v in (config or {}).items()
							if k not in ('zones', 'penalties', 'concerns') }
		return

	def errors(self):
		""" Checks the scorecard and the concern mapping agree
		Returns
			A list of problems, empty when every priced event maps to a concern
		"""
		problems	= []

		if not self.vocabulary:
			problems.append( 'concerns.vocabulary is empty' )

		for event in self.penalties:
			concern	= self.concern( event )
			if concern is None:
				problems.append( f'event {event!r} is priced but maps to no concern' )
			elif concern not in self.vocabulary:
				problems.append( f'event {event!r} maps to {concern!r}, which is not in the vocabulary' )

		for event, concern in self.concerns.items():
			if concern not in self.vocabulary:
				problems.append( f'event {event!r} maps to {concern!r}, which is not in the vocabulary' )

		return problems

	@staticmethod
	def lookup(table:dict, event:str):
		""" Most specific entry for an event: 'COLREG.Rule14.a', then 'COLREG.Rule14', then 'COLREG'
		Arguments
			table -- Event -> value
			event -- Event identifier
		Returns
			The value, or None when nothing on the path is listed
		"""
		if event is None:
			return None

		if event in table:
			return table[event]

		name	= str(event).split('/')[0]
		while name:
			if name in table:
				return table[name]
			if '.' not in name:
				break
			name	= name.rsplit('.', 1)[0]

		return None

	def concern(self, event:str):
		""" The cross-cutting concern a violation scores into
		Arguments
			event -- Violation identifier
		Returns
			A concern from the vocabulary, or None when the event is unmapped
		"""
		return self.lookup( self.concerns, event )

	def priced(self, event:str)->bool:
		""" Whether the scorecard prices an event
		Arguments
			event -- Violation identifier
		"""
		return self.lookup( self.penalties, event ) is not None

	def section(self, name:str)->dict:
		""" An examiner-specific configuration block
		Arguments
			name -- Block name, e.g. 'collision', 'signal', 'weather'
		"""
		return self.sections.get( name, {} ) or {}

	@staticmethod
	def enclosing(shapes, position):
		""" Map shapes containing a position.

		The caller supplies the shapes, collected once with
		objmgr.get_all('/World/Sea') as COLREG.Evaluator does, rather than this
		module guessing at an attribute on the world.
		Arguments
			shapes -- Map shapes to test
			position -- (x, y) position
		"""
		found	= []
		if position is None:
			return found

		for shape in (shapes or []):
			try:
				if shape.contains( position ):
					found.append( shape )
			except Exception:
				continue		# A shape with no usable polygon simply does not match

		return found

	def seabed_depth(self, shapes):
		""" Shallowest nominal depth among the shapes a vessel is inside.
		Shallowest rather than mean: a vessel grounds on the shallowest thing
		beneath it, not on the average.
		Arguments
			shapes -- Map shapes enclosing the vessel
		Returns
			Depth in metres, or None when no shape reports one
		"""
		depths	= [ s.nominal_depth for s in shapes
					if getattr(s, 'nominal_depth', None) is not None ]

		return min( depths ) if depths else None

	def rules_at(self, shapes):
		""" Merged rules for the shapes a vessel is inside
		Arguments
			shapes -- Map shapes enclosing the vessel
		"""
		merged	= dict( self.defaults )

		for shape in shapes:
			name	= getattr( shape, 'type', None )
			if name is not None:
				merged.update( self.types.get( self.type_name(name), {} ) or {} )

		for shape in shapes:
			merged.update( self.zones.get( getattr(shape, 'name', None), {} ) or {} )

		# The map itself has the last word, so a scenario can override a zone.
		for shape in shapes:
			merged.update( self.overrides( shape ) )

		return merged

	def overrides(self, shape):
		""" Rule overrides carried in a map shape's own settings
		Arguments
			shape -- Map shape
		"""
		config	= getattr( shape, 'config', None )
		if config is None:
			return {}

		args		= ArgList( config.get('settings', None) )
		overrides	= {}

		for key in ('speed_limit', 'overtaking', 'berthing_margin',
					'grounding_margin', 'restricted_cargo'):
			value	= args[key]
			if value is not None:
				overrides[key]	= value

		return overrides

	def penalty(self, event:str, fallback=0.0)->float:
		""" Penalty score for a violation
		Arguments
			event -- Violation identifier
			fallback -- Score to use when the event is not in the scorecard
		"""
		value	= self.lookup( self.penalties, event )
		if value is None:
			return float( fallback )

		try:
			return float( value )
		except (TypeError, ValueError):
			return float( fallback )

	@staticmethod
	def type_name(type)->str:
		""" Readable name for a Sea.Type value
		Arguments
			type -- Sea.Type flag, or anything with a name
		"""
		if isinstance( type, SeaType ):
			return type.name

		return getattr( type, 'name', str(type) )

	@staticmethod
	def applies_in(rules, key, shapes)->bool:
		""" Checks whether any enclosing shape's type is listed under a rule key.
		Used to keep Berthing (inland) and Grounding (sea) apart in config
		rather than in code.
		Arguments
			rules -- Merged rules
			key -- Rule key holding a list of Sea.Type names
			shapes -- Map shapes enclosing the vessel
		"""
		listed	= rules.get( key )
		if not listed:
			return False

		names	= { ZoneRules.type_name(getattr(s, 'type', None)) for s in shapes }
		return len( names.intersection(listed) ) > 0


class SpatialZones:
	""" The i axis of the risk formalism: which of a territory's spatial zones
	a vessel is in.

	Four zones in the published formalism - high seas, territorial waters,
	internal waters, port - but the membership of each is a matter of national
	jurisdiction, so the Sea.Type mapping is supplied per territory rather
	than fixed here.
	"""

	def __init__(self, config=None):
		""" Constructor
		Arguments
			config -- The 'spatial_zones' block of a territory's risk file
		"""
		config			= config or {}

		self.order		= list( config.get('order', []) )
		self.fallback	= config.get( 'default' )
		self.mapping	= {}

		for zone, types in (config.get('mapping', {}) or {}).items():
			for name in (types or []):
				self.mapping[name]	= zone

		return

	def classify(self, shapes)->str:
		""" The spatial zone a vessel is in
		Arguments
			shapes -- Map shapes enclosing the vessel
		Returns
			A zone name, or the configured default when nothing jurisdictional
			encloses the vessel
		Note
			A vessel usually sits inside several overlapping shapes at once - a
			traffic lane inside a strait inside a territorial sea - so the
			INNERMOST match in the declared order wins. Types absent from the
			mapping are ignored rather than defaulted, because a traffic lane
			describes the water and not the jurisdiction over it.
		"""
		best	= None

		for shape in (shapes or []):
			zone	= self.mapping.get( ZoneRules.type_name(getattr(shape, 'type', None)) )
			if zone is None:
				continue

			if (best is None) or (self.rank(zone) > self.rank(best)):
				best	= zone

		return best if best is not None else self.fallback

	def rank(self, zone)->int:
		""" How far inshore a zone is; higher is more confined
		Arguments
			zone -- Zone name
		"""
		try:
			return self.order.index( zone )
		except ValueError:
			return -1

	def errors(self):
		""" Checks the declaration is usable
		Returns
			A list of problems, empty when the declaration is sound
		"""
		problems	= []

		if not self.order:
			problems.append( 'spatial_zones.order is empty' )

		unordered	= sorted( set(self.mapping.values()) - set(self.order) )
		if unordered:
			problems.append( f'zones mapped but absent from order: {unordered}' )

		if (self.fallback is not None) and (self.fallback not in self.order):
			problems.append( f'default zone {self.fallback!r} is not in order' )

		return problems


if __name__ == "__main__":
	test = ZoneRules()
