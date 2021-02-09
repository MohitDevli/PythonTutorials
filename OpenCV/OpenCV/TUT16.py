"""
Blending Images: Merging Images, with blended line of merging to look them real.

"""
import cv2
import numpy as np

img1=cv2.imread("lena.jpg")
img2=cv2.imread("messi.jpg")
img1=cv2.resize(img1, (512,512))
img2=cv2.resize(img2, (512,512))

#Image Priamid Technique
# Genrete gausian primid for img1
img1_copy=img1.copy()
gp_img1=[img1_copy]

for i in range(6):
	img_copy = cv2.pyrDown(img1_copy)
	gp_img1.append(img1_copy)
	
# Genrete gausian primid for img2
img2_copy=img2.copy()
gp_img2=[img2_copy]

for i in range(6):
	img2_copy = cv2.pyrDown(img2_copy)
	gp_img1.append(img2_copy)
	
#Genrete Laplasian Primid for img1
img1_copy= gp_img1[5]
lp_img1= [img1_copy]

for i in range(5,0,-1):
	gausian_expended=cv2.pyrUp(gp_img1[i])
	laplasian =cv2.subtract(gp_img1[i-1], gausian_expended)
	lp_img1.append(laplasian)

#Genrete Laplasian Primid for img2
img2_copy= gp_img2[5]
lp_img2= [img2_copy]

for i in range(5,0,-1):
	gausian_expended=cv2.pyrUp(gp_img2[i])
	laplasian =cv2.subtract(gp_img2[i-1], gausian_expended)
	lp_img2.append(laplasian)

#Join the half os these Image
img_img2_primid=[]
n=[]

for img1_lap, img2_lap in zip(lp_img1, lp_img2):
	n=n+1
	cols, rows, ch= img1_lap.shape
	laplacian = np.hstack((img1_lap[:,0:int(cols/2)], img2_lap[:,int(cols/2):]))
	img_img2_primid.append(laplacian)

#Reconstruct Image.
img12_reconstruct= img_img2_primid[0]
for i in range(1,6):
	img12_reconstruct=cv2.pyrUp(img12_reconstruct)
	img12_reconstruct= cv2.add(img_img2_primid[i], img12_reconstruct)
	
#Merging Images without blending line of sepretion
img1_2=np.hstack((img1[:,:256], img2[:,256:]))


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)




cv2.waitKey(0)
cv2.destroyAllWindows()


