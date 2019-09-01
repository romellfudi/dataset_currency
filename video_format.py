import cv2
import numpy as np
import os
import sys
import time
capture = cv2.VideoCapture('videofile.mp4')
frameCount = 0
start_time = time.time()
capture_duration = 2
print(capture.get(cv2.CAP_PROP_FPS))
while( int(time.time() - start_time) < capture_duration ):
    cv2.waitKey(220)
    ret, frame = capture.read()
    frameCount = frameCount+1

print('Total frames: ',frameCount)
