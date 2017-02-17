import cv2
import numpy as np
import sys, os, time
import datetime

os.system ("cls")

cap = cv2.VideoCapture(0)       # captura video en "cap"
print "espere..."
time.sleep(2) 
os.system ("cls")                  # espera 2 segundos (espera a que la camara obtenga los primeros fotogramas)
print "Ejecutando \nPrecione 'esc' para salir."
X = cap.get(3)                  # captura ancho y largo de la imagen (resolucion)
Y = cap.get(4)

print "ancho",X," alto",Y      # Imprime la resolucion obtenida por la camara

template = cv2.imread("C:\Users\Programmer-A\Documents\GitHub\Vision\Tracking methods\img.png", 0)
template2 = cv2.imread("C:\Users\Programmer-A\Documents\GitHub\Vision\Tracking methods\img2.png", 0)
cv2.namedWindow("ventana1")     # Crea ventanas para futura referencia
cv2.imshow("template", template)
cv2.imshow("template2", template2)

while(True):
    ret, frame = cap.read()                      # Recojemos fotograma a fotograma lo que hay en "cap"
    co=0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)

    q, r = template2.shape[::-1]
    res2 = cv2.matchTemplate(gray, template2, cv2.TM_CCOEFF_NORMED)

    th = 0.8
    loc = np.where(res >= th)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0]+w, pt[1]+h),(0,255,0),2)
        co = co + 1
    loc2 = np.where(res2 >= th)
    for pt in zip(*loc2[::-1]):
        cv2.rectangle(frame, pt, (pt[0]+w, pt[1]+h),(255,0,0),2)
        co = co + 1

    cv2.putText(frame, "Matches:["+ str(co)+"]", (0, 15), cv2.FONT_HERSHEY_SIMPLEX, .5, ( 255, 255, 255), 1)#Imprime el numero de objetos en pantalla 
    cv2.putText(frame, "X", (0, 35), cv2.FONT_HERSHEY_SIMPLEX, .5, ( 0, 255, 0), 2)    
    cv2.putText(frame, "->", (0, 55), cv2.FONT_HERSHEY_SIMPLEX, .5, ( 255, 0, 0), 2)               
    cv2.putText(frame, str(datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')), (0,470), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 1) #relog
    
    cv2.imshow("ventana1", frame)  # Muestra el fotograma resulante
    key = cv2.waitKey(1)      #Rompe ciclo con "esc"
    if key == 27:  
      break

cap.release()                 #libera cap (apaga camara)
cv2.destroyAllWindows()       #cierra todas las ventanas
sys.exit()                    #salir del programa