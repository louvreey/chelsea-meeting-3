import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode = False, maxHands = 2, modelComplexity = 1, detectionConfidence = 0.5, trackConfidence = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity)
        self.mpDraw = mp.solutions.drawing_utils
        

def findHands(self, frame, draw = True):
    frameRGB = cv2.cvtcolor(frame, cv2.COLOR_BGR2RGB)
    self.results = self.hands.process(frameRGB) #selfhand di proses, disave di self results
    if self.results.multi_hand_landmarks: #dgn for loop, landmarks yg didetect digambar dgn method draw_landmarks()
        for handLms in self.results.multi_hand_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(frame, handLms, self.mphands.HAND_CONNECTIONS)
            return frame