#include <iostream>

#include "constants.h"
#include "board.h"
#include "sudoku.h"
#include "leaderboard.h"

using namespace std;

int main()
{
    int board[SIZE][SIZE];

    loadEasy(board);

    int errors = 0;

    cout << "==== Sudoku ====\n";

    while(!isSolved(board))
    {
        printBoard(board);

        int row;
        int col;
        int value;

        cout << "Zeile (1-9): ";
        cin >> row;

        cout << "Spalte (1-9): ";
        cin >> col;

        cout << "Wert (1-9): ";
        cin >> value;

        row--;
        col--;

        if(row < 0 || row >= SIZE ||
           col < 0 || col >= SIZE)
        {
            cout << "Ungueltige Position!\n";
            continue;
        }

        if(board[row][col] != 0)
        {
            cout << "Feld bereits belegt!\n";
            continue;
        }

        if(isCorrectMove(
            row,
            col,
            value))
        {
            board[row][col] = value;

            cout << "Richtig!\n";
        }
        else
        {
            errors++;

            cout << "Falsch! Fehler: "
                 << errors
                 << endl;
        }
    }

    cout << "\nSudoku geloest!\n";

    char name[50];

    cout << "Name eingeben: ";
    cin >> name;

    saveScore(
        name,
        errors
    );

    showScores();

    return 0;
}