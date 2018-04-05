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
ColorSoldado = (143, 93, 214) #BGR
Color1 = (80, 232, 205) #BGR
Color2 = (113, 171, 246) #BGR



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
	cv2.imshow("Imagen filtrada",im_with_keypoints)
	cv2.waitKey(1)

	# Analisis de los Keypoints

	print("Se encontraron", len(keypoints), "blobs")

	if(len(keypoints)==3):

		DistanciaSoldado = 9999
		Distancia1 = 9999
		Distancia2 = 9999

		XSoldado = 0
		YSoldado = 0

		X1 = 0
		Y1 = 0

		X2 = 0
		Y2 = 0

		for key in keypoints:

			ColorActualAlSoldado = np.linalg.norm( imOriginal[int(keypoints[0].pt[1]), int(keypoints[0].pt[0])] - ColorSoldado )
			ColorActualAl1 = np.linalg.norm( imOriginal[int(keypoints[0].pt[1]), int(keypoints[0].pt[0])] - Color1 )
			ColorActualAl2 = np.linalg.norm( imOriginal[int(keypoints[0].pt[1]), int(keypoints[0].pt[0])] - Color2 )

			if ColorActualAlSoldado < DistanciaSoldado:
				DistanciaSoldado = ColorActualAlSoldado
				XSoldado = keypoints[0].pt[0]
				YSoldado = keypoints[0].pt[1]

			if ColorActualAl1 < Distancia1:
				Distancia1 = ColorActualAl1
				X1 = keypoints[0].pt[0]
				Y1 = keypoints[0].pt[1]

			if ColorActualAl2 < Distancia2:
				Distancia2 = ColorActualAl2
				X2 = keypoints[0].pt[0]
				Y2 = keypoints[0].pt[1]

		print("X_Soldado:",XSoldado,"Y_Soldado:",YSoldado,"X1:",X1,"Y1:",Y1,"X2:",X2,"Y2:",Y2)

	e2 = cv2.getTickCount()
	t = (e2 - e1)/cv2.getTickFrequency()
	print( t )
