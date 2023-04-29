import numpy as np
import mediapipe as mp


class HandAlgorithm():
    def __init__(self):
        self.gestures = [[0, 0, 0, 0, 0],  # 0
                         [0, 1, 0, 0, 0],  # 1
                         [0, 1, 1, 0, 0],  # 2
                         [0, 1, 1, 1, 0],  # 3
                         [0, 1, 1, 1, 1],  # 4
                         [1, 1, 1, 1, 1],  # 5
                         [1, 0, 0, 0, 1],  # 6
                         [1, 1, 0, 0, 1],  # 7
                         [1, 1, 0, 0, 0]]  # 8
        self.fingerIndex = [4, 8, 12, 16, 20]  # all finger indexes
        # [THUMB_TIP，INDEX_FINGER_TIP,MIDDLE_FINGER_TIP,RING_FINGER_TIP,PINKY_TIP]

    def determineGesture(self, handLms):
        # compare the y
        ans = []
        for id in self.fingerIndex:
            if id == 4:
                if handLms.landmark[id].y < handLms.landmark[5].y:
                    ans.append(1)
                else:
                    ans.append(0)
            else:
                if handLms.landmark[id].y < handLms.landmark[id - 2].y:
                    ans.append(1)
                else:
                    ans.append(0)

        print(ans)
        for id in range(self.gestures.__len__()):
            if ans == self.gestures[id]:
                return id
        return -1
