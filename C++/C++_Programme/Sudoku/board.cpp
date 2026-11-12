#include <iostream>
#include "board.h"

using namespace std;

void printBoard(int board[SIZE][SIZE])
{
    cout << "\n";

    for(int i = 0; i < SIZE; i++)
    {
        for(int j = 0; j < SIZE; j++)
        {
            if(board[i][j] == 0)
                cout << ". ";
            else
                cout << board[i][j] << " ";
        }

        cout << endl;
    }

    cout << endl;
}