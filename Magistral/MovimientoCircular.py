#Animaciones de un movimiento circular 
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.animation as anim 

A = 1 
omega = 2*np.pi/10 
N = 20
t = np.linspace(0,10,N)
r = np.zeros((N,2))
def GetPosotion():
#Remplaza a toda la fiña p columna especicifaca
    r[:,0] = A*np.cos(omega*t)
    r[:,0] = A*np.sin(omega*t)

