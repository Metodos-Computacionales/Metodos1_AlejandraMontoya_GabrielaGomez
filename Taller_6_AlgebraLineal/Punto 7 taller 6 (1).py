#!/usr/bin/env python
# coding: utf-8

# In[23]:


from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt


# In[24]:


G=(lambda x,y,z,w: (x**2)+(y**2)+(z**2)+(w**2)-1)


# In[25]:


def GetVectorF(G,r):
    
    v = G(r[0],r[1],r[2],r[3])
        
    return np.array([v])


# In[26]:


def GetJacobian(G,r,h=1e-6):
    
    J = np.zeros((1,4))
    for i in range(4):
        J[0,0] =(G(r[0]+h,r[1],r[2],r[3]) - G(r[0]-h,r[1],r[2],r[3]))/(2*h)
        J[0,1] =(G(r[0],r[1]+h,r[2],r[3]) - G(r[0],r[1]-h,r[2],r[3]))/(2*h)
        J[0,2] =(G(r[0],r[1],r[2]+h,r[3]) - G(r[0],r[1],r[2]-h,r[3]))/(2*h) 
        J[0,3] =(G(r[0],r[1],r[2],r[3]+h) - G(r[0],r[1],r[2],r[3]-h))/(2*h)
    return np.transpose(J)


# In[27]:


def GetMetric(G,r):
    v = GetVectorF(G,r)
    return np.linalg.norm(v)


# In[28]:


x=np.random.uniform(-1,1)
y=np.random.uniform(-1,1)
z=np.random.uniform(-1,1)
w=np.random.uniform(-1,1)
vector=np.array([x,y,z,w])


# In[29]:


def GetSolve(G,r,lr=1e-3,epochs=int(1e5),error=1e-7):
    
    d = 1
    it = 0
    Vector_F = np.array([])
    R_vector = np.array(r)
   
    while d > error and it < epochs:
        
        CurrentF = GetMetric(G,r)
        J = GetJacobian(G,r)
        GVector = GetVectorF(G,r)
        
        #Machine Learning
        r -= lr*np.dot(J,GVector) 
        R_vector = np.vstack((R_vector,r))
        NewF = GetMetric(G,r)
        Vector_F = np.append(Vector_F,NewF)
        d = np.abs( CurrentF - NewF )/NewF
        
        
        it += 1
    
    if d < error:
        print(' Entrenamiento completo ', d, 'iteraciones', it)    

    if it == epochs:
        print(' Entrenamiento no completado ')
        
    return r


# In[30]:


xsol = GetSolve(G,vector)
print(xsol)


# In[31]:


#Para 1000 puntos


# In[32]:


n=10**3
X=np.random.uniform(-1,1,n)
Y=np.random.uniform(-1,1,n)
Z=np.random.uniform(-1,1,n)
W=np.random.uniform(-1,1,n)

res=np.zeros((1000,4))
for i in tqdm(range(n)):
    xsol= GetSolve(G,[X[i],Y[i],Z[i],W[i]])
    res[i][0]=xsol[0]
    res[i][1]=xsol[1]
    res[i][2]=xsol[2]
    res[i][3]=xsol[3]


# In[34]:


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)

ax.set_xlim(-1,1)
ax.set_ylim(-1,1)

ax.scatter(res[:,0],res[:,1],color='r')


# In[ ]:




