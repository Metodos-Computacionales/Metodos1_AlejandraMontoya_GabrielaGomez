#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np 
import matplotlib.pyplot as plt


# In[ ]:


#Para 2 puntos 


# In[10]:


Roots,Weights = np.polynomial.legendre.leggauss(2)


# In[11]:


a=1
b=2


# In[12]:


def f(x):
    f=1/x**2
    return f


# In[13]:


t = 0.5*((b-a)*Roots + a + b)
integral = 0.5*(b-a)*np.sum(Weights*f(t))


# In[14]:


print(integral)


# In[15]:


#Para 3 puntos 


# In[18]:


Roots2,Weights2 = np.polynomial.legendre.leggauss(3)


# In[21]:


t2 = 0.5*((b-a)*Roots2 + a + b)
integral2 = 0.5*(b-a)*np.sum(Weights2*f(t2))


# In[22]:


print(integral2)

