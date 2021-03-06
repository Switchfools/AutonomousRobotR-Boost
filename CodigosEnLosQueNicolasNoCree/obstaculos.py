import imageio
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
def Voro():
    M=500
    N=700
    Obstaculos=np.zeros([M,N])
    centros=np.zeros([M,N])
    Undos=list()
    Nodos=list()
    ConNodos=list()
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
    plt.savefig('voro.png')
    fig = plt.figure()
    plt.hold(True)
    # Mark the Voronoi vertices.

    for vpair in vor.ridge_vertices:
        uno,dos=vor.vertices[vpair[0]]
        tres,cuatro=vor.vertices[vpair[1]]
        if uno<M and uno>0 and dos<N and dos>0 and tres<M and tres>0 and cuatro<N and cuatro>0 :
            if(Obstaculos[int(uno),int(dos)]!=255 and Obstaculos[int(tres),int(cuatro)]!=255):
                ConNodos.append([vpair[0],vpair[1]])
                v0 = vor.vertices[vpair[0]]
                v1 = vor.vertices[vpair[1]]
                Nodos.append(v0)
                Nodos.append(v1)
                # Draw a line from v0 to v1.
                plt.plot([v0[0], v1[0]], [v0[1], v1[1]], 'k', linewidth=1)
    NNN=np.array(Nodos)
    plt.plot(NNN[:,0], NNN[:, 1], 'ko', ms=4)
    plt.savefig('realpath.png')
    lena,lenb=np.shape(vor.vertices)
    MAdyacencia=np.zeros([lena+2,lena+2],dtype=int)
    for i in range(len(ConNodos)):
        A,B=ConNodos[i]
        MAdyacencia[A,B]=1
        MAdyacencia[B,A]=1
    inicio=[40,40]
    final=[M-100,N-300]
    bestlenIn=10000
    bestlenEnd=10000
    for i in range(len(Nodos)):
        x,y=Nodos[i]
        reallenIn=np.sqrt((x-inicio[0])**2+(y-inicio[1])**2)
        reallenEnd=np.sqrt((x-final[0])**2+(y-final[1])**2)
        if(reallenIn<bestlenIn):
            bestlenIn=reallenIn
            posIn=Nodos[i]
        if(reallenEnd<bestlenEnd):
            bestlenEnd=reallenEnd
            posEnd=Nodos[i]
    for i in range(len(vor.vertices)):
        x,y=vor.vertices[i]
        if(posIn[0]==x and posIn[1]==y):
            MAdyacencia[0,i]=1
        if(posEnd[0]==x and posEnd[1]==y):
            MAdyacencia[i,0]=1
    Vertices=np.zeros([lena+2,2])
    for i in range(lena+2):
        if(i==0):
            Vertices[i,0]=inicio[0]
            Vertices[i,1]=inicio[1]
        elif(i!=0 and i!=lena+2):
            Vertices[i,0]=vor.vertices[i-2,0]
            Vertices[i,1]=vor.vertices[i-2,1]
        else:
            Vertices[i,0]=final[0]
            Vertices[i,1]=final[1]
    return(MAdyacencia,Vertices)
    #plt.figure()
    #plt.scatter(vor.ridge_vertices[:,0],vor.ridge_vertices[:,1])
    #plt.show()
    imageio.imwrite('obstaculos.png',Obstaculos)
Voro()
