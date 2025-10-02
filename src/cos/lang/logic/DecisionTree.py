#!/usr/bin/python
# Filename: DecisionTree.py
# Description: Base class for an decision tree and supporting classes

from cos.lang.logic.Decision import Decision, DecisionType
from cos.core.utilities.Tree import Tree, TreeNode
from cos.core.utilities.Errors import ErrorCode

class EvaluateCtxt:
	def __init__(self, ctxt):
		""" Constructor
		Arguments
			ctxt -- Context argument
			log -- Logger interface
		"""
		self.ctxt		= ctxt
		self.result		= []
		self.error		= []
		return

	def __str__(self) -> str:
		""" TODO: __str__
		""" 
		lines		= []
		for e in self.error:
			lines.append( str(e) )
		return '\n'.join(lines)

class DecisionTree(Tree):
	def __init__(self, root:TreeNode=None):
		""" Constructor
		Arguments
			root -- Root decision node
		"""
		if root is None:
			root = Decision(None, None, DecisionType.TYPE_ROOT_DECISION)
		Tree.__init__(self, root)
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		""" 
		# Traverse each node and apply a decision
		ectxt		= EvaluateCtxt(ctxt)
		result		= self.traverse( self.__evaluate_node, ectxt, 1 )
		return ectxt

	@staticmethod
	def evaluate_node(ctxt, node:Decision):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		""" 
		# Traverse each node and apply a decision
		ectxt		= EvaluateCtxt(ctxt)
		return DecisionTree.__evaluate_node( ectxt, node )

	@staticmethod
	def __evaluate_node( ctxt:EvaluateCtxt, node:Decision ):
		""" Pumps messages in a queue node
		Arguments
			ctxt -- Context argumen
			node -- Node to process
		"""
		result = node.apply(ctxt)
		if result in  [ErrorCode.ERROR_NO_MORE_ITEMS, ErrorCode.S_OK, ErrorCode.ERROR_CONTINUE]:
			return ErrorCode.ERROR_CONTINUE
		return result

if __name__ == "__main__":
	test = DecisionTree()


