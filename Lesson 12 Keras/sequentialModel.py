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






