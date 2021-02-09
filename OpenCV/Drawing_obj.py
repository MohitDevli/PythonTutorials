import cv2
import numpy as np

cv2.namedWindow('Drawing',cv2.WINDOW_NORMAL)
img=np.zeros((512,512,3),np.uint8)

cv2.imshow('Drawing',img)

#DRAWING START
img=cv2.line(img,(50,50),(511,511),(255,0,0),5)
img=cv2.rectangle(img,(384,0),(510

cv2.waitKey(0)
cv2.destroyAllWindows()