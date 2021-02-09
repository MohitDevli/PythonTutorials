'''
import cv2
img=cv2.imread('lena.jpg',1)
cv2.imshow('Window',img)
k= cv2.waitKey(0)

if k==27:
	cv2.destroyAllWindows()
if k==ord('s'):
	cv2.imwrite('lena_copy.png',img)
	cv2.destroyAllWindows'''



'''
import cv2
cap=cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_AUTOFOCUS))  #Properties of Camaera Used.
print(cap.isOpened())  #True or False

fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
fps=30
out=cv2.VideoWriter('output.avi', fourcc, 30, (640,480))

while (cap.isOpened()):
	ret, frame = cap.read() #ret:True, False and frame is a type of numpy array
	
	if ret ==True:
		gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('Frame',gray)
		
		out.write(frame)
		
		if cv2.waitKey(1)==ord('q'):
			break
	
	else:
		break
	
cap.release()
out.release()
cv2.destroyAllWindows()'''

'''
import cv2

img=cv2.imread('lena.jpg', 1)

img=cv2.line(img, (0,0), (255,255), (255,0,0) ,5)
img=cv2.arrowedLine(img, (100,0), (255,255), (0,255,0) ,5)
img=cv2.rectangle(img, (384,384), (450,210), (0,255,0), 1) #last argument also be -1 for full fill
img=cv2.circle(img, (300,300), 50, (145,20,144), 5)

font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img, 'OpenCV', (0,500),font, 4 ,(120,41,132),5,cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''	
'''
import cv2
import numpy as np
img=np.zeros(shape=(450,450))
cv2.imshow('Numpy zeros',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Sets Properties.
'''
import cv2

cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

h=cap.set(cv2.CAP_PROP_FRAME_HEIGHT ,780)
w=cap.set(cv2.CAP_PROP_FRAME_WIDTH ,1280)

print(cap.get(3),'\n', cap.get(4))

while True:
	ret, frame= cap.read()
	
	cv2.imshow('Image', frame)
	
	cv2.waitKey(1)
	
cap.release()
cv2.destroyAllWindows()'''

#Handling Mouse Event
'''
import numpy as np
import cv2

events=[i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags ,param):
	if event== cv2.EVENT_LBUTTONDOWN:
		print(x ,'', y)
		font=cv2.FONT_HERSHEY_COMPLEX
		strxy= str(x)+','+str(y)
		cv2.putText(img,strxy, (x,y),font, 0.7, (255,255,255),1)
		cv2.imshow('Window', img)
		

def click_event_two(event, x, y, flags ,param):
	
	if event==cv2.EVENT_MOUSEMOVE:
		cv2.circle(img, (x,y), 3, (0,0,255) ,-1)
		points.append((x,y))
		if len(points)>=2:
			cv2.line(img,points[-1],points[-2],(255,0,0), 5)
			cv2.imshow('Window', img)
			print(points)
		cv2.imshow('Window', img)
		
img=np.zeros((512,512,3), np.uint8)
cv2.imshow('Window', img)

points=[]

cv2.setMouseCallback('Window',click_event_two)

cv2.waitKey(0)
cv2.destroyAllWindows()'''

#Arthamatic Operation on the Images

import cv2

img=cv2.imread('lena.jpg',1)

print(img.shape)
print(img.size)  #Total no of pixel in Images
print(img.dtype) #uint8

b,g,r=cv2.split(img)  #Provide sepreate bgr channels of images

cv2.merge((b,g,r)) #Merge all bgr channels together


#ROI of Image is the Region of Intrest.


ball= img[50:150, 120:160]  #Point One
img[100:160, 100:160] = ball


cv2.imshow('Win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



