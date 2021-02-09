"""
Smothing or bluring images: remove unwanted noice

Homogeneous Filter: is most simple filter, each output pixel is the mean of its 
kernal neighbours. In this all pixel contibute with euqal weight.

In homogenous kernal is : 1/KernalWidht*KeranlHeight
	
	e.g(Homeginous):
		[1,1,1,1,1
		1,1,1,1,1
		1,1,1,1,1
		1,1,1,1,1]


Gausian Filter: is nothing but using diffrebt-weight-kernal, in both x and y direction
	e.g: 
		[1,4,6,4,1
		4,25,45,84,65
		4,12,35,2,0
		45,87,41,21]

Median Filter: is Something that replace each pixel's value with median of its 
neighboring pixels. This method is great when dealing with 'salt and paper noise'(bsicalyy when pixels are distored)

Biletral Filter: By using above filter, we also smooth the edges, but for
preserving edges we are use BiletralFilter

"""

import cv2
import numpy as np


img=cv2.imread("lena.jpg")

#Creating Kernal
kernal=np.ones((5,5), np.float32)/25
dst=cv2.filter2D(img, -1, kernal) # IMage,depth, kernal

#BLur method: Averaging
blur=cv2.blur(img, (3,2)) #image, kernal

#GausianBlur Filter
gblur=cv2.GaussianBlur(img, (5,5), 0) #image, kernal, sigma-x value, 

#Medain Filter
mblur=cv2.medianBlur(img, 5) #image, kernal(must be odd except 1(or it will give original image)), 

#Biletral Filter
bilteral= cv2.bilateralFilter(img, 9, 75,75) #image, diamter of pixel neighbourhood, sigma color, sigma space


cv2.imshow("imgReal", img)
cv2.imshow("Median", bilteral)


cv2.waitKey(0)
cv2.destroyAllWindows()




