"""
An image Gradient is a directional change in the intensity or color in an image
It may used to find edges in the images

LaplacianGradeint:

"""


import cv2
import numpy as np

img=cv2.imread("sudoko.jpeg", cv2.IMREAD_GRAYSCALE)

#Laplacian Method
lap= cv2.Laplacian(img, cv2.CV_64F, ksize=3) #Image, datatype(64F=64Float) , kernalSize(optinal)
lap=np.uint8(np.absolute(lap))

#Sobel Method
sobelx=cv2.Sobel(img, cv2.CV_64F, 1,0) # Image, datatype, dx(0-1), dy, ksize(optinal)
sobely=cv2.Sobel(img, cv2.CV_64F,0,1)

sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))

#Comining Sobelx and sobely
sobel=cv2.bitwise_or(sobelx, sobely)

cv2.imshow("Img", img)
cv2.imshow("sobelx", sobelx)
cv2.imshow("sobely", sobely)
cv2.imshow("sobel", sobel)

cv2.waitKey(0)

cv2.destroyAllWindows()

