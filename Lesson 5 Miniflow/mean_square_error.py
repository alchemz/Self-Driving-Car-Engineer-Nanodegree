class MSE(Node):
	def __init__(self, y, a):
		Node.__init__(self, [y, a])

	def forward(self):
		y = self.inbound_nodes[0].value.reshape(-1,1)
		a = self.inbound_nodes[1].value.reshape(-1,1)
		"""
		Todo: calculate the mean squared error

		use np.square
		Cost = C(w, b) = 1/m * np.sum(np.square(y-a))
		"""
		m = self.inbound_nodes[0].value.shape[0]
		self.value = np.sum((y-a)**2)/m