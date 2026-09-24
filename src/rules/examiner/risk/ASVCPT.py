#!/usr/bin/python
# Filename: ASVCPT.py
# Description: ASV conditional probability table

from cos.math.risk.ConditionalProbabilityTable import CPT
import numpy as np
import os, yaml


# Reads the ASV risk model from YAML configuration.
# 
# The whole model - its structure, its states and its conditional probabilities -
# lives in one file, which the caller names; config/risk/asv.model.yaml is the
# one the platform ships. This module is the only reader of that file, so the
# two halves cannot drift into disagreeing about what a node is called or how
# many states it has.
# 
# 	inference:
# 	  network:
# 	    nodes:    node -> kind, label, states
# 	    hazards:  the hazardous events, used as a joint inference target
# 	    edges:    [parent, child] pairs
# 	sources:      provenance keys
# 	nodes:        node -> source, parents, table
# 
# The two 'nodes' blocks describe the same nodes from two sides: the one under
# inference.network declares what a node IS, the top-level one declares what it
# is WORTH believing. read() checks that they name the same set.
# 
# Matrix orientation, enforced by cos.math.risk.ConditionalProbabilityTable:
# 
# 	rows    = parent configurations, itertools.product over the parents as
# 	          declared, FIRST parent varying SLOWEST
# 	columns = the node's states, in the order inference.network declares them
# 	every row sums to 1

# No default path. This module is a reader, and a reader that guesses where its
# input lives is guessing on behalf of a caller that knows better: inside a
# running simulation the path comes from ctxt.sim.config, which resolves
# $(CONFIG) and the territory variables that a constant here cannot see. Every
# entry point names its own file.

UNKNOWN_SOURCE = 'unattributed'


class Network:
	""" The structure half of the model: what the nodes are and how they connect.
	"""

	def __init__(self, nodes=None, edges=None, hazards=None):
		""" Constructor
		Arguments
			nodes -- node -> {kind, label, states}
			edges -- [parent, child] pairs
			hazards -- Names of the hazardous event nodes
		"""
		self.nodes		= dict( nodes or {} )
		self.edges		= [ tuple(e) for e in (edges or []) ]
		self.hazards	= tuple( hazards or () )
		return

	def kind(self, node)->str:
		return self.nodes[node]['kind']

	def label(self, node)->str:
		return self.nodes[node]['label']

	def states(self, node):
		return list( self.nodes[node]['states'] )

	def labels(self)->dict:
		""" node -> label, for the caption sidecar """
		return { node: body['label'] for node, body in self.nodes.items() }

	def by_kind(self)->dict:
		""" kind -> [node], for the report """
		grouped	= {}
		for node, body in self.nodes.items():
			grouped.setdefault( body['kind'], [] ).append( node )

		return grouped

	def errors(self):
		""" Checks the structure declares a usable graph
		Returns
			A list of problems, empty when the network is usable
		"""
		problems	= []

		if len( self.nodes ) == 0:
			problems.append( 'no nodes declared' )

		for node, body in self.nodes.items():
			if not isinstance( body, dict ):
				problems.append( f'{node}: entry is not a mapping' )
				continue
			for field in ('kind', 'label', 'states'):
				if body.get( field ) in (None, '', []):
					problems.append( f'{node}: no {field}' )
			states	= body.get( 'states' ) or []
			if len( set(states) ) != len( states ):
				problems.append( f'{node}: repeated state in {states}' )
			# A state that YAML read as a boolean is a quoting mistake in the
			# file: 'yes' unquoted loads as True and then matches no label.
			for state in states:
				if isinstance( state, bool ):
					problems.append( f'{node}: state {state!r} needs quoting in YAML' )

		for edge in self.edges:
			if len( edge ) != 2:
				problems.append( f'edge {edge} is not a [parent, child] pair' )
				continue
			for end in edge:
				if end not in self.nodes:
					problems.append( f'edge {edge} names undeclared node {end!r}' )

		for hazard in self.hazards:
			if hazard not in self.nodes:
				problems.append( f'hazard {hazard!r} is not a declared node' )

		return problems


def read(path)->tuple:
	""" Reads the whole model from configuration
	Arguments
		path -- Path to the model file. Required: see the note above on why this
			module holds no default.
	Returns
		(network, tables)
	Raises
		ValueError when no path is given or the file is malformed. Matrix shapes
		are checked later, by apply_all against the built network, which is the
		only place a node's true dimensions are known.
	"""
	if not path:
		raise ValueError( 'no model file given; ASVCPT holds no default path' )

	with open( path, encoding='utf-8' ) as handle:
		config	= yaml.safe_load( handle ) or {}

	network		= __network( config )
	tables		= __tables( config )

	problems	= network.errors()

	declared	= set( network.nodes )
	quantified	= { table.node for table in tables }

	for node in sorted( quantified - declared ):
		problems.append( f'{node}: has a table but is not declared in inference.network' )
	for node in sorted( declared - quantified ):
		problems.append( f'{node}: is declared in inference.network but has no table' )

	if problems:
		raise ValueError( f'{path}: ' + '; '.join(problems) )

	return network, tables


def load(path):
	""" The tables alone, for a caller that does not need the structure
	Arguments
		path -- Path to the model file
	"""
	return read( path )[1]


def __network(config)->Network:
	""" Builds the structure half
	Arguments
		config -- The parsed file
	"""
	block	= ((config.get('inference') or {}).get('network') or {})

	return Network( block.get('nodes'), block.get('edges'), block.get('hazards') )


def __tables(config):
	""" Builds the quantified half
	Arguments
		config -- The parsed file
	"""
	sources		= config.get( 'sources', {} ) or {}
	nodes		= config.get( 'nodes', {} ) or {}

	tables		= []
	problems	= []

	for node, entry in nodes.items():
		if not isinstance( entry, dict ):
			problems.append( f'{node}: table entry is not a mapping' )
			continue

		rows	= entry.get( 'table' )
		if not rows:
			problems.append( f'{node}: no table' )
			continue

		widths	= { len(row) for row in rows }
		if len( widths ) != 1:
			problems.append( f'{node}: rows have differing widths {sorted(widths)}' )
			continue

		key		= entry.get( 'source' )
		if (key is not None) and (key not in sources):
			problems.append( f'{node}: source {key!r} is not declared in sources' )
			continue

		tables.append( CPT(
			node,
			entry.get( 'parents' ) or [],
			np.array( rows, dtype=float ),
			sources.get( key, UNKNOWN_SOURCE ) ) )

	if problems:
		raise ValueError( '; '.join(problems) )

	return tables


if __name__ == "__main__":
	import sys

	if len( sys.argv ) != 2:
		print( f'usage: {os.path.basename(sys.argv[0])} <model.yaml>', file=sys.stderr )
		sys.exit( 2 )

	network, tables = read( sys.argv[1] )
	print( f'nodes {len(network.nodes)}  edges {len(network.edges)}  '
		   f'hazards {len(network.hazards)}  tables {len(tables)}' )
	for table in tables:
		print( f'  {table}' )
