import cv2
from imutils.object_detection import non_max_suppression
from imutils import resize #object detection 
import numpy as np #number calculation

hog = cv2.HOGDescriptor()#person description eg the head, arms, body
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

img = cv2.imread('people5.jpg') # image of file
img = resize(img,height=500)#eveytime find  person, recreate img around him/her

rects,weights = hog.detectMultiScale(img,winStride=(4,4),padding=(8,8),scale=1.05)
copy = img.copy()#we want to copy the image

for x,y,w,h in rects: #x and y coordinates to find where person is on the photo

    cv2.rectangle(copy,(x,y),(x+w,y+h),(0,0,255),2) #scale change to 255
#allows us to edit the photo

cv2.imshow('before suppression',copy)
#to know which img is 1st/2nd
cv2.waitKey(0) #press 0 to stop or refresh photo (eg 1st person....)

r = np.array([[x,y,x+w,y+h] for x,y,w,h in rects])
#width, height(which is length), of the person
#w is how fat/skinny you are

pick = non_max_suppression(r,probs=None,overlapThresh=0.65)
#prob shappe to find out which shape we want
#if person size is less than 0.65%, will not be considered a human
# if the person is blocked or disfigured or missing parts in body, still is human


for xa,ya,xb,yb in pick:
    cv2.rectangle(img,(xa,ya),(xb,yb),(0,255,0),2)

cv2.imshow('after suppression',img) # show the image
cv2.waitKey(0)

cv2.destroyAllWindows() #delete all the unesssacery windows
