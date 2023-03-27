import cv2

# cv2.namedWindow("WindowName", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("name",0)

mat = cv2.imread("fingers.jpg",cv2.IMREAD_GRAYSCALE)
print(type(mat))