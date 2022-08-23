#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


theta = np.linspace(0, 2*np.pi)
a=0
b=1
r=a+b*theta
x=np.cos(theta)*r
y=np.sin(theta)*r

plt.plot(x,y)
plt.show()



# In[ ]:




