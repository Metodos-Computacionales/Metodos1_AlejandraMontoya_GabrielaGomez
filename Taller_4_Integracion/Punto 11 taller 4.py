#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt


# In[6]:


def f(x):
    f=(1+np.e**(-x**2))**0.5
    return f


# In[23]:


n=10000
def simpson_38(a,b):
    suma=f(a)+f(b)
    sumapares = 0
    sumaimpares = 0
    paso=(b-a)/n
    for i in range(1,n):
        if (i%2==0):
            sumapares += f(a+i*paso)
        else:
            sumaimpares += f(a+i*paso)
    suma += 2*sumaimpares + 3*sumapares
    integral = 3*paso*suma/8
    return integral

print(simpson_38(-1,1))


# In[ ]:




