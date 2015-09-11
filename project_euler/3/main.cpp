#include <iostream>
#include <math.h>
#include <algorithm>

using namespace std;



int main()
{
    unsigned long long n, rn,mx;
    n=600851475143;
    rn=sqrt(n);

    for(unsigned long long i=2; i<=rn; i++)
    {

        if (n%i == 0 )
        {

            mx=i;
            while(n%i==0) n=n/i;
        }
    }
    mx=max(mx,n);

    cout << mx << endl;
    return 0;
}

