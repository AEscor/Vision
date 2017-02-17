import cv2
import numpy as np
import sys, os, time
import datetime
import transform
from matplotlib import pyplot as plt 

os.system ("cls")

cap = cv2.VideoCapture(0)    
print "espere..."
time.sleep(2) 
os.system ("cls")                  
print "Ejecutando \nPrecione 'esc' para salir."

template = cv2.imread("C:\pyprog\Trycam\img3.png", 0)

cv2.namedWindow("ventana1")     # Crea ventanas para futura referencia
screenCnt = [0]

while(True):
    ret, frame = cap.read() 
    cframe = frame.copy()                   
    co=0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)


    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
 
    for c in cnts:

	    peri = cv2.arcLength(c, True)
	    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	    if len(approx) == 4:
		    screenCnt = approx
            co = co + 1
    
    cv2.drawContours(frame, [screenCnt], -1, (0, 255, 0), 2)
    cv2.putText(frame, "Matches:["+ str(co)+"]", (0, 15), cv2.FONT_HERSHEY_SIMPLEX, .5, ( 255, 255, 255), 1)
    cv2.putText(frame, str(datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')), (0,470), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 1) 
    

    warped = transform.four_point_transform(cframe, screenCnt.reshape(4, 2))
    cv2.imshow("target", warped)

    cv2.imshow("ventana1", frame)
    cv2.imshow("edged", edged)
    key = cv2.waitKey(1)     
    if key == 27:  
      break

cap.release()                 
cv2.destroyAllWindows()       
sys.exit()
