import cv2
import time
cap= cv2.VideoCapture(0)
while(True):
    _,img = cap.read()
    cv2.imwrite('Documents\\'+ str(time.time())+ '.png',img)