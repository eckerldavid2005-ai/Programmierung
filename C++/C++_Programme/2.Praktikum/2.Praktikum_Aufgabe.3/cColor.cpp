#include <iostream>
#include "cColor.h"

using namespace std;

cColor::cColor(int blau, int rot, int gruen)
{
    r = rot;                                    //kopiert Wert des Parameters r in das Attribut r des Objekts
    g = gruen;                                
    b = blau;
}

void cColor::display()
{
    cout << "(" << r << ", " << g << ", " << b << ")" << endl; 
}

int cColor::hilfsmethode()
{
    int wert;
    cin >> wert; //hier geht es weiter nach r=hilfsmethode

    while (cin.fail() || wert<0 || wert>255 )
    {
        cin.clear();
        cout << "Fehlereingabe, bitte nur Zahlen zwischen 0 und 255" << endl;
        cin.ignore (1000, '\n');
        cin >> wert;
    }
    return wert;
}


void cColor::chooseColor()
{
    cout << "Geben sie den Farbwert fuer rot ein" << endl;
    r=hilfsmethode();

    cout << "Geben sie den Farbwert fuer gruen ein" << endl;
    g=hilfsmethode();

    cout << "Geben sie den Farbwert fuer blau ein" << endl;
    b=hilfsmethode();

    cout << "Ihre gewaehlte Farbe:";
    cout << "(" << r << "," << g << "," << b <<")" << endl;

}