#!/usr/bin/python
# Filename: ScenarioGenerator.py
# Description: Implementation of the ScenarioGenerator class

from cos.cluster.runtime.TemplateReplicator import TemplateReplicator, Declarations

import sys, uuid, os

class ScenarioGenerator:
	def __init__(self, templatedir, command, scenarios):
		""" Constructor
		Arguments
			templatedir -- #TODO
			command -- #TODO
			scenarios -- #TODO
		"""
		self.src		= templatedir
		self.command	= command
		self.scenarios	= scenarios
		return

	def generate(self, outdir, taskfile, count=-1):
		""" Generates the  cluster task including profiles for all the scenarios
		Arguments
			outdir -- Output directory
			taskfile -- Output task file (for SCRUM) 
			count -- Maximum number of scenarios to generate
		"""
		self.maxcount	= count

		# Generate all the possible permutations of scenarios
		dims	= list(self.scenarios.keys())
		cases	= []
		self.permutation( cases, dims )

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
			decl	= Declarations()
			for arg in case[1]:
				decl[arg[0]]	= arg[1]

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
	generator = ScenarioGenerator( 'E:\\users\\ntnu\\modcolreg\\cluster\\config',
		'python ${COS_DIR}/apps/coslaunch/main.py -config $$COS_CONFIG$$',
		{
		"LOCATION":["alesund","trondheim","molde","liekanger"],
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
		"SITUATION":["crossing","headon","overtaking","giveway","standon",
			   "restricted.visibility","narrow.channels","anchored"],
		"ZONE":["tss","narrow.channels","deep.water","roundabouts","inshore",
		  	"precautionary","restricted.visibility","anchor.areas",
			"restricted.speed","clearance"],

		"JURISDICTION":["territorial","contiguous","exclusive.economic","high.sea",
				  "international","archipelagic"]
	})

	# Generating only 10 scenarios, default generates 120k+ scenarios
	generator.generate('output','tasks.conf', 10)

