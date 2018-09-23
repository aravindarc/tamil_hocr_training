import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg')

c = cv2.reduce(img, 1, cv2.REDUCE_SUM, dtype=cv2.CV_32S)

plt.imshow(c)
plt.show()