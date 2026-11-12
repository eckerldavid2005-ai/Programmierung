#include <iostream>
#include <fstream>
#include <string>

#include "leaderboard.h"

using namespace std;

void saveScore(
    const char name[],
    int errors
)
{
    ofstream file(
        "scores.txt",
        ios::app
    );

    if(file.is_open())
    {
        file << name
             << " "
             << errors
             << endl;

        file.close();
    }
}

void showScores()
{
    ifstream file("scores.txt");

    string name;
    int errors;

    cout << "\n===== Rangliste =====\n";

    while(file >> name >> errors)
    {
        cout << name
             << " - Fehler: "
             << errors
             << endl;
    }

    file.close();
}