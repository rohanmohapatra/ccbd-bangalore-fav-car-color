#import important libraries
import os
import sys
from PIL import Image

#resize function
def resize(folder, fileName,k):
    fname,extension = os.path.splitext(fileName)
    filePath = os.path.join(folder, fileName)
    #open image
    im = Image.open(filePath)
    w, h  = im.size
    newIm = im.resize((int('500'), int('288'))) #resizeimage
    #saving to another folder
    newIm.save("D:/Study/CCBD/Assignment/resize/pics"+"/"+"test-"+str(k)+".png")


#bulk resize which calls helper resizefunction
def bulkResize(imageFolder):
    k=0;
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

#main code to run
if __name__ == "__main__":
    imageFolder='D:/Study/CCBD/Assignment/original' # first arg is path to image folder
    bulkResize(imageFolder) #to process and resize
