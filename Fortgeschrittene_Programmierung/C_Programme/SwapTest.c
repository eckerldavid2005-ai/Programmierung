
#include <conio.h>
#include <stdio.h>

#define MAX 20

void fillX(float *fptr, int anzahl, float start, float incr);
void printX(float *fptr, int anzahl);


int main(void)
{
    float xFeld[MAX];

    fillX(xFeld, MAX, -2.5, 0.5);
    printX(xFeld, MAX);
    getch();
    return 0;
}

void fillX(float *fptr, int anzahl, float start, float incr)
{
    float wert=start;
    for(int i=0; i<anzahl; i++)
    {
        *fptr++=start;
        wert+=incr;
    }
}
void printX(float *fptr, int anzahl)
{
    for(int i=0; i<anzahl; i++)
    {
        printf("%.1f,", fptr++);
    }
}
