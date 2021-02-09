"""
Canny Edge detection algorithim is composed in 5 steps:
	1. Noice Reduction : To apply gousian image filter to smmoth image and remove noice
	2. Gradeint calulation : To find the intensity gradeint of Image
	3. Non-Maximum suppresion : To apply Non-Maximum suppresion to get rid of bad reponse in edge detection 
	4. Double ThreshHold : To determine Potential Images
	5. Edge TRacking by Hystersis : To track edges by Hystersis
	
"""

import cv2
import numpy as np

img=cv2.imread("messi.jpg")

canny=cv2.Canny(img, 100,200) #image , first threshold value, second threshold value

cv2.imshow("Img", img)
cv2.imshow("Canny", canny)


cv2.waitKey(0)
cv2.destroyAllWindows()

