'''
Apply k-means clustering on each image
to perform colour quantization.
k=4
Result: image reconstructed using 4 most prominent colours in that image.
'''

import os
import sys
import cv2
import numpy as np

def quantize(folder, fileName,k):
    # get the file name and extension
    fname,extension = os.path.splitext(fileName)
    filePath = os.path.join(folder, fileName)

    #read image
    img = cv2.imread(filePath)
    Z = img.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 4
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))


    # Save quantized image
    cv2.imwrite("quantized"+"/"+"q-"+str(k)+".png",res2)

def bulkQuantize(imageFolder):
    k=0;
    imgExts = ["png", "bmp", "jpg", "jpeg"]

    #Go through the folder and call quantize function for each image
    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            print(fileName)
            fname,extension = os.path.splitext(fileName)
            if(len(extension.split("."))>1):
                ext = extension.split(".")[1].lower()
            else:
                ext = extension.split(".")[0].lower()
            if ext not in imgExts:
                continue

            quantize(path, fileName,k)
            k=k+1

if __name__ == "__main__":
    imageFolder='cropped' # first arg is path to image folder
    bulkQuantize(imageFolder)
