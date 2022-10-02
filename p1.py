from matplotlib import pyplot as plt
import numpy as np

tMax=20
dt=0.01
m=1
epsilon=5
omega0=1
omegaD=7
F=15
xIni=0.5
yIni=0.5
radius=1

k = epsilon/m

t = np.linspace(0,tMax,int(1/dt))

x = [0,0,0]
y = [0,0,0]

for i in range(0,tMax-2):
    x[i+2] = x[i+1] * (2 + k*dt - k*x[i]*dt) - x[i]*(1+k*dt) + k*x[i]*x[i]*dt - omega0*omega0*x[i]*dt*dt + F*np.cos(omegaD*t)*dt*dt
    y[i+2] = y[i+1] * (2 + k*dt - k*y[i]*dt) - y[i]*(1+k*dt) + k*y[i]*y[i]*dt - omega0*omega0*y[i]*dt*dt + F*np.cos(omegaD*t)*dt*dt
    x.append(0)
    y.append(0)

print(x)
