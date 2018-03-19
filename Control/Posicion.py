import numpy as np
#datos que se inicializan
AnguloRViejo=0
Xviejo=0
Yviejo=0
velocidad_AngularIzquierda=0
velocidad_AngularDerecha=0
RadioRuedas=(3.0/2)
SeparacionRuedas=13.0
#Las entradas son las velocidades que salen del control y las reales del robot
#se calculan con cada toma de datos, solo se necesita de entrada el numero de vueltas trasncurridas entre cada ejecución del codigo
def ControlPosicion(Xdeseado,Ydeseado,NumeroVueltasI,NumeroVueltasD):
    Desplazamiento_Izquierda=(2*np.pi*RadioRuedas)*(NumeroVueltasI)
    Desplazamiento_Derecha=(2*np.pi*RadioRuedas)*(NumeroVueltasD)
    Desplazamiento_Promedio=(Desplazamiento_Izquierda+Desplazamiento_Derecha)/2
    Rotación_Promedio=(Desplazamiento_Derecha-Desplazamiento_Izquierda)/(2*SeparacionRuedas)
    AnguloRobotNuevo=Rotación_Promedio+AnguloRViejo
    XRobotNuevo=Xviejo+(Desplazamiento_Promedio*np.cos(AnguloRobotNuevo))
    YRobotNuevo=Yviejo+(Desplazamiento_Promedio*np.sin(AnguloRobotNuevo))
    print('La posición Actual del Robot es','x',XRobotNuevo,'y',YRobotNuevo,'theta',AnguloRobotNuevo)

    #Ahora se Aplica el control, se necesita el desado para X,Y
    #ConstanteProporcional VelocidadLineal(Falta Sintonizar)
    K_pv=0.1
    #ConstanteProporcional VelocidadAngular(Falta Sintonizar)
    K_ph=0.1
    VelocidadControl=(K_pv)*np.sqrt((Xdeseado-XRobotNuevo)**2+(Yviejo-YRobotNuevo)**2)
    ThetaDesired=np.atan2((Yviejo-YRobotNuevo)/(Xdeseado-XRobotNuevo))
    AngularVelocity=K_ph*(ThetaDesired-AnguloRobotNuevo)
    #Estas dos cantidades se mandan al controlador del pwm de cada motor
    velocidad_AIzquierdaControl=((2*VelocidadControl)-(AngularVelocity*SeparacionRuedas))/(2*RadioRuedas)
    velocidad_ADerechaControl=((2*VelocidadControl)+(AngularVelocity*SeparacionRuedas))/(2*RadioRuedas)
    # de forma ideal se espera que el error sea aprrox a 0
    KI=0.3;
    KD=0.3;
    PWMI=KI*velocidad_AIzquierdaControl
    PWMD=KD*velocidad_ADerechaControl
    Error=np.sqrt((Xdeseado-XRobotNuevo)**2+(Ydeseado-YRobotNuevo)**2)
    return(PWMI,PWMD,Error)
    
    Xviejo=XRobotNuevo
    Yviejo=YRobotNuevo
    AnguloRViejo=AnguloRobotNuevo


