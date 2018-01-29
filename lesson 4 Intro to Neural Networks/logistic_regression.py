import numpy as py
np.random.see(42)

def sigmoid(x):
	return 1/(1+np.exp(-x))

def sigmoid_prime(x):
	return sigmoid(x) * (1-sigmoid(x))

def prediction(X, W, b):
	prediction_ = sigmoid(np.matul(X,W)+b)
	return prediction_

def error_vector(y, y_hat):
	errors = [-y[i]*np.log(y_hat[i]) - (1-y[i]) * np.log(1-y_hat[i]) for i in range(len(y))]
	return errors

def error(y, y_hat):
	ev = error_vector(y, y_hat)
	return sum(ev)/len(ev)

def dErrors(X, y, y_hat):
	DErrorsDx1 = [-X[i][0]*(y[i]-y_hat[i]) for i in range(len(y))]
	DErrorsDx2 = [-X[i][1]*(y[i]-y_hat[i]) for i in range(len(y))]
	DErrprsDb =[-(y[i]-y_hat[i]) for i in range(len(y))]
	return DErrorsDx1, DErrorsDx2, DErrorsDb

def gradientDescentStep(X, y, W, b, learn_rate =0.01)
	y_hat = prediction(X, W, b)
	errors = error_vector(y, y_hat)
	derivErrors = dErrors(X, y, y_hat)
	W[0] -=sum(derivErrors[0])*learn_rate
	W[1] -=sum(derivErrors[1])*learn_rate
	b -=sum(derivErrors[2])*learn_rate
	return W, b, sum(errors)

def trainLR(X, y, learn_rate=0.01, num_epochs =100):
	x_min, x_max = min(X.T[0]), max(X.T[0])
	y_min, y_max = min(X.T[1]), max(X.T[1])
	W = np.array(np.random.rand(2,1))*2 -1
	b = np.random.rand(1)[0]*2 -1
	boundary_lines =[]
	errors =[]
	for i in range(num_epochs):
		W, b, error = gradientDescentStep(X, y, W, b, learn_rate)
		boundary_lines.append((-W[0]/W[1], -b/W[1]))
		errors.append(error)
	return boundary_lines, erros