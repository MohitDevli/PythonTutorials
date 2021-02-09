#Thresholding tecniques

import cv2
import numpy as np

img=cv2.imread("gra.jpeg",0)

"""
In binary if pixel value is less than 125, pixel value set to be 0, else if greter than 125 than set to 1 (255)
In Trunc, if pixel value reaches 125, it will remain to 125, further for all pixel
In TOZERO, if pixel value is less than threshold(125), it will remain 0.

125 is global value as it will be same for all pixels or threshvalue

Adoptive thresholding: where the threshold is calculated for the smmaler region, unling global ones.


"""
_, th1=cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
__, th2=cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)
___, th3=cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO)
____, th4=cv2.threshold(img, 125, 255, cv2.THRESH_TRIANGLE)
_____, th5=cv2.threshold(img, 125, 255, cv2.THRESH_TRUNC)
______, th6=cv2.threshold(img, 125, 255, cv2.THRESH_OTSU)

cv2.imshow("img", img)
cv2.imshow("th4", th6)

cv2.waitKey(0)

cv2.destroyAllWindows()
