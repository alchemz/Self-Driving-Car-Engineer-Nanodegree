import pandas as pd

weight1 = 0.0
weight2 = 0.0
bias = -1

test_inputs = [(0,0), (0,1), (1,0), (1,1)]
correct_outputs = [False, False, False, True]0
outputs = []

for test_inputs, correct_outputs in zip(test_inputs, correct_outputs):
	linear_combination = weight1 * test_inputs[0] + weight2* test_inputs[1] + bias
	output = int(linear_combination > =0)
	is_correct_string = 'Yes' if output == correct_output else 'No'
	output.append([test_inputs[0], test_inputs[1], linear_combination, output, is_correct_string)

def perceptronStep(X, y, W, b, learn_rate = 0.01):
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i]-y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b
