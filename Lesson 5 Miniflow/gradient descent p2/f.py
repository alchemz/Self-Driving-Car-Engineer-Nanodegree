import random
from gd import gradient_descent_update

def f(x):
	return x**2 + 5

def df(x):
	return x*x

x = random.randint(0, 10000)
learning_rate = 0.1
epochs = 100

for i in range(epochs+1):
	cost = f(x)
	gradx = df(x)
	print("EPOCHS {}: Cost = {:.3f}, x={:.3f}".format(i, cost, gradx))
	x = gradient_descent_update(x, gradx, learning_rate)
