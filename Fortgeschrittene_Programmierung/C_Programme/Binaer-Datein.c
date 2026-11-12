#include <stdio.h>
#include <string.h>
#include <conio.h>

int main(void)
{
    FILE *fp;
    fp=fopen("datenneu.bin", "wb");  
    if(fp==NULL) {
        printf("Datei konnte nicht geoeffnet werden!\n");
        return 1;
    }

    long int Menge = 4321;
    float Gewicht = 43.21f;
    char Beschreibung[24] = "Das ist ein Text 4321";

    fwrite(&Menge, sizeof(long), 1, fp);
    fwrite(&Gewicht, sizeof(float), 1, fp);
    fwrite(Beschreibung, sizeof(char), 24, fp);

    printf("long: %zu Byte\n", sizeof(long));

    fclose(fp);

    
    fp=fopen("daten.bin", "rb");  
    if(fp==NULL) {
        printf("Datei konnte nicht geoeffnet werden!\n");
        return 1;
    }

    long mengeb = 0;
    float gewichtb = 0.0f;
    char beschreibungb[24] = "";

    fread(&mengeb, sizeof(long), 1, fp);
    fread(&gewichtb, sizeof(float), 1, fp);
    fread(beschreibungb, sizeof(char), 24, fp);

    printf("\nGelesene Werte:\n");
    printf("Menge: %ld, Gewicht: %.6f, Beschreibung: %s\n",
           mengeb, gewichtb, beschreibungb);

    fclose(fp);

    getch();
    return 0;
}
