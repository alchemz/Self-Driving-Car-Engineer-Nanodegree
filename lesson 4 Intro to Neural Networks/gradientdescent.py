import numpy as np

def sigmoid(x):
	#calculate sigmoid
	return 1/(1+np.exp(-x))

def sigmoid_prime(x):
	return sigmoid(x)*(1-sigmoid(x))

#input data
x=np.array([0.1, 0.3])
#target
y=0.2
#input to output weights
weights = np.array([-0.8, 0.5])

learnrate=0.5

#the neural network output(y_hat)
nn_output = sigmoid(x[0]*weights[0] + x[1]*weights[1])
#output error(y-y_hat)
error = y-nn_output
#error term(lowercase delta)
error_term = error*sigmoid_prime(np.dot(x, weights))
#gradient descent step
del_w =[learnrate*error_term * x[0],
		learnrate*error_term * x[1]]
#
