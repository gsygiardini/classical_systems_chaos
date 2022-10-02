from scipy.integrate import odeint
from matplotlib import pyplot as plt
import numpy as np

m = 1
epsilon = 2
omega0 = 1
omegaD = 1
F = 1
dt = 0.0001

def f(r,t):
    return(r[1],(1/m)*(epsilon * (1.0 - r[0]*r[0])*r[1] - m*omega0*omega0*r[0] + F*np.cos(omegaD*t)))


#Solving differential equation
y0=[5,0]

t = np.linspace(1,100,int(2/dt))
x = odeint(f,y0,t)

xs = x[:,0]
xDot = []

for i in range(0,len(xs)-1):
    xDot.append((xs[i+1]-xs[i])/dt)

xs = np.delete(xs,len(xs)-1)
t = np.delete(t,len(t)-1)

# plt.plot(t,xs)

plt.plot(xs,xDot)
plt.xticks([])
plt.yticks([])
plt.show()
