#include <iostream>
#include <fstream>
#include <array>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    array<array<unsigned long,50>,100> table;
    ifstream inf;
    char c;
    inf.open("../13/in.txt");
    for(int i=0; i<100; i++)
    {
        for (int j=0; j<50; j++)
        {
            c=0;
            while(c<'0' || '9'<c)
                inf.get(c);
            table[i][j]=c-'0';
        }
    }
    inf.close();

    vector<int> num;
    unsigned long carry=0;
    for (int i=49; i>=0; i--)
    {
        for (int j=0; j<100; j++)
        {
            carry+=table[j][i];
        }
        num.push_back(carry%10);
        carry/=10;
    }
    while (carry!=0)
    {
        num.push_back(carry%10);
        carry/=10;
    }





    for (int i=num.size()-1; i>=0; i--)
    {
        cout << num[i];
    }
    cout << endl;


    return 0;
}

