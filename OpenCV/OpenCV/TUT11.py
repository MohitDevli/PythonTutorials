import cv2
import numpy as np

#img=cv2.imread("lena_copy.png")
#cv2.imwrite("Egde", cv2.Canny(0.5,0.5,50))
#cv2.imshow("img real", img)
#img=cv2.Canny(img, 200,250)
#cv2.imshow("IMg", img)

cap=cv2.VideoCapture(0)

while True:
	_, frame= cap.read()
	
	frame=cv2.Canny(frame, 100,250)
	cv2.imshow("Frame", frame)
		
	cv2.waitKey(1)
	
cv2.destroyAllWindows()

