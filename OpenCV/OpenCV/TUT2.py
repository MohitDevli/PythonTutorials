""" """
import cv2

cap=cv2.VideoCapture(0)  #0 is camera device index
#cap=cv2.VideoCapture('video.mp4') #for video import
out=cv2.VideoWriter('output.mp4',)

while True:
    ret, frame=cap.read()

    #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#this is used to get the video property like height and width
    #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame',gray)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()