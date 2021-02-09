import cv2

img= cv2.imread("3.jpg")

img=cv2.resize(img, (780,480))

def drawBounds(tuple(x1,y1), tuple(x2, y2), tuple(r,b,g), thickness):
	cv2.rectangle(img, (50,10), (50,480), (255,0,0), 3)
	cv2.rectangle(img, (730,10), (730,480), (255,0,0), 3)


def drawSign(x, y):
	cv2.putText(img, "^", (390,450), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,0), 3, cv2.LINE_AA)



drawBounds((50,10),(50,480))
drawSign()

cv2.imshow("frame", img)

cv2.waitKey(0)

cv2.destroyAllWindows()


