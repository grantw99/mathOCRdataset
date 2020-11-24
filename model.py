#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K


# In[18]:


class VGGNet:
	@staticmethod
	def build(width, height, depth, classes, activFct="softmax"): #finalAct='softmax' for single-label classification || finalAct='sigmoid' for multi-label classification 
		# initialize the model along with the input shape to be
		# "channels last" and the channels dimension itself
		inputShape = (height, width, depth)
 
		# if we are using "channels first", update the input shape
		# and channels dimension
		if K.image_data_format() == "channels_first":
			inputShape = (depth, height, width)
			chanDim = 1
        # CONV => RELU => POOL

    model = Sequential([
      Conv2D(32, (3,3), activation='relu', input_shape = inputShape,
      MaxPooling2D(pool_size = (2,2)),
      Conv2D(32, (3,3), activation='relu'),
      MaxPooling2D(pool_size = (2,2)),
      Flatten(),
      Dense(1024, activation = 'tanh'),
      Dropout(0.5),  #to reduce overfitting
      Dense(classes, activation='softmax')
    ])

 
		# return the constructed network architecture
		return model


# In[ ]:

 


