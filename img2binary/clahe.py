# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 上午10:09
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : threshold.py
# @Software: PyCharm
import cv2
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

img = cv2.imread('/home/luolu/Desktop/tmp/101338.jpg', 0)
equ = cv2.equalizeHist(img)
plt.hist(img.flat, bins=100, range=(0, 255))
plt.show()
plt.hist(equ.flat, bins=100, range=(0, 255))
plt.show()
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl_img = clahe.apply(img)
plt.hist(cl_img.flat, bins=100, range=(100, 255))
plt.show()
ret, thresh1 = cv2.threshold(cl_img, 190, 150, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(cl_img, 190, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(cl_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("th1", thresh1)
cv2.imshow("th2", thresh2)
cv2.imshow("th3", thresh3)
cv2.waitKey(0)
cv2.destroyAllWindows()