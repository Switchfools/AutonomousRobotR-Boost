import imageio
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
M=500
N=700
Obstaculos=np.zeros([M,N])
centros=np.zeros([M,N])
Undos=list()
Nodos=list()
for i in range(int(M/2 - 50),int(M/2 + 50)):
    for j in range(int(N/2 - 50),int(N/2 + 50)):
        Obstaculos[i,j]=255
for i in range(int(M/2 - 200),int(M/2 - 150)):
    for j in range(int(N/2 - 50),int(N/2 + 50)):
        Obstaculos[i,j]=255
for i in range(int(M/2 - 200),int(M/2 - 150)):
    for j in range(int(N/2 - 200),int(N/2 - 150)):
        Obstaculos[i,j]=255
for i in range(int(M - 200),int(M - 150)):
    for j in range(int(N - 200),int(N- 150)):
        Obstaculos[i,j]=255
for i in range(int(M - 50),int(M-25)):
    for j in range(int(N/2 - 100),int(N/2 + 50)):
        Obstaculos[i,j]=255
for i in range(M):
    Obstaculos[i,0:10]=255
    Obstaculos[i,N-10:N]=255
for i in range(N):
    Obstaculos[0:10,i]=255
    Obstaculos[M-10:M,i]=255
for i in range(1,M-1):
    for j in range(1,N-1):
        Med=Obstaculos[i+1,j]+Obstaculos[i+1,j+1]+Obstaculos[i+1,j-1]+Obstaculos[i,j+1]+Obstaculos[i,j-1]+Obstaculos[i-1,j]+Obstaculos[i-1,j+1]+Obstaculos[i-1,j-1]
        if(Obstaculos[i,j]==255 and (Med==3*(255)or Med==7*(255))):
            Undos.append([i,j])
            for l in range(i-1,i+1):
                for m in range(j-1,j+1):
                    centros[i,j]=255
vor = Voronoi(Undos)
voronoi_plot_2d(vor)
plt.show()
print(vor.vertices)
'''
for i in range(len(vor.vertices)):
    x,y=vor.vertices[i]
    print(x,y)
    if(Obstaculos[int(x),int(y)]!=255):
        Nodos.append(int(x),int(y))
print(Nodos)
'''
imageio.imwrite('obstaculos.png',centros)
