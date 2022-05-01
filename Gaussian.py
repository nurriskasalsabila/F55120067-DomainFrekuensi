import numpy as np
import cv2

img_root='Images'
img_name='leaf.JPG'

#Reading the image
img = cv2.imread(img_name,cv2.IMREAD_UNCHANGED)

gaussBlur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Gaussian Smoothing",np.hstack((img,gaussBlur)))
cv2.waitKey(0)
cv2.destroyAllWindows()