
import mediapipe as mp
import time
import cv2
cap = cv2.VideoCapture(0)  ## Open camera
preTime = 0

while True:
    success, img = cap.read()

    curTime = time.time()
    frequence = 1 / (curTime - preTime)  # 这里能够先用后定义，可能是因为使用了cv2
    preTime = curTime
    
    cv2.putText(img,str(int(frequence)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("", img)
    cv2.waitKey(1)



