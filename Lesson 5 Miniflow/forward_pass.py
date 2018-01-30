def forward_pass(output_node, sorted_nodes):
	"""
	Performs a forward pass through a list of sorted nodes

	Arguments:
		'output_node'
		'sorted_nodes'

	Returns the output node's value
	"""

	for n in sorted_nodes:
		n.forward()
	return output_node.value
	