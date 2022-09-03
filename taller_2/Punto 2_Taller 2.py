#!/usr/bin/env python
# coding: utf-8

# In[108]:


import numpy as np
import matplotlib.pyplot as plt


# In[109]:


xi,xf,N=-4,4,25
x=np.linspace(xi,xf,N)
y=x.copy()


# In[110]:


X,Y = np.meshgrid(x,y)
plt.scatter(X,Y)


# In[111]:


V=2
R=2
def Potencial(x,y):
    phi=V*x*(1-(R**2/(x**2+y**2)))
    return phi


# In[112]:



dx= lambda  x,y,f :  (f(x+h , y )-f(x-h , y ))/(2*h)

dy= lambda  x,y,f:  -(f(x,y+h )-f(x,y-h ))/(2*h)


# In[113]:


def campo(x,y):
    camx=dx(x,y,Potencial)
    camy=dy(x,y,Potencial)
    print(camx,camy)
    return camx, camy


# In[114]:


u = 2

def Graficar_campo(x,y):
    
    camx = np.zeros((N,N))
    camy = np.zeros((N,N))
    
    for i in range(N):
        for j in range(N):
            if x[i]<=-u or x[i] >=  u or y[j]<=-u or y[j]>=u:
                camx[i,j],camy[i,j] = campo(x[i],y[j])
            
    return camx , camy

camx,camy = Graficar_campo(x,y)


# In[115]:


fig=plt.figure(figsize=(5,5))

ax=fig.add_subplot(1,1,1)
for i in range(25):
    for j in range(25):
        ax.quiver(x[i],y[j],camx[i,j],camy[i,j],color='blue',alpha=0.8)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




