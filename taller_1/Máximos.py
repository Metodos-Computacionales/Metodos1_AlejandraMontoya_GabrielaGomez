#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import matplotlib.pyplot as plt


# In[23]:


data = np.loadtxt("Datos_Métodos.txt", delimiter=",", skiprows=1)


# In[27]:


X = data[:, 0]
Y = data[:, 1]


# In[95]:


Xsort= X.copy()
Xsort.sort()
def coordenadasysort(X,Y):
    yfinal=[]
    for i in range(len(X)):
        valor= Xsort[i]
        posicion= np.where(X==valor)
        coordenaday= Y[posicion]
        yfinal.append(coordenaday)
    return yfinal
def maximos(X,Y):
    lista= coordenadasysort(X,Y)
    maximosy= []
    maximosx=[]
    for i in range(1, len(lista)-1):
        if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
            maximosy.append(lista[i])
    for i in range(len(maximosy)):
        valor= maximosy[i]
        posicion= np.where(Y== valor)
        coordenadax= X[posicion]
        maximosx.append(coordenadax)
    plt.plot(X, Y,color='blue')
    plt.plot(maximosx,maximosy,'o',color='red')
    return  maximosx, maximosy        
    


# In[96]:


print(maximos(X,Y))


# In[ ]:




