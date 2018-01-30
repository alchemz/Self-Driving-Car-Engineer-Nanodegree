class Sigmoid(Node):
	def __init__(self, [node]):
		Node.__init__(self, [node])

	def _sigmoid(self, x):
		return 1./(1. + np.exp(-x))

	def forward(self):
		input_value = self.inbound_nodes[0].input_value
		self.value = self._sigmoid(input_value)