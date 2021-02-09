#Adoptive thresholding: where the threshold is calculated for the smmaler region, unling global ones.

import cv2
import numpy as np

img=cv2.imread("sudoko.jpeg",0)



_, th1=cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

th2=cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) #src, max val of pixel, adoptive method , threashold type, blocksize, value of C (contant) , used to find mean

th3=cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) 

cv2.imshow("img", img)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)

cv2.waitKey(0)

cv2.destroyAllWindows()
