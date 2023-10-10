import numpy as np
import sympy as sym

xi = np.array([8.3,8.6])
fi = np.array([17.5649, 18.50515])
muestras = 1001

xi = np.array(xi)
B = np.array(fi)
n = len(xi)

D = np.zeros(shape=(n,n),dtype =float)
for i in range(0,n,1):
    for j in range(0,n,1):
        potencia = (n-1)-j
        D[i,j] = xi[i]**potencia

coeficiente = np.linalg.solve(D,B)

x = sym.Symbol('x')
polinomio = 0
for i in range(0,n,1):
    potencia = (n-1)-i  
    termino = coeficiente[i]*(x**potencia)
    polinomio = polinomio + termino

px = sym.lambdify(x,polinomio)
    
# SALIDA
print('Matriz: ')
print(D)
print('los coeficientes del polinomio: ')
print(coeficiente)
print('Polinomio de interpolación: ')
print(polinomio)