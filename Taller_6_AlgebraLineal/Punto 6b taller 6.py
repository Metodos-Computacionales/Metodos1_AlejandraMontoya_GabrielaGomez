#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
import matplotlib.pyplot as plt


# In[40]:


def sistema(x1,x2,x3):
    a=6*x1-2*np.cos(x2*x3)-1
    b=9*x2+((x1**2+np.sin(x3)+1.06)**0.5)+0.9
    c=60*x3+3*np.e**(-x1*x2)+10*np.pi-3
    return a,b,c


# In[41]:


for i in range(3):
    print(sistema(0,0,0)[i])


# In[42]:


def VectorF(G,r):
    
    dim=3
    
    v=np.zeros(dim)
    
    for i in range(dim):
        v[i]=sistema(r[0],r[1],r[2])[i]
    return v


# In[43]:


VectorF(sistema,[0,0,0])


# In[44]:


def GetJacobian(sistema,r,h=1e-6):
    
    dim = 3
    
    J = np.zeros((dim,dim))
    
    for i in range(dim):
        J[i,0] = (sistema(r[0]+h,r[1],r[2])[i] - sistema(r[0]-h,r[1],r[2])[i])/(2*h)
        J[i,1] = (sistema(r[0],r[1]+h,r[2])[i] - sistema(r[0],r[1]-h,r[2])[i])/(2*h)
        J[i,2] = (sistema(r[0],r[1],r[2]+h)[i] - sistema(r[0],r[1],r[2]-h)[i])/(2*h)
    return J.T


# In[45]:


GetJacobian(sistema,[0,1,-1])


# In[49]:


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


# In[50]:


r,it,distancias = NewtonRaphson(sistema,[1,2,3])
print(r,it)


# In[51]:


plt.plot(distancias)


# In[52]:


np.round(VectorF(sistema,r))

