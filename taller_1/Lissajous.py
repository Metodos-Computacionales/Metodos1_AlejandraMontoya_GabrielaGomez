import matplotlib.pyplot as plt
import numpy as np 

n_sides = 5
delta = (np.pi)/2
n_x = [1,1,1,1,1,2,2,2,2,3,3,3,4,4,5]
n_y = [1,2,3,4,5,2,3,4,5,3,4,5,4,5,5]
t = np.linspace(-(np.pi),2*np.pi,300)
k=1
for i in range(0,15):
  x = np.sin(n_x[i] * t + delta)
  y = np.sin(n_y[i] * t)
  plt.subplot(5,5,k)
  k+=1
  plt.plot(x,y)
  plt.axis("off")


