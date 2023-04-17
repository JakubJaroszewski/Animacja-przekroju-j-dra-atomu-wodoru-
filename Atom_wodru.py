import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from numpy.polynomial import Laguerre
from IPython.core.display import HTML
from matplotlib.animation import FuncAnimation
import warnings

warnings.filterwarnings("ignore")
n=5
l=3
m=1
a=10
def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    return 1

def Psi(x,y,z):
        p=special.genlaguerre(n-l-1, 2*l+1)
        return np.sqrt((2/(n*a))**3*silnia(n-l-1)/(2*n*silnia(n+l)))*np.e**(-np.sqrt(x**2+y**2+z**2)/(n*a))*special.sph_harm(m, n, np.arcsin(z/np.sqrt(x**2+y**2+z**2)), np.arctan(y/x))*p(2*np.sqrt(x**2+y**2+z**2)/(n*a))  

X = np.arange(-125, -1, 0.1)+ np.arange(1, 125, 0.1)   
Y = np.arange(-100, 100, 0.1)
X, Y = np.meshgrid(X,Y)
funkcja = Psi(X,Y,-150)
levels = np.linspace(Psi(X,Y,0).min(), Psi(X,Y,0).max(), 30)
ax.contourf(X, Y, funkcja, levels=levels)

def animate(i):
    
    i=i-90
    ax.clear()
    ax.contourf(X,Y,Psi(X,Y,i),levels=levels)
    
ani = FuncAnimation(fig, animate, frames=180, interval=100,blit=False)
#ani.save('Phi1.gif',writer='pillow',fps=50,dpi=200)
HTML(ani.to_jshtml())