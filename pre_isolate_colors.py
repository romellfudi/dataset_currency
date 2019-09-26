# %%
import fnmatch
import os
import re
import glob
import math
import cv2
import numpy as np
import operator
from matplotlib import pyplot as plt

point = '.'
extension = 'jpg'
point_extension = '.' + extension
tag = '_isolate'

# %%
def preview(image):
    plt.imshow(image), plt.axis("off")
    plt.show()
# %%


def insensitive_glob(pattern):
    def either(c):
        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c
    return glob.glob(''.join(map(either, pattern)))


def main():
    for filename in insensitive_glob(os.path.join('data', '*', '*.{}').format(extension)):
        if '.DS_Store' in filename or '_' in filename:
            continue
        image_bgr = cv2.imread(filename, cv2.IMREAD_COLOR)
        image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
        low = 7
        lower = np.array([low, low, low])
        limit = 40

        upper_red = np.array([limit, 255, 255])
        mask_red = cv2.inRange(image_hsv, lower, upper_red)

        upper_blue = np.array([255, limit, 255])
        mask_blue = cv2.inRange(image_hsv, lower, upper_blue)

        upper_green = np.array([255, 255, limit])
        mask_green = cv2.inRange(image_hsv, lower, upper_green)

        mask = cv2.bitwise_or(mask_green, mask_blue, mask_red)
        image_bgr_masked = cv2.bitwise_and(image_bgr, image_bgr, mask=~mask)

        image_rgb = image_bgr_masked
        # image_rgb =  cv2.cvtColor(image_bgr_masked, cv2.COLOR_BGR2RGB)
        # preview(image_rgb)
        (name, ext) = filename.split('.')
        status = cv2.imwrite(name+tag+point_extension, image_rgb)
        image_rgb[np.where((image_rgb == [0, 0, 0]).all(axis=2))] = [ 255, 255, 255]
        # preview(image_rgb)
        status = cv2.imwrite(name+tag+'2'+point_extension, image_rgb)


#%%
if __name__ == '__main__':
    main()
    print('Isolate photos successful!!!')

# %%
