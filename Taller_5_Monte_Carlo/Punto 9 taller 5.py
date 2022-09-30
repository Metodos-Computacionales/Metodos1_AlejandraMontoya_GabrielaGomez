#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np 
import matplotlib.pyplot as plt


# In[7]:


N=10000
l=[]
for i in range(N):
    x1=np.random.uniform(0,1)
    x2=np.random.uniform(0,1)
    x3=np.random.uniform(0,1)
    x4=np.random.uniform(0,1)
    x5=np.random.uniform(0,1)
    x6=np.random.uniform(0,1)
    x7=np.random.uniform(0,1)
    x8=np.random.uniform(0,1)
    f=(2**-7)*((x1+x2+x3+x4+x5+x6+x7+x8)**2)
    l.append(f)

print(np.mean(l))


# In[ ]:




