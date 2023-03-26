import cv2
import mediapipe as mp
import time
import autopy

cap = cv2.VideoCapture(0) ## Open camera

mpHands = mp.solutions.hands
hands = mpHands.Hands

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


    cv2.imshow("",img)
    cv2.waitKey(1)