import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# img = "yolov5/data/images/zidane.jpg"
# /Users/kobe/ml_hand_detection/yolov5/data/images/zidane.jpg
# result = model(img)
# plt.imshow(np.squeeze(result.render()))
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
