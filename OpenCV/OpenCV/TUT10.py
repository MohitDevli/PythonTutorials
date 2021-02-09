import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("smarties.png", cv2.IMREAD_GRAYSCALE)

titles=["image"]
images=[img]

plt.imshow(img)
plt.show()
	
cv2.waitKey(0)
cv2.destroyAllWindows()

