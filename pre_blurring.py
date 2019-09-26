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
tag = '_blurring'

#%%
def preview(image):
    plt.imshow(image, cmap='gray'), plt.xticks([]), plt.yticks([])
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
        image_blurry = cv2.blur(image, (5,5))
        # preview(image_blurry)
        (name, ext) = filename.split('.')
        status = cv2.imwrite(name+tag+point_extension,image_blurry)

#%%
if __name__ == '__main__':
    main()
    print('Blurring photos sucessful!!!')

#%%