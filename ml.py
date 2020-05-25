from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2
from keras.datasets import mnist
from keras.utils import np_utils
import keras

#Load the mnist dataset 
(X_train, y_train), (X_test, y_test)  = mnist.load_data()

'''Changing the shape of input data from (60000,28,28) to (60000,28,28,1)
as Keras takes input arrays of Dimensions 4'''

X_train = X_train.reshape( X_train.shape[0] , X_train[0].shape[0] , X_train[1].shape[0] , 1 )
X_test = X_test.reshape( X_test.shape[0] , X_test[0].shape[0] , X_test[1].shape[0] , 1 )



# store the shape of a single image 
input_shape = ( X_train[0].shape[0] , X_train[1].shape[0], 1)



# change our image type to float32 data type
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')



# Normalize our data by changing the range from (0 to 255) to (0 to 1)
X_train /= 255
X_test /= 255


# Now we one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

num_classes = y_test.shape[1]
num_pixels = X_train.shape[1] * X_train.shape[2]



#Funtion for tweaking the parametres
def CRP_layer(layers , filters , filterSize , poolSize , strideSize):
  for i in range(layers):
    model.add(Conv2D(filters, (filterSize, filterSize),
                 padding = "same"))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size = (poolSize, poolSize), strides = (strideSize, strideSize)))
  return

#lets move to building our model

model = Sequential()

model.add(Conv2D(20, (5, 5),
                 padding = "same", 
                 input_shape = input_shape))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2), strides = (2, 2)))

#Calling Tweak file to get tweaking inputs
import tweak as T
X = T.run()

print('additional CRP layers = {}'.format(X[0]))
print('no. of filters = {}'.format(X[1]))
print('size of filters = {}'.format(X[2]))
print('size of pool = {}'.format(X[3]))
print('size of stride = {}'.format(X[4]))

#Calling the Additonal CRP layer adding function
CRP_layer(X[0] , X[1] , X[2] , X[3] , X[4] )


# Fully connected layers (w/ RELU)
model.add(Flatten())
model.add(Dense(500))
model.add(Activation("relu"))

# Softmax (for classification)
model.add(Dense(num_classes))
model.add(Activation("softmax"))
           
model.compile(loss = 'categorical_crossentropy',
              optimizer = keras.optimizers.Adadelta(),
              metrics = ['accuracy'])


# Training Parameters
batch_size = 128
epochs = 3

history = model.fit(X_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(X_test, y_test),
          shuffle=True)

# Evaluate the performance of our trained model
scores = model.evaluate(X_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

oldaccuracy = open('/mlops/accuracy.txt','r')
old = float(oldaccuracy.read())
oldaccuracy.close()
new  = scores[1]

if new > old :
  accuracyStored = open('/mlops/accuracy.txt','w')
  accuracyStored.write(str(new))
  accuracyStored.close()
  model.save("ArpitFinalModel.h5")
else :
  print("No improverment , model is saved with previous accuracy of {}".format(old))