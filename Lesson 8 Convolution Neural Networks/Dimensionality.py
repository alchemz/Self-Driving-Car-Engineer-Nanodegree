#Dimensionality
"""
W: Width of input layer
H: Height of input layer
F: A filter size of convolutional layer
S: Stride
P: padding
K: number of filters
"""
W_out = [(W-F+2P)/S] +1
H_out = [(H-F+2P)/S] +1
D_out = K
Volume_out = W_out * H_out * D_out

input = tf.placeholder(tf.float32, (None, 32, 32, 3))
filter_weights = tf.Variable(tf.truncated_normal((8,8,3,20))) #(height, weight, input_depth, output_depth)
filter_bias = tf.Variable(tf.zeros(20))
strides = [1, 2, 2, 1]
padding = 'Same'
conv = tf.nn.conv2d(input, filter_weights, strides, padding) + filter_bias

# 'Same' padding
out_height = ceil(float(in_height)/float(strides[1]))
out_width = ceil(float(in_width)/float(strides[2]))

#'Valid' padding
out_height = ceil(float(in_height - filter_height +1)/float(strides[1]))
out_width = ceil(float(in_width - filter_width+1)/float(strides[2])

#Total number of parameters on convolutional layer
(filter_layer_size + bias) * (output_layer_size)

#Parameters sharing
(filter_layer_size + bias) * output_depth

input = tf.placeholder(tf.float32, (None, 4, 4, 5))
filter_shape = [1, 2, 2, 1]
strides = 'VALID'
pool = tf.nn.max_pool(input, filter_shape, strides, padding)