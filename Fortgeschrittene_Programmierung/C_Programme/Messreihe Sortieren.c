#include <stdio.h>
#include <conio.h>
#include <string.h>



int main(void)
{
    int n=4; //Anzahl der Messergebnise
    float Stromwerte[]={0.8, 0.5, 1.3, 1.1};
    float Messreihe[20][2];
    float Zeit = 0.0;
    
    for(int i=0; i<n; i++)
        {
            Messreihe[i][0]= Zeit;            //an der stelle i in spalte 0
            Messreihe[i][1] = Stromwerte[i];  //übertrage in 1 spalte die stromwerte an stelle i in messreihe an stelle i
            Zeit += 2.5;         
        }
    
    printf("Unsortiere Messreihe:\n");
    printf("Zeit[min]  Strom[A]\n");
    for(int i=0; i<n; i++)
        {
            printf("  %.1f        %.1f\n", Messreihe[i][0], Messreihe[i][1]);
        }
    
    for(int i=0; i<n-1; i++)
        {
            for(int j=0; j<n-1-i; j++)
            {
                if(Messreihe[j][1]<Messreihe[j+1][1])
                {
                    float tempzeit = Messreihe[j][0];
                    float tempstrom = Messreihe[j][1];

                    Messreihe[j][0] = Messreihe[j+1][0];
                    Messreihe[j][1] = Messreihe[j+1][1];

                    Messreihe[j+1][0] = tempzeit;
                    Messreihe[j+1][1] = tempstrom;

                }
            }
        }
    
    printf("\nSortierte Messreihe:\n");
    printf("Zeit[min]  Strom[A]\n");
    for(int i=0; i<n; i++)
        {
            printf("  %.1f        %.1f\n", Messreihe[i][0], Messreihe[i][1]);
        }
        
    

    getch();
    return 0;


}