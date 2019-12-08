#Import libraries
import numpy as np
from math import *
import matplotlib.pyplot as mpl

print('Trajectory of a Projectile')
H= float(input('Enter the initial height of the projectile above the ground in meters: '));
V= float(input('Enter the magnitude of the velocity in m/s: '));
th= float(input('Enter the angle in degrees with respect to the positive x-axis at which the projectile is fired: '));
Ax= float(input('Enter the x-component of the acceleration in m/s^2 (include the sign): '));
Ay= float(input('Enter the y-component of the acceleration in m/s^2 (include the sign): '));
#cox(x) and sin(x) are in radian mode 
#to get the value of cos(x) and sin(x) in degree mode the angle must be converted to radians
Vx=(V*(cos(radians(th))))
Vy=(V*(sin(radians(th))))

#For ideal trajectory, gravity is the only force acting on the object
#lists that will save XI and YI values as function of time
g=-9.8
YIvalues=[]
XIvalues=[]
i=0
if V==0:
    raise ValueError('The velocity cannot be zero. The object must be moving')
elif H<0:
    raise ValueError('Height must be above the reference point which is the ground')
elif V<0:
    raise ValueError('Magnitude of velocity cannot be negative')
elif (th<0) or (th>180):
    raise ValueError('Angle must not be less than 0 degrees and must not exceed 180 degrees')
elif H==0:
    t=float(abs((-(Vy)-(((Vy**2)-4*(.5*(g))*(-H))**(1/2)))/(2*(.5*g))))
    while i<=t:
        YI=H+(Vy*i)+((.5)*(g)*(i**2))
        XI=(Vx*i)
        #add new XI and YI values to the list
        YIvalues.append(YI)
        XIvalues.append(XI)
        i=i+0.001
else:
    tt=float(abs((Vy/g)-abs((((Vy**2)/(g**2))-((2*H)/(g)))**(1/2))))
    while i<=tt:
        YI=H+(Vy*i)+((.5)*(g)*(i**2))
        XI=(Vx*i)
        #add new XI and YI values to the list
        YIvalues.append(YI)
        XIvalues.append(XI)
        i=i+0.001
        
mpl.subplot(1,2,2)
mpl.plot(XIvalues,YIvalues)
mpl.title('Ideal Trajectory')
mpl.xlabel('Range')
mpl.ylabel('Height')

#For non-ideal trajectory, the x component of the acceleration must be considered    
Yvalues=[]
Xvalues=[]
i=0
if Ay==0:
    raise ValueError('The Y-component of the acceleration cannot be zero')
elif H<0:
    raise ValueError('Height must be above the reference point which is the ground')
elif V==0:
    raise ValueError('The velocity cannot be zero. The object must be moving')
elif V<0:
    raise ValueError('Magnitude of velocity cannot be negative')
elif (th<0) or (th>180):
    raise ValueError('Angle must not be less than 0 degrees and must not exceed 180 degrees')
elif H==0:
    t=float(abs((-(Vy)-(((Vy**2)-4*(.5*(Ay))*(-H))**(1/2)))/(2*(.5*Ay))))
    while i<=t:
        Y=H+(Vy*i)+((.5)*(Ay)*(i**2))
        X=(Vx*i)+((.5)*(Ax)*(i**2))
        #add new X and Y values to the list
        Yvalues.append(Y)
        Xvalues.append(X)
        i=i+0.001
else:
    tt=float(abs((Vy/Ay)-abs((((Vy**2)/(Ay**2))-((2*H)/(Ay)))**(1/2))))
    while i<=tt:
        Y=H+(Vy*i)+((.5)*(Ay)*(i**2))
        X=(Vx*i)+((.5)*(Ax)*(i**2))
        #add new X and Y values to the list
        Yvalues.append(Y)
        Xvalues.append(X)
        i=i+0.001

#Plotting the X and Y values using the lists made
mpl.subplot(1,2,1)
mpl.plot(Xvalues,Yvalues)
mpl.title('Non-Ideal Trajectory')
mpl.xlabel('Range')
mpl.ylabel('Height')
