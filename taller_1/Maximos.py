import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("Datos_Métodos.txt", delimiter=",", skiprows=1)
X = data[:, 0]
Y = data[:, 1]
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
    plt.plot(X, Y,color='black')
    plt.plot(maximosx,maximosy,'o',color='red')
    return  maximosx, maximosy        
    
