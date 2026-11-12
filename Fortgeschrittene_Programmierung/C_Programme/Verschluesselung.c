#include <stdio.h>
#include <string.h>
#include <conio.h>

int main(void)
{
    char KlartextA[] = "Hallo Welt!";
    char Schluessel[] ="Testo";
    char Chiffre[100];
    char KlartextB[100];

    printf("Klartext-A: %s\n", KlartextA);
    printf("Schluessel: %s\n", Schluessel);

    int laengek=strlen(KlartextA);
    int laenges=strlen(Schluessel);

    for(int i=0; i<laengek; i++)
        {
            char E = KlartextA[i];
            char S = Schluessel[i % laenges];

            if(E==S)
                {
                    Chiffre[i]=E;
                }

            else
                {
                    Chiffre[i]=E^S;
                }
        }
    Chiffre[laengek]= '\0';


    printf("Chiffre\n");
    printf("   Zeichenkette: %s \n", Chiffre);

    printf("     ASCII-Code (Dez.):");

    for(int i=0; i<laengek; i++)
    {
        printf("%d ", Chiffre[i]);
    }

    for(int i=0; i<laengek; i++)
    {
        char E= Chiffre[i];
        char S= Schluessel[i % laenges];


        if(E==S)
            {
            KlartextB[i]=E;
            }

        else
            {
                KlartextB[i]=E^S;
            }
    }
    KlartextB[laengek]='\0';

    printf("\nKlartextB: %s\n", KlartextB);

    getch();
    return 0;
}