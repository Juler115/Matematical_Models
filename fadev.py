import numpy as np

def faddeev_leverrier(matrix):
    n = matrix.shape[0]
    identity = np.eye(n)
    coefficients = []
    b = np.copy(matrix)
    for i in range(1, n+1):
        coefficients.append(-1 / i * np.trace(b))
        b = np.dot(matrix, b) - coefficients[-1] * identity
    coefficients.append(1)
    return np.flip(coefficients)

# Matriz dada
matrix = np.array([[3, 2, 4],
                   [2, 0, 2],
                   [4, 2, 3]])

# Obtener el polinomio característico
polynomial = faddeev_leverrier(matrix)

# Construir el polinomio característico como una cadena de texto
polynomial_str = ""
for i, coeff in enumerate(polynomial):
    if i == 0:
        polynomial_str += f"{coeff}*λ^{len(polynomial)-1}"
    else:
        polynomial_str += f" + {coeff}*λ^{len(polynomial)-i-1}"

print("Polinomio característico:")
print(polynomial_str)
