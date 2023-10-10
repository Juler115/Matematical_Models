import numpy as np
from scipy.linalg import eigvals

def krylov(matrix, vector, k):
    n = matrix.shape[0]
    krylov_matrix = np.zeros((n, k))
    krylov_matrix[:, 0] = vector
    for i in range(1, k):
        krylov_matrix[:, i] = np.dot(matrix, krylov_matrix[:, i-1])
    return krylov_matrix

# Matriz dada
matrix = np.array([[1, -1, 4],
                   [3, 2, -1],
                   [2, 1, -1]])

# Vector inicial
vector = np.array([1, 0, 0])

# Número de iteraciones
k = 10

# Calcular los autovalores utilizando el método de Krylov
krylov_matrix = krylov(matrix, vector, k)
eigenvalues = eigvals(matrix)

# Construir el polinomio característico utilizando los autovalores
polynomial = np.poly(eigenvalues)

# Obtener el polinomio característico como una cadena de texto
polynomial_str = ""
for i, coeff in enumerate(polynomial):
    if i == 0:
        polynomial_str += f"{coeff}*λ^{len(polynomial)-1}"
    else:
        polynomial_str += f" + {coeff}*λ^{len(polynomial)-i-1}"

print("Polinomio característico utilizando el método de Krylov:")
print(polynomial_str)
