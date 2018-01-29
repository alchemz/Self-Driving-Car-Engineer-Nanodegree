import numpy as np
from data_prep import features, targets, features_test, targets_test

np.random.seed(21)

def sigmoid(x):
	return 1/(1+exp(-x))

n_hidden = 2
epochs = 900
learnrate = 0.005

n_records, n_features = features.shape
last_loss = None
#initailize weights
weights_input_hidden = np.random.normal(scale=1/n_features ** .5,
										size=(n_features, n_hidden))
weights_hidden_output = np.random.normal(scale=1/n_features ** .5,
										size=n_hidden)

for e in range(epochs):
	del_w_input_hidden = np.zeros(weights_input_hidden.shape)
	del_w_hidden_output = np.zeros(weights_hidden_output.shape)
	for x, y in zip(features.values, targets):
		##forward pass
		hidden_input = np.dot(x, weights_input_hidden)
		hidden_output = sigmoid(hidden_input)

		output = sigmoid(np.dot(hidden_output, weights_hidden_output))

		##backward pass
		error = y- output

		#error gradient in output unit
		output_error = error * output*(1-output)

		#propagate errors to hidden layer
		hidden_error = np.dot(output_error, weights_hidden_output) * \
							 hidden_output*(1-hidden_output)

		#update changes in weights
		del_w_hidden_output += output_error * hidden_output
		del_w_input_hidden += hidden_error * x[:, None]

	# udpate weights
	weights_input_hidden += learnrate * del_w_input_hidden /n_records
	weights_hidden_output += learnrate * del_w_hidden_output/n_records

	if e%(epochs /10) ==0:
		hidden_output = sigmoid(np.dot(x, weights_input_hidden))
		out = sigmoid(np.dot(hidden_output, weights_hidden_output))
		loss = np.mean((out-targets)**2)

		if last_loss and last_loss < loss:
			print("Train loss: ", loss, "Warning - Loss Increasing")
		else:
			print("train loss: ", loss)
		last_loss = loss

hidden = sigmoid(np.dot(features_test, weights_input_hidden))
out = sigmoid(np.dot(hidden, weights_hidden_output))
predictions = out >0.5
accuracy = np.mean(predictions == target_test)
print("Prediction accuracy: {:.3f}".format(accuracy))