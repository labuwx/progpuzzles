#include <iostream>

using namespace std;

unsigned long diff(unsigned long n)
{
    unsigned long a=n*(n+1)/2;
    unsigned long b=n*(n+1)*(2*n+1)/6;
    return a*a-b;
}

int main()
{
    cout << diff(100) << endl;
    return 0;
}

