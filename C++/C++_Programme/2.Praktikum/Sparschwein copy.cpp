//Ersteller: David Eckerl
//Kommentare fehlen vermehrt da die Attribut- und Methoden Namen weise gewählt wurden
//Außerdem könnte das Programm etwas unübersichtlich aussehen da ich mein eigentliches Programm mit Header Dateien 
//und .cpp Dateien mit dem Sparschwein verbunden habe. Somit habe ich eine cColor.cpp (enthält alle Methoden und Funktionen), 
//eine cColor.h (enthält Klasse), eine Sparschwein.cpp (enthält Sparschwein Programm, cColor.h und cColor.cpp) 
//und eine Farben und Assoziation.cpp (enthält main)
//Verwendung von const bei Methoden die nichts ändern 

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

        void display()const;                    //Ausgabe Methode
        void chooseColor();                     //Bediener Abfrage
};

class piggyBank
{
    private: //Privat Attribute die in meiner main() fiktiv mit Werten befüllt werden
        bool Das_Schwein_ist_aufgebrochen; //Variable/Attribute die Wert des Zusands des Schweins übergeben bekommt (1 oder 0)
        int Anzahl_1_Euro=0;               //Variablen//Attribute die mithilfe der add... Methoden
        int Anzahl_50_Cent=0;              //einen Wert Anzahl zugewiesen bekommen und am Anfang 0 gesetzt werden
        int Anzahl_10_Cent=0;              //sodass das Schwein am Anfang wirklich leer ist 
        int Anzahl_1_Cent=0;
        const int Max_Muenzenanzahl=500;         //Maximale Münzenanzahl des Sparschweins

        cColor farbe;



    public:
        void add_1_Euro(int Anzahl1Euro);  //Methoden zur Zusammenrechnung der Anzahl der jeweiligen Münzen
        void add_50_Cent(int Anzahl50Cent);      
        void add_10_Cent(int Anzahl10Cent);
        void add_1_Cent(int Anzahl1Cent);
          
        int getAnzahl_1_Euro()const;            //Methoden für die globale Ausgabe welche
        int getAnzahl_50_Cent()const;           //die Anzahl... Attributen als Rückgabe bekommen
        int getAnzahl_10_Cent()const;
        int getAnzahl_1_Cent()const;

        int Anzahl_Muenzen()const;              //Anlegen der restlichen Methoden die weiter unten 
        double Summe_Geldbetrag()const;         //deffiniert werden
        bool Schwein_Zustand(); 
        bool Schwein_Ueberfuellt()const;
        int Groesse_Sparschwein()const;

        void Farbwahl();
        void Farbausgabe()const;

};

void piggyBank::Farbwahl()
{
    farbe.chooseColor();
}

void piggyBank::Farbausgabe()const
{
    farbe.display();
}

//Nachfolgenden 4 getAnzahl... Methoden: Methoden für meine globale Funktion Ausgabe damit 
//ich auf meine Privat Attribute zugreifen kann
int piggyBank::getAnzahl_1_Euro()const
{
    return Anzahl_1_Euro;
}

int piggyBank::getAnzahl_50_Cent()const
{
    return Anzahl_50_Cent;
}

int piggyBank::getAnzahl_10_Cent()const
{
    return Anzahl_10_Cent;
}

int piggyBank::getAnzahl_1_Cent()const
{
    return Anzahl_1_Cent;
}

//Nachfolgende 4 add... Methoden: Mit meinen 4 nachfolgenden Methoden kann ich meine jeweilige Attribute 
//befüllen um den Wert Anzahl der in der main abgefragt wird 
void piggyBank::add_1_Euro(int Anzah1Euro)
{
    Anzahl_1_Euro += Anzah1Euro;
}

void piggyBank::add_50_Cent(int Anzahl50Cent)
{
    Anzahl_50_Cent += Anzahl50Cent;
}

void piggyBank::add_10_Cent(int Anzahl10Cent)
{
    Anzahl_10_Cent += Anzahl10Cent;
}

void piggyBank::add_1_Cent(int Anzahl1Cent)
{
    Anzahl_1_Cent += Anzahl1Cent;
}

//In dieser Methode wird meine gesammt Anzahl der Münzen berechnet und der Methode zurückgegeben
//damit ich am ende mit dieser Methode z.B. den Zustand des Spaarschweins abprüfen kann
int piggyBank::Anzahl_Muenzen()const
{
    return Anzahl_1_Cent + Anzahl_10_Cent + Anzahl_50_Cent + Anzahl_1_Euro;
}

//In dieser Methode wird die Gesammt Summe berechnet indem ich meine Attribute mal den Geldwert (1, 0.5, 0.1, 0.01)
//und der Methode für späteren Gebrauch zurückgegeben
double piggyBank::Summe_Geldbetrag()const
{
    return Anzahl_1_Euro * 1 + Anzahl_50_Cent * 0.5 + 
           Anzahl_10_Cent * 0.1 + Anzahl_1_Cent * 0.01;
}

//Der Zustand (Überfüllt oder nicht) wird mit meinen vorhin mit Werten befüllten Methoden geprüft
//fals mehr Münzen als zulässige enthalten sich (AnzahlMünzen>=Größe...) wird der wert 1 (true)
//der Methode zurückgegeben und in der Main wird die Ausgabe Schwein aufgebrochen ausgegeben,
//fals nicht dann 0 (false) Schwein noch nicht voll
bool piggyBank::Schwein_Zustand()  //Auf oder Zu
{
    if(Anzahl_Muenzen()>=Groesse_Sparschwein())
        {
            Das_Schwein_ist_aufgebrochen = true;
            return true;
        }
    else
        {
            return false;
        }
    
}

