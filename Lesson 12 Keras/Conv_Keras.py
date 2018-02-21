#Conv_Keras.py
import pickle
import numpy as numpy
import tensorflow as tensorflow
tf.python.control_flow_ops = tf

with open('small_train_traffic.p', mode='rb') as f: data = pickle.load(f)

X_train, y_train = data['features'], data['labels']

#Initial setup for Keras
from keras.model import Sequential
from keras.layers.core import Dense, Activation, Flatten
from keras.layers.convolutional import Convolution2D
from keras.layers import Convolution2D

#Build Convolutional Neural Network in Keras here
model = Sequential()
model.add(Conv2D(32, 3, 3, activation = 'relu', input_shape=(32, 32, 3)))
model.add(Activation('relu'))
model.add(Flatten())
model.add(Dense())
model.add(Activation('relu'))
model.add(Dense(5))
model.add(Activation('softmax'))

#Preprocess data
X_normalized = np.array(X_train/255.0 - 0.5)

from sklearn.preprocessing import LabelBinarizer
label_binarizer = LabelBinarizer()
y_one_hot = label_binarizer.fit_transform(y_train)

model.compile('adam', 'categorical_crossentropy', ['accuracy'])
history = model.fit(X_normalized, y_one_hot, nb_epoch=3, validation_split=0.2)