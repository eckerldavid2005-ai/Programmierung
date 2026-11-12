#include <stdio.h>
#include <string.h>
#include <conio.h>

int main(void) {
    FILE *fp;
    long menge = 4321;
    float gewicht = 43.21f;
    char beschreibung[24] = "Das ist ein Text 4321";

    // Datei zum Schreiben öffnen
    fp = fopen("daten.bin", "wb");
    if (fp == NULL) {
        printf("Fehler: Datei konnte nicht geöffnet werden!\n");
        return 1;
    }

    // Daten schreiben
    fwrite(&menge, sizeof(long), 1, fp);
    fwrite(&gewicht, sizeof(float), 1, fp);
    fwrite(beschreibung, sizeof(char), 24, fp);

    // Dateigröße bestimmen
    long pos = ftell(fp);
    printf("Dateigröße: %ld Byte\n", pos);

    fclose(fp);
    printf("Datei 'daten.bin' erfolgreich erstellt.\n");

    // Datei wieder öffnen und auslesen
    fp = fopen("daten.bin", "rb");
    if (fp == NULL) {
        printf("Fehler: Datei konnte nicht geöffnet werden!\n");
        return 1;
    }

    long menge_r = 0;
    float gewicht_r = 0.0f;
    char beschreibung_r[24] = "";

    fread(&menge_r, sizeof(long), 1, fp);
    fread(&gewicht_r, sizeof(float), 1, fp);
    fread(beschreibung_r, sizeof(char), 24, fp);

    printf("\nGelesene Werte:\n");
    printf("Menge: %ld, Gewicht: %.6f, Beschreibung: %s\n",
           menge_r, gewicht_r, beschreibung_r);

    fclose(fp);
    printf("\nDatei 'daten.bin' geschlossen.\n");

    getch();
    return 0;
}
