import cv2
import numpy as np
img = np.zeros((500,500,3),np.uint8)
cv2.line(img,(0,0),(250,500),(340,800,700),30)
cv2.line(img,(500,0),(250,500),(340,800,700),30)
cv2.line(img,(30,0),(250,400),(340,800,700),30)
cv2.line(img,(488,0),(250,400),(340,800,700),30)
cv2.line(img,(250,500),(250,-500),(340,800,700),30)
cv2.imshow("hi",img)
cv2.waitKey(0)