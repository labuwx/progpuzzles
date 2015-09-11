#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

int main()
{
    map<pair<int,int>, unsigned long long > tr;
    ifstream inf;
    int n=100;
    unsigned int c;
    unsigned long long l, r, mx;
    mx=0;
    inf.open("../18_67/67.txt");
    for (int i=0; i<n; i++)
    {

        for(int j=0-i; j<=i; j+=2)
        {
            inf >> c;
            l= j==0-i ? 0 : tr[make_pair(i-1,j-1)] ;
            r= j==i ? 0: tr[make_pair(i-1,j+1)];
            tr[make_pair(i,j)]=c+max(l,r);
            if (i==n-1 && tr[make_pair(i,j)]>mx) mx=tr[make_pair(i,j)];


        }
    }
    inf.close();
    cout << mx << endl;
    return 0;
}

