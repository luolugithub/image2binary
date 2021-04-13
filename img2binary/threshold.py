# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 上午10:09
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : threshold.py
# @Software: PyCharm
import cv2

img = cv2.imread('/home/luolu/Desktop/tmp/c2m06.jpg', 2)
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Image", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
