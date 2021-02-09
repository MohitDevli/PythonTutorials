"""
OpenCv read a image in BGR format, and
MatPlotlib reads a image in RBG format, show when we use them both they show diffrent color images.


"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("lena.jpg",-1)
cv2.imshow("ie", img)

'''
b,g,r=cv2.split(img)

img2=cv2.merge((r,g,b))
plt.imshow(img2)
plt.show()
'''
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

