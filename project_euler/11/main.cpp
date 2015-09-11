#include <iostream>
#include <fstream>
#include <array>
#include <algorithm>

using namespace std;

int main()
{
    array<array<unsigned long,20>,20> table;
    ifstream inf;
    inf.open("../11/in.txt");
    for(int i=0; i<20; i++)
    {
        for (int j=0; j<20; j++)
        {
            inf >> table[i][j];
        }
    }
    inf.close();

    unsigned long mx=0;


    for (int i=0; i<20; i++)
        for (int j=0; j<20; j++)
        {
            if (j<17) mx=max(mx, table[i][j]*table[i][j+1]*table[i][j+2]*table[i][j+3]);
            if (i<17) mx=max(mx, table[i][j]*table[i+1][j]*table[i+2][j]*table[i+3][j]);
            if (i<17 && j<17) mx=max(mx, table[i][j]*table[i+1][j+1]*table[i+2][j+2]*table[i+3][j+3]);
            if (3<=i && j<17) mx=max(mx, table[i][j]*table[i-1][j+1]*table[i-2][j+2]*table[i-3][j+3]);

        }

    cout << mx << endl;
    return 0;
}

