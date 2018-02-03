from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

n_input = 784 #data input size 28*28
n_classes = 10

mnist = input_data.read_data_sets('/datasets/ud730/mnist', one_hot=True)

train_features = mnist.train.images
test_features = mnist.test.images

train_labels = mnist.train.labels.astype(np.float32)
test_labels = mnist.test.labels.astype(np.float32)

weights = tf.Variable(tf.random_normal([n_input, n_classes]))
bias = tf.Variable(tf.random_normal([n_classes]))

##### None for batch size
features = tf.placeholder(tf.float32, [None, n_input])
labels = tf.placeholder(tf.float32, [None, n_classes])

#4 samples of features
example_features = [
					['F11', 'F12', 'F13', 'F14'],
					['F21', 'F22', 'F23', 'F24'],
					['F31', 'F32', 'F33', 'F34']
					['F41', 'F42', 'F43', 'F44']]
example_labels = [
					['L11', 'L12'],
					['L21', 'L22'],
					['L31', 'L32'],
					['L41', 'L42']]
example_batches = batches(3, example_features, example_labels)

