import numpy as np
import matplotlib.pyplot as plt
c = 2
def f(x,c):
    return 1-np.exp(-c*x) -x
def df(x,c):
    return c*np.exp(-c*x)-1
    
def newton_rapson(f, df, x0):
  cent = True
  while cent:
    x = x0 - f(x0,c)/ df(x0,c) 
    x0 = x
    ver = f(x0,c)/ df(x0,c)
    if  ver[-1] < 0.0001:
      print ("El error relativo es",ver[-1])
      cent = False
  return x

def dibujar_raices(f, x_ini, x_fin, raices):
  x = np.linspace(x_ini, x_fin)
  plt.scatter(raices, f(raices,c), c = "red", zorder = 1)
  plt.plot(x, f(x,c), zorder = 1)
  plt.show

iteraciones = 10
x0=np.linspace(-1,2.5,50)
solution_a = newton_rapson(f, df, x0)
plt.show
print("La solucion para c = 2 es {resp}".format(resp=solution_a[-1]))
dibujar_raices(f,-1, 10,solution_a[-1])

#Punto 2

c=np.linspace(0,3,100)
csolution_a = newton_rapson(f, df, c)
plt.plot(c,csolution_a)
plt.savefig('MontoyaJennifer_Ejercicio03.png')