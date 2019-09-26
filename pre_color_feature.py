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
        image_rgb = cv2.imread(filename, cv2.IMREAD_COLOR)
        channels = cv2.mean(image_rgb)
        observation = np.array([(channels[2], channels[1], channels[0])])
        preview(image_rgb)
        preview(observation)

#%%
if __name__ == '__main__':
    main()
    print('Color feature successful!!!')

#%%