//Der Methode wird die Attribute der max. Münzenanzahl übergeben
//Die Methode wird benötigt um z.B. den Zustand des Schweins abzuprügen
int piggyBank::Groesse_Sparschwein()const
{
    return Max_Muenzenanzahl;
}

//In der Methode wird geprüft ob das Schwein bereits überfüllt ist wenn die Anzahl der Münzen größer der 
//größe des Spaarschweins ist, dann wird wieder 1 (true) der Methode übergeben und in der main ausgegeben
bool piggyBank::Schwein_Ueberfuellt()const
{
    if(Anzahl_Muenzen()>Groesse_Sparschwein())
    {
        return true;
    }
    return false;
}

//Das ist meine globale Ausgabe. Für sie habe ich im vorhinein meine Methoden erstellt weil ich nur 
//mit Methoden auf meine Attributen zugreifen kann (nicht möglich mit globalen Funktionen auf Provat zuzugreifen)
//die die Anzahl der Münzen enthalten
// Ausgabe bekommt ein Objekt der Klasse piggyBank übergeben Schwein kann auf Daten von newpiggyBank zugreifen
void Ausgabe(piggyBank Schwein) 
{
    cout << "Anzahl der 1 Euro Muenzen:" << Schwein.getAnzahl_1_Euro() << endl;   //außerhalb der Klasse deshalt
    cout << "Anzahl der 50 Cent Muenzen:" << Schwein.getAnzahl_50_Cent() << endl; //mit getAnzahl...
    cout << "Anzahl der 10 Cent Muenzen:" << Schwein.getAnzahl_10_Cent() << endl;
    cout << "Anzahl der 1 Cent Muenzen:" << Schwein.getAnzahl_1_Cent() << endl;
   
}

cColor::cColor(int blau, int rot, int gruen)    //allgemeiner Konstruktor (Definition)
{
    r = rot;                                    //kopiert Wert des Parameters r in das Attribut r des Objekts
    g = gruen;                                
    b = blau;
}

void cColor::display()const
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

    cout << "Ihre gewaehlte Farbe fuer das Schwein:";
    cout << "(" << r << "," << g << "," << b <<")" << endl << endl;

}

//In meiner main() werden alle restlichen Ausgaben ausgeführt
//Hier wird das Befüllen des Sparschweins durchgeführt durch manuelle Eingabe
int main()
{
    int Anzahl1Euro, Anzahl50Cent, Anzahl10Cent, Anzahl1Cent, gesamt=0;
         // Klasse   Objekt
    class piggyBank newpiggyBank; //newpiggyBank ist meine Objektvariable und piggyBank ist der 
                                  //Typ der Objektvariablen

    cout << "Bitte Farbe des Schweins eingeben" << endl;
    newpiggyBank.Farbwahl();

    
    
                
    //Eingabe der Münzen
    cout << "Geben sie die Anzahl der 1 Euro Muenzen an" << endl;
    cin >> Anzahl1Euro;
    gesamt += Anzahl1Euro;


    if(gesamt<newpiggyBank.Groesse_Sparschwein())
        {
            cout << "Geben sie die Anzahl der 50 Cent Muenzen an" << endl;
            cin >> Anzahl50Cent;
            gesamt +=Anzahl50Cent;
        }

    if(gesamt<newpiggyBank.Groesse_Sparschwein())

        {
        cout << "Geben sie die Anzahl der 10 Cent Muenzen an" << endl;
        cin >> Anzahl10Cent;
        gesamt +=Anzahl10Cent;
        }

    if(gesamt<newpiggyBank.Groesse_Sparschwein())
        {
            cout << "Geben sie die Anzahl der 1 Cent Muenzen an" << endl;
            cin >> Anzahl1Cent;
                gesamt +=Anzahl1Cent;
        }

    newpiggyBank.add_1_Euro(Anzahl1Euro);
    newpiggyBank.add_50_Cent(Anzahl50Cent);
    newpiggyBank.add_10_Cent(Anzahl10Cent);
    newpiggyBank.add_1_Cent(Anzahl1Cent);
    Ausgabe(newpiggyBank);
    
    cout << "Gesammtbetrag:" <<newpiggyBank.Summe_Geldbetrag() << endl;
   
    if(newpiggyBank.Schwein_Zustand())
    {
        cout << "Schwein ist Aufgebrochen" << endl;
        cout << "Farbe des Aufgebrochenen Schweins:" << endl;
        newpiggyBank.Farbausgabe();
    }
    else
    {
        cout << "Schwein ist noch nicht voll" << endl;    
    }

    if(newpiggyBank.Schwein_Ueberfuellt())
    {
        cout << "Schwein bereits aufgebrochen, Muenzen befinden sich nicht mehr im Schwein" << endl << endl;
    }

    cout << "Sonstige Farben:" << endl << endl;


    //Allgemeiner Konstruktor Aufruf
    cColor schwarz;
    schwarz.display();

    cColor weiss(255);
    weiss.display();

    cColor gelb(0);
    gelb.display();

    cColor cyan(0, 255, 255);
    cyan.display();


    getch();
    return 0;

}

//Testfälle:
//Buchstaben, Sonderzeichen und Zahlen außerhalb des Bereichs 0-255 eingeben, Ausgabe: Fehlereingabe, bitte nur Zahlen zwischen...
//z.B.: a13 Ausgabe: Fehlereingabe, bitte nur Zahlen zwischen 0 und 255
//z.B.: + oder # oder "" Ausgabe: Fehlereingabe, bitte nur Zahlen zwischen 0 und 255
// richtige Eingabe z.B.: 20, 30, 40 Ausgabe: Ihre gewaehlte Farbe fuer das Schwein:(20,30,40)
