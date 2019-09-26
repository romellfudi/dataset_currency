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
tag = '_shi_corner'

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
        # Number of corners to detect
        corners_to_detect = 8
        minimum_quality_score = 0.15
        minimum_distance = 250

        # Detect corners
        corners = cv2.goodFeaturesToTrack(image_gray, 
                                        corners_to_detect, 
                                        minimum_quality_score,
                                        minimum_distance)
        corners = np.float32(corners)
        
        # Draw white circle at each corner
        for corner in corners:
            x, y = corner[0]
            cv2.circle(image_bgr, (x,y), 10, (255,255,255), -1)
            
        # Convert to grayscale
        image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
        # preview(image_gray)

        (name, ext) = filename.split('.')
        status = cv2.imwrite(name+tag+point_extension,image_gray)

#%%
if __name__ == '__main__':
    main()
    print('Shi Tomasi Corners photos successful!!!')

#%%