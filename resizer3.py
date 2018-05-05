import os
import sys
from PIL import Image

# Function to resize the image
def resize(folder, fileName,k):
    fname,extension = os.path.splitext(fileName)
    filePath = os.path.join(folder, fileName)
    
    im = Image.open(filePath)
    w, h  = im.size
    # Resizing to 500px * 288px
    newIm = im.resize((int('500'), int('288')))
    # Saving resized pictures
    newIm.save("resize/pics"+"/"+"test-"+str(k)+".png")

#This function calls resize() on every image in the folder
def bulkResize(imageFolder):
    k=449;
    imgExts = ["png", "bmp", "jpg", "jpeg"]
    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            print(len(files))
            fname,extension = os.path.splitext(fileName)
            if(len(extension.split("."))>1):
                ext = extension.split(".")[1].lower()
            else:
                ext = extension.split(".")[0].lower()
            if ext not in imgExts:
                continue

            resize(path, fileName,k)
            k=k+1

if __name__ == "__main__":
    imageFolder='dataset' # first arg is path to image folder
    bulkResize(imageFolder)
