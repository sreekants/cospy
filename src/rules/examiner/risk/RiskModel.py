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


def exposure(engine, loss, concerns):
	""" Expected economic loss per cross-cutting concern.

	Summing expectations is valid whatever the dependence between consequences -
	E[X+Y] = E[X] + E[Y] unconditionally - and is right physically: one collision
	may damage both vessels and harm a person, and those costs accumulate.
	Arguments
		engine -- An engine built by make_engine(), already inferred
		loss -- Consequence node -> {state: economic loss}
		concerns -- Consequence node -> cross-cutting concern
	"""
	result	= {}

	for node, costs in loss.items():
		posterior	= engine.posterior( node )
		expected	= sum( float(posterior[{node: s}]) * c for s, c in costs.items() )
		concern		= concerns.get( node, 'unclassified' )
		result[concern]	= result.get( concern, 0.0 ) + expected

	return result


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
