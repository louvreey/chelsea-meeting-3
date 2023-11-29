import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

detector = htm.handDetector(detectionConfidence=0.85)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

myListDirectory = os.listdir(
    "/Users/wincentbastian/Documents/timedoor/ai-dev-18c/chelsea-meeting-3/Virtual_Painter/header")
overlayList = []

print(myListDirectory)

for imPath in myListDirectory:
    image = cv2.imread(
        f"/Users/wincentbastian/Documents/timedoor/ai-dev-18c/chelsea-meeting-3/Virtual_Painter/header/{imPath}")
    overlayList.append(image)

header = overlayList[0]

while True:
    res, frame = cap.read()
    frame[0: 125, 0: 1280] = header
    frame = cv2.flip(frame, 1)
    print(frame)
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=True)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
