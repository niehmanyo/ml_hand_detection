import torch
import matplotlib as plt
import numpy as np
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
img = "yolov5/data/images/zidane.jpg"
result = model(img)
# plt.imshow(np.squeeze(result.render()))
# plt.show()
print(result)