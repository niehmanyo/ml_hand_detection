import cv2
import mediapipe as mp
import math
import time
import osascript
import pyautogui

"""
developer: Nie Wenyu
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
                 ):
        self.mode = static_image_mode
        self.max_num_hands = max_num_hands  ## This project only need 1 hand to control

        """
        https://github.com/google/mediapipe/blob/master/mediapipe/python/solutions/hands.py
        """

        self.myHands = mp.solutions.hands  ## type = <class 'module'>
        self.hands = self.myHands.Hands(self.mode,
                                        max_num_hands,
                                        )
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
                    h, w, c = img.shape  ##h = height.w = width, c = channel
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    if (id == 4):
                        cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    if (id == 8):
                        cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

                distance = math.dist(id_4, id_8)

                x = pyautogui.size().width * handLms.landmark[0].x
                y = pyautogui.size().height * handLms.landmark[0].y
                pyautogui.moveTo(x, y)

                # set the volume
                # volume = 100 / 260 * (distance - 20)
                # osascript.osascript("set volume output volume " + str(volume))
                #     # pyautogui.mouseDown()
                # cv2.line(img, id_4, id_8, (255, 255, 255), 3)
                self.myDraw.draw_landmarks(img, handLms, self.myHands.HAND_CONNECTIONS)
        return img


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
