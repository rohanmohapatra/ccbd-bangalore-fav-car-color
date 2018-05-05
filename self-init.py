print(__doc__)
import shutil
from time import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

import sys
import os
from PIL import Image

file_names=[]
newpath = 'self-init/'
n_digits = 27 #no of clusters

# delete cluster folders if they already exist
for i in range(n_digits):
    if os.path.exists(newpath+str(i)):
        shutil.rmtree(newpath+str(i))
# make new folders, one per cluster
for i in range(n_digits):
    os.makedirs(newpath+str(i))


# opening the image
im=Image.open("quantized/q-0.png")
shape=np.array(im).shape
print(shape)

def process_directory(directory):
    '''Returns an array of feature vectors for all the image files in a
    directory (and all its subdirectories). Symbolic links are ignored.

    Args:
      directory (str): directory to process.

    Returns:
      list of list of float: a list of feature vectors.
    '''
    training = []
    for root, _, files in os.walk(directory):
        index=0
        for file_name in files:
            # if condition is to find indices of the centroids
            if file_name in ['q-864.png','q-486.png','q-1003.png','q-326.png','q-674.png','q-943.png','q-675.png','q-555.png','q-487.png','q-854.png','q-282.png','q-938.png','q-66.png','q-7.png','q-743.png','q-81.png','q-156.png','q-562.png','q-767.png','q-1022.png','q-1069.png','q-765.png','q-673.png','q-610.png','q-118.png','q-72.png','q-37.png','q-827.png','q-1058.png','q-719.png','q-58.png','q-673.png','q-765.png']:
                print(file_name+': '+str(index))
            index+=1
            file_names.append(file_name)          
            file_path = os.path.join(root, file_name)
            img_feature = process_image_file(file_path)
            
            training.append(img_feature)
    return training

def process_image_file(image_path):
    '''Given an image path it returns its feature vector.

    Args:
      image_path (str): path of the image file to process.

    Returns:
      list of float: feature vector on success, None otherwise.
    '''
    try:
        image = Image.open(image_path)
        return process_image(image)
    except IOError:
        return None

def process_image(image):
    '''Given a PIL Image object it returns its feature vector.

    Args:
      image (PIL.Image): image to process.
      blocks (int, optional): number of block to subdivide the RGB space into.

    Returns:
      list of float: feature vector if successful. None if the image is not
      RGB.
    '''
    arr = np.array(image)
    flat_arr = arr.ravel()
    return flat_arr





np.random.seed(42)
initial_data = np.array(process_directory("quantized"))

n_samples, n_features = initial_data.shape

sample_size = 300

print("n_digits: %d, \t n_samples %d, \t n_features %d"
      % (n_digits, n_samples, n_features))


print(82 * '_')

# Initialise the centroids
startpts=np.array([initial_data[650],initial_data[382],initial_data[771],initial_data[103],initial_data[890],initial_data[67],initial_data[770],initial_data[719],initial_data[821],initial_data[79],initial_data[28],initial_data[823],initial_data[596],initial_data[145],initial_data[871],initial_data[797],initial_data[1013],initial_data[704],initial_data[748],initial_data[285],initial_data[512],initial_data[588],initial_data[721],initial_data[334],initial_data[7],initial_data[194],initial_data[692]])
# Use kmeans to cluster the images
kmeans = KMeans(init=startpts, n_clusters=n_digits, n_init=1) 
kmeans.fit(initial_data)


# Find how images are clustered. Use last trained model.
Z = kmeans.predict(initial_data)

# Save the clustered images in respective folders.
for i in range(len(Z)):
    folder=Z[i]
    flat_image=np.matrix(initial_data[i])
    arr2=np.asarray(flat_image).reshape(shape)
    img=Image.fromarray(arr2,'RGB')
    img.save("self-init/"+str(folder)+"/"+file_names[i])
