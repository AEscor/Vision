import cv2
import numpy as np

def createTbar(win):
	def nothing(x):
		pass
	cv2.createTrackbar('H', win ,0,179,nothing) # Trackbar, ajuste de valores HSV (Hue, Saturation, Value)
	cv2.createTrackbar('h', win ,0,179,nothing) # H,D,V para valores maximos, h,s,v para valores minimos
	cv2.createTrackbar('S', win ,0,255,nothing)
	cv2.createTrackbar('s', win ,0,255,nothing)
	cv2.createTrackbar('V', win ,0,255,nothing)
	cv2.createTrackbar('v', win ,0,255,nothing)

def setTbar(win,(A,a),(B,b),(C,c)):
	cv2.setTrackbarPos('H', win , A)          # valores por "default"
	cv2.setTrackbarPos('h', win , a)
	cv2.setTrackbarPos('S', win , B)
	cv2.setTrackbarPos('s', win , b)
	cv2.setTrackbarPos('V', win , C)
	cv2.setTrackbarPos('v', win , c)

def  getTbarMask(frame, win):

	kernel = np.ones((5,5),np.uint8)

	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	H = cv2.getTrackbarPos('H', win)           # Muestra las trackbar en la ventana "mask"
	h = cv2.getTrackbarPos('h', win)
	S = cv2.getTrackbarPos('S', win)
	s = cv2.getTrackbarPos('s', win)
	V = cv2.getTrackbarPos('V', win)
	v = cv2.getTrackbarPos('v', win)

	mincolor=np.array([h,s,v])                   # Rango maximo y minimo para buscar color, se almacenan en arrays
	maxcolor=np.array([H,S,V])

	ran = cv2.inRange(hsv, mincolor, maxcolor)  # Se buscan los pixeles que esten dentro del rango dictado por mincolor y maxcolor y crea una mascara.
	flt1 = cv2.morphologyEx(ran, cv2.MORPH_OPEN, kernel) # Se filtra la mascara obtenida.
	flt2 = cv2.morphologyEx(flt1, cv2.MORPH_CLOSE, kernel)
	
	return flt2