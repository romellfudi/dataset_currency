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
tag = '_edges'

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
        image_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        
        median_intensity = np.median(image_gray)
        lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
        upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))

        image_canny = cv2.Canny(image_gray, lower_threshold, upper_threshold)
        # preview(image_canny)
        (name, ext) = filename.split('.')
        status = cv2.imwrite(name+tag+point_extension,image_canny)

#%%
if __name__ == '__main__':
    main()
    print('Edges photos successful!!!')

#%%