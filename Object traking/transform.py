import numpy as np
import cv2

def order_pts(pts):
	# Se declaran los 4 puntos, y son inicializados en 0.
	rect = np.zeros((4, 2), dtype = "float32")

 	# Se encuentra la esquina superior izquierda [0] como la suma menor de los puntos x,y.
	# Se encuentra la esquina inferior derecha [2] como la suma mayor de los puntos x,y.
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
 	
	# Se encuentra la esquina superior derecha [1] como la diferencia menor los puntos x,y.
	# Se encuentra la esquina inferior izquierda [3] como la diferecia mayor de lo
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
 

	return rect