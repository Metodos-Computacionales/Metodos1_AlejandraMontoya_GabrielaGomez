#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 


# In[3]:


def f(x): 
    f=(np.e)**(-x**2)
    return f


# In[5]:


def dx(x,f,h=1*10**-6):
    dx=(f(x+h)-2*f(x)+f(x-h))/h**2
    return dx


# In[6]:


def trapecio(f,x0,xn,n):
    x=np.linspace(x0,xn,n)
    tol=0.005
    h=x[-1]-x[0]
    integral=0
    e=((h**3)/(12*(len(x)-1)**2))*max(abs(dx(x,f)))
    for i in range(len(x)-1):
        integral+=((x[i+1]-x[i])/2)*(f(x[i])+f(x[i+1]))
    if e<tol:
        return integral
    else: 
        "El error supera la tolerancia"


# In[9]:


print(trapecio(f,0,1,7))


# In[ ]:




