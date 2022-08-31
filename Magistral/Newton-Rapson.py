
import numpy as np
import matplotlib.pyplot as plt
# dibujar la función 
def f(x):
  return 5*(1-np.exp(-x))-x



x = np.linspace(-3, 5.5, 50)
y = f(x)


plt.axhline( y= 0, color="red")
plt.plot(x, y, ".")
plt.show
print(x)

def df(f,x,h=le-6):
    return ((f(x+h)-f(x-h))/(2*h))


def newton_rapson(f, df, iteraciones, x0):
  for i in range(iteraciones):
    x = x0 - f(x0)/ df(x0) 
    x0 = x
    
  return x

def dibujar_raices(f, x_ini, x_fin, raices):
  x = np.linspace(x_ini, x_fin)
  plt.axhline( y= 0, color="gray")
  plt.scatter(raices, f(raices), c = "red", zorder = 2)
  plt.plot(x, f(x), zorder = 1)
  plt.show

iteraciones = 10
x0 = np.array([-2.1, 1.9, 4.1])
raices = newton_rapson(f, df, iteraciones, x0)

dibujar_raices(f,-3, 5.5, raices)