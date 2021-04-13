# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 下午3:36
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : adaptive_mean.py
# @Software: PyCharm
import cv2
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

img = cv2.imread('/home/luolu/Desktop/tmp/101338.jpg', 0)
img = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                            cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                            cv2.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
