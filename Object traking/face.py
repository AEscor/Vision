import cv2
import numpy as np
import sys, os, time


os.system ("cls")

cap = cv2.VideoCapture(0)       
print "espere..."
time.sleep(2) 
#os.system ("cls")
print "Ejecutando \nPrecione 'esc' para salir."

eye = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
face = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')   

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eye.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)


    cv2.imshow("ventana1", frame) 
    key = cv2.waitKey(1)  
    if key == 27:  
      break

cap.release()              
cv2.destroyAllWindows()      
sys.exit()