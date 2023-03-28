
import mediapipe as mp
import time
import cv2
cap = cv2.VideoCapture(0)  ## Open camera

Hand = mp.solutions.hands
hands = Hand.Hands()
mpDraw = mp.solutions.drawing_utils

preTime = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_RGBA2BGR)

    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms)

    curTime = time.time()
    frequence = 1 / (curTime - preTime)  # 这里能够先用后定义，可能是因为使用了cv2
    preTime = curTime

    cv2.putText(img,str(int(frequence)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("", img)
    cv2.waitKey(1)



