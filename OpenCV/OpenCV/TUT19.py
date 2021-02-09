import cv2
import numpy as np

#img=cv2.imread("smarties.png")

frame=cv2.VideoCapture(0)

while True:
	_, img =frame.read()
	img_grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	_, thresh=cv2.threshold(img_grey, 240,255, cv2.THRESH_BINARY)
	
	_, contours,_=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	
	for countour in contours:
		approx= cv2.approxPolyDP(countour, 0.01*cv2.arcLength(countour, True) , True) #coridinates, epsilon True mean closed shape
		cv2.drawContours(img, [approx], -1, (0,255,0) ,5)
		x=approx.ravel()[0]
		y=approx.ravel()[1]
		
		
		if len(approx)== 3:
			print("Triangle")
		elif len(approx)==4:
			print("Rectangle or Square")
		
		
	cv2.imshow("img", img)
	
	cv2.waitKey(1000)
cv2.destroyAllWindows()



