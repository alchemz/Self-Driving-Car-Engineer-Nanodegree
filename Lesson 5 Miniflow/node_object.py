Class Node(object):
	def __init__(self, inbound_nodes[]):
		# node(s) from which this node receives values
		self.inbound_nodes = inbound_nodes
		# node(s) to which this node passes values
		self.outbound_nodes = []
		# foor each inbound node here, add this node as an outbound node to _that_ node
		for n in self.inbound_nodes:
			n.outbound_nodes.append(self)
		self.value = None

	def forward(self):
		"""
		"""

		raise NotImplemented
		