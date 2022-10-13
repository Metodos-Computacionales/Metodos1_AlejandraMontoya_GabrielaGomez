#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import matplotlib.pyplot as plt


# In[31]:


def sistema(x1,x2):
    a=np.log(x1**2+x2**2)-np.sin(x1*x2)-np.log(2)-np.log(np.pi)
    b=np.e**(x1-x2)+np.cos(x1*x2)
    return a,b


# In[32]:


for i in range(2):
    print(sistema(2,2)[i])


# In[33]:


def VectorF(G,r):
    
    dim=2
    
    v=np.zeros(dim)
    
    for i in range(dim):
        v[i]=sistema(r[0],r[1])[i]
    return v


# In[34]:


VectorF(sistema,[2,2])


# In[35]:


def GetJacobian(G,r,h=1e-6):
    
    dim = 2
    
    J = np.zeros((dim,dim))
    
    for i in range(dim):
        J[i,0] = (G(r[0]+h,r[1])[i] - G(r[0]-h,r[1])[i])/(2*h)
        J[i,1] = (G(r[0],r[1]+h)[i] - G(r[0],r[1]-h)[i])/(2*h)
        
    return np.transpose(J)


# In[36]:


GetJacobian(sistema,[2,2])


# In[41]:


def NewtonRaphson(sistema,r,error=1e-10):
    
    it = 0
    d = 1
    Vector_d = np.array([])
    
    while d > error:
        
        it += 1
        
        rc = r
        
        F = VectorF(sistema,r)
        J = GetJacobian(sistema,r)
        InvJ = np.linalg.inv(J)
        
        r = rc - np.dot( InvJ, F )
        
        diff = r - rc
        print(diff)
        
        d = np.linalg.norm(diff)
        
        Vector_d = np.append( Vector_d , d )
        
    return r,it,Vector_d


# In[42]:


r,it,distancias=(NewtonRaphson(sistema,[2,2]))


# In[43]:


plt.plot(distancias)


# In[44]:


print(r)


# In[ ]:




