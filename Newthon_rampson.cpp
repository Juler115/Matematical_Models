#include <bits/stdc++.h>

using namespace std;

double f(double x) {
    return x*x*x*x-20*x*x*x+0.1*x;
}


double taylor(double x0, double h) {
    double f0 = f(x0);
    double f1 = f(x0 + h);
    double f2 = f(x0 + 2 * h);
    double df = (f2 - 2 * f1 + f0) / pow(h, 2);
    double d2f = (f2 - 2 * f1 + f0) / pow(h, 2);
    return f0 + f1 * (x0 + h - x0) + df * pow(x0 + h - x0, 2) / tgamma(2) + d2f * pow(x0 + h - x0, 3) / tgamma(3);
}

double biseccion_taylor(double a, double b, int max_iter, double tol) {
    int i = 0;
    double fa = taylor(a, tol);
    double fb = taylor(b, tol);
    double c = (a + b) / 2.0;
    double fc = taylor(c, tol);
    while (i < max_iter && abs(fc) > tol) {
        if (fa * fc < 0) {
            b = c;
            fb = fc;
        } else {
            a = c;
            fa = fc;
        }
        c = (a + b) / 2.0;
        fc = taylor(c, tol);
        i++;
    }
    return c;
}

int main() {
    double a = 1, b = 100, tol = 1e-9;
    int max_iter = 10000;
    double raiz = biseccion_taylor(a, b, max_iter, tol);
    cout << "La raiz de f(x) es: " << raiz-5 << endl;
    return 0;
}
