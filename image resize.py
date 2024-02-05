import cv2
def mousepoint (event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print (x,y)




img = cv2.imread("resources/Screenshot 2024-01-30 084417.png")

cv2.imshow("hi",img)
cv2.waitKey(0)
print (img.shape)



cv2.setMouseCallback("eh",mousepoint)