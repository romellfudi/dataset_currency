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
tag = '_rmbk'

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
        image_bgr = cv2.imread(filename)
        width, hight,_ = image_bgr.shape
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        padding = 70
        rectangle = (padding, padding, \
             width - padding, hight - padding)

        mask = np.zeros(image_rgb.shape[:2], np.uint8)

        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        cv2.grabCut(image_rgb, # Our image
                    mask, # The Mask
                    rectangle, # Our rectangle
                    bgdModel, # Temporary array for background
                    fgdModel, # Temporary array for background
                    5, # Number of iterations
                    cv2.GC_INIT_WITH_RECT) # Initiative using our rectangle

        mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
        image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]
        # preview(image_rgb_nobg)
        
        image_rgb = cv2.cvtColor(image_rgb_nobg,cv2.COLOR_BGR2RGB)

        (name, ext) = filename.split('.')
        status = cv2.imwrite(name+tag+point_extension,image_rgb)

if __name__ == '__main__':
    main()
    print('Remove Background photos successful!!!')

#%%