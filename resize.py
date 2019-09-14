import cv2
import os

dir_ = "images/"
output = 'images/'
width = 512
height = 512
dim = (width, height)
for filename in os.listdir(dir_): 
    if filename == '.DS_Store':
        continue
    img = cv2.imread(os.path.join(dir_,filename), cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(os.path.join(output,filename),resized)
cv2.destroyAllWindows()