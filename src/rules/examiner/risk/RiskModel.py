#!/usr/bin/python
# Filename: riskcore.py
# Description: Risk arithmetic for the Bayesian risk-assessment faculty
#
# Prototype. Intended home in cospy: src/risk/bayesian/riskcore.py
#
# Deliberately free of COS imports so the arithmetic can be unit-tested without
# a simulation. RiskAssessment.py supplies the plumbing; this file supplies the
# probability and cost handling, which is where the subtle mistakes live.

import pyagrum as gum

HAZARDS = ('collision', 'grounding', 'loss_of_comms')

# Sentinel for "no assessment yet". A plain None would collide with a genuine
# first observation of None, silently dropping the opening exposure.
UNASSESSED = object()


def make_engine(bn, hazards=HAZARDS):
	""" Builds an inference engine that can answer both the marginals and the
	joint over the hazardous events.
	Arguments
		bn -- Bayesian network
		hazards -- Names of the hazardous event nodes
	Note
		addAllTargets() must come first. Declaring a joint target switches
		pyAgrum to optimized inference, which otherwise discards every marginal
		that was not explicitly requested, and exposure() needs the consequence
		node marginals.
	"""
	engine	= gum.LazyPropagation( bn )
	engine.addAllTargets()
	engine.addJointTarget( set(hazards) )
	return engine


def load(path, hazards=HAZARDS):
	""" Loads a network from disk and returns it with a ready inference engine
	Arguments
		path -- Path to the network (.xdsl, .bif, .net, ...)
		hazards -- Names of the hazardous event nodes
	"""
	bn	= gum.loadBN( path )
	return bn, make_engine( bn, hazards )


def hazard_probabilities(engine, hazards=HAZARDS):
	""" Probability of each hazardous event, and of any of them occurring.

	'any' is the exact joint, 1 - P(none of them). It needs no independence
	assumption because the network already carries the dependence between the
	hazards through their shared ancestors.

	'sum' is eq. (14) of Kristensen et al. (2025), P_C + P_G + P_L. That is
	Boole's inequality - an upper bound which may exceed 1, and a non-uniform
	one, so it can order two situations differently from the exact joint. It is
	returned only so that the two can be compared in the recorded data.
	Arguments
		engine -- An engine built by make_engine(), already inferred
		hazards -- Names of the hazardous event nodes
	"""
	marginals		= { h: float(engine.posterior(h)[{h: 'yes'}]) for h in hazards }

	joint			= engine.jointPosterior( set(hazards) )
	none			= float( joint[{ h: 'no' for h in hazards }] )

	result			= dict( marginals )
	result['any']	= 1.0 - none
	result['sum']	= sum( marginals.values() )
	return result


# MATLAB matrix literal punctuation: [a, b; c, d];
CELL_SEPARATOR		= ', '
ROW_SEPARATOR		= '; '
STATEMENT_TERMINATOR	= ';'

# Every valuation in the platform is USD. Declared once, here, rather than
# stored per row: a currency column can only ever record a disagreement.
CURRENCY			= 'USD'


def number(value)->str:
	""" One matrix cell, written so MATLAB reads it and a person can too.
	Fixed notation rather than %g, because a loss of 5179400 should not be
	stored as 5.1794e+06 in a column someone will eyeball.
	Arguments
		value -- Cell value
	"""
	text	= f'{float(value):.4f}'.rstrip('0').rstrip('.')

	return text if text not in ('', '-0') else '0'


class LossMatrix:
	""" Rl, the zone-specific loss matrix of the risk formalism.

	Rl is the third facet of R_ev = Ro . Rw . Rl. The CS&Law paper leaves it to
	be averaged from historical infraction penalties; here it is computed from
	the risk network instead - the network supplies the probability of each
	consequence, the territory's risk file supplies what that consequence is
	worth, and the product is a cell:

	    Rl[zone][concern] = SUM over the concern's consequence nodes of
	                            SUM over states of P(state) * cost[node][state]
	                        * zone_factor[zone][concern]

	Nothing here is declared in code. A territory that prices a life
	differently, or that treats a spill in confined water as worse than one at
	sea, edits its own YAML and no Python changes.
	"""

	def __init__(self, config=None):
		""" Constructor
		Arguments
			config -- The 'risk' block of a territory's risk file
		"""
		config				= config or {}

		# No currency field. Every valuation in the platform is USD, so a
		# per-territory currency would only invite two territories to disagree
		# about what a stored number means.
		self.concerns		= list( config.get('concerns', []) )
		self.consequences	= dict( config.get('consequences', {}) or {} )
		self.cost			= dict( config.get('cost', {}) or {} )
		self.factors		= dict( config.get('zone_factor', {}) or {} )
		return

	def errors(self, bn=None):
		""" Checks the matrix against its own declarations and, when given, the
		network it will be evaluated over
		Arguments
			bn -- Bayesian network, optional
		Returns
			A list of problems, empty when the matrix is usable
		"""
		problems	= []

		if not self.concerns:
			problems.append( 'no concern vector declared' )

		unknown		= sorted( set(self.consequences.values()) - set(self.concerns) )
		if unknown:
			problems.append( f'consequences map to undeclared concerns: {unknown}' )

		unpriced	= sorted( set(self.consequences) - set(self.cost) )
		if unpriced:
			problems.append( f'consequence nodes with no cost: {unpriced}' )

		unmapped	= sorted( set(self.cost) - set(self.consequences) )
		if unmapped:
			problems.append( f'costed nodes with no concern: {unmapped}' )

		for zone, row in self.factors.items():
			missing	= sorted( set(self.concerns) - set(row or {}) )
			if missing:
				problems.append( f'zone_factor[{zone}] is missing {missing}' )

		if bn is not None:
			names	= set( bn.names() )
			absent	= sorted( set(self.cost) - names )
			if absent:
				problems.append( f'costed nodes absent from the network: {absent}' )
			for node, states in self.cost.items():
				if node not in names:
					continue
				variable	= bn.variable( node )
				legal		= { variable.label(i) for i in range(variable.domainSize()) }
				bad			= sorted( set(states) - legal )
				if bad:
					problems.append( f'cost[{node}] names unknown states {bad}' )

		return problems

	def base(self, engine):
		""" Expected loss per concern before any zone factor is applied.

		Summing expectations is valid whatever the dependence between
		consequences - E[X+Y] = E[X] + E[Y] unconditionally - and is right
		physically: one collision may damage both vessels and harm a person,
		and those costs accumulate.
		Arguments
			engine -- An engine built by make_engine(), already inferred
		"""
		result	= { concern: 0.0 for concern in self.concerns }

		for node, costs in self.cost.items():
			posterior	= engine.posterior( node )
			expected	= sum( float(posterior[{node: s}]) * c for s, c in costs.items() )
			concern		= self.consequences.get( node, 'unclassified' )
			result[concern]	= result.get( concern, 0.0 ) + expected

		return result

	def row(self, engine, zone):
		""" One row of Rl: the expected loss per concern in a given zone
		Arguments
			engine -- An engine built by make_engine(), already inferred
			zone -- Spatial zone the vessel is in
		Note
			An unknown zone takes a factor of 1.0 rather than zero. Silently
			valuing every consequence at nothing would look like a safe vessel.
		"""
		factors	= self.factors.get( zone, {} ) or {}

		return { concern: value * float( factors.get(concern, 1.0) )
				 for concern, value in self.base(engine).items() }

	def matrix(self, engine):
		""" The whole of Rl for the current inference: zone -> concern -> loss.
		Used for reporting a complete matrix rather than the single row the
		vessel currently occupies.
		Arguments
			engine -- An engine built by make_engine(), already inferred
		"""
		base	= self.base( engine )

		return { zone: { concern: base.get(concern, 0.0) * float(row.get(concern, 1.0))
						 for concern in self.concerns }
				 for zone, row in self.factors.items() }

	def matlab(self, engine, zones):
		""" The whole of Rl as a MATLAB matrix literal.

		    [1.5, 2.7, 3.9; 4.1, 5.2, 6.3];

		One row per spatial zone in the order given, one column per concern in
		the order declared by the territory. Storing the matrix as a single
		string keeps the fact schema fixed: a territory that adds a concern or
		a zone changes the shape of this literal and nothing else, with no
		column to add and no warehouse schema to regenerate.

		The cost of that is a matrix whose axes are not in the row. Anything
		reading these strings must know the zone and concern order that
		produced them, which is why axis_labels() is logged at startup and why
		the order must not be edited mid-sweep.
		Arguments
			engine -- An engine built by make_engine(), already inferred
			zones -- Spatial zone names, in row order
		"""
		cells	= self.matrix( engine )

		rows	= [ ROW_SEPARATOR.join(
					CELL_SEPARATOR.join( number(cells.get(zone, {}).get(concern, 0.0))
										 for concern in self.concerns )
					for zone in zones ) ]

		return f'[{"".join(rows)}]{STATEMENT_TERMINATOR}'

	def axis_labels(self, zones):
		""" The axis order a stored matrix was written with, for the log and
		for anything decoding it later
		Arguments
			zones -- Spatial zone names, in row order
		"""
		return f'rows[{", ".join(zones)}] cols[{", ".join(self.concerns)}]'


class Binding(dict):
	""" One evidence binding: a simulation term, the BN node it feeds, and the
	discretization that turns an observation into a node state.
	"""

	def discretize(self, value):
		""" Maps an observed value onto a state of the bound node
		Arguments
			value -- Observed value
		Returns
			A state label, or None when the value cannot be discretized
		"""
		method	= self.get("discretize", "state")

		if method == "state":
			return str(value)

		if method == "threshold":
			above, below	= self["states"]
			return above if float(value) > float(self["at"]) else below

		if method == "bins":
			edges	= self.get("edges")
			if edges is not None:
				index	= 0
				while (index < len(edges)) and (float(value) >= float(edges[index])):
					index	+= 1
				return f'state_{index + 1}'

			index	= int( float(value) // float(self["width"]) )
			index	= min( max(index, 0), int(self["count"]) - 1 )
			return f'state_{index + 1}'

		return None


class VoyageTrack:
	""" Accumulated risk cost for one vessel over one voyage.

	Two corrections to a naive running sum:

	  1. Survival weighting. A hazardous event earlier in the voyage would have
	     ended the mission, so an exposure later on is only incurred if the
	     vessel got there. Eq. (15) of the source paper omits this, which the
	     authors note makes it an over-estimate.
	  2. One charge per distinct risk picture. The faculty samples on a timer,
	     so an unchanged situation would otherwise be charged once per tick - a
	     ten-minute encounter at 1 Hz would be counted six hundred times.
	"""

	def __init__(self):
		""" Constructor
		"""
		self.survival	= 1.0
		self.cost		= 0.0
		self.evidence	= UNASSESSED
		self.charges	= 0
		return

	def charge(self, cost, p_any, evidence):
		""" Charges one exposure against the voyage, if the risk picture changed
		Arguments
			cost -- Instantaneous expected economic loss
			p_any -- Probability that any hazardous event occurs
			evidence -- Evidence that produced this assessment
		Returns
			The amount added to the voyage total, zero when nothing changed
		"""
		if evidence == self.evidence:
			return 0.0

		increment		= self.survival * cost
		self.cost		+= increment
		self.survival	*= (1.0 - p_any)
		self.evidence	= evidence
		self.charges	+= 1
		return increment
