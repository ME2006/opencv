import cv2

img = cv2.imread("resources/Screenshot 2024-01-30 084417.png")

video_path = r"C:\Users\moura\OneDrive\سطح المكتب\opencv\resources\YBOT2797.MP4"
vid = cv2.VideoCapture(0)
vid.set(40,60)
vid.set(20,100)
while True:
    success, frame = vid.read()

    if not success:
        break

    cv2.imshow("hi", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
