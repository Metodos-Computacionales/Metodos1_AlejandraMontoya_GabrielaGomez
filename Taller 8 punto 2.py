#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Urna 1


# In[3]:


PU1=np.array([3/10,1/10,6/10])
F1=np.cumsum(PU1)


# In[4]:


PU=np.array([1/3,2/3])
FU=np.cumsum(PU)
PU2=np.array([6/10,2/10,2/10])
P=np.array([PU1,PU2])


# In[5]:


F=np.cumsum(P,axis=1)


# In[8]:


c=np.zeros(1000)
for i, (x1,x2) in enumerate(np.random.rand(1000,2)):
    n_urna=np.searchsorted(FU,x1)
    c[i]=np.searchsorted(F[n_urna],x2)


# In[10]:


plt.hist(c,bins=[0,1,2,3],density=True)


# In[11]:


names={0:"Rojo",1:"Negro",2:"Verde"}


# In[12]:


plt.hist([names[x] for x in c])


# In[13]:


#Probablidad de que sea roja 
#P(R)=P(R/U1)P(U1)+P(R/U2)P(U2)


# In[14]:


PR=PU1[0]*PU[0]+PU2[0]*PU[1]
print(PR)


# In[15]:


#Probablidad de que sea negra
#P(N)=P(N/U1)P(U1)+P(N/U2)P(U2)


# In[16]:


PN=PU1[1]*PU[0]+PU2[1]*PU[1]
print(PN)


# In[17]:


#Probabilidad de que sea de la urna 1 si es bola negra
#Teorema de Bayes
#P(U1/N)=P(N/U1)·P(U1)/P(N)


# In[19]:


PU1_negra=(PU1[1]*PU[0])/(PN)
print(PU_negra)


# In[20]:


#Probabilidad de que sea de la urna 2 si es bola negra
#Teorema de Bayes
#P(U2/N)=P(N/U2)·P(U2)/P(N)


# In[21]:


PU2_negra=(PU2[1]*PU[1])/(PN)
print(PU2_negra)


# In[ ]:




