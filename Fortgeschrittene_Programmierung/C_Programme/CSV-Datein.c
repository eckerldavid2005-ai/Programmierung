#include <stdio.h>
#include <math.h>
#include <conio.h>

void f2str(double zahl, char *ziel) {
    sprintf(ziel, "%.4f", zahl);
    for (int i = 0; ziel[i]; i++)
        if (ziel[i] == '.') ziel[i] = ',';
}

int main(void) {
    FILE *fp;
    double xGrad, xBogen, wurzel, cosx, PI = 3.14;
    char cosStr[32], wurzelStr[32];

    fp = fopen("tabelle.csv", "w");
    if (fp == NULL) {
        printf("Datei konnte nicht geoeffnet werden!\n");
        return 1;
    }

    fprintf(fp, "x;Cos;Wurzel\n");

    for (xGrad = 0; xGrad <= 180; xGrad += 10) {
        xBogen = (xGrad / 360.0) * 2.0 * PI;
        cosx = cos(xBogen);
        wurzel = sqrt(xGrad);
        f2str(cosx, cosStr);
        f2str(wurzel, wurzelStr);

        fprintf(fp, "%.0f;%s;%s\n", xGrad, cosStr, wurzelStr);
    }

    fclose(fp);

    fp = fopen("tabelle.csv", "r");
    if (fp == NULL) {
        printf("Datei konnte nicht geoeffnet werden!\n");
        return 1;
    }

    printf("\nErsten fuenf Zeilen aus tabelle.csv:\n\n");
    char zeile[128];
    int zeilenNr = 0;
    while (fgets(zeile, sizeof(zeile), fp) != NULL && zeilenNr < 5) {
        printf("%s", zeile);
        zeilenNr++;
    }

    fclose(fp);

    getch();
    return 0;
}
