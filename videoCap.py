import cv2
import time
cap= cv2.VideoCapture(0)
while(True):
    time.sleep(2)
    _,img = cap.read()
    cv2.imwrite('Documents\\'+ str(time.time())+ '.png',img)
    print("picture taken")