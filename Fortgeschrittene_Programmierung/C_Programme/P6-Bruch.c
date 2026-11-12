#include <stdio.h>
#include <conio.h>


struct Bruch {
    int zaehler;
    int nenner;
};

struct Bruch Add(struct Bruch x, struct Bruch y) {
    struct Bruch z;
    z.zaehler=x.zaehler*y.nenner+x.nenner*y.zaehler;
    z.nenner=x.nenner*y.nenner;
    return z;
}

struct Bruch Sub(struct Bruch x, struct Bruch y) {
    struct Bruch z;
    z.zaehler=x.zaehler*y.nenner-x.nenner*y.zaehler;
    z.nenner=x.nenner*y.nenner;
    return z;
}

struct Bruch Mul(struct Bruch x, struct Bruch y) {
    struct Bruch z;
    z.zaehler=x.zaehler*y.zaehler;
    z.nenner=x.nenner*y.nenner;
    return z;
}

struct Bruch Div(struct Bruch x, struct Bruch y) {
    struct Bruch z;
    z.zaehler=x.zaehler*y.nenner;
    z.nenner= x.nenner*y.zaehler;
    return z;
}

int ggT(int a, int b) {
    if(b==0)return a;
    return ggT(b, a % b);
}

struct Bruch Kuerzen(struct Bruch z) {
    int g=ggT(z.zaehler, z.nenner);
    z.zaehler/= g;
    z.nenner/= g;
    return z;
}

void Ausgabe(struct Bruch *b) {
    double dez=(double)b->zaehler / (double)b->nenner;
    printf("%d / %d = %.6f\n", b->zaehler, b->nenner, dez);
}

int main(void) {
    struct Bruch x={5, 4};
    struct Bruch y={1, 2};
    struct Bruch z;

    printf("x = "); Ausgabe(&x);
    printf("y = "); Ausgabe(&y);

    z=Add(x, y);
    printf("x + y = "); Ausgabe(&z);
    z=Kuerzen(z);
    printf("gekuerzt = "); Ausgabe(&z);

    z=Sub(x, y);
    printf("x - y = "); Ausgabe(&z);
    z=Kuerzen(z);
    printf("gekuerzt = "); Ausgabe(&z);

    z=Mul(x, y);
    printf("x * y = "); Ausgabe(&z);
    z=Kuerzen(z);
    printf("gekuerzt = "); Ausgabe(&z);

    z=Div(x, y);
    printf("x / y = "); Ausgabe(&z);
    z=Kuerzen(z);
    printf("gekuerzt = "); Ausgabe(&z);

    getch();
    return 0;
}
