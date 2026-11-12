#include <stdio.h>
#include <conio.h>
#include <math.h>


float Mantel(float r, float h, float PI)
{
    return 2.0*r*PI*h;
}

float Volumen(float r, float h, float PI)
{
    return r*r*PI*h;
}

float Masse(float r, float rho, float h, float PI)
{
    return Volumen(r, h, PI)  * rho;
}

double Funktion(double x)
{
    return log(x);
}

double Stammfunktion(double x)
{
    return x*log(x)-x;
}

double Exact(double b, double a)
{
    return Stammfunktion(b)-Stammfunktion(a);
}


double Approx(double a, double b, int n) 
{
    double dx = (b - a) / n;
    double sum = 0.0;

    for (int i = 0; i < n; i++) {
        double xi= a+dx*i;
        sum += Funktion(xi) * dx;
    }
    return sum;
}



int main(void)
{
    float r=1.2, h=3.4, rho=5.6, PI=3.141592;
    printf("Mit den Werten: r=%.2f cm, h=%.2fcm, rho %.2fg/cm3\n", r, h, rho);


    float M = Mantel(r, h, PI);
    float V = Volumen(r, h, PI);
    float m = Masse(r, h, rho, PI);

    printf("ergibt sich: M= %fcm2  V=%fcm3  m=%fg\n", M, V, m);

    printf("Montag\n");


    int a=1, b=5, n=1000;

    double exact = Exact(b, a);
    double Iapprox = Approx(a, b, n);
    printf("Mit den Werten: a=%i, b=%i, n=%i\n", a, b, n);
    printf("ergibt sich: Iexakt= %f und Iapprox=%f\n", exact, Iapprox);

    getch();
    return 0;

}