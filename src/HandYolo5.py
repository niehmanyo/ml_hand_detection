import torch

model = torch.hub.load("ultralytics/yolov5","yolov5s")

img = "../VOCData/images/1.png"

result = model(img)

print(result)