import numpy as np

def sigmoid(x)
	return 1/(1+np.exp(-x))

learnrate =0.5
x = np.array([1,2])
y = np.array(0.5)
w = np.array([0.5, -0.5])

nn_output = sigmoid(np.dot(x,w))

error = y - nn_output

del_w = learnrate * error * nn_output * (1-nn_output)*x
