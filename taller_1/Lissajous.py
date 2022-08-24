import matplotlib.pyplot as plt
import numpy as np 

n_sides = 5
def Lissajous():
    fig = plt.figure()
    k = 0
    n_x = [1,2,3,4,5]
    n_y = [1,2,3,4,5]
    theta = np.linspace(0, 2*np.pi, 100)
    for i in range(5):
        for j in range(5):
            k += 1
            if n_x[i] <= n_y[j]:
                x = np.sin(n_x[i]*theta)
                y = np.sin(n_y[j]*theta)
                liss = fig.add_subplot(n_sides,n_sides,k)
                liss.plot(x,y)
                plt.axis('off')
    pass

Lissajous()