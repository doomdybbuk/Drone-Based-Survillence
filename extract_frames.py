import cv2
import os

videocap = cv2.VideoCapture("C:/Users/Manan Niklank Jain/Downloads/random.mp4")
success, image = videocap.read()
count =0
while videocap.isOpened():
    success, image = videocap.read()
    cv2.imwrite("C:/Users/Manan Niklank Jain/OneDrive/Desktop/Drone Based Survillence/video_frames/%d.png" %count,image)
    count += 1
# https://youtu.be/r1EXdcZd6SQ?feature=shared