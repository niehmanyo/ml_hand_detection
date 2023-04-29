import cv2
import numpy as np
import mediapipe as mp

model = tf.keras.models.load_model('mp_hand_gesture')
myHands = mp.solutions.hands
hands = myHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
myDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split("\n")
f.close()
print(classNames)
