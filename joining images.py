import cv2
import numpy as np


cap=cv2.VideoCapture(0)


while True: 
    success , img = cap.read()
    cv2.imshow("hi",img)
    krn= np.ones((5,5),np.uint8)
    print (krn)

    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img3 = cv2.GaussianBlur(img,(5,11),5)
    img4 = cv2.dilate(img,krn , iterations=1 )
    img5= cv2.erode(img,krn,iterations = 2)
       


    if cv2.waitkey(1) & 0xFF == ord ('q'):
        break