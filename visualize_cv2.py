# python visualize_cv2.py 0
import cv2
import numpy as np
import os
import sys
from mrcnn.model import MaskRCNN
from mrcnn.config import Config

ROOT_DIR = os.getcwd()
MODEL_DIR = os.path.join(ROOT_DIR, "logs")
COCO_MODEL_PATH = "mask_rcnn_peruvian_bill_0005.h5"

class InferenceConfig(Config):
    NAME = "PERUVIAN_BILL"
    NUM_CLASSES = 1 + 4
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    STEPS_PER_EPOCH = 100
    LEARNING_RATE = 0.0006

config = InferenceConfig()
config.display()

model = MaskRCNN( mode="inference", model_dir=MODEL_DIR, config=config )
model.load_weights(COCO_MODEL_PATH, by_name=True)
class_names = [ 'BG', 'B10','B100','B20','B50']

def random_colors(N):
    np.random.seed(1)
    colors = [tuple(255 * np.random.rand(3)) for _ in range(N)]
    return colors

colors = random_colors(len(class_names))
class_dict = { name: color for name, color in zip(class_names, colors) }

def apply_mask(image, mask, color, alpha=0.5):
    for n, c in enumerate(color):
        image[:, :, n] = np.where( mask == 1,
            image[:, :, n] * (1 - alpha) + alpha * c,
            image[:, :, n])
    return image

def display_instances(image, boxes, masks, ids, names, scores):
    n_instances = boxes.shape[0]

    if n_instances:
        assert boxes.shape[0] == masks.shape[-1] == ids.shape[0]

    for i in range(n_instances):
        if not np.any(boxes[i]):
            continue

        y1, x1, y2, x2 = boxes[i]
        label = names[ids[i]]
        color = class_dict[label]
        score = scores[i] if scores is not None else None
        caption = '{} {:.2f}'.format(label, score) if score else label
        mask = masks[:, :, i]

        image = apply_mask(image, mask, color)
        image = cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        image = cv2.putText( image, caption, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2 )

    return image

if __name__ == '__main__':
    capture = cv2.VideoCapture(0)

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    import time
    frame_rate = 10
    prev = 0
    while True:
        time_elapsed = time.time() - prev
        ret, frame = capture.read()
        if time_elapsed > 1./frame_rate:
            prev = time.time()
            results = model.detect([frame], verbose=0)
            r = results[0]
            frame = display_instances( frame, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])
        cv2.imshow('frame', frame)
        cv2.waitKey(60)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    capture.release()
    cv2.destroyAllWindows()
