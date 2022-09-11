#!/usr/bin/env python
# coding: utf-8

# In[108]:


#Punto 1
"""El error correspondiente al método de Newton-Raphson se debe al error de truncamiento el cual se basa la aproximación del valor exacto de las raíces"""


# In[109]:


#Punto 2
"""Con el fin de aumentar la presición de este método es necesario disminuir el exponente de lo que se refiere como tolerancia, es decir, que el error tolerado sea menor a un orden por ejemplo de 10 a la menos 9 y así tener una mayor exactitud"""


# In[94]:


import numpy as np 
import matplotlib.pyplot as plt 
import sympy as sym


# In[95]:


def f(x):
    f=(3*x**5)+(5*x**4)-(x**3)
    return f


# In[96]:


def df(f,x,h=1e-6):
    df=(f(x+h)-f(x-h))/(2*h)
    return df


# In[97]:


n=100
tol=10**-6
def Newton_Raphson(f,df,xi):
    for i in range(n):
        xip1=xi-((f(xi))/df(f,xi))
        er=(abs(xip1-xi))/xip1
        if er<tol:
            break
        xi=xip1
    return xi


# In[98]:


def Raíces(x,tolerancia=8):
    
    Raíces= np.array([])
    
    for i in x:
        root = Newton_Raphson(f,df,i)
        
        if root != False:
            
            croot = np.round( root, tolerancia )
            
            if croot not in Raíces:
                Raíces = np.append(Raíces,croot)
                
    Raíces.sort()
    
    return Raíces


# In[105]:


xtrial = np.linspace(-10,10,100)
Roots = Raíces(xtrial)
print(Roots)


# In[100]:


from scipy.special import laguerre
from scipy.special import legendre


# In[103]:


xl=np.linspace(-1,1,100)
r=np.array([])
n=21 #Número de polinomios


# In[106]:


for i in range(n):
    funcion=legendre(i)
    roots=Raíces(xl,funcion)
    print(np.append(r,roots))


# In[107]:


xl2=np.linspace(0,10000,1000)
for i in range(n):
    funcion=laguerre(i)
    roots=Raíces(xl2,funcion)
    print(np.append(r,roots))


# In[ ]:




