import matplotlib.pyplot as plt
import numpy as np 

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
        
def armar_lista():
    total = 0 
    n = 2
    lst =[]
    while total<100:
        if is_prime(n):
            lst.append(n)
            total +=1
        n+=1
    return lst
x = np.arange(0,100)
y = armar_lista()
plt.plot(x,y,label="Puntos",linewidth=1,c="red")
