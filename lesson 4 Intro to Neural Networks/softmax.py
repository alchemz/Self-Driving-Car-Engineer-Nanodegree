import numpy as np

def softmax(L):
	expl = np.exp(L)
	sumExpL = sum(expL)
	result = []
	for i in expL:
		result.append(i*1.0 /sumExpL)
	return result

