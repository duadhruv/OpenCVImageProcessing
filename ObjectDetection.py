import cv2
import numpy as np



#mg_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg')
#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('match.jpg',0)
w, h = template.shape[::-1]


cap=cv2.VideoCapture(1)


while(1):
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    #cv2.imshow('gray',gray)

    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

    cv2.imshow('Detected',frame)
    
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
