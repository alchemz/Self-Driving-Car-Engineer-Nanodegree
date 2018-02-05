import tensorflow as tf
import numpy as numpy

x = np.array([[0,1,0.5, 10], [2,2.5,1,-8],[4,0,5,6],[15,1,2,3]], dtype=np.float32).reshape((1,4,4,1))
x = tf.constant(x)

def maxpool(input):
	ksize = [1, 2, 2, 1] # filter dimension [batch, height, width, channels]
	strides = [1, 2, 2, 1]
	padding = 'VALID'
	return tf.nn.max_pool(input, ksize, strides, padding)

out = maxpool(x)

#out_height = ceil(float(in_height - filter_height + 1) / float(strides[1]))
#out_width  = ceil(float(in_width - filter_width + 1) / float(strides[2]))

#