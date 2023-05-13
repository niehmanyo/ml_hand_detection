import cv2
import mediapipe as mp
import math
import time
import osascript
import pyautogui
import numpy as np

from HandAlgorithm import HandAlgorithm

"""
developer: niewenyu
"""


def controlKeyBoard():
    pyautogui.keyDown("command")
    pyautogui.keyDown("shift")
    pyautogui.press("L")
    pyautogui.keyUp("command")
    pyautogui.keyUp("shift")


class HandDetector():
    def __init__(self,
                 static_image_mode=False,
                 max_num_hands=1,
                 model_complexity=1,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5
                 ):
        self.mode = static_image_mode
        self.max_num_hands = max_num_hands  ## This project only need 1 hand to control
        self.model_complexity = model_complexity
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        """
        https://github.com/google/mediapipe/blob/master/mediapipe/python/solutions/hands.py
        """

        self.myHands = mp.solutions.hands  ## type = <class 'module'>
        self.hands = self.myHands.Hands(self.mode,
                                        max_num_hands,
                                        model_complexity,
                                        min_detection_confidence,
                                        min_tracking_confidence)
        self.myDraw = mp.solutions.drawing_utils

    def findHands(self, img):  # process the img and find the hand
        imgRGB = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                ## handLms.landmark is the 20 landmark of my finger
                distance = math.inf
                h, w, c = img.shape
                id_4 = [int(handLms.landmark[4].x * w), int(handLms.landmark[4].y * h)]
                id_8 = [int(handLms.landmark[8].x * w), int(handLms.landmark[8].y * h)]
                for id, lm in enumerate(handLms.landmark):
                    # print(id,lm)
                    # print(type(handLms.landmark))
                    h, w, c = img.shape  ##h = height.w = width, c = channel
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # print("4",id_4)
                    # print("8",id_8)
                    if (id == 4):
                        # id_4[0] = cx / 100
                        # id_4[1] = cy / 100
                        # print(id, cx, cy, id_4)
                        cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    if (id == 8):
                        # id_8[0] = cx / 100
                        # id_8[1] = cy / 100
                        # print(id, cx, cy, id_8)
                        # distance = math.sqrt(math.pow((id_4[0] - id_8[0]), 2) + math.pow((id_4[1] - id_8[1]), 2))
                        cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                        # if distance < 0.8:
                        #     cv2.circle(img, (cx,cy), 25, (255, 0, 255), cv2.FILLED)

                #     print("distance", distance)
                distance = math.dist(id_4, id_8)
                # print("distance",distance)


                #
                # if distance > 300:
                #     controlKeyBoard()

                x = pyautogui.size().width * handLms.landmark[0].x
                y = pyautogui.size().height * handLms.landmark[0].y
                pyautogui.moveTo(x,y)
                if distance < 30:
                    # set the volume
                    # volume = 100 / 260 * (distance - 20)
                    # osascript.osascript("set volume output volume " + str(volume))
                    pyautogui.mouseDown()
                else:
                    pyautogui.mouseUp()
                cv2.line(img, id_4, id_8, (255, 255, 255), 3)
                self.myDraw.draw_landmarks(img, handLms, self.myHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0):
        results = self.hands.process(img)


def main():
    preTime = 0
    cap = cv2.VideoCapture(0)
    hd = HandDetector()
    while True:
        curTime = time.time()
        success, img = cap.read()
        img = hd.findHands(img)
        frequency = 1 / (curTime - preTime)  # 这里能够先用后定义，可能是因为使用了cv2
        preTime = curTime
        cv2.putText(img, str(int(frequency)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
