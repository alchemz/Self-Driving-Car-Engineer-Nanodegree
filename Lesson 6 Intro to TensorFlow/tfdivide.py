import tensorflow as tf

# Todo: convert the following to tensorflow
# x = 10
# y = 2
# z =x/y -2

#Todo: print z from a session
x = tf.constant(10)
y = tf.constant(2)
z = tf.substract(tf.divide(x,y), tf.cast(tf.constant(1), tf.float64))
z = tf.subtract(tf.cast(tf.divide(x, y), tf.int32), tf.constant(1))

w = tf.add(5,7)
a = tf.substract(10, 4)
b = tf.multiply(2,5)
# tf.substract(tf.constant(2.0), tf.constant(1)) will fail with valueerror
tf.substract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))

with tf.Session() as sess:
	output = sess.run(z)
	print(output)