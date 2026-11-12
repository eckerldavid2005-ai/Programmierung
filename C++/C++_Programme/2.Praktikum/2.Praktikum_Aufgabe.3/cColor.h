#ifndef CCOLOR_H
#define CCOLOR_H

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

        cColor(int b, int r=255, int g=255);    //allgemeiner Konstruktor

        void display();                         //Ausgabe Methode
        void chooseColor();                     //Bediener Abfrage
};

#endif
