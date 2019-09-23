#%%
from sklearn.linear_model import LogisticRegression
import pickle
#%%
filename_model = 'peru_bills_LogisticRegression_multi_class.pickle'
#%%
# loaded_model = joblib.load(filename)
with open(filename_model, 'rb') as handle:
    loaded_model = pickle.load(handle)
print(loaded_model)

#%%
import cv2
IMG_SIZE = 100
def process_data(path=None):
    img_array = cv2.imread(path,cv2.IMREAD_GRAYSCALE)  
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    standarize_array = new_array/255.0
    return loaded_model.predict(standarize_array.reshape(1,IMG_SIZE * IMG_SIZE))[0]
    
#%%
process_data('data/Billetes 10/P9030002.JPG') 

#%%
process_data('data/Billetes 20/P9030077.JPG')    

#%%
process_data('data/Billetes 100/P9030129.JPG')    

#%%
process_data('data/Billetes 50/P9030128.JPG')    

#%%
