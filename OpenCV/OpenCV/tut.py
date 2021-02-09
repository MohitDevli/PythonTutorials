"""WRITE, SAVE, AND IMPORT IMAGES"""

import cv2

img=cv2.imread('lena.jpg',0)#here first acept image name, secong argument calleg flag
"""flag has 3 value:0,1,-1
(cv2.imread_color)1:loads colorimage
(cv2.imread_grayscale)0:grayscale loading
(cv2.imread_unchanged)-1:load image include alpha channels
"""

cv2.imshow('Tut1',img)
"""here it first take  first argument window name,
 than second atgument is our image variable"""
k=cv2.waitKey(0)   #it take value of time in millisecond
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lena_copy.jpg', img) #this make a copy of image
    cv2.destroyAllWindows()