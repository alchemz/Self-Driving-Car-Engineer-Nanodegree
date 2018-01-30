"""
Linear Equations
"""
class Linear(Node):
	def __init___(self, inputs, weights, bias):
		Node.__init__(self, [inputs, weights, bias])

	def forward(self):
		inputs = self.inbound_nodes[0].value
		weights = self.inbound_nodes[1].value
		bias = self.inbound_nodes[2].value
		self.value = bias

		for x, w in zip(inputs, weights):
			self.value += x*w