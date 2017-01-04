import cv2
import numpy as np
import sys, os, time
import hsv
import datetime

os.system ("cls")

cap = cv2.VideoCapture(0)       # captura video en "cap"
print "espere..."
time.sleep(2) 
os.system ("cls")                  # espera 2 segundos (espera a que la camara obtenga los primeros fotogramas)
print "Ejecutando \nPrecione 'esc' para salir."
X = cap.get(3)                  # captura ancho y largo de la imagen (resolucion)
Y = cap.get(4)
C=0                             #Declaracion de variables
e=False
e1=False
print "ancho",X," alto",Y      # Imprime la resolucion obtenida por la camara

cv2.namedWindow("ventana1")     # Crea ventanas para futura referencia
cv2.namedWindow("mask")

hsv.createTbar("mask")

hsv.setTbar("mask",(179,168),(255,120),(255,0))

while(True):
    ret, frame = cap.read()                      # Recojemos fotograma a fotograma lo que hay en "cap"

    filt = hsv.getTbarMask(frame, "mask")
    
    res = cv2.bitwise_and(frame,frame, mask= filt)           #Toma del frame los pixeles encontrados por la mascara.

    cv2.line(frame,(550,0),(550,480),(255,0,0),2)            #Linea imaginaria para contar, color azul
    contours, hierarchy = cv2.findContours(filt.copy(), 1, 2)#Busca en una copia de la mascara los bordes, crea matrices.
    co=0
    for cnt in contours:                                     #por cada contorno encontrado, ejecuta el ciclo
           if np.size(cnt) > 80:                             #si el borde es mayor a 80 ejecuta el siguiente bloque
               x,y,w,h=cv2.boundingRect(cnt)                 #Busca los valores maximos de la altura y anchura (w,h)del borde encontrado, asi como su posicion en el frame (x,y)
               cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) #Dibuja un rectangulo con (x,y) como punto inicial, y (x+w,y+h) como final
               cx=x+w/2                                      # Calcula el centro del rectantulo dibujado
               cy=y+h/2
               cv2.circle(frame,(cx,cy),5,(0,0,255),-1)      #Dibuja un circulo en el centro del rectangulo
               cv2.putText(frame,str(cx)+"X ,"+str(cy)+"Y",(x,y-3), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1) #Imprime en el extremo superior del rectangulo
               co=co+1                                       #Cuenta objeto en pantalla y almacena en "co"          #las cordenadas del centro.

               if cv2.waitKey(1)&0xFF==ord("q"):                    #si se preciona "q", reinicia el conteo de objetos
                    C=0                                             
               if 555>cx>545:                                       #Si el centro del objeto encontrado se encuentra en las coorenadas x de la linea azul
                    cv2.line(frame,(550,0),(550,480),(255,255,0),3) #Cambia el color de la linea a azul celeste
                    e=True                                          
                    if e==True and e1==False:                       #Si e el verdadero y e1 falso
                        C=C+1                                       #Cuenta el objeto
               else:                                                #Las variables booleanas e y e1 se utilizan para evitar el conteo ciclado del objeto
                    e=False                                         
               e1=e


    cv2.putText(frame, "Contador:["+ str(C)+"]", (0, 15), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 0), 1)      #Imprime el numero de objetos que han cruzado por la linea  
    cv2.putText(frame, "Num. Objetos:["+ str(co)+"]", (0, 35), cv2.FONT_HERSHEY_SIMPLEX, .5, (0 ,0 , 0), 1)#Imprime el numero de objetos en pantalla                    

    cv2.putText(frame, str(datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')), (0,470), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 1) #relog
    
    cv2.imshow('mask',filt)        # Muetra la mascara (despues del filtrado) en la ventana "Mask"
    cv2.imshow('res',res)          # Muestra los pixeles tomados del fotograma dentro del area de la mascara, y muetralos en la ventana "res"
    cv2.imshow("ventana1", frame)  # Muestra el fotograma resulante
    key = cv2.waitKey(1)           #Rompe ciclo con "esc"
    if key == 27:  
      break

cap.release()                 #libera cap (apaga camara)
cv2.destroyAllWindows()       #cierra todas las ventanas
sys.exit()                    #salir del programa