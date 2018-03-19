function[x,y,Errorx,Errory,angulo] = Controlador(xi,yi,anguloi,xd,yd,tiempo,R,L)
V=zeros(1,tiempo);
W=zeros(1,tiempo);
k=0.1075+0.0003;    
t1=0.0448+0.0018;
t2=0.6282+0.0014;
y=zeros(1,tiempo);
x=zeros(1,tiempo);
tf1=tf(k,[t1*t2 t1+t2 1]);
angulo=zeros(1,tiempo);
Errorx=1;
Errory=1;
i=1;
Kv= 3.15;
Kw= 15;
vr=zeros(1,tiempo);
vl=zeros(1,tiempo);
while  i<=tiempo
 t= linspace(0,i,tiempo);
    if i==1      
      x(i)=xi;       
      y(i)=yi;
      angulo(i)=anguloi;
  else
      
      anguloE=atan((yd-y(i-1))/(xd-x(i-1)));
      V(i)=Kv*sqrt((xd-x(i-1))^2 + (yd-y(i-1))^2);
      W(i)=Kw*(anguloE-angulo(i-1));
      
      vr(i)= (V(i)/R) + W(i)/2*R;
      vl(i)= (V(i)/R) - W(i)/2*R;     
    
      [wr,o]=lsim(tf1,[vr(i-1), vr(i)],[t(i-1), t(i)]);    
      [wl,p]=lsim(tf1,[vl(i-1), vl(i)],[t(i-1), t(i)]);
      angulo(i)= angulo(i-1) + (R/L*(wr(2)-wl(2)));
      x(i)= x(i-1) + (R/2 * (wr(2)+wl(2))*cos(angulo(i)));
      y(i)= y(i-1) + (R/2 * (wr(2)+wl(2))*sin(angulo(i)));
     
      

   end
Errorx= abs(xd-x(i));
Errory= abs(yd-y(i));
i=i+1;
end

end