import numpy as np

def softmax(x):
	return np.exp(x) /np.sum(np.exp(x), axis=0)

logits = [3.0, 1.0, 0.2]
print(softmax(logits))