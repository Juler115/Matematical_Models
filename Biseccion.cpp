#include <iostream>
#include <cmath>

using namespace std;

double f(double x) {
    return x*x*x*x-20*x*x*x+0.1*x; // Función a la cual se le busca la raíz
}

double bisection(double a, double b, double tol) {
    double c;
    do {
        c = (a + b) / 2;
        if (f(a) * f(c) < 0) {
            b = c;
        } else {
            a = c;
        }
    } while (abs(b - a) > tol);
    return c;
}

int main() {
    double a = 1, b = 100, tol = 0.0001; // Intervalo inicial [1,2] y tolerancia de 0.0001
    double root = bisection(a, b, tol);
    cout << "La raíz de la función es: " << root << endl;
    return 0;
}
