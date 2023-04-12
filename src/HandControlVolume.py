import HandDetectionModule as hdm
import cv2


h = hdm.HandDetector()

cap = cv2.VideoCapture(0)

while True:
    sucess, img = cap.read()
    img = h.findHands(img)
    cv2.putText(img,"asd",(20,50),cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("asd",img)
    cv2.waitKey(1)
