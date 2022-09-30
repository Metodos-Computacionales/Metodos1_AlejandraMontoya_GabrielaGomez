#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np 
import matplotlib.pyplot as plt


# In[43]:


def fact(n):
    r=np.math.factorial(n-1)
    return r


# In[44]:


def f(x,a,b):
    f=(fact(a+b)/(fact(a)*fact(b)))*(x**(a-1))*((1-x)**(b-1))
    return f


# In[59]:


def metodo(a,b,f,N):
    x=np.zeros(N)
    fx=np.zeros(N)
    y=np.zeros(N)
    #Paso 1 
    for i in range(N):
        x[i]=np.random.uniform(a,b)
        fx[i]=f(x[i],2,4)
    
    #Paso 2
    ymax=np.max(fx)
    r=[]
    for i in range(N):
        y[i]=np.random.uniform(a,b)
        if y[i]<fx[i]:
            r.append(x[i])
    return r,ymax        


# In[60]:


N=1000
ymax=metodo(0,1,f,1000)[1]
n=len(metodo(0,1,f,1000)[0])
vol=ymax*1
A=(n/N)*vol
print(A)


# In[ ]:




