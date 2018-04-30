from scipy import misc
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
im = misc.imread('b.png', flatten=True)
def voro(cuadros, esquinas):
    Undos=list(cuadros)
    Undos.append(esquinas)
    Nodos=list()
    print(Undos)
    vor = Voronoi(Undos)
    voronoi_plot_2d(vor)
    plt.show()
    for i in range(len(vor.vertices)):
        x,y=vor.vertices[i]
        if(abs(x)<M and abs(y)<N):
            if(Obstaculos[int(x),int(y)]!=255):
                Nodos.append([int(x),int(y)])
    return(Nodos)
voro(im)
