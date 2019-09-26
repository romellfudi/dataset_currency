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
tag = '_binarize'

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
        image_grey = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        
        max_output_value = 255
        neighorhood_size = 49
        subtract_from_mean = 10
        image_binarized = cv2.adaptiveThreshold(image_grey, 
                                                max_output_value, 
                                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                                cv2.THRESH_BINARY, 
                                                neighorhood_size, 
                                                subtract_from_mean)

        # preview(image_binarized)
        (name, ext) = filename.split('.')
        status = cv2.imwrite(name+tag+point_extension,image_binarized)

#%%
if __name__ == '__main__':
    main()
    print('Binarize photos successful!!!')

#%%