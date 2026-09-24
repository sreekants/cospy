#!/usr/bin/python
# Filename: ScenarioGenerator.py
# Description: Implementation of the ScenarioGenerator class

from cos.cluster.runtime.TemplateReplicator import TemplateReplicator, Declarations

import sys, uuid, os, random, re, configparser, yaml

class ScenarioGenerator:
	def __init__(self, templatedir, command, scenarios):
		""" Constructor
		Arguments
			templatedir -- #TODO
			command -- #TODO
			scenarios -- Mapping of dimension -> list of values. A tuple key such as
				('COUNTRY','LOCATION') declares a paired dimension whose values are
				tuples, so only pairs that exist are swept (see sites())
		"""
		self.src		= templatedir
		self.command	= command
		self.scenarios	= scenarios
		return

	def generate(self, outdir, taskfile, count=-1, seed=None, country=None):
		""" Generates the  cluster task including profiles for all the scenarios
		Arguments
			outdir -- Output directory
			taskfile -- Output task file (for SCRUM)
			count -- Maximum number of scenarios to generate
			seed -- Seed used to shuffle the scenarios when count is specified
			country -- Optional country code (e.g. 'tk'), to generate only the
				scenarios in that country
		"""
		self.maxcount	= count

		# Generate all the possible permutations of scenarios
		dims	= list(self.scenarios.keys())
		cases	= []
		self.permutation( cases, dims )

		# Restrict to one country before sampling, so that count is drawn
		# from that country's scenarios alone
		cases	= self.select( cases, country )

		# Shuffle so that a limited count samples the whole space rather than
		# the first cases in recursion order (see COS.002)
		self.shuffle( cases, seed )
		if self.maxcount > 0:
			cases	= cases[:self.maxcount]

		# Refuse to generate anything if a case points at missing data
		self.validate( cases )

		# Generate the templates
		configs	= self.generate_templates( outdir, cases )

		# Generate the taskfile
		self.generate_tasks( taskfile, configs )

		return configs

	def generate_tasks(self, taskfile, configs ):
		""" Generates te task file
		Arguments
			taskfile -- Output task file (for SCRUM) 
			configs -- Configuration settings
		"""
		with open(taskfile, 'w+t') as f:
			n	= 1
			for configfile in configs:
				command		= self.command.replace( '$$COS_CONFIG$$', configfile )
				f.write( f'{n} {command}\n' )
				n	= n+1
		return

	def generate_templates(self, outdir, cases ):
		""" Generates test configuration for each test container
		Arguments
			outdir -- Output directory for the container profile
			cases -- List of test cases to generate template for
		"""
		configs	= []

		ncases	= 0

		# For each scenario, generate a runtime template
		for case in cases:
			decl	= self.declarations( case )

			if outdir[-1] != os.sep:
				outdir	= outdir+os.sep

			path	= f'{outdir}{str(case[0])}'
			rep 	= TemplateReplicator( decl, True )

			rep.replicate( self.src, f'{path}' )

			configs.append( path )

			ncases = ncases+1

			if ncases == self.maxcount:
				break

		return configs

	def declarations(self, case):
		""" Builds the template declarations for a test case
		Arguments
			case -- Test case, (id, [(dimension, value), ...])
		"""
		decl	= Declarations()
		for dim, value in case[1]:
			if isinstance( dim, tuple ):
				for d, v in zip( dim, value ):
					decl[d]	= v
			else:
				decl[dim]	= value
		return decl

	def select(self, cases, country=None):
		""" Selects the test cases of one country
		Arguments
			cases -- List of test cases
			country -- Country code to keep, or None to keep every case
		"""
		if country is None:
			return cases

		selected	= [ case for case in cases
						if self.declarations(case).replace_text('$$COUNTRY$$') == country ]
		if not selected:
			raise ValueError( f'ScenarioGenerator: no scenarios for country \'{country}\'' )
		return selected

	def validate(self, cases, keys=('SIMULATION','MAP')):
		""" Checks that the data of every test case exists: the data directories, and
		the weather databases the case's weather.yaml will load
		Arguments
			cases -- List of test cases to validate
			keys -- EnvironmentVariables in cos.ini that must name existing directories
		"""
		template	= os.path.join( self.src, 'cos.ini' )
		with open( template, 'rt' ) as f:
			text	= f.read()

		missing	= {}
		modules	= {}		# weather.yaml path -> its modules, parsed once
		for case in cases:
			inifile		= self.declarations(case).replace_text(text)
			settings	= ScenarioGenerator.settings( inifile )
			for key in keys:
				path	= settings.get( key )
				if (path is None) or (os.path.isdir(path) == False):
					missing.setdefault( f'{key}={path}', [] ).append( case[1] )

			for path in ScenarioGenerator.weather_databases( inifile, settings, modules ):
				if os.path.isfile(path) == False:
					missing.setdefault( f'WEATHER={path}', [] ).append( case[1] )

		if missing:
			lines	= [ f'  {k} ({len(v)} cases, e.g. {v[0]})' for k, v in missing.items() ]
			raise ValueError( 'ScenarioGenerator: scenario data does not exist:\n' + '\n'.join(lines) )
		return

	@staticmethod
	def weather_databases(text, settings, cache=None):
		""" Lists the weather databases a generated cos.ini will load
		Arguments
			text -- Contents of a generated cos.ini
			settings -- Its resolved variables, from settings()
			cache -- Optional mapping of weather.yaml path -> modules, to parse each file once
		Returns
			Resolved database paths of the enabled modules in [Environment] Weather, or the
			weather.yaml path itself if that file does not exist
		"""
		parser	= configparser.ConfigParser( inline_comment_prefixes=(';',) )
		parser.read_string( text )
		if parser.has_option('Environment', 'Weather') == False:
			return []

		config	= ScenarioGenerator.resolve( parser.get('Environment', 'Weather', raw=True), settings )
		if os.path.isfile(config) == False:
			return [config]

		if cache is None:
			cache	= {}
		if config not in cache:
			with open( config, 'rt' ) as f:
				data	= yaml.safe_load( f ) or {}
			cache[config]	= (data.get('packages') or {}).get('modules') or []

		paths	= []
		for module in cache[config]:
			if (module.get('enable', True) == False) or (module.get('database') is None):
				continue
			path	= ScenarioGenerator.resolve( module['database'], settings )
			if path not in paths:
				paths.append( path )
		return paths

	@staticmethod
	def resolve(value, values):
		""" Replaces $(NAME) references in a value
		Arguments
			value -- Text to resolve
			values -- Mapping of upper-case variable name -> value
		"""
		return re.sub( r'\$\(([A-Za-z_]+)\)',
			lambda m: values.get(m.group(1).upper(), m.group(0)), value )

	@staticmethod
	def settings(text):
		""" Resolves the Folders and EnvironmentVariables of a cos.ini text
		Arguments
			text -- Contents of a generated cos.ini
		Returns
			Mapping of upper-case variable name -> resolved value
		"""
		parser	= configparser.ConfigParser( inline_comment_prefixes=(';',) )
		parser.read_string( text )

		values	= { k: v for k, v in os.environ.items() }
		for section in ['Folders','EnvironmentVariables']:
			if parser.has_section(section) == False:
				continue
			for k, v in parser.items(section, raw=True):
				values[k.upper()]	= ScenarioGenerator.resolve( v, values )
		return values

	@staticmethod
	def sites(configdir):
		""" Lists the (country, location) pairs that have simulation data
		Arguments
			configdir -- Configuration root, containing simulation/<country>/<location>
		"""
		root	= os.path.join( configdir, 'simulation' )
		pairs	= []
		for country in sorted( os.listdir(root) ):
			if os.path.isdir( os.path.join(root, country) ) == False:
				continue
			for location in sorted( os.listdir(os.path.join(root, country)) ):
				if os.path.isdir( os.path.join(root, country, location) ):
					pairs.append( (country, location) )
		return pairs

	def shuffle(self, cases, seed=None):
		""" Shuffles the test cases in place if a maximum count is specified
		Arguments
			cases -- List of test cases to shuffle
			seed -- Seed for a reproducible shuffle
		"""
		if self.maxcount > 0:
			random.Random(seed).shuffle( cases )
		return cases

	def permutation(self, cases, dims, result=[]):
		""" Create a permutations of a test recursively
		Arguments
			cases -- Output list of test case
			dims -- Dimensions of the permutation
			result -- Accumulated result fo the next permutation
		"""
		if not dims:
			cases.append( (uuid.uuid1(), result) )
			return cases

		first	= dims[0]
		rest	= dims[1:]
		for case in self.scenarios[first]:
			next	= result.copy()
			next.append( (first,case) )
			self.permutation( cases, rest, next )
		return cases

if __name__ == "__main__":
	generator = ScenarioGenerator( 'E:\\users\\ntnu\\cospy\\templates\\cluster\\config',
		'python ${COS_DIR}/apps/coslaunch/main.py -config $$COS_CONFIG$$',
		{
		# Paired so that only (country, location) pairs with simulation data are swept
		("COUNTRY","LOCATION"):ScenarioGenerator.sites('E:\\users\\ntnu\\cospy\\config'),
		"WEATHER":["clearsky","cloudy","foggy","heavyrain","highsea","hurricane",
			 "lightrain","snow","wind"],
		"TRAFFIC":[
			 "hdta",			# High density
			 "mdta",			# Medium density
			 "ldta",			# Low density
			 "ctz",				# Controlled traffic zone
			 "rdta",			# Regional traffic ??
			 "vdta",			# ??
			 "seasonal"			# Seasonal traffic
			 ],
	})

	# Generating only 10 scenarios, in Turkey
	generator.generate('output','tasks.conf', 10, country='tk')
