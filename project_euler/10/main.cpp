#include <iostream>
#include <math.h>

using namespace std;

bool isprime(unsigned long n)
{
    unsigned long rn=sqrt(n);
    bool b=true;
    for(unsigned long i=2; i<=rn && b; i++)
        b&= n%i!=0;
    b&= n!=0 && n!=1;
    return b;
}


int main()
{
    unsigned long long sum=0;
    for (unsigned int i=1; i<=2000000; i++)
        if (isprime(i)) sum+=i;
    cout << sum << endl;
    return 0;
}

