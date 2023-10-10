import numpy as np

def jacobi(A, b, x0, tol, maxiter):
    """
    Implementación del método de Jacobi para resolver un sistema de ecuaciones lineales
    Ax = b, donde A es una matriz de coeficientes, b es el vector de términos independientes,
    x0 es la aproximación inicial, tol es la tolerancia del error y maxiter es el número máximo
    de iteraciones permitidas.
    """
    n = len(b)
    x = x0.copy()
    for k in range(maxiter):
        x_prev = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i,:], x_prev) + A[i,i]*x_prev[i])/A[i,i]
        if np.linalg.norm(x - x_prev) < tol:
            print(f'Jacobi convergió en {k+1} iteraciones')
            return x
    print('Jacobi no converge')
    return x

#2x + y + z = 5
#x + 3y + z = 10
#x + y + 4z = 13

A = np.array([[4 , 1, 1],
              [2, -5 , 1],
              [1, 2, 7 ]])

b = np.array([6, -2, 10])

x0 = np.array([0, 0, 0])
tol = 1e-6
maxiter = 100

x = jacobi(A, b, x0, tol, maxiter)
print(x)
