import cv2
import numpy as np

car_cascade = cv2.CascadeClassifier("xmls/cars.xml")

start=0
imageFolder="Resized/topview/"

for i in range(start,47):
    imageAddress=imageFolder+"test-"+str(i)+".png"
    # Read the image
    frame=cv2.imread(imageAddress)
    # Convert to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Detect all the cars in the image
    cars=car_cascade.detectMultiScale(gray,1.009,12)

    carnum=1
    for (x,y,w,h) in cars:
        # Extract the cars from the image
        car=frame[y:y+h,x:x+w]
        newWidth = 60.0
        newHeight = 60 .0
        dim = (newHeight, newWidth)
        #Resize to 60px * 60px
        car = cv2.resize(car, dim, interpolation = cv2.INTER_AREA)
        # Save the cars so obtained
        cv2.imwrite('extracted-cars/topview/t-'+str(i)+'-'+str(carnum)+'.png',car)
        carnum+=1
