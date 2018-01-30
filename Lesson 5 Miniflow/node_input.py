class Input(Node):
	def __init__(self):
		Node.__init__(self)

	def forward(self, value = None):
		# Overwrite the value if one is passed in
		if value is not None:
			self.value = value