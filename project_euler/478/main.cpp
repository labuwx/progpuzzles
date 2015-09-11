#include <iostream>
#include <vector>

using namespace std;

unsigned long gcd (unsigned long a, unsigned long b)
{
    unsigned long tmp;

    while (a%b!=0)
    {
        tmp=b;
        b=a%b;
        a=tmp;
    }

    return b;
}

unsigned long gcd (unsigned long a, unsigned long b, unsigned long c)
{
    unsigned long tmp=gcd(a, b);
    return gcd(tmp, c);

}

bool relp (unsigned long a, unsigned long b, unsigned long c)
{
    return 1 == gcd(a, b, c);
}

unsigned long lcd (unsigned long a, unsigned long b)
{
    return a*b/gcd(a,b);
}

vector< unsigned long >  combine( vector< vector< unsigned long > > m, vector< vector< unsigned long > > r)
{
    vector< unsigned long > mixt=vector< unsigned long >(3,0);

    unsigned long lcdt=1;

    for (unsigned int i=0; i<r.size(); i++)
    {
        lcdt=lcd(lcdt,r[i][1]);
    }

    //unsigned long tmp;

    for (unsigned int i=0; i<r.size(); i++)
    {
        r[i][0]*=lcdt/r[i][1];

        mixt[0]+=m[i][0]*r[i][0];
        mixt[1]+=m[i][1]*r[i][0];
        mixt[2]+=m[i][2]*r[i][0];

    }



    unsigned long gcdt=gcd(mixt[0], mixt[1], mixt[2]);
    mixt[0]/=gcdt;
    mixt[1]/=gcdt;
    mixt[2]/=gcdt;
    return mixt;
}

int main()
{
    cout << gcd(33,42) << endl;
    return 0;
}

