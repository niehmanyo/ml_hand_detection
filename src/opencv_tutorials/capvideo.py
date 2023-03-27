import cv2

cap = cv2.VideoCapture(0)

# 1. create window
cv2.namedWindow("video", cv2.WINDOW_AUTOSIZE)

while True:  # always capture img
    success, frame = cap.read()  # two return values
    cv2.imshow("video", frame)
    key = cv2.waitKey(0)
    print(key)
    if key == 'q':
        break

cap.release()
cv2.destroyAllWindows()

