
function [Salida]=CinematicaDirec(V)
D=V;
D=transpose(D);
R=10;
assignin('base','R',R);
L=25;
assignin('base','L',L);
TT=100;
assignin('base','time',TT);
K=0.1705+0.0007;
assignin('base','K',K);
tau_2=0.6282+0.0018;
assignin('base','tau_2',tau_2);
tau_1=0.0448+0.0019;
assignin('base','tau_1',tau_2);
TimeValues=linspace(0,TT,100);
%DataValuesR=[5*ones(25,1);4*ones(25,1);-3*ones(25,1);0*ones(25,1)];
%DataValuesL=[3*ones(25,1);4*ones(25,1);3*ones(25,1);7*ones(25,1)];
DataValuesR=D(1:length(D),1);
DataValuesL=D(1:length(D),2);
VoltageWheelsRight = timeseries(DataValuesR,TimeValues);
assignin('base','VoltageWheelsRight',VoltageWheelsRight);
VoltageWheelsLeft = timeseries(DataValuesL,TimeValues);
assignin('base','VoltageWheelsLeft',VoltageWheelsLeft);
sim('Cinematica.slx');
XX = Pos_X.Data;
YY = Pos_Y.Data;
MX=max(XX)+1;
mX=min(XX)-1;
MY=max(YY)+1;
mY=min(YY)-1;
h = animatedline;
axis([mX,MX,mY,MY])
Salida=[XX,YY];
a = tic; % start timer
k=1;
while k <= length(XX)-1
    b = toc(a); % check timer
    if b > (1/30)
        addpoints(h,XX(k),YY(k));
        %addpoints(h,[XX(k)  0 ;  0 0 ], [0  0 ;0 YY(k)]);
        drawnow % update screen every 1/30 seconds
        a =tic; % reset timer after updating
        k=k+1;
    end
end
end
 