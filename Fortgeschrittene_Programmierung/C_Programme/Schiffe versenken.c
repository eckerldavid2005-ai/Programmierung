#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>


#define NX 5
#define NY 5

int main(void)
{
    int Spielbrett[NX][NY] = {0};
    int Anzahlschiffe = (0.2*NX*NY);     //Anzahl der Schiffe auf Feld

    srand(time(NULL));

    int gesetzteschiffe = 0;
    while(gesetzteschiffe<Anzahlschiffe)
    {
        int x= rand()% NX;   //zufällig setzen
        int y= rand()% NY;

        if(Spielbrett[x][y]==0)
        {
            Spielbrett[x][y]=1;
            gesetzteschiffe++;
        }

    }
    printf("Spielbrett\n");

    for (int y = 0; y < NY; y++) {
        for (int x = 0; x < NX; x++) {
            if (Spielbrett[x][y] == 1)
                printf("S ");
            else
                printf(". ");
        }
        printf("\n");
    }


    getch();
    return 0;
}

