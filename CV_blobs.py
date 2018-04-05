import cv2
import numpy as np

# Iniciar comunicacion con la camara
capture = cv2.VideoCapture(0)
capture.set(3,1280)
capture.set(4,720)

# Crea el detector
params = cv2.SimpleBlobDetector_Params()
params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False
params.filterByArea = False
detector = cv2.SimpleBlobDetector_create(params)

# Color a buscar
Color1 = (80, 232, 205) #BGR
Color2 = (113, 171, 246) #BGR
ColorSoldado = (143, 93, 214) #BGR


while(True):

	e1 = cv2.getTickCount()

	# Leer imagen
	ret, imOriginal = capture.read()


	lower_red = np.array([18, 18, 101])
	upper_red = np.array([74, 74, 255])

	lower_1 = np.array([80, 170, 215])
	upper_1 = np.array([100, 190, 255])

	lower_2 = np.array([210, 130, 235])
	upper_2 = np.array([255, 190, 255])

	mask1 = cv2.inRange(imOriginal, lower_red, upper_red)
	mask2 = cv2.inRange(imOriginal, lower_1, upper_1)
	mask3 = cv2.inRange(imOriginal, lower_2, upper_2)


	MascaraCompleta = mask1 + mask2 + mask3


	im = cv2.bitwise_not(MascaraCompleta)

	im = cv2.medianBlur(im ,5)
	 
	# Detectar blobs.
	keypoints = detector.detect(im)
	 
	# Dibujar las detecciones en una nueva imagen (en rojo)
	im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	 
	# Muestra
	cv2.imshow("imagenfinal.jpg",im_with_keypoints)
	cv2.waitKey(1)

	# Analisis de los Keypoints

	print("Se encontraron ", len(keypoints), " blobs")

	if(len(keypoints)==3):

		x1 = int(keypoints[0].pt[1])
		y1 = int(keypoints[0].pt[0])

		x2 = int(keypoints[1].pt[1])
		y2 = int(keypoints[1].pt[0])

		x3 = int(keypoints[2].pt[1])
		y3 = int(keypoints[2].pt[0])

		print("X1:",x1,"Y1:",y1,"X2:",x2,"Y2:",y2,"X3:",x3,"Y3:",y3)

	e2 = cv2.getTickCount()
	t = (e2 - e1)/cv2.getTickFrequency()
	print( t )
