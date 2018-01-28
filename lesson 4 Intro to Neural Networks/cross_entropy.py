import numpy as no

def corss_entropy(Y, P):
	Y = np.float_(Y)
	P = np.float_(P)
	result = -np.sum(Y * np.log(P) + (1-Y) * np.log(1-p))
	return result