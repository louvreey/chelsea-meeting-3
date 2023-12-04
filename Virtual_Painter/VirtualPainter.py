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

drawColor = (0, 0, 255)
brushThickness = 7
eraserThickness = 40
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    res, frame = cap.read()
    frame[0: 125, 0: 1280] = header
    frame = cv2.flip(frame, 1)
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=True)
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
    fingers = detector.fingersUp()
    print(fingers)
    # if fingers[1] and fingers[2]:
    #     xp, yp = 0, 0
    #     print("SELECTION MODE")
    #     cv2.rectangle(frame, (x1, y1 - 25), (x2, y2 + 25),
    #                   drawColor, cv2.FILLED)
    #     if y1 < 125:
    #         if 320 < x1 < 480:
    #             header = overlayList[0]
    #             drawColor = (0, 0, 255)
    #         elif 480 < x1 < 630:
    #             header = overlayList[1]
    #             drawColor = (0, 255, 0)
    #         elif 630 < x1 < 840:
    #             header = overlayList[2]
    #             drawColor = (255, 0, 0)
    #         elif x1 < 1000:
    #             header = overlayList[3]
    #             drawColor = (0, 0, 0)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
