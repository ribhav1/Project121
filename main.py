import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)
image = cv2.imread('bg.jpg')

for i in range(60):
    ret, bg = video_capture.read()

while(video_capture.isOpened()):

    ret, frame = video_capture.read()

    if not ret: 
        break

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])

    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    f = frame - res
    f = np.where(f == 0, image, f)

    cv2.imshow('video', frame)
    cv2.imshow('mask', f)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()