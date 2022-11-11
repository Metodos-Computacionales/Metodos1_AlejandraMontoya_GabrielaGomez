#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def c_rep(r,n):
    return (np.math.factorial(r+n-1))/((np.math.factorial(r))*(np.math.factorial(n-1)))


# In[3]:


c_rep(10,3)


# In[ ]:




