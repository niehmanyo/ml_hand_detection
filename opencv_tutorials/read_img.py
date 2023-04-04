import cv2

cv2.namedWindow("WindowName", cv2.WINDOW_AUTOSIZE)  # create a window
mat = cv2.imread("fingers.jpg", cv2.IMREAD_GRAYSCALE)  # read an image
print(type(mat))
cv2.imshow("img", mat)
key = cv2.waitKey(0)  ## 0 = always wait

if key == ord('q'):
    print("key == 'q'")
    cv2.destroyAllWindows()
