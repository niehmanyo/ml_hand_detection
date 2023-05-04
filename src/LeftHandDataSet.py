import cv2
import numpy as np
import mediapipe as mp

Hand = mp.solutions.hands
hands = Hand.Hands(max_num_hands=1)  ## For my project, I just need one hand
mpDraw = mp.solutions.drawing_utils
for i in range(1, 4):
    file = "left-direction/" + str(i) + ".jpg"
    img = cv2.imread(file)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            ## handLms.landmark is the 20 landmark of my finger
            h, w, c = img.shape
            for id, lm in enumerate(handLms.landmark):
                print(id, lm.x * w, lm.y * h)
        print("*" * 50)
    mpDraw.draw_landmarks(img, handLms, Hand.HAND_CONNECTIONS)
    cv2.putText(img, "", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("", img)
    cv2.waitKey(0)

