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
tag = '_contrast_gray'

#%%
def preview(image):
    plt.imshow(image,cmap='gray'), plt.axis("off")
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
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        image_enhanced = cv2.equalizeHist(image)
        # preview(image_enhanced)
        (name, ext) = filename.split('.')
        status = cv2.imwrite(name+tag+point_extension,image_enhanced)

#%%
if __name__ == '__main__':
    main()
    print('Enhance constrast Gray photos successful!!!')

#%%