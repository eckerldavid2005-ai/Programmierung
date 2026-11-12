#include <stdio.h>
#include <string.h>
#include <conio.h>

int main(void)
{
    char zeichen[100];
    char kopie[200];
    char muster[] = "David";
    int laenge;

    printf("Geben Sie eine Zeichenkette ein: ");
    fgets(zeichen, 100, stdin); //weil ich auch Leerzeichen lesen will

    zeichen[strcspn(zeichen, "\n")] = '\0'; //Entfernt meinen Zeilenumbruch

    laenge = strlen(zeichen);
    printf("Die Zeichenkette ist %d Zeichen lang\n", laenge);

    int i = 0;
    int laengemitschleife = 0;

    while (zeichen[i] != '\0')
        {
            laengemitschleife++;
            i++;
        }

    printf("Die Laenge mit der Schleife ist: %d\n", laengemitschleife);


    strcpy(kopie, zeichen);
    strcat(kopie, "Schluss");

    printf("Ausgabe der Kopie: %s\n", kopie);

    if (strcmp(zeichen, muster) == 0)
    {
        printf("Sie haben genau '%s' eingegeben.\n", muster);
    }
    else
    {
        if (strncmp(zeichen, muster, strlen(muster)) == 0)
        {
            printf("Sie haben '%s' am Anfang eingegeben.\n", muster);
        }
        else
        {
            if (strstr(zeichen, muster) != NULL)
            {
                printf("Sie haben '%s' eingegeben, aber nicht am Anfang.\n", muster);
            }
            else
            {
                printf("Sie haben '%s' gar nicht eingegeben.\n", muster);
            }
        }
    }
    printf("Raum: J0.09");

    getch();
    return 0;
}