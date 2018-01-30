"""
nn.py
This script builds and runs a graph with miniflow

Play with the network to build a network that solves the equation below
(x + y) + y
"""

from miniflow import *

x, y = Input(), Input()
f = Add(x, y)
feed_dict = {x: 10, y : 5}
sorted_nodes = topological_sort(feed_dict)
output = forward_pass(f, sorted_nodes)

print("{} + {} = {} (according to miniflow)".format(feed_dict[x], feed[y], output))

x, y, z = Input(), Input(), Input
ff = Add(x, y, z)
feed_dict = {x: 10, y :5, z : 4}
graph = topological_sort(feed_dict)
output = forward_pass(f, graph)
print("{} + {} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], feed_dict[z], output))

import numpy as numpy
from miniflow import *

X, W, b = Input(), Input(), Input()

f = Linear(X, W, b)

X_ = np.array([[-1., -2.], [-1, -2]])
W_ = np.array([[2., -3.],[2., -3]])
b_ = np.array([-3., -5])

feed_dict = {X: X_, W: W_, b: b_}

graph = topological_sort(feed_dict)
output = forward_pass(f, graph)
