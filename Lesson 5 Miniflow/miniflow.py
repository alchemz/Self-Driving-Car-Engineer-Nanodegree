class Node(object):
	def __init__(self, inbound_nodes=[]):
		self.inbound_nodes = inbound_nodes
		self.outbound_nodes = []
		self.value = None
		for n in self.inbound_nodes:
			n.outbound_nodes.append(self)

	def forward(self):
		raise NotImplemented


class Input(Node):
	def __init__(self):
		Node.__init__(self)

	def forward(self, value = None):
		if value is not None:
			self.value = value


class Add(Node):
	def __init__(self, *input):
		Node.__init__(self, input)

	def forward(self):
		self.value = 0
		for n in self.inbound_nodes:
			self.value = self.value + n.value
		return(self.value)

def topological_sort(feed_dict):
	"""
	Sort the nodes in topological order using Kahn's Algorithm

	Argument: 'feed_dict'

	returns a list of sorted nodes
	"""
	input_nodes = [n for n in feed_dict.keys()]

	G = {}
	nodes = [n for n in input_nodes]
	while len(nodes) > 0
		n = nodes.pop(0)
		if n not in G:
			G[n] = {'in': set(), 'out': set()}
		for m in n.outbound_nodes:
			if m not in G:
				G[m] = {'in': set(), 'out': set()}
			G[n]['out'].add(m)
			G[m]['in'].add(n)
			nodes.append(m)

	L = []
	S = set(input_nodes)
	while len(S) > 0
		n = S.pop()

		if isinstance(n, input):
			n.value = feed dict[n]

		L.append(n)
		for m in n.outbound_nodes:
			G[n]['out'].remove(m)
			G[m]['in'].remove(n)
			# if no other incoming deges add to S
			if len(G[m]['in']) == 0:
				S.add(m)
	return L

def forward_pass(output_node, sorted_nodes):
	"""
	Perform a forward pass through a list of sorted nodes
	"""
	for n in sorted_nodes:
		n.forward()
	return output_node.value