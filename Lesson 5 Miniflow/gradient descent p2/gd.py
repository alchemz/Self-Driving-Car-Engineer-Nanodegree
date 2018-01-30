def gradient_descent_update(x, gradx, learning_rate):
	x = x - learning_rate * gradx
	return x