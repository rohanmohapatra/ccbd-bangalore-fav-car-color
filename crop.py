import os
import sys
from PIL import Image

# Function to crop the images
def crop(folder, fileName,k):
    fname,extension = os.path.splitext(fileName)
    filePath = os.path.join(folder, fileName)
    
    im = Image.open(filePath)
    # Cropped image starts from (20,20) to (50,40), starting from top-left corner
    im = im.crop((20,20,50,40))
    # resize the cropped image to 50px * 50px
    im = im.resize((int('50'),int('50')))
    # Saving the cropped image
    im.save("cropped"+"/"+"crop-"+str(k)+".png")

def bulkCrop(imageFolder):
    k=0;
    imgExts = ["png", "bmp", "jpg", "jpeg"]
    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            fname,extension = os.path.splitext(fileName)
            if(len(extension.split("."))>1):
                ext = extension.split(".")[1].lower()
            else:
                ext = extension.split(".")[0].lower()
            
            if ext not in imgExts:
                continue

            crop(path, fileName,k)
            k=k+1

if __name__ == "__main__":
    imageFolder='extracted-images/topview' # first arg is path to image folder
    bulkCrop(imageFolder)
