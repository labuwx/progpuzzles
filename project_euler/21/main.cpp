#include <iostream>
#include <vector>
#include <map>
#include <math.h>

using namespace std;

unsigned long divsum(unsigned long n)
{
    unsigned long s=1;
    int mult;
    unsigned long tmp;
    unsigned long n0=n;
    for (unsigned int i=2; i<=n0; i++)
    {
        mult=0;
        while(n%i==0)
        {
            n/=i;
            mult++;
        }

        tmp=1;
        while(mult>=0)
        {
            tmp*=i;
            mult--;
        }
        s*=(tmp-1)/(i-1);
    }
    return s-n0;

}

int main()
{
    unsigned long s=0;
    for (unsigned long i=2; i<=10000; i++)
        if (i==divsum(divsum(i)) && i!=divsum(i)) s+=i;


    cout << s << endl;

    for(int i=1; i<11; i++)
    {
        cout << i << " " << divsum(i) << endl;
    }
    return 0;
}

