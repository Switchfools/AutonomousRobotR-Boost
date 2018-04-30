import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
def voro(img):
    M,N=np.shape(img)
    Obstaculos=np.zeros([M,N])
    centros=np.zeros([M,N])
    Undos=list()
    Nodos=list()
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
    for i in range(len(vor.vertices)):
        x,y=vor.vertices[i]
        if(abs(x)<M and abs(y)<N):
            if(Obstaculos[int(x),int(y)]!=255):
                Nodos.append([int(x),int(y)])
    return(Nodos)
