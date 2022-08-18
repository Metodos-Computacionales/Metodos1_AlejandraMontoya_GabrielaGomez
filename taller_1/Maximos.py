import numpy as np
import matplotlib.pyplot as plt 
plt.style.use('ggplot')

def f(x):
  return (x+2)*(x-2)*(x-4)
def df(x):
  return 3*x**2 -8*x-4
def seg_df(x):
  return 6*x-8
def newton_rapson(f, df, iteraciones, x0):
  for i in range(iteraciones):
    x = x0 - f(x0)/ df(x0) 
    x0 = x
  return x

def dibujar_raices(f, x_ini, x_fin, raices):
  x = np.linspace(x_ini, x_fin)
  plt.axhline( y= 0, color="gray")
  plt.scatter(raices, df(raices), c = "red", zorder = 2)
  plt.plot(x, f(x), zorder = 1)
  plt.show