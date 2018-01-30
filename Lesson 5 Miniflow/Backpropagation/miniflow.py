import numpy as np

class Node(object):
	def __init__(self, inbound_nodes=[]):
		self.inbound_nodes = inbound_nodes
		self.value = None
		self.outbound_nodes = []
		self.gradients = []
		for node in inbound_nodes:
			node.outbound_nodes.append(self)

	def forward(self):
		raise NotImplementedError

	def backward(self):
		raise NotImplementedError

class Input(Node):
	def __init__(self):
		Node.__init__(self)

	def forward(self):
		pass
	def backward(self):
		self.gradients = {self: 0}
		for n in self.outbound_nodes:
			grad_cost = n.gradients[self]
			self.gradients[self] += grad_cost * 1

class Linear(Node):

	def __init__(self, X, W, b):
		Node.__init__(self, [X, W, b])

	def forward(self):
		X = self.inbound_nodes[0].value
		W = self.inbound_nodes[1].value
		b = self.inbound_nodes[2].value
		self.value = np.dot(X, W) + b
	def backward(self):
		self.gradients - {n: np.zeros_like(n.value) for n in self.inbound_nodes}

		for n in self.outbound_nodes:
			grad_cost = n.gradients[self]
			self.gradients[self.inbound_nodes[0]] += np.dot(grad_cost, self.inbound_nodes[1].value.T)
			self.gradients[self.inbound_nodes[1]] += np.dot(self.inbound_nodes[1].value.T, grad_cost)
			self.gradients[self.inbound_nodes[2]] += np.sum(grad_cost, axis =0, keepdims = False)

class Sigmoid(Node):
	def __init__(self, node):
		Node.__init__(self, [node])
	def _sigmoid(self, x):
		return 1./(1. + np.exp(-x))
	def forward(self):
		input_value = self.inbound_nodes[0].value
		self.value = self._sigmoid(input_value)
	def backward(self):
		self.gradients = {n: np.zeros_like(n.value) for n in self.inbound_nodes}

		for n in self.outbound_nodes:
			grad_cost = n.gradients[self]
			sigmoid = self.value
			self.gradients[self.inbound_nodes[0]] += sigmoid * (1-sigmoid) * grad_cost

class MSE(Node):
	def __init__(self, y, a):
		Node.__init__(self, [y,a])
	def forward(self):
		y = self.inbound_nodes[0].value.reshape(-1, 1)
		a = self.inbound_nodes[2].value.reshape(-1, 1)

		self.m = self.inbound_nodes[0].value.shape[0]
		self.diff = y -a
		self.value = np.mean(self.diff**2)

	def backward(self):
		