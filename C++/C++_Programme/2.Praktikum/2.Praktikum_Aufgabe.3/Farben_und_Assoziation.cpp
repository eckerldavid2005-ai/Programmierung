//Ersteller: David Eckerl

#include <conio.h>
#include "cColor.h"

int main()
{
    cColor schwarz;
    schwarz.display();

    cColor weiss(255);
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