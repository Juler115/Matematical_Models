def secante(func, x0, x1, tol=1e-8, max_iter=10):
    iter_count = 0
    while iter_count < max_iter:
        # Calcula la siguiente aproximación de la raíz utilizando la fórmula de la secante.
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        
        # Comprueba si la aproximación es lo suficientemente cercana a una raíz.
        if abs(x2 - x1) < tol:
            return x2, iter_count
        
        # Actualiza las aproximaciones anteriores para la siguiente iteración.
        x0 = x1
        x1 = x2
        iter_count += 1

    raise Exception("El método de la secante no convergió después de {} iteraciones.".format(max_iter))

# Ejemplo de uso:
def f(x):
    return x**2 + x**4

x0 = -3
x1 = -4
root, iterations = secante(f, x0, x1)
print("Raíz encontrada:", root)
print("Número de iteraciones:", iterations)
