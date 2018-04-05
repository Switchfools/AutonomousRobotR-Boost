import numpy as np
import matplotlib.pylab as plt
import cv2
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    
    # Toma una foto por cada cuadro
    _, frame = cap.read()
    
    # me cambia el perfil de RGB a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # determino el rango de los azules permitidos en HSV
    lower_blue = np.array([160, 100, 100])
    upper_blue = np.array([179, 255, 255])
    
    # mascara para solo coger los colores azules
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask =cv2.medianBlur(mask ,5)
    res = cv2.bitwise_and(frame,frame, mask=mask)
    circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    if circles is None:
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        continue
    # ahora solo coge de la imagen original la parte que tiene la mascara.
    for i in circles[0,:]:
    # draw the outer circle
        cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),1)
    # draw the center of the circle
        cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    #cambio el valor de k a 27 si presiono la tecla ESC
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
