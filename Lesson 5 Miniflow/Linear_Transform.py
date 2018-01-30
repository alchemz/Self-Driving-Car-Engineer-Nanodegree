class Linear(Node):
	def __init__(self, X, W, b):
		Node.__init__(self, [X, W, b])

	def forward(self):
		X = self.inbound_nodes[0].value
		W = self.inbound_nodes[1].value
		b = self.inbound_nodes[2].value

		self.value = np.dot(X, W) + b