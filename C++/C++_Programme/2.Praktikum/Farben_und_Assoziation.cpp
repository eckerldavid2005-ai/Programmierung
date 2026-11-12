//Ersteller: David Eckerl

#include <iostream>
#include <conio.h>

using namespace std;

class cColor
{
    private:
        int r;
        int g;
        int b;
        int hilfsmethode();                     //enthält Schleife für falsche Eingabe

    public:
        cColor()                                //Standart Konstruktor
        {
            r=0;
            g=0;
            b=0;
        }

        cColor(int b, int r=255, int g=255);    //allgemeiner Konstruktor (Deklaration)

        void display();                         //Ausgabe Methode
        void chooseColor();                     //Bediener Abfrage
};

cColor::cColor(int blau, int rot, int gruen)    //Definition des Konstruktors (allgemeine Konstruk. müssen immer definiert werden)
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

int main()
{
    //Objekte der Klasse cColor
    cColor schwarz;
    schwarz.display();

    cColor weiss(255);                          //Aufruf des Konstruktors
    weiss.display();

    cColor gelb(0);
    gelb.display();

    cColor cyan(0, 255, 255);
    cyan.display();

    cColor myFavorite;
    myFavorite.chooseColor();


    getch();
    return 0;


};