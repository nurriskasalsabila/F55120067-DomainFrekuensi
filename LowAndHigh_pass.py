import numpy as np
import cv2

img_root='Images'
img_name='leaf.JPG'

#reading the image
img = cv2.imread(img_name,cv2.IMREAD_UNCHANGED)

kernel = np.ones((10,10),np.float32)/25
meanfilter = cv2.filter2D(img,-1,kernel)
gaussBlur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)

#teknik lowpass
lowpass = cv2.filter2D(img,-1, kernel)
lowpass = img - lowpass
cv2.imshow("Low Pass",np.hstack((img, lowpass)))

#teknik highpass
highPass = img - gaussBlur
cv2.imshow("high Pass",np.hstack((img, highPass)))

cv2.waitKey(0)
cv2.destroyAllWindows()