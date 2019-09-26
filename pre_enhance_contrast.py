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
tag = '_contrast'

#%%
def preview(image):
    plt.imshow(image), plt.axis("off")
    plt.show()
#%%
def insensitive_glob(pattern):
    def either(c):
        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c
    return glob.glob(''.join(map(either, pattern)))

#%%
def main():
    for filename in insensitive_glob(os.path.join('data','*','*.{}').format(extension)): 
        if '.DS_Store' in filename or '_' in filename:
            continue
        image_bgr = cv2.imread(filename)
        
        # Convert to YUV
        image_yuv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YUV)
        # Apply histogram equalization
        image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])
        # Convert to RGB
    
        image_rgb = cv2.cvtColor(image_yuv,cv2.COLOR_BGR2RGB)

        # preview(image_yuv)
        # preview(image_rgb)
        (name, ext) = filename.split('.')
        status = cv2.imwrite(name+tag+point_extension,image_rgb)

#%%
if __name__ == '__main__':
    main()
    print('Enhance constrast Color photos successful!!!')

#%%