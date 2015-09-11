#include <iostream>
#include <vector>

using namespace std;



bool isab(unsigned int n)
{
    unsigned long sum=0;
    for (unsigned int i=1; i<n && sum<=n; i++)
        if (n%i==0) sum+=i;
    return sum>n;
}


unsigned int m=28124;
vector<bool> abs;

bool isgood(unsigned int n)
{
    bool b=false;
    for (unsigned int i=12; i<n && !b; i++)
        b|= abs[i-1] && abs[n-i-1];

    return b;

}


int main()
{

    abs=vector<bool>(m);
    for (unsigned int i=1; i<=m; i++)
    {
        abs[i-1]=isab(i);
    }

    unsigned long sum=0;

    for (unsigned int i=1; i<=m; i++)
    {
        if (!isgood(i)) sum+=i;
    }



    cout  << sum << endl;
    return 0;
}

