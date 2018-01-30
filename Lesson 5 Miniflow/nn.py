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