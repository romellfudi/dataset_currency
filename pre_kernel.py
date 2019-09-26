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
tag = '_kernel'

#%%
def preview(image):
    plt.imshow(image, cmap='gray'), plt.axis("off")
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
        image = cv2.imread(filename, )
        # Create kernel
        kernel = np.array([[0, -1, 0], 
                        [-1, 5,-1], 
                        [0, -1, 0]])
        image_sharp = cv2.filter2D(image, -1, kernel)
        # preview(image_sharp)

        (name, ext) = filename.split('.')
        status = cv2.imwrite(name+tag+point_extension,image_sharp)

#%%
if __name__ == '__main__':
    main()
    print('Kernel photos successful!!!')

#%%