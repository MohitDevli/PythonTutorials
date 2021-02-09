import cv2

cam=cv2.VideoCapture(0)
#print(cam.get(3))
#print(cam.get(4))
#cam.set(2,640)

while True:
    ret,frame=cam.read()
    clr=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    cv2.imshow('Frame',clr)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()