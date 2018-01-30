def sgd_update(trainables, learning_rate = 1e-2):
	"""
	Update the value of each trainable with SGD
	"""
	#Todo: update all trainable with SGD
	#gradient descent update equation: x = x - alpa * sigmoid * (1-sigmoid) * grad_cost
	# trainables[0].value = trainables[0].value - learning_rate * sigmoid * (1-sigmoid) * grad_cost
	# trainables[1].value = trainables[1].value - learning_rate * sigmoid * (1-sigmoid) * grad_cost
	# trainables[2].value = trainables[2].value - learning_rate * sigmoid * (1-sigmoid) * grad_cost
	# trainables[3].value = trainables[3].value - learning_rate * sigmoid * (1-sigmoid) * grad_cost
	for t in trainables:
		partial = t.gradients[t]
		t.value -= learning_rate * partial
