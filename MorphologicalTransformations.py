import cv2
import numpy as np


cap=cv2.VideoCapture(1)

while(1):
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_col=np.array([100,100,20])
    upper_col=np.array([255,255,210])

    mask=cv2.inRange(hsv,lower_col,upper_col)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    kernel=np.ones((2,2),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations=1)

    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)    
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)

    cv2.imshow('opening',opening)

    cv2.imshow('closing',closing)

    

    k=cv2.waitKey(5) & 0XFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
