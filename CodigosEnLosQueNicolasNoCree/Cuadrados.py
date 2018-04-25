import numpy as np
import cv2
import matplotlib.pyplot as plt

def find_squares(img):
	img = cv2.GaussianBlur(img, (5, 5), 0)
	squares = []
	for gray in cv2.split(img):
		for thrs in range(0, 255, 26):
			if thrs == 0:
				bin = cv2.Canny(gray, 0, 50, apertureSize=5)
				bin = cv2.dilate(bin, None)
			else:
				_retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
			bin, contours, _hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
			for cnt in contours:
				cnt_len = cv2.arcLength(cnt, True)
				cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
				if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
					cnt = cnt.reshape(-1, 2)
					max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in range(4)])
					if max_cos < 0.35:

						agregar = True

						for cuadrado in squares:

							Cuadrado1 = np.sort(cuadrado, axis=0)
							Cuadrado2 = np.sort(cnt, axis=0)

							distancia = np.linalg.norm(Cuadrado1-Cuadrado2)
							if distancia<20:
								agregar = False


						if agregar:
							squares.append(cnt)
	return squares

def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

cap = cv2.VideoCapture(0)

plt.show()


while True:

	ret, frame = cap.read()

	#frame = cv2.imread('Pista.jpg')

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower = np.array([160,78,180])
	upper = np.array([180,173,255])

	frame = cv2.inRange(frame, lower, upper)

	squares = find_squares(frame)

	frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

	cv2.drawContours( frame, squares, -1, (0, 0, 255), 2 )
	print("Cuadrados:", len(squares))
	cv2.imshow('squares', frame)
	ch = cv2.waitKey(1)
	if ch == 27:
		cv2.destroyAllWindows()

	plt.clf()
	plt.xlim((0, 1280))
	plt.ylim((0, 720))

	for a in squares:
		#plt.plot(np.concatenate([a[:,0],[a[0,0]]]), np.concatenate([a[:,1],[a[0,1]]]), color='red', alpha=0.8, linewidth=3, solid_capstyle='round', zorder=2)
		plt.fill(a[:,0], a[:,1] , edgecolor='r', fill=True)

	plt.draw()
	plt.pause(1e-17)



