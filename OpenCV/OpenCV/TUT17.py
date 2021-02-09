"""
Contour : the cordinates
"""
import cv2
import numpy as np
img=cv2.imread("messi.jpg")
imgray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh=cv2.threshold(imgray, 127, 255, 0)

__,contours,_ =cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #Image, contour mode, Contour approximation methdo
#print(len(contours))
#print(contours[0])
print(__,'\n',_)

cv2.drawContours(img, contours, 3, (0,255,0),3) # image, conours, index -1 mean this draw all contours, color, thicness

cv2.imshow("img", img)
cv2.imshow("imgray", imgray)
cv2.imshow("thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()