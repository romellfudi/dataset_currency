import os 

def rename(dir_): 
    i = 0
    for filename in os.listdir(dir_): 
        src_old = dir_+'/'+filename 
        src_new =dir_+'/'+dir_.replace(' ','_')+ '_'+filename 
        os.rename(src_old, src_new)
  
if __name__ == '__main__':       
    list_dir = ['Billetes 10','Billetes 20','Billetes 50','Billetes 100']
    map(list_dir,rename)