#%%
import fnmatch, os, re
import glob
import math
import cv2
import numpy as np
import operator
from matplotlib import pyplot as plt

point = '.'
extension = 'jpg'
point_extension = '.'+ extension
tag = '_corners'

#%%
def preview(image):
    plt.imshow(image, cmap='gray'), plt.axis("off")
    plt.show()
#%%
def insensitive_glob(pattern):
    def either(c):
        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c
    return glob.glob(''.join(map(either, pattern)))

def main():
    for filename in insensitive_glob(os.path.join('data','*','*.{}').format(extension)): 
        if '.DS_Store' in filename or '_' in filename:
            continue
        image_bgr = cv2.imread(filename)
        image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
        image_gray = np.float32(image_gray)
        # Set corner detector parameters
        block_size = 4
        aperture = 19
        free_parameter = 0.04
        # Detect corners
        detector_responses = cv2.cornerHarris(image_gray, block_size, aperture, free_parameter)
        # Large corner markers
        detector_responses = cv2.dilate(detector_responses, None)

        # Only keep detector responses greater than threshold, mark as white
        threshold = 0.02
        image_bgr[detector_responses > threshold * detector_responses.max()] = [255,255,255]
        
        # Convert to grayscale
        image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
        # preview(image_gray)

        (name, ext) = filename.split('.')
        status = cv2.imwrite(name+tag+point_extension,image_gray)

#%%
if __name__ == '__main__':
    main()
    print('Corners photos successful!!!')

#%%