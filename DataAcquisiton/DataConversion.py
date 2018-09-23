import numpy as np 
from PIL import Image
from matplotlib import pyplot as plt
from tempfile import TemporaryFile
import pandas as pd 

np.random.seed(123)

NUM_OF_RAW_IMAGES = 151
NUM_OF_CLASSES = 247
NUM_OF_SPECIAL_CLASSES = 19
NUM_OF_UYIR_MEI_CLASSES = 234
IMG_H_W = 65
DELIMITER = ','
RESULTANT_STORAGE_PATH = '../ImageStorage/ResultantStorage/'
LABEL_MAP_PATH = '../LabelMaps/'
BINARY_STORAGE_PATH = '../DataBinaryStorage/'

def shuffle_in_unison(a, b):
    assert len(a) == len(b)
    shuffled_a = np.empty(a.shape, dtype=a.dtype)
    shuffled_b = np.empty(b.shape, dtype=b.dtype)
    permutation = np.random.permutation(len(a))
    for old_index, new_index in enumerate(permutation):
        shuffled_a[new_index] = a[old_index]
        shuffled_b[new_index] = b[old_index]
    return shuffled_a, shuffled_b

dataArray = np.zeros((NUM_OF_RAW_IMAGES * NUM_OF_CLASSES, 
            IMG_H_W, 
            IMG_H_W), 
            dtype = int)
dataLabel = np.zeros(NUM_OF_RAW_IMAGES * NUM_OF_CLASSES, 
            dtype = int)
'''
specialArray = np.zeros((NUM_OF_RAW_IMAGES * NUM_OF_SPECIAL_CLASSES, 
            IMG_H_W,
            IMG_H_W),
            dtype = int)
specialLabel = np.zeros(NUM_OF_RAW_IMAGES * NUM_OF_SPECIAL_CLASSES, 
            dtype = int)

meiArray = np.zeros((NUM_OF_UYIR_MEI_CLASSES * NUM_OF_RAW_IMAGES,
            IMG_H_W,
            IMG_H_W), 
            dtype = int)
meiLabel = np.zeros(NUM_OF_UYIR_MEI_CLASSES * NUM_OF_RAW_IMAGES,
            dtype = int)

uyirArray = np.zeros((NUM_OF_CLASSES * NUM_OF_RAW_IMAGES,
            IMG_H_W,
            IMG_H_W), 
            dtype = int)
uyirLabel = np.zeros(NUM_OF_CLASSES * NUM_OF_RAW_IMAGES,
            dtype = int)

meiMap = np.genfromtxt(LABEL_MAP_PATH + 'mei_label_map.csv', delimiter=DELIMITER, dtype = int)
meiMap = meiMap.reshape(247)

uyirMap = np.genfromtxt(LABEL_MAP_PATH + 'uyir_label_map.csv', delimiter=DELIMITER, dtype = int)
uyirMap = uyirMap.reshape(247)
'''
dataI = 0
meiI = 0
uyirI = 0
for i in range(0, NUM_OF_RAW_IMAGES):
    for j in range(0, 247):
        img = Image.open(RESULTANT_STORAGE_PATH + str(i) + '/' + str(j) + '.png')
        array = np.array(img)
        dataArray[dataI] =  array
        dataLabel[dataI] = j
        dataI += 1
    print('loading', i, end='\r')
'''
        if meiMap[j] != -1:
            meiArray[meiI] = array
            meiLabel[meiI] = meiMap[j]
            meiI += 1
        if uyirMap[j] != -1:
            uyirArray[uyirI] = array
            uyirLabel[uyirI] = uyirMap[j]
            uyirI += 1
'''

data = [dataArray, dataLabel]

fileName = BINARY_STORAGE_PATH + "data.npz"
np.savez(fileName, dataArray=dataArray, dataLabel=dataLabel)
