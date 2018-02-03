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
