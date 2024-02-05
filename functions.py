import cv2
import numpy as np
krnl = (np.ones((5,5),np.uint8))
img = cv2.imread("resources/Screenshot 2024-01-30 084417.png")

cv2.imshow("hello",img)
cv2.waitKey(0)

img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("hi",img2)
cv2.waitKey(0)

img3 = cv2.GaussianBlur(img,(5,11),5)

cv2.imshow("hi",img3)
cv2.waitKey(0)

img4 = cv2.dilate(img,krnl , iterations=1 )
cv2.imshow("hi",img4)
cv2.waitKey(0)

img5= cv2.erode(img,krnl,iterations = 2)
cv2.imshow("hi",img5)
cv2.waitKey(0)

