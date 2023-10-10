def runge_kutta(f, x0, y0, h, n):
    """
    Implementación del método de Runge-Kutta de cuarto orden (RK4) para resolver una ecuación diferencial.
    
    Args:
        f: Función que define la ecuación diferencial dy/dx = f(x, y).
        x0: Valor inicial de x.
        y0: Valor inicial de y correspondiente a x0.
        h: Tamaño del paso.
        n: Número de pasos.
        
    Returns:
        Una lista con los valores de x y y obtenidos mediante el método RK4.
    """
    x_values = [x0]
    y_values = [y0]
    
    for i in range(n):
        x = x_values[-1]
        y = y_values[-1]
        
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        x_next = x + h
        y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        
        x_values.append(x_next)
        y_values.append(y_next)
    
    return x_values, y_values

def f(x, y):
    return (y/x)**2 + y/x

x0 = 1
y0 = 1
h = 0.1
n = 10

x_values, y_values = runge_kutta(f, x0, y0, h, n)

# Imprimir los resultados
for x, y in zip(x_values, y_values):
    print(f"x = {x:.2f}, y = {y:.6f}")
