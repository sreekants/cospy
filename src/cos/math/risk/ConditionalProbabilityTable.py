#!/usr/bin/python
# Filename: ConditionalProbabilityTable.py
# Description: Conditional probability tables as numpy matrices


# A CPT is held as a 2-D numpy array in one fixed, human-readable orientation:
#
# Note: 
#     rows    = parent configurations, in itertools.product order over the
#               parents as DECLARED here, first parent varying slowest
#     columns = states of the node itself, in declaration order
#     every row sums to 1
#
# This is the orientation CPTs are printed in, which makes an elicited table
# copy straight in, and it is the orientation a table LEARNED from simulation
# counts comes out in - normalise a (parent configuration x state) count matrix
# along axis 1 and it is ready to apply.
#
# pyAgrum stores the same numbers differently. cpt(x).names is (x, *parents)
# with parents in ARC-INSERTION order, but the array is laid out along the
# REVERSED axes: cpt(x).toarray().shape == tuple(reversed(dims of names)), so
# the node is the LAST axis and the parents run backwards. Beware of checking
# this on a palindromic shape such as (3, 2, 3) - it cannot tell the two
# conventions apart. apply() and read() do the conversion, including the parent
# permutation, so the declared parent order here is independent of the order
# arcs were added, and asv_risk_model.py round-trips every table to prove it.

import itertools

import numpy as np

TOLERANCE = 1e-9


class CPT:
	""" One conditional probability table, as a numpy matrix.
	"""

	def __init__(self, node, parents, table, source='PLACEHOLDER'):
		""" Constructor
		Arguments
			node -- Name of the node the table belongs to
			parents -- Parent names, in the order the rows are indexed by
			table -- (parent configurations x states) array, or a 1-D vector
				for a root node
			source -- Where the numbers come from, carried into the audit output
		"""
		self.node		= node
		self.parents	= list( parents )
		self.source		= source

		table			= np.asarray( table, dtype=float )
		self.table		= table.reshape( 1, -1 ) if table.ndim == 1 else table
		return

	@property
	def shape(self):
		return self.table.shape

	def errors(self, bn):
		""" Checks the table against the network
		Arguments
			bn -- Bayesian network
		Returns
			A list of human-readable problems, empty when the table is usable
		"""
		problems	= []

		if self.node not in bn.names():
			return [ f'{self.node}: not a node in the network' ]

		declared	= set( self.parents )
		actual		= { bn.variable(i).name() for i in bn.parents(self.node) }
		if declared != actual:
			problems.append(
				f'{self.node}: declared parents {sorted(declared)} '
				f'!= network parents {sorted(actual)}' )
			return problems

		rows	= int( np.prod([ bn.variable(p).domainSize() for p in self.parents ]) ) if self.parents else 1
		cols	= bn.variable( self.node ).domainSize()

		if self.table.shape != (rows, cols):
			problems.append( f'{self.node}: table is {self.table.shape}, expected {(rows, cols)}' )
			return problems

		if (self.table < -TOLERANCE).any():
			problems.append( f'{self.node}: negative probabilities' )

		sums	= self.table.sum( axis=1 )
		bad		= np.flatnonzero( np.abs(sums - 1.0) > 1e-6 )
		if bad.size:
			problems.append(
				f'{self.node}: {bad.size} row(s) do not sum to 1, '
				f'first is row {int(bad[0])} summing to {sums[bad[0]]:.6f}' )

		return problems

	def apply(self, bn):
		""" Writes the table into the network
		Arguments
			bn -- Bayesian network
		"""
		problems	= self.errors( bn )
		if problems:
			raise ValueError( '; '.join(problems) )

		cols		= bn.variable( self.node ).domainSize()

		if not self.parents:
			bn.cpt( self.node ).fillWith( self.table.reshape(cols).tolist() )
			return

		dims		= [ bn.variable(p).domainSize() for p in self.parents ]
		rank		= len( self.parents )

		# (rows x states) -> (declared parents..., state)
		array		= self.table.reshape( *dims, cols )

		# -> pyAgrum's storage order: (last parent, ..., first parent, node)
		reverse		= list( reversed( list(bn.cpt(self.node).names)[1:] ) )
		array		= np.transpose( array, [ self.parents.index(p) for p in reverse ] + [rank] )

		bn.cpt( self.node ).fillWith( array.ravel().tolist() )
		return

	def rows(self, bn):
		""" Labels for each row, for printing and for auditing an elicited table
		Arguments
			bn -- Bayesian network
		"""
		if not self.parents:
			return [ '(prior)' ]

		states	= [ [ bn.variable(p).label(i) for i in range(bn.variable(p).domainSize()) ]
					for p in self.parents ]
		return [ ', '.join(combo) for combo in itertools.product(*states) ]

	def __repr__(self):
		given	= f' | {", ".join(self.parents)}' if self.parents else ''
		return f'CPT({self.node}{given}) {self.shape[0]}x{self.shape[1]} [{self.source}]'


def read(bn, node, parents=None):
	""" Reads a table back out of a network, in this module's orientation.
	The inverse of CPT.apply(), so a network loaded from .xdsl can be edited as
	a matrix and written back.
	Arguments
		bn -- Bayesian network
		node -- Node name
		parents -- Parent order for the rows; defaults to the network's own
	"""
	order		= list( bn.cpt(node).names )[1:]
	parents		= list( parents ) if parents is not None else order

	array		= bn.cpt( node ).toarray()			# (last parent, ..., first parent, node)

	if not parents:
		return CPT( node, [], array.reshape(1, -1), source='read' )

	reverse		= list( reversed(order) )
	rank		= len( parents )

	# -> (declared parents..., state)
	array		= np.transpose( array, [ reverse.index(p) for p in parents ] + [rank] )

	cols		= array.shape[-1]
	return CPT( node, parents, array.reshape(-1, cols), source='read' )


# --- builders ---------------------------------------------------------------

def uniform(rows, cols):
	""" A flat table. The paper uses this for the dynamic input nodes, because
	their evidence is always supplied during operation, so the prior never shows.
	Arguments
		rows -- Number of parent configurations
		cols -- Number of states
	"""
	return np.full( (rows, cols), 1.0 / cols )


def binary(p_yes):
	""" A two-column table from the probability of the first state.
	Arguments
		p_yes -- Scalar, or an array of one probability per parent configuration
	"""
	p	= np.atleast_1d( np.asarray(p_yes, dtype=float) )
	return np.column_stack( [p, 1.0 - p] )


def normalize(counts):
	""" Turns a (parent configuration x state) count matrix into a CPT.
	This is the path a table LEARNED from simulation counts takes.
	Arguments
		counts -- Non-negative count matrix
	"""
	counts	= np.asarray( counts, dtype=float )
	totals	= counts.sum( axis=1, keepdims=True )
	return np.divide( counts, totals, out=np.full_like(counts, 1.0 / counts.shape[1]),
					where=totals > 0 )


def apply_all(bn, cpts):
	""" Applies a collection of tables, reporting every problem rather than
	stopping at the first.
	Arguments
		bn -- Bayesian network
		cpts -- Iterable of CPT
	Returns
		A list of problems, empty when every table applied
	"""
	problems	= []

	for cpt in cpts:
		found	= cpt.errors( bn )
		if found:
			problems.extend( found )
			continue
		cpt.apply( bn )

	missing	= set( bn.names() ) - { c.node for c in cpts }
	if missing:
		problems.append( f'no table supplied for {sorted(missing)}' )

	return problems
