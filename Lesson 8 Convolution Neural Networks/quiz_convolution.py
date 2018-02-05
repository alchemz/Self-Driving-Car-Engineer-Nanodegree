import tensorflow as tf
import numpy as np

x = np.array([[0,1,0.5, 10],
			 [2,2.5, 1, -8],
			 [2,0,5,6],
			 [15,1,2,3]],dtype = np.float32).reshape((1,4,4,1))
X = tf.constant(x)

def con2d(input):
	F_W = tf.Variable(tf.truncated_normal((2, 2, 1, 3)))
	F_b = tf.Variable(tf.zeros(3))
	strides = [1, 2, 2, 1]
	padding = 'VALID'
	return tf.nn.conv2d(input, F_W, strides, padding) + F_b

out = conv2d(X)