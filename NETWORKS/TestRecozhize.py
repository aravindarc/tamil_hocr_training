from __future__ import print_function
import keras
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K 
from keras.layers.normalization import BatchNormalization
import numpy as np
from matplotlib import pyplot as plt

np.random.seed(100)

batch_size = 128
num_classes = 26
epochs = 30

img_rows, img_cols = 65, 65

DELIMITER = ','
(_, _, _, _, _, _, a, b) = np.load('RecozhitionData.npy', encoding = 'bytes')

(x_train, x_test, _), (y_train, y_test, _) = np.split(a, [10127, 11115]), np.split(b, [10127, 11115])
    
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

json_file = open('uyir_model.json', 'r')
uyir_model = json_file.read()
json_file.close()
uyir_model = model_from_json(uyir_model)

uyir_model.load_weights("uyir_weights.h5")
print("Loaded uyir_model from disk")

uyir_model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])

json_file = open('mei_model.json', 'r')
mei_model = json_file.read()
json_file.close()
mei_model = model_from_json(mei_model)

mei_model.load_weights("mei_weights.h5")
print("Loaded mei_model from disk")

mei_model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])

labelMap = np.genfromtxt('uyir_mei_label.csv', delimiter=DELIMITER, dtype = int)


n = 10
def predict(imgArr):
    tempArr = imgArr.reshape(1, 65, 65, 1)
    y = uyir_model.predict_classes(tempArr)[0]
    if y > 12:
        x = 18
        y -= 13
    else:
        x = mei_model.predict_classes(tempArr)[0]
    return([x, y, labelMap[x][y]])

x = predict(x_test[n])
print('Uyir class: ', str(x[0]))
print('Mei class: ', str(x[1]))
print('UyirMei class: ', str(x[2]))

plt.imshow(x_test[n])
plt.show()