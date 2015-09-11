#include <iostream>

using namespace std;

unsigned long tri(unsigned long n)
{
    return n*(n+1)/2;
}

int main()
{
    unsigned long n, t, s,d,c;
    n=1;
    s=1;
    while (s!=0)
    {
        t=tri(n);
        s=1;
        d=2;

        while(t!=1)
        {
            c=1;
            while(t%d==0)
            {
                c++;
                t/=d;
            }
            s*=c;
            d++;
        }
        if (s>500) s=0;
        else n++;
    }
    cout << tri(n) << endl;
    return 0;
}

