#hidden layer with ReLu activation function
hidden_layer = tf.add(tf.matmul(features, hidden_weights), hidden_biases)
hidden_layer = tf.nn.relu(hidden_layer)

ouput = tf.add(tf.matul(hidden_layer, output_weights), out_biases)