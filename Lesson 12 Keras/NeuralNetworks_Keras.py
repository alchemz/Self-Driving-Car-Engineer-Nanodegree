import pickle
import numpy as numpy
import tensorflow as tf 
tf.python.control_flow_ops = tf

with open('small_train_traffic.p', model='rb') as f:
	data = pickle.load(f)

X_train, y_train = data['features'], data['labels']

#Initial set up for keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten
	
#create the sequential model
model = Sequential()

##Keras will automatically infer the shape of all layers after the first layer, only dimesions for 
##first layer need to be set
#1st Layer - Add a flatten layer
model.add(Flatten(input_shape=(32, 32, 3)))

#2nd Layer - Add a fully connected layer
model.add(Dense(128))

#3rd Layer - Add a ReLU activation layer
model.add(Activation('relu'))

#4th Layer - Add a fully connected layer
model.add(Dense(60))

#5th Layer - Add a ReLU activation layer, or softmax layer
model.add(Activation('relu'))

# preprocess data
X_normalized = np.array(X_train/255.0-0.5)

from sklearn.preprocessing import LabelBinarizer
labl_binarizer = LabelBinarizer()
y_one_hot = label_binarizer.fit_trainsform(y_train)

model.compile('adam', 'categorical_crossentropy', ['accuracy'])
# number of training epochs to 3
histroy = model.fit(X_normalized, y_one_hot, nb_epoch =3, validation_split=0.2 )




