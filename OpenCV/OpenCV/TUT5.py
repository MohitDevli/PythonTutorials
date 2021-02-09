import cv2
import numpy as np

img1=cv2.imread("messi.jpg")
img2=cv2.imread("smarties.png")

img1=cv2.resize(img1, (512,512))
img2=cv2.resize(img2, (512,512))

#dst=cv2.add(img1, img2)
dst=cv2.addWeighted(img1, .5,img2, .5 ,0) #weight , weight , gamma

cv2.imshow("img", dst)
cv2.waitKey(0)

cv2.destroyAllWindows()