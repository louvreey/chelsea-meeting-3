import cv2
import numpy as np
import time
import os

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

myListDirectory = os.listdir("header")
# cv2.imshow(myListDirectory)
overlayList = []

for imPath in myListDirectory:
    image = cv2.imread(f'header/{imPath}')
    overlayList.append(image)

while True:
    res, frame = cap.read()
    cv2.imshow("Frame", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()