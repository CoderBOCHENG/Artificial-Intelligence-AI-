import cv2
import numpy as np

img = cv2.imread('someshapes.png')
cv2.imshow('1. Orginal Image', img) #make a copy of the original image
cv2.waitkey(0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('2. gray image', gray_img)
cv2.waitkey(0)

edges = cv2.Canny(gray_img, 50,200)
cv2.imhshow('3. edges', edges)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(
    edges.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    approx = cv2.approxPoloDP(cnt,0.03*cv2.arcLength(cnt,True),True)#the program that can detect the shapes
    print(len(approx))

    if len(approx) == 3: #triangle (3 sides)
        shape = 'Triangle'
        M=cv2.moments(approx)
        cx = int(M['m10']/M['m00']
        cy = int(M['m01']/M['m00'] #the program can now identify shape as triangle
    elif len(approx) = 4: #shape with (4 sides)
        x,y,w,h = cv2.boundingRect(cnt)
        if abs(w-h) < 5:#if it is rectangle, width-height must be less than 5
            shape = 'Square'
            M=cv2.moments(approx)
            cx = int(M['m10']/M['m00']
            cy = int(M['m01']/M['m00']
        else:
            M=cv2.moments(approx)
            cx = int(M['m10']/M['m00']
            cy = int(M['m01']/M['m00']
    elif len(approx)= 10: #a star (10 sides)
        shape = 'Star'
        M=cv2.moments(approx)
        cx = int(M['m10']/M['m00']
        cy = int(M['m01']/M['m00']
    elif len(approx) == 8: #a circle
        shape = 'Circle'
        M=cv2.moments(approx)
        cx = int(M['m10']/M['m00']
        cy = int(M['m01']/M['m00']

    cv2.putText(img,shape,(cx-30. cy),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),1)
    cv2.drawingContours(img,cnt,-1,(0,255,0),2)
    cv2.imshow('cnt',img)
    cv2.waitkey(0) #set a time for the wait key


cv2.destroyAllWindows() #we do this because we created a lot of windows
        
