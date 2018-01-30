import tensorflow as tf

# Todo: convert the following to tensorflow
# x = 10
# y = 2
# z =x/y -2

#Todo: print z from a session
x = tf.constant(10)
y = tf.constant(2)
z = tf.substract(tf.divide(x,y), tf.cast(tf.constant(1), tf.float64))

with tf.Session() as sess:
	output = sess.run(z)
	print(output)