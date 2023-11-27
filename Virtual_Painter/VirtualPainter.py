import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

detector = htm.handDetector(detectionConfidence = 0.85)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

myListDirectory = os.listdir("C:\Meeting_3_MediaPipe\Virtual_Painter\header")
print(myListDirectory)
overlayList = []

for imPath in myListDirectory:
    image = cv2.imread(f"C:\Meeting_3_MediaPipe\Virtual_Painter\header\{imPath}") 
    overlayList.append(image) 
    print(imPath)

print(overlayList)



header = overlayList[0]

while True:
    res, frame = cap.read()
    frame[0 : 125, 0 : 1280] = header
    frame = cv2.flip(frame, 1)
    frame = detector.findHands(frame)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()