#include <iostream>
#include <math.h>

using namespace std;


bool isprime(unsigned long n)
{
    unsigned long rn=sqrt(n);
    bool b=true;
    for(unsigned int i=2; i<=rn && b; i++)
        b&= n%i!=0;
    b&= n!=0 && n!=1;
    return b;


}

int main()
{
    unsigned long x,n;
    n=0;
    x=0;
    while(n<10001)
    {
        x++;
        if (isprime(x)) n++;
    }
    cout << x << endl;
    return 0;
}

