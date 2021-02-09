"""
Image Pramid:
Type:
	Guasian Priamid: 
	
	Laplasian Pramid: A level in thiss formed in opencv by diffrence between that level in 
		Gausian Priamid and expanded version of its upper level in 
		Gausian Priamid
	
"""

import cv2
import numpy as np

img=cv2.imread("lena.jpg")

# Guasian Priamid
lr1=cv2.pyrDown(img)
lr2=cv2.pyrUp(lr1)

# Laplasian Priamid
"""
lr2 is upper layer and lr1 is lower layer
"""




cv2.imshow("Image",img)
cv2.imshow("Lr1",lr1)
cv2.imshow("Lr2",lr2)

cv2.waitKey(0)
cv2.destroyAllWindows()

