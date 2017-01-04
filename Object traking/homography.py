import cv2
import numpy as np
import sys, os, time
import datetime
from matplotlib import pyplot as plt 

os.system ("cls")

cap = cv2.VideoCapture(0)    
print "espere..."
time.sleep(2) 
os.system ("cls")                  
print "Ejecutando \nPrecione 'esc' para salir."
X = cap.get(3)                 
Y = cap.get(4)

print "ancho",X," alto",Y      

template = cv2.imread("C:\pyprog\Trycam\img3.png", 0)

cv2.namedWindow("ventana1")     # Crea ventanas para futura referencia
cv2.imshow("template", template)

orb = cv2.ORB()

while(True):
    ret, frame = cap.read()                    
    co=0
    kp1, des1 = orb.detectAndCompute(template, None)
    kp2, des2 = orb.detectAndCompute(frame, None)
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key = lambda x:x.distance)
    img3= cv2.drawMatches(template, kp1, frame, kp2, matches[:10], None, flags=2)

    cv2.putText(frame, "Matches:["+ str(co)+"]", (0, 15), cv2.FONT_HERSHEY_SIMPLEX, .5, ( 255, 255, 255), 1)
    cv2.putText(frame, str(datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')), (0,470), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 1) 
    cv2.show(img3), plt.show()
    cv2.imshow("ventana1", frame)
    key = cv2.waitKey(1)     
    if key == 27:  
      break

cap.release()                 
cv2.destroyAllWindows()       
sys.exit()                    