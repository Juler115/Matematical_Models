#include <iostream>
#include <cmath>
#include <complex>


using namespace std;

double g(double x) {
    return x*x*x*x-20*x*x*x+0.1*x;
}

int main() {
    double x0=12;
    double tol = 1e-9;
    double xn = x0;
    double error = tol + 1;
    int iter = 0;

    while (error > tol && iter < 100) {
        double xn1 = g(xn);
        error = abs(xn1 - xn);
        xn = xn1;
        iter++;
    }

    if (iter == 100) {
        cout << "El metodo no converge en " << iter << "\niteraciones." << endl;
    } else {
        cout << "La raiz de la ecuacion es " << xn << "\ncon un error de " << error << "\ndespues de " << iter << " iteraciones." << endl;
    }

    return 0;
}

