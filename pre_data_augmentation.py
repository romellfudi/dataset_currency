#%%
import fnmatch, os, re
import glob
import math
import cv2
import numpy as np
import operator
from matplotlib import pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, array_to_img
point = '.'
extension = 'jpg'
point_extension = '.'+ extension
tag = '_data_au{}_'

#%%
def preview(image):
    plt.imshow(image, cmap='gray'), plt.xticks([]), plt.yticks([])
    plt.show()
#%%
def insensitive_glob(pattern):
    def either(c):
        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c
    return glob.glob(''.join(map(either, pattern)))

#%%
def main():
    list_images = []
    IMG_DIM = (640, 480)
    for filename in insensitive_glob(os.path.join('data','*','*.{}').format(extension)): 
        if '.DS_Store' in filename or '_' in filename:
            continue
        list_images.append(filename)
    train_datagen = ImageDataGenerator(rescale=1./255, zoom_range=0.3, rotation_range=50,
                                   width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, 
                                   horizontal_flip=True, fill_mode='nearest')

    print(list_images)
    # val_datagen = ImageDataGenerator(rescale=1./255)
    # validation_imgs_scaled  = validation_imgs.astype('float32')
    # validation_imgs_scaled /= 255
    
    train_imgs = [img_to_array(load_img(img, target_size=IMG_DIM)) for img in list_images]
    train_imgs = np.array(train_imgs)
    train_imgs_scaled = train_imgs.astype('float32')
    train_imgs_scaled /= 255


    train_labels =['100','50','10','20']
    print(train_imgs.shape)

    bill_generator = train_datagen.flow(train_imgs, train_labels,
                                   batch_size=1)
    bill =  [next(bill_generator) for i in range(0,5)]
    fig, ax = plt.subplots(1,5, figsize=(15, 6))
    print('Labels:', [item[1][0] for item in bill])
    l = [ax[i].imshow(bill[i][0][0]),ax.set_yticks([]), plt.set_xticks([]) for i in range(0,5)]
    
                  
    history = model.fit_generator(train_generator, steps_per_epoch=100, epochs=100,
                                validation_data=val_generator, validation_steps=50, 
                                verbose=1) 
    
#%%
if __name__ == '__main__':
    main()
    print('Data Augmentation has been generated!!!')

#%%