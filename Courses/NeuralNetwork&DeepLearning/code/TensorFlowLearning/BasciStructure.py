import tensorflow as tf
import numpy as np

coefficients = np.array([[1.], [-10], [20]])
x = tf.placeholder(tf.float32, [3, 1])
w = tf.Variable(0, dtype=tf.float32)  # specify the training variables

# we simply defined the cost as a function of other quantities, but did not evaluate its value
cost = x[0][0] * w ** 2 + x[1][0] * w + x[2][0]
train = tf.train.GradientDescentOptimizer(0.3).minimize(cost)

# That initialized the cost variable
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# in the last line we were finally able to evaluate the value of loss and print its value.
sess.run(train, feed_dict={x: coefficients})
print(sess.run(w))

for i in range(10):
	sess.run(train, feed_dict={x: coefficients})
print(sess.run(w))
