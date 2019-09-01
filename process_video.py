import cv2
import numpy as np
from visualize_cv2 import model, display_instances, class_names

capture = cv2.VideoCapture('videofile.mp4')
size = (
    int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
)
codec = cv2.VideoWriter_fourcc(*'DIVX')
fps = capture.get(cv2.CAP_PROP_FPS)
output = cv2.VideoWriter('videofile_masked.avi', codec, fps, size)
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count/fps
minutes = int(duration/60)
seconds = duration%60

print('fps = ' + str(fps))
print('number of frames = ' + str(frame_count))
print('duration (S) = ' + str(duration))
print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret:
        results = model.detect([frame], verbose=0)
        r = results[0]
        frame = display_instances(
            frame, r['rois'], r['masks'], r['class_ids'], class_names, r['scores']
        )
        output.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()

print('The video was processed')
