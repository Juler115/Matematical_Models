def euler_method(f, x0, y0, h, n):

    """
    Devuelve:
    - Una lista de tuplas (xi, yi) que representan los puntos (x, y) de la aproximación.
    """
    points = [(x0, y0)]
    for _ in range(n):
        xi, yi = points[-1]  # Obtener el último punto agregado
        slope = f(xi, yi)   # Calcular la pendiente en el punto (xi, yi)
        xi_next = xi + h    # Calcular el siguiente valor de x
        yi_next = yi + h * slope  # Calcular el siguiente valor de y usando la pendiente
        points.append((xi_next, yi_next))  # Agregar el punto a la lista de puntos
    return points

def example_function(x, y):
    return (y/x)**2 + y/x

# Valores iniciales
x0 = 1
y0 = 1
h = 0.1 #segundo-primero / n
n = 10
approximation = euler_method(example_function, x0, y0, h, n)

# Imprimir los puntos aproximados
for point in approximation:
    print(f"x = {point[0]}, y = {point[1]}")
