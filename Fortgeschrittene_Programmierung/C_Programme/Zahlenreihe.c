#include <stdio.h>
#include <conio.h>


void Ausgabe(float Zahlenreihe[], int n, char *Wort)
{
    printf("%s", Wort);       //mit %p bekomme ich Adresse mit %s den Inhalt 
    for(int i=0; i<n; i++)
    {
        printf("%.2f ", Zahlenreihe[i]);
    }
}

int Mittelwert(float Zahlenreihe[], int n, float *erg)
{
    float sum=0;
    for(int i=0; i<n; i++)
    {
        sum+=Zahlenreihe[i];
    }
    *erg= (sum/n);   //ich gebe erg durch zeiger aus
    return 0;
}

int Varianz(float *Zahlenreihe, int n, float mw, float *var)
{
    float sum=0;
    for(int i=0; i<n; i++)
    {
        float diff = *Zahlenreihe[i]-mw;
        sum += diff * diff;
    }
    *var=(sum/n);
    return 0;

} 


int Sortieren(float *Zahlenreihe, int n, char reihenfolge[])
{
    for(int i = 0; i < n - 1; i++)
    {
        for(int j = 0; j < n - 1 - i; j++)
        {
            
            if(strcmp(reihenfolge, "auf") == 0 &&Zahlenreihe[j]>Zahlenreihe[j + 1])
            {
                float temp = Zahlenreihe[j];
                Zahlenreihe[j] = Zahlenreihe[j + 1];
                Zahlenreihe[j + 1] = temp;
            }

            if(strcmp(reihenfolge, "ab") == 0 &&Zahlenreihe[j]<Zahlenreihe[j + 1])
            {
                float temp = Zahlenreihe[j];
                Zahlenreihe[j] = Zahlenreihe[j + 1];
                Zahlenreihe[j + 1] = temp;
            }
        }
    }

    return 0;
}





int main(void)
{
    
    float Zahlenreihe[] = {3, 0, 1, 2, 4, 8, 2};
    int n=7;
    char *Wort = "Unsortiert:";

    Ausgabe(&Zahlenreihe[0], n, Wort);

    float erg;
    Mittelwert(&Zahlenreihe[0], n, &erg);
    printf("\nMittelwert: %.3f", erg);

    float var;
    float mw=erg;
    Varianz(Zahlenreihe, n, mw, &var);
    printf("\nVarianz: %.3f", var);

    char reihenfolge[4];
    printf("\nIn welcher Reihenfolge soll sortiert werden? (auf/ab): ");
    scanf("%3s", reihenfolge);   //3 zeichn möglich
    Sortieren(Zahlenreihe, n, reihenfolge);

    printf("\nSortierte Reihe: ");
    for(int i = 0; i < n; i++)
        printf("%.2f ", Zahlenreihe[i]);

    
    printf("\nPraktikum ist Montags");




    getch();
    return 0;


}