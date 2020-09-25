import keras
import numpy as np
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from keras.models import Sequential
from Load_Dataset_CNN import *


batch_size = 12
num_classes = 20
epochs = 5

X_Data, Y_Data = load_dataset()
X_Data = X_Data.reshape(40)
print(X_Data.shape)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(metrics=['accuracy'])
model.fit(X_Data, Y_Data, batch_size=40, epochs=3, validation_split=0.3)
