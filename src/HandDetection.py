import math

import mediapipe as mp
import time
import cv2

cap = cv2.VideoCapture(0)  ## Open camera

Hand = mp.solutions.hands
hands = Hand.Hands(max_num_hands=1)  ## For my project, I just need one hand
mpDraw = mp.solutions.drawing_utils

preTime = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            ## handLms.landmark is the 20 landmark of my finger
            distance = math.inf
            id_4 = [1, 1]
            id_8 = [500, 500]
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                # print(type(handLms.landmark))
                h, w, c = img.shape  ##h = height.w = width, c = channel
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                if (id == 4):
                    id_4[0] = cx / 100
                    id_4[1] = cy / 100
                    print(id, cx, cy, id_4)
                if (id == 8):
                    id_8[0] = cx / 100
                    id_8[1] = cy / 100
                    print(id, cx, cy, id_8)
                    distance = math.sqrt(math.pow((id_4[0] - id_8[0]), 2) + math.pow((id_4[1] - id_8[1]), 2))
                    if distance < 0.8:
                        cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

                print("distance", distance)
            mpDraw.draw_landmarks(img, handLms, Hand.HAND_CONNECTIONS)

    preTime = 0
    curTime = time.time()
    frequency = 1 / (curTime - preTime)  # 这里能够先用后定义，可能是因为使用了cv2
    preTime = curTime

    cv2.putText(img, str(int(frequency)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("", img)
    cv2.waitKey(1)
