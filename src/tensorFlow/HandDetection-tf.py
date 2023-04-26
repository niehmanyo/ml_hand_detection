import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.python.keras.models import load_model

# THE IMPORTANT THING
# some website use from tensorflow.keras.models import load_model

myHands = mp.solutions.hands
hands = myHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
myDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names','r')
classNames = f.read().split("\n")
f.close()
print(classNames)
