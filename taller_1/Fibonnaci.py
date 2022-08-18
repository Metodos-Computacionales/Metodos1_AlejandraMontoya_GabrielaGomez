import matplotlib.pyplot as plt
import numpy as np 

def fibonnaci(final): 
    lst = [1,1]
    for i in range(1,final-1):
        aux = lst[-1]
        num =lst[-1] + lst[-2]
        lst.append(num)
    return lst
x = np.arange(0,25)
final = len(x)
y = fibonnaci(final)
plt.plot(x,y,label="Puntos",linewidth=3,c="red")

#Numero aureo
phi = (1+(5)**(1/2))/2
#Para 20 num
n_1 = fibonnaci(final+1)[-1]
n = fibonnaci(final)[-1]
phi_fibonnaci = n_1/n
print(phi,phi_fibonnaci)